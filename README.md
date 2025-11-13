# A Robust Testbed for rapid prototyping LLM applications with DSPy

Building robust, production-ready applications with modern LLM frameworks like DSPy introduces unique challenges. The non-deterministic nature of models, the R&D-heavy development process, and the need for new kinds of observability require a development paradigm that goes beyond traditional software engineering.

This repo provides a comprehensive, 3-pillar framework for designing a testbed that addresses these challenges. It is built to create a system that is traceable, reproducible, and integrates seamlessly with modern AI coding assistants. Drop these files in your empty project folder, make Cascade read and follow the instructions, and start working on your first item.

## Table of Contents

- [Theoretical Foundation: The 3-Pillar Framework](#theoretical-foundation-the-3-pillar-framework)
  - [1. The "System of Record" (AI Context & Norms)](#1-the-system-of-record-ai-context--norms)
  - [2. "Hypothesis-Driven Development" (R&D Planning)](#2-hypothesis-driven-development-rd-planning)
  - [3. The "Reproducible Test Harness" (Implementation)](#3-the-reproducible-test-harness-implementation)
- [Implementation Overview](#implementation-overview)
  - [📂 Folder & File Structure](#-folder--file-structure)
  - [🏄 Windsurf Artifacts](#-windsurf-artifacts)
    - [1. Memories (The "What")](#1-memories-the-what)
    - [2. Rules (The "How")](#2-rules-the-how)
    - [3. Workflows (The "Do")](#3-workflows-the-do)

---

## Theoretical Foundation: The 3-Pillar Framework

The following three pillars represent the **theory** behind this very practical, 2-minute-setup system. Understanding these principles will help you customize and extend the framework to fit your specific needs, but you don't need to master them to get started—the implementation in this repo handles the details for you.

### 1. The "System of Record" (AI Context & Norms)

This pillar addresses the core challenge of "context management," especially when working with an AI assistant. The goal is to give the AI a persistent, high-quality "memory" of the project's state, standards, and history.

* **The Problem:** AI assistants have a limited context window and no long-term "memory" of project-specific decisions or code state. This leads to repeating cycles, re-implementing existing functions, and deviating from project norms.
* **The Best Practice:** The solution is to **"Externalize and Automate Context."** Instead of relying on volatile chat history (which is low-quality and high-creep), context is treated as a first-class citizen of the repository.
* **Solution Details:**
    * **For Development Norms:** Use "explicit context provisioning." Create a `/.project_dev/` directory at the project root. This directory contains key markdown files like `DEV_NORMS.md`, `TDD_PROCESS.md`, and `DOC_STANDARDS.md`. Any AI assistant "Workflow" for a coding task is programmed to *always* read these files before writing code. This is a one-time setup that enforces standards.
    * **For Code Context:** To prevent the AI from re-implementing existing code, use "local indexing." Automate a script (e.g., `python scripts/generate_context_map.py`) that parses the source code to generate a `CODE_CONTEXT.md` file. This file lists all key `dspy.Module` and function signatures along with their docstrings. The AI's workflow is to consult this high-signal file *before* writing new code, rather than polluting its context with the raw codebase.
    * **For Development Status:** Maintain a simple, high-signal `PROJECT_LOG.md` for "Iterative Process" tracking. At the end of each development session, the AI is prompted to summarize: "What did we try? What was the decision? What is the next step?" This curated summary is appended to the log. The *next* day's workflow *starts* by reading this file, directly preventing the repetition of failed experiments.

---

### 2. "Hypothesis-Driven Development" (R&D Planning)

This pillar reframes the R&D process away from traditional backlogs and toward a system designed for learning and discovery.

* **The Problem:** Traditional backlogs (e.g., Jira tickets) are "implementation-focused." R&D, by contrast, is "learning-focused." A standard backlog fails to capture the invaluable *learnings* from failed experiments.
* **The Best Practice:** Adopt **"Hypothesis-Driven Development,"** a core MLOps principle. The goal is to create a structured log of experiments and their outcomes, turning both successes and failures into actionable assets.
* **Solution Details:**
    * **The Hypothesis Log:** The `HYPOTHESES.md` file serves as the central "plan." It is not a list of *tasks* but a list of *assumptions* to be tested. Each item tracks:
        1.  **Hypothesis:** "We believe adding a `dspy.ChainOfThought` signature to the RAG module will improve answer relevance."
        2.  **POC:** The branch or commit for the experiment.
        3.  **Outcome:** (e.g., `Lesson` or `Feature`)
        4.  **Actionable Lesson:** "CoT was too slow (avg. 3.5s) for a marginal gain. Lesson: Monitor latency as a key metric for this module."
    * **Post-hoc Documentation:** This system avoids pre-emptive, heavy documentation by embracing **"Documentation-as-Code."** The DSPy framework's `dspy.Signature` already acts as declarative documentation. This is enforced by a rule (in `DOC_STANDARDS.md`) that all function docstrings must explain their `Purpose`, `Role`, and `Assumptions`. When the dust settles, documentation is generated by a script that scrapes these structured docstrings to build a complete `README.md` or technical guide.

---

### 3. The "Reproducible Test Harness" (Implementation)

This is the most critical pillar for a non-deterministic DSPy application. The governing principle is: **you cannot manage what you do not measure.**

* **The Problem:** LLM outputs are non-deterministic. A small change in one module (a prompt, a signature, a model parameter) can have unpredictable, cascading effects on the final user experience.
* **The Best Practice:** Implement **"Full-Lifecycle Evaluation and Observability."** This means treating your test data, evaluation code, *and evaluation results* as versioned artifacts in source control.
* **Solution Details:**
    * **Rigid E2E Process:** The core of the testbed is an `evaluate.py` script. This script loads a `gold_set.jsonl` (a set of `dspy.Example` objects representing your test cases). It runs the *entire* DSPy application against this set and generates `results.jsonl`. This is the one rigid process that must be run for every change.
    * **Version Control Everything:** To achieve perfect reproducibility, *all* components of an experiment are committed to source control:
        1.  **Code:** The DSPy application modules.
        2.  **Test Data:** The `gold_set.jsonl` (using Git LFS if large).
        3.  **Parameters:** A `config.json` for all settings.
        4.  **Results:** The output `results.jsonl` and `metrics.json` files.
        This allows a developer to check out *any* commit from history, run `evaluate.py`, and get the *exact* same metrics, providing a perfect, traceable history of UX degradation or improvement.
    * **Extreme Observability:** The system is built for 100% transparency using two levels of logging:
        1.  **DSPy Native:** Use built-in DSPy features like `dspy.inspect_history(n=1)` to log the final, compiled prompt/completion pairs for quick debugging.
        2.  **Custom Logging:** For "verbose" mode, implement a custom `dspy.BaseCallback` handler. This advanced DSPy feature allows the system to log *every single event* the application takes: every module start/end, every LLM call (with full I/O), and every tool use. This log dumps everything, making the entire chain fully transparent and debuggable.

By integrating these three pillars, this framework moves beyond simple scripting to create a mature development system. It yields a testbed that is traceable, reproducible, and self-documenting, enabling rapid, hypothesis-driven R&D while maintaining production-grade stability and observability.

## Implementation Overview

This section describes, how that theoretical setup is implemented in practice.

### 📂 Folder & File Structure

This is an example setup for project folder structure that separates the AI's "brain" (`.project_dev`), the R\&D plan (`HYPOTHESES.md`), and the application code (`src`, `test_data`).

```
dspy_project/
├── .project_dev/
│   ├── DEV_NORMS.md           # Rules for branching, commits, PRs
│   ├── TDD_PROCESS.md         # How to write tests, what defines a "pass"
│   ├── DOC_STANDARDS.md       # Required docstring format (Purpose, Role, Assumptions)
│   ├── CODE_CONTEXT.md        # (Auto-generated) List of all modules, classes, signatures
│   └── PROJECT_LOG.md         # (Manually curated) Log of decisions & next steps
│
├── config/
│   ├── dev_config.json        # LLM keys, dev endpoints, lightweight settings
│   └── prod_config.json       # Production model settings, endpoints
│
├── logs/
│   ├── .gitignore             # (Contains "*")
│   └── evaluation.log         # Verbose, untracked output for local debugging
│
├── results/
│   ├── .gitkeep               # To track the folder
│   └── H-001_eval_2025-11-13/ # (Example) Source-controlled results for a hypothesis
│       ├── results.jsonl      # The raw outputs from the gold set
│       └── metrics.json       # The calculated metrics (e.g., accuracy, latency)
│
├── scripts/
│   └── generate_context_map.py # Script to parse 'src/' and create 'CODE_CONTEXT.md'
│
├── src/
│   ├── modules/
│   │   ├── __init__.py
│   │   └── rag_module.py      # Example: A dspy.Module class
│   ├── signatures/
│   │   ├── __init__.py
│   │   └── qa_signatures.py   # Example: dspy.Signature definitions
│   ├── __init__.py
│   └── main_pipeline.py       # Assembles the full DSPy application
│
├── test_data/
│   ├── gold_set.jsonl         # The main E2E evaluation set (inputs + expected outputs)
│   └── dev_set.jsonl          # A small, 10-item set for rapid TDD
│
├── .gitignore
├── evaluate.py                # The main test harness script
├── HYPOTHESES.md              # The R&D plan (replaces a traditional backlog)
└── README.md                  # Project overview, setup, and (eventually) generated docs
```

-----

### 🏄 Windsurf Artifacts

These are the "Rules, Workflows, and Memories" you'll configure in your AI tool.

### 1\. Memories (The "What")

Memories are the specific, high-quality context files the AI is given access to.

  * **Static Norms Memory:**

      * **Content:** A collection of files pointing to:
          * `./.project_dev/DEV_NORMS.md`
          * `./.project_dev/TDD_PROCESS.md`
          * `./.project_dev/DOC_STANDARDS.md`
      * **Purpose:** To provide the fixed, high-level "rules of the road" for development.

  * **Code Context Memory:**

      * **Content:** A single file pointer:
          * `./.project_dev/CODE_CONTEXT.md`
      * **Purpose:** To give the AI a complete, up-to-date map of all existing code.
      * **Note:** This memory's *content* is updated by running the `generate_context_map.py` script, but the *pointer* never changes.

  * **Dynamic Status Memory:**

      * **Content:** A single file pointer:
          * `./.project_dev/PROJECT_LOG.md`
      * **Purpose:** To provide session-to-session continuity. This is the AI's "short-term memory."

  * **Hypothesis Memory:**

      * **Content:** A single file pointer:
          * `./HYPOTHESES.md`
      * **Purpose:** To give the AI awareness of the R\&D plan, the "why" behind any task.

-----

### 2\. Rules (The "How")

Rules are high-level instructions that govern the AI's behavior *at all times*.

1.  **Read Before Writing:** "Before generating any code or plan, you **must** read the contents of the **Static Norms Memory** and the **Code Context Memory**."
2.  **Context-First:** "Before implementing any new function, class, or `dspy.Signature`, you **must** consult the **Code Context Memory**. If similar functionality exists, propose its reuse. Do not re-implement existing logic."
3.  **Adhere to Norms:** "All code, tests, and documentation you generate **must** strictly adhere to the standards defined in the **Static Norms Memory**."
4.  **Traceability:** "Every new feature or experiment **must** be associated with an ID from the **Hypothesis Memory** (`HYPOTHESES.md`)."
5.  **Status Aware:** "At the beginning of any new session, you **must** read the **Dynamic Status Memory** (`PROJECT_LOG.md`) to understand the last-known state."

-----

### 3\. Workflows (The "Do")

Workflows are specific, automated "recipes" for common, multi-step tasks.

  * **Workflow: `Start_Day_Session`**

    1.  **Trigger:** User starts a new session.
    2.  **Read:** `Dynamic Status Memory` (`PROJECT_LOG.md`).
    3.  **Read:** `Hypothesis Memory` (`HYPOTHESES.md`).
    4.  **Summarize:** "Welcome back. Here is the last-known status: [Summary of last entry in PROJECT\_LOG.md]. The current open hypotheses are: [List hypotheses with 'Pending' status]. What is our objective today?"

  * **Workflow: `Start_New_Feature`**

    1.  **Trigger:** User asks to build a new feature (e.g., "Let's add a summarization module").
    2.  **Prompt:** "Great. Which `Hypothesis ID` from `HYPOTHESES.md` does this feature test?" (User provides ID, e.g., `H-002`).
    3.  **Read:** `Static Norms Memory` (specifically `TDD_PROCESS.md` and `DOC_STANDARDS.md`).
    4.  **Read:** `Code Context Memory`.
    5.  **Action:** "Understood. Per `TDD_PROCESS.md`, I will first create a new test file in `test_data/` and add a failing test to `evaluate.py` for Hypothesis `H-002`. Please confirm."
    6.  *(...continues with TDD loop...)*

  * **Workflow: `Run_Full_Experiment`**

    1.  **Trigger:** User wants to validate a completed POC.
    2.  **Prompt:** "Which `Hypothesis ID` are we evaluating?" (User provides `H-002`).
    3.  **Action:** "I will now run the full test harness against the gold set and save the results to a new, version-controlled directory."
    4.  **Execute Shell Command:** `python evaluate.py --config config/dev_config.json --test_set test_data/gold_set.jsonl --output_dir results/H-002_eval_$(date +%Y-%m-%d)`
    5.  **Summarize:** "Evaluation complete. The outputs are in `results/H-002.../`. The `metrics.json` file shows: [Key metrics]. How should we update `HYPOTHESES.md`?"

  * **Workflow: `Update_Code_Context`**

    1.  **Trigger:** User asks "Update the code context" or after a new module is merged.
    2.  **Action:** "Updating the code context map..."
    3.  **Execute Shell Command:** `python scripts/generate_context_map.py`
    4.  **Confirm:** "The `CODE_CONTEXT.md` file in the **Code Context Memory** is now up-to-date with the latest `src/` directory."

  * **Workflow: `End_Day_Session`**

    1.  **Trigger:** User says "Let's wrap up."
    2.  **Prompt:** "Okay. To update the `PROJECT_LOG.md`, please summarize:
          * What did we try today?
          * What were the key decisions or results?
          * What is the next step for tomorrow?"
    3.  **Write:** The AI formats the user's answers and appends them with a timestamp to `PROJECT_LOG.md` (in the `Dynamic Status Memory`).
    4.  **Confirm:** "The project log is updated. Session concluded."
