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
  - [🏄 Cascade AI Configuration](#-cascade-ai-configuration)

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

This is an example setup for project folder structure that separates the AI configuration (`.cascade/`, `.project_dev/`), the R&D plan (`HYPOTHESES.md`), and the application code (`src/`, `test_data/`).

```
dspy_project/
├── .cascade/
│   ├── README.md              # Configuration documentation
│   ├── rules/                 # Non-negotiable constraints for Cascade
│   └── workflows/             # Step-by-step procedural guides
│
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

### 🏄 Cascade AI Configuration

The `.cascade/` directory contains rules and workflows that configure Cascade's behavior. This ensures consistent, standards-compliant development without manual intervention.

#### Structure

```
.cascade/
├── rules/          # Enforced constraints (MUST follow)
└── workflows/      # Step-by-step procedures (HOW to do tasks)
```

#### Rules (Enforced Constraints)

Rules are non-negotiable standards that Cascade automatically enforces:

- **DSPy Documentation Standards** - All `dspy.Signature` and `dspy.Module` classes must follow structured docstring formats
- **Hypothesis Traceability** - All branches, commits, and results must reference hypothesis IDs (H-XXX format)
- **Code Context Consultation** - Must check `CODE_CONTEXT.md` before implementing new code to prevent duplication

#### Workflows (Procedural Guides)

Workflows provide step-by-step processes for common tasks:

- **Session Start Protocol** - Reads `PROJECT_LOG.md` and `HYPOTHESES.md` to establish context
- **Pre-Implementation Checklist** - Ensures standards are consulted before writing code

#### Context Memories

Cascade maintains awareness of key project files:

- **Static Norms:** `.project_dev/DEV_NORMS.md`, `TDD_PROCESS.md`, `DOC_STANDARDS.md`
- **Code Context:** `.project_dev/CODE_CONTEXT.md` (auto-generated map of existing code)
- **Development Status:** `.project_dev/PROJECT_LOG.md` (session-to-session continuity)
- **R&D Plan:** `HYPOTHESES.md` (hypothesis-driven development tracking)

For detailed information about the Cascade configuration, see [`.cascade/README.md`](.cascade/README.md).
