import rich
import asyncio
from pydantic import BaseModel
from connection import config
from agents import (
    Agent,
    Runner,
    trace,
    output_guardrail,
    GuardrailFunctionOutput,
    OutputGuardrailTripwireTriggered,
)

# Output model for ChildQuery
class ChildQuery(BaseModel):
    reply: str
    isFoodReady: bool

# Sub-agent: Hungry Child
hungry_child = Agent(
    name="Hungry Child",
    instructions="""
    You are a child who just heard your mother's response.
    Check if she said the food is ready.
    If food is ready, return isFoodReady = true.
    If not, return isFoodReady = false.
    Your job is only to decide this based on her reply.
    """,
    output_type=ChildQuery,
)

# Output guardrail function to evaluate mother's response
@output_guardrail
async def child_guardrail(ctx, agent: Agent, output: str) -> GuardrailFunctionOutput:
    result = await Runner.run(hungry_child, output, run_config=config)

    rich.print("[bold green]Child Analysis:[/bold green]", result.final_output)

    return GuardrailFunctionOutput(
        output_info=result.final_output.reply,
        tripwire_triggered= not result.final_output.isFoodReady  # This triggers the guardrail
    )

# Main agent: Mother
mother_agent = Agent(
    name="Mother",
    instructions="""
    You are a mother replying to your child who is hungry.
    If the food is ready, say: 'Food is ready, you can eat now.'
    If the food is not ready, say: 'Food is not ready yet, please wait.'
    """,
    output_guardrails=[child_guardrail],
)

# Main execution
async def main():
    with trace("Mother Response"):
        try:
            result = await Runner.run(
                mother_agent,
                "I am hungry i need food",
                run_config=config
            )
            rich.print("\n[bold yellow]Mother's response [bold yellow] result.final_output")
        except OutputGuardrailTripwireTriggered:
            rich.print("\n[bold red]Tripwire Triggered! Food is ready.[/bold red]")

if __name__ == "__main__":
    asyncio.run(main())
