---
title: Anthropic’s Three-Agent Harness for Long-Running AI Development
author: InfoQ
url: https://www.infoq.com/news/2026/04/anthropic-three-agent-harness-ai/
ingested: 2026-04-07
---

# Anthropic’s Three-Agent Harness for Long-Running AI Development

Anthropic has developed a specialized multi-agent harness designed to facilitate **long-running autonomous application development**. This framework is specifically engineered to handle complex frontend and full-stack tasks that span several hours, overcoming traditional AI limitations like context loss and "amnesia."

## 1. The Three-Agent Framework
The core of the design is the separation of concerns into three distinct roles to maintain coherence and quality:

- **Planning Agent:** Defines the roadmap and task structure.
- **Generation Agent:** Executes the actual coding or design work.
- **Evaluation Agent:** Critiques the output against specific rubrics.

> "Separating the agent doing the work from the agent judging it proves to be a strong lever to address this issue." — **Prithvi Rajasekaran**, Engineering Lead at Anthropic Labs.

## 2. Solving "Context Amnesia"
Extended AI sessions often fail because models lose track of the original goal or become overly cautious as they approach context limits. Anthropic’s solution includes:
- **Context Resets:** Periodically clearing the window to prevent performance degradation.
- **Structured Handoff Artifacts:** Using "state" documents (like JSON feature specs) so the next agent can resume work without needing the entire previous chat history.
- **Init Scripts:** Ensuring every new session starts with a functional, working environment.

## 3. Iterative Evaluation & Grading
To prevent agents from overrating their own work (especially in subjective areas like UI design), the **Evaluator Agent** uses specific tools and criteria:

### Evaluation Mechanics
- **Tools:** Uses **Playwright MCP** to navigate live pages and interact with interfaces.
- **Cycles:** Runs between **5 to 15 iterations** per task, sometimes lasting up to **four hours**.
- **Grading Criteria:**
  1. **Design Quality:** Visual appeal and layout.
  2. **Originality:** Uniqueness of the solution.
  3. **Craft:** Attention to detail and code cleanliness.
  4. **Functionality:** Ensuring the app actually works as intended.

## 4. Key Insights & Industry Perspectives
- **Structure as Breakthrough:** Artem Bredikhin notes that the success of the harness relies on "JSON feature specs, enforced testing, [and] commit-by-commit progress."
- **Repeatability:** The framework provides a standardized workflow for multi-hour sessions, ensuring reliability that single-agent prompts cannot match.
- **Human Role:** While evaluations are automated, human oversight is critical for the initial calibration of scoring mechanisms and final quality validation.

## 5. Future Outlook
As AI models become more capable, the harness will evolve. While next-gen models may absorb some of these tasks natively, the harness will likely shift toward managing even higher levels of complexity, such as distributed processing of tasks across parallel agent streams.

### Summary of Actionable Information for Engineers
| Feature | Implementation Strategy |
| :--- | :--- |
| **Task Management** | Decompose large projects into planning, generation, and evaluation phases. |
| **State Management** | Use structured handoff artifacts (JSON) instead of relying on long-term chat context. |
| **Quality Control** | Calibrate a separate evaluator agent with few-shot examples and strict scoring rubrics. |
| **Tooling** | Integrate browser automation (like Playwright) to allow agents to "see" and test their own frontend work. |
