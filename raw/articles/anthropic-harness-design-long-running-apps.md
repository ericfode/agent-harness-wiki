---
title: Harness Design for Long-Running Application Development
author: Anthropic
url: https://www.anthropic.com/engineering/harness-design-long-running-apps
ingested: 2026-04-07
---

# Harness Design for Long-Running Application Development

This report summarizes Anthropic’s engineering research into "harness design"—the structural orchestration of AI agents—to overcome performance ceilings in frontend design and autonomous software engineering.

## 1. The Core Problem: Why Naive Agents Fail
Even advanced models like Claude hit "ceilings" when tasked with complex, multi-hour projects. Two primary failure modes were identified:

- **Context Anxiety & Coherence Loss:** As context windows fill, models lose track of the goal or "wrap up" prematurely to avoid hitting limits.
- **Self-Evaluation Bias:** Agents are poor at grading their own work. When asked to evaluate their output, they tend to be over-confident and overlook mediocrity, especially in subjective areas like design.

> "Tuning a standalone evaluator to be skeptical turns out to be far more tractable than making a generator critical of its own work."

---

## 2. Breakthrough: The GAN-Inspired Multi-Agent Structure
To solve these issues, Anthropic implemented a structure inspired by **Generative Adversarial Networks (GANs)**, separating the "doing" from the "judging."

### A. Frontend Design Harness
To move Claude beyond "safe, predictable layouts," a generator-evaluator loop was established using four specific grading criteria:
1. **Design Quality:** Coherence of mood and identity.
2. **Originality:** Evidence of custom decisions vs. AI-generated patterns (e.g., avoiding "purple gradients over white cards").
3. **Craft:** Technical execution (typography, spacing, contrast).
4. **Functionality:** Usability and navigation.

**Key Insight:** By weighting **Originality** and **Design Quality** more heavily, the model was pushed toward "aesthetic risk-taking."

### B. Full-Stack Coding Architecture (The Three-Agent System)
For autonomous application building, the harness evolved into a three-persona system:

| Persona | Responsibility |
| :--- | :--- |
| **Planner** | Expands a 1-4 sentence prompt into a full product spec. Focuses on high-level design to avoid cascading technical errors. |
| **Generator** | Works in "sprints," implementing one feature at a time using a specific stack (React, Vite, FastAPI, PostgreSQL). |
| **Evaluator** | Uses **Playwright MCP** to interact with the live app like a user. Tests UI, APIs, and DB states against a "sprint contract." |

---

## 3. Key Technical Strategies
- **Context Resets vs. Compaction:** While compaction summarizes history, a **Context Reset** (starting a fresh agent with a structured handoff artifact) was found essential for Claude 4.5 to eliminate "context anxiety."
- **Sprint Contracts:** Before coding, the Generator and Evaluator negotiate what "done" looks like. This bridges the gap between vague user stories and testable code.
- **Automated QA:** The Evaluator doesn't just look at code; it "clicks" through the app.

### Example Evaluator Findings (Actionable Bugs)
| Contract Criterion | Evaluator Finding |
| :--- | :--- |
| Rectangle fill tool allows click-drag | **FAIL** — Tool only places tiles at drag start/end points. `fillRectangle` function exists but isn't triggered. |
| User can reorder animation frames via API | **FAIL** — `PUT /frames/reorder` route defined after `/{frame_id}`. FastAPI matches 'reorder' as an integer. |

---

## 4. Results & Evolution (Claude 4.5 vs. 4.6)
Anthropic tested the harness by building a **Retro Video Game Maker** and a **Digital Audio Workstation (DAW)**.

- **Solo vs. Harness:** A solo agent run ($9, 20 min) produced a broken app with a rigid UI. The full harness run ($200, 6 hours) produced a polished, functional game maker with AI-assisted sprite generation and working physics.
- **Model Improvements:** With the release of **Claude 4.6**, the need for "sprint decomposition" decreased. The model could run coherently for 2+ hours in a single session.
- **Cost/Performance Trade-off:** The harness is significantly more expensive but moves the output from "non-functional prototype" to "usable application."

---

## 5. Actionable Lessons for AI Engineers
1. **Harnesses are Dynamic:** Every component in a harness assumes a model limitation. When models improve (e.g., 4.5 to 4.6), strip away redundant scaffolding to reduce latency and cost.
2. **The Evaluator is the Lever:** If an agent is underperforming, don't just prompt the generator; build a more skeptical, tool-equipped evaluator.
3. **Decompose by Persona, Not Just Task:** Separating Planning, Generating, and QAing allows for specialized prompts and tools (like Playwright for QA) that a single agent cannot manage effectively.

> "The space of interesting harness combinations doesn't shrink as models improve. Instead, it moves."
