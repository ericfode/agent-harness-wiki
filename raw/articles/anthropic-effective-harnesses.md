---
title: Effective Harnesses for Long-Running Agents
author: Anthropic
url: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
ingested: 2026-04-07
---

# Effective Harnesses for Long-Running Agents

**Source:** [Anthropic Engineering](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
**Key Focus:** Solving the "context window gap" for AI agents performing complex tasks that span hours or days.

---

## The Core Challenge: The "Memory Gap"
Long-running agents operate in discrete sessions. Because context windows are limited, each new session essentially starts with "no memory" of previous work.

**Observed Failure Patterns:**
1. **The "One-Shot" Trap:** Agents try to do too much at once, running out of context mid-implementation and leaving the code in an undocumented, broken state.
2. **Premature Completion:** Later agent instances see existing progress and incorrectly declare the entire project finished.
3. **Testing Gaps:** Agents often mark features as complete without verifying end-to-end functionality (e.g., using unit tests but ignoring UI failures).

---

## The Two-Fold Solution
Anthropic developed a harness strategy using two specialized roles (defined by distinct prompts) to bridge sessions.

### 1. The Initializer Agent
The first session is dedicated to environment setup rather than coding. It creates the foundation for all future work.
- **`init.sh`:** A script to start development servers and run basic tests.
- **`claude-progress.txt`:** A log for agents to record what has been done.
- **`feature_list.json`:** A comprehensive list of requirements (often 200+ items) where all features are initially marked as `passes: false`.

**Example Feature Schema:**
```json
{
  "category": "functional",
  "description": "New chat button creates a fresh conversation",
  "steps": [
    "Navigate to main interface",
    "Click the 'New Chat' button",
    "Verify a new conversation is created",
    "Check that chat area shows welcome state",
    "Verify conversation appears in sidebar"
  ],
  "passes": false
}
```

### 2. The Coding Agent
Every subsequent session follows a strict protocol to ensure incremental progress and a "clean state" for the next agent.
- **Incremental Focus:** Tasked with working on only **one feature at a time**.
- **Git Integration:** Required to use descriptive commit messages and progress summaries. This allows agents to revert bad changes and recover working states.
- **Self-Verification:** Prompted to use browser automation (e.g., Puppeteer MCP) to test features as a human user would.

---

## The "Getting Bearings" Workflow
To save tokens and prevent errors, every coding agent follows these steps at the start of a session:

1. **`pwd`**: Confirm the working directory.
2. **Read Logs**: Review `claude-progress.txt` and `git log --oneline -20`.
3. **Prioritize**: Read `feature_list.json` and pick the highest-priority "failing" feature.
4. **Verify State**: Run `init.sh` and perform a basic end-to-end test to ensure the previous agent didn't leave the app broken.

> *"This ensured that Claude could quickly identify if the app had been left in a broken state, and immediately fix any existing bugs. If the agent had instead started implementing a new feature, it would likely make the problem worse."*

---

## Summary of Failure Modes & Solutions

| Problem | Initializer Agent Behavior | Coding Agent Behavior |
| :--- | :--- | :--- |
| **Premature Victory** | Creates a structured JSON feature list based on the spec. | Reads the list; chooses one feature; only marks "passing" after testing. |
| **Broken Environments** | Initializes a Git repo and progress notes file. | Starts by reading logs/notes; ends by committing code and updating progress. |
| **Setup Overhead** | Writes an `init.sh` script to run the dev server. | Starts every session by reading and running `init.sh`. |
| **False Positives** | Defines end-to-end test steps in the feature list. | Uses browser automation (Puppeteer) to verify features as a human user. |

---

## Key Insights & Future Directions
- **JSON over Markdown:** Anthropic found that models are less likely to accidentally overwrite or corrupt JSON files compared to Markdown when tracking progress.
- **Vision Limitations:** Current agents still struggle with browser-native elements (like alert modals) that Puppeteer cannot "see" easily.
- **Multi-Agent Potential:** Future work may involve specialized agents for QA, cleanup, or testing rather than a single general-purpose coding agent.
- **Generalization:** While this demo focused on full-stack web development, the "harness" approach is likely applicable to scientific research and financial modeling.
