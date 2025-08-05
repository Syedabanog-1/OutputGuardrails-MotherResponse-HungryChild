** Project Highlight: "Intelligent Child-Mother Simulation using Output Guardrails in OpenAI Agent SDK"

Objective:
**********
To simulate a realistic interaction between a hungry child and a mother, using AI agents and Output Guardrails to monitor and validate responses based on emotional needs and conditions — such as food readiness.

Key Features:
*************

✅ Two AI Agents:

Mother Agent responds based on food readiness.

Hungry Child Agent interprets the mother’s reply to decide if food is ready.

✅ Output Guardrail with Tripwire:

A custom @output_guardrail function checks the child's interpretation.

If the child thinks the food isn't ready, it triggers a tripwire to flag unmet needs.

✅ Pydantic Integration:

Strong type-checking with the ChildQuery model ensures structured output (reply + isFoodReady boolean).

✅ Traceable Workflow:

Uses trace() and rich.print() for visual debugging and detailed step-wise logs.

✅ Resilient Execution:

Workflow Overview:
*****************

**Mother Agent replies to the child's hunger message.

**Child Agent analyzes this reply:

If it says food is ready → isFoodReady = True

If not → isFoodReady = False

**A Guardrail function intercepts and evaluates this child analysis.

**If food is not ready → Tripwire is triggered and an alert is shown.

**All actions are logged with rich formatting for transparency.



https://github.com/user-attachments/assets/37b5ce64-656f-4299-8f85-8c423e9b3a7f

<img width="1605" height="903" alt="output-guradrails-motherResponse-output" src="https://github.com/user-attachments/assets/904d67cb-d327-4dd1-ab0e-30a752ce9384" />
<img width="1607" height="903" alt="hungry child generation" src="https://github.com/user-attachments/assets/c3468370-8692-4129-a90a-4561acd9964f" />
<img width="1605" height="905" alt="mother-agent-generation" src="https://github.com/user-attachments/assets/d169da48-0d00-43e5-95d1-93cbd3d82814" />
<img width="1614" height="907" alt="triggered True" src="https://github.com/user-attachments/assets/1e0f16f6-fc18-43d2-ab42-4254f310429b" />
<img width="1610" height="907" alt="child-agent-tripewire-triggered" src="https://github.com/user-attachments/assets/638bc4bb-30c0-4079-859f-94918cc5ab27" />



Handles failures gracefully using OutputGuardrailTripwireTriggered for meaningful alerts when food is not

