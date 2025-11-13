#!/usr/bin/env python3
"""
Automated DSPy Workspace Setup Script

Purpose: Creates the complete folder structure and all files for a DSPy project
         following the 3-pillar framework.

Usage: 
    python setup_workspace.py [target_directory]
    
    If no target_directory is provided, creates in current directory.

Note: This script reads from SETUP_CONTENT_PART1.md and SETUP_CONTENT_PART2.md
      to extract file contents.
"""

import os
import sys
import json
from pathlib import Path


def create_folder_structure(base_path):
    """Create all required folders."""
    folders = [
        '.project_dev',
        'config',
        'logs',
        'results',
        'scripts',
        'src/modules',
        'src/signatures',
        'test_data'
    ]
    
    print("Creating folder structure...")
    for folder in folders:
        folder_path = base_path / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"  ✓ {folder}/")
    print()


def create_file(base_path, filepath, content):
    """Create a file with given content."""
    file_path = base_path / filepath
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✓ {filepath}")


def setup_workspace(target_dir=None):
    """Main setup function."""
    if target_dir:
        base_path = Path(target_dir).resolve()
    else:
        base_path = Path.cwd()
    
    print(f"\n{'='*60}")
    print(f"DSPy Workspace Setup")
    print(f"{'='*60}")
    print(f"Target directory: {base_path}\n")
    
    # Create folder structure
    create_folder_structure(base_path)
    
    # Create files
    print("Creating files...")
    
    # .project_dev files
    create_file(base_path, '.project_dev/DEV_NORMS.md', """# Development Norms

## Branching Strategy

- **Main Branch:** `main` - Always production-ready, protected
- **Feature Branches:** `feature/H-XXX-description` - Linked to hypothesis ID
- **Experiment Branches:** `experiment/H-XXX-description` - For POCs that may be discarded
- **Hotfix Branches:** `hotfix/description` - For urgent production fixes

## Commit Standards

- **Format:** `[H-XXX] Type: Brief description`
- **Types:** `feat`, `fix`, `test`, `docs`, `refactor`, `perf`, `chore`
- **Examples:**
  - `[H-001] feat: Add ChainOfThought to RAG module`
  - `[H-002] test: Add evaluation for summarization accuracy`

## Pull Request Process

1. **Title Format:** `[H-XXX] Brief description of change`
2. **Required Sections:**
   - **Hypothesis:** Link to the hypothesis being tested
   - **Changes:** Bullet list of key changes
   - **Test Results:** Link to `results/H-XXX_eval_YYYY-MM-DD/metrics.json`
   - **Learnings:** What did we learn?
3. **Approval:** Requires passing evaluation metrics and code review
4. **Merge:** Squash and merge to keep history clean

## Code Review Checklist

- [ ] All `dspy.Module` classes have proper docstrings (Purpose, Role in execution, Assumptions)
- [ ] All `dspy.Signature` docstrings are purely functional (task instructions only)
- [ ] Utility functions have proper docstrings (Purpose, Role, Assumptions)
- [ ] Tests pass with `evaluate.py`
- [ ] Results are committed to `results/` directory
- [ ] `HYPOTHESES.md` is updated with outcome
- [ ] `CODE_CONTEXT.md` is regenerated if new modules added
""")
    
    create_file(base_path, '.project_dev/TDD_PROCESS.md', """# Test-Driven Development Process

## Philosophy

For DSPy applications, "testing" means **evaluation against a gold set**. The primary test is: "Does this change improve the metrics on our evaluation dataset?"

## The TDD Loop

### 1. Write the Test First

Before implementing any feature:
1. Add new test cases to `test_data/dev_set.jsonl`
2. Define expected behavior in `dspy.Example` format
3. Update `evaluate.py` to include the new metric

### 2. Run and Fail

```bash
python evaluate.py --config config/dev_config.json --test_set test_data/dev_set.jsonl
```

Expected: The test should fail or show poor metrics.

### 3. Implement the Feature

- Write minimal code to pass the test
- Follow `DOC_STANDARDS.md` for all docstrings
- Consult `CODE_CONTEXT.md` to avoid reimplementing existing logic

### 4. Run and Pass

```bash
python evaluate.py --config config/dev_config.json --test_set test_data/dev_set.jsonl
```

Expected: Metrics improve or test passes.

### 5. Full Evaluation

Run against the full gold set:

```bash
python evaluate.py --config config/dev_config.json \\
  --test_set test_data/gold_set.jsonl \\
  --output_dir results/H-XXX_eval_$(date +%Y-%m-%d)
```

### 6. Commit Results

```bash
git add results/H-XXX_eval_YYYY-MM-DD/
git commit -m "[H-XXX] test: Full evaluation results"
```

## What Defines a "Pass"?

1. **Functional:** Code runs without errors
2. **Metric Improvement:** Key metrics meet or exceed baseline
3. **No Regression:** Performance on existing tests doesn't degrade
4. **Reproducible:** Same commit produces identical results

## Red Flags

- **Overfitting:** Great on dev_set but poor on gold_set
- **Latency Creep:** Accuracy improves but response time degrades
- **Prompt Brittleness:** Small input changes cause failures
""")
    
    create_file(base_path, '.project_dev/DOC_STANDARDS.md', """# Documentation Standards

## CRITICAL: DSPy-Specific Documentation Rules

**DSPy Signatures are functional code, not decorative documentation.**

| Artifact | Purpose | Docstring Usage | Scraped for Docs? |
|----------|---------|-----------------|-------------------|
| **`dspy.Signature`** | Functional LLM instruction | Task definition ONLY | **NO** |
| **`dspy.Module`** | Human/AI context | Purpose, Role, Assumptions | **YES** |
| **Utility Functions** | Standard Python docs | Standard docstrings | **YES** |

---

## Docstring Format by Type

### 1. DSPy Module Docstrings (HUMAN/AI CONTEXT)

**Template:**

```python
class MyModule(dspy.Module):
    \"\"\"
    Purpose: [One sentence: What does this module do?]
    
    Role in execution: [One sentence: Where does this fit in the pipeline?]
    
    Assumptions:
    - [Key assumption 1]
    - [Key assumption 2]
    - [Dependencies, constraints, expected inputs/outputs]
    \"\"\"
    def __init__(self, config):
        super().__init__()
        # ... implementation
```

**Example:**

```python
class RAGModule(dspy.Module):
    \"\"\"
    Purpose: Retrieves relevant documents and generates an answer using RAG.
    
    Role in execution: Core QA module in the main pipeline, called after query preprocessing.
    
    Assumptions:
    - Requires a configured retriever (e.g., ColBERTv2)
    - Expects input: {"question": str}
    - Returns: {"answer": str, "sources": List[str]}
    - Minimum 3 documents retrieved per query
    \"\"\"
    def __init__(self, retriever):
        super().__init__()
        self.retriever = retriever
        self.generate = dspy.ChainOfThought(SummarizeSignature)
```

---

### 2. DSPy Signature Docstrings (FUNCTIONAL ONLY)

**CRITICAL:** Signature docstrings are instructions sent to the LLM. They are optimized by Teleprompters. Keep them purely functional.

**Template:**

```python
class MySignature(dspy.Signature):
    \"\"\"[Concise task instruction for the LLM]\"\"\"
    
    input_field = dspy.InputField(desc="Description of input")
    output_field = dspy.OutputField(desc="Description of expected output")
```

**Example:**

```python
class SummarizeSignature(dspy.Signature):
    \"\"\"Generate a concise 2-3 sentence summary of the document.\"\"\"
    
    document = dspy.InputField(desc="The full text to summarize")
    summary = dspy.OutputField(desc="A 2-3 sentence summary")
```

**DO NOT add Purpose/Role/Assumptions to Signature docstrings!**

---

### 3. Utility Function Docstrings (STANDARD PYTHON)

**Template:**

```python
def my_function(param1: str, param2: int) -> dict:
    \"\"\"
    Purpose: [One sentence: What does this do?]
    
    Role: [One sentence: Where is this used?]
    
    Assumptions:
    - Assumes param1 is valid JSON
    - Requires param2 > 0
    \"\"\"
    pass
```

---

## Auto-Generated Documentation

`CODE_CONTEXT.md` is auto-generated by `scripts/generate_context_map.py`. It:
- **Extracts and lists** all `dspy.Module` classes with their full docstrings
- **Ignores** `dspy.Signature` docstrings (they are functional, not for human docs)
- **Lists** all utility functions with their signatures and docstrings

This ensures the AI assistant has a complete map of the codebase without polluting its context with functional LLM instructions.
""")
    
    create_file(base_path, '.project_dev/CODE_CONTEXT.md', """# Code Context Map

**Last Updated:** [Auto-generated timestamp]

**Purpose:** High-level map of all modules, signatures, and functions. Auto-generated by `scripts/generate_context_map.py`.

---

## DSPy Modules

*No modules defined yet. Run `scripts/generate_context_map.py` after creating your first module.*

---

## DSPy Signatures

*No signatures defined yet.*

---

## Utility Functions

*No utility functions defined yet.*

---

**Note:** This file is automatically regenerated. Do not edit manually.
""")
    
    create_file(base_path, '.project_dev/PROJECT_LOG.md', """# Project Development Log

**Purpose:** Tracks session-to-session progress, decisions, and next steps. The AI assistant's "short-term memory."

---

## Session: [YYYY-MM-DD]

### What We Tried
- [Bullet list of experiments or features attempted]

### Key Decisions
- [Important decisions made]

### Results
- [Key metrics or outcomes]

### Next Steps
- [What to do in the next session]

---

*Add new session entries above this line*
""")
    
    # Root files
    create_file(base_path, 'HYPOTHESES.md', """# Hypothesis Log

**Purpose:** The R&D plan. Each hypothesis represents an assumption to be tested.

---

## Active Hypotheses

### H-001: [Hypothesis Title]

**Hypothesis:** We believe that [specific change] will [expected outcome] because [reasoning].

**POC Branch/Commit:** `feature/H-001-description` or `abc123def`

**Test Plan:**
- Metric to measure: [e.g., accuracy, latency, F1 score]
- Test set: `test_data/gold_set.jsonl`
- Success criteria: [e.g., "Accuracy > 85%"]

**Status:** `Pending` | `In Progress` | `Completed`

**Outcome:** [To be filled after evaluation]
- **Result:** `Lesson` | `Feature` | `Rejected`
- **Metrics:** [Link to `results/H-001_eval_YYYY-MM-DD/metrics.json`]
- **Actionable Lesson:** [What did we learn?]

---

## Completed Hypotheses

*Move completed hypotheses here for historical reference*
""")
    
    # Config files
    dev_config = {
        "llm": {
            "model": "gpt-4o-mini",
            "temperature": 0.0,
            "max_tokens": 2000,
            "api_key_env": "OPENAI_API_KEY"
        },
        "retriever": {
            "type": "colbertv2",
            "index_path": "./data/colbert_index",
            "k": 5
        },
        "evaluation": {
            "metrics": ["accuracy", "f1", "latency"],
            "verbose": True
        },
        "logging": {
            "level": "DEBUG",
            "output_file": "logs/evaluation.log"
        }
    }
    
    prod_config = dev_config.copy()
    prod_config["llm"]["model"] = "gpt-4o"
    prod_config["evaluation"]["verbose"] = False
    prod_config["logging"]["level"] = "INFO"
    
    create_file(base_path, 'config/dev_config.json', json.dumps(dev_config, indent=2))
    create_file(base_path, 'config/prod_config.json', json.dumps(prod_config, indent=2))
    
    # Other files
    create_file(base_path, 'logs/.gitignore', "*\n!.gitignore\n")
    create_file(base_path, 'results/.gitkeep', "# This file ensures the results/ directory is tracked by git\n")
    
    # Test data
    create_file(base_path, 'test_data/dev_set.jsonl', 
                '{"input": "What is DSPy?", "expected_output": "DSPy is a framework for programming with language models."}\n' +
                '{"input": "How do I create a signature?", "expected_output": "Create a class that inherits from dspy.Signature and define input/output fields."}\n')
    
    create_file(base_path, 'test_data/gold_set.jsonl',
                '{"input": "What is DSPy?", "expected_output": "DSPy is a framework for programming with language models."}\n' +
                '{"input": "How do I create a signature?", "expected_output": "Create a class that inherits from dspy.Signature and define input/output fields."}\n' +
                '{"input": "What is a dspy.Module?", "expected_output": "A dspy.Module is a building block that encapsulates logic and can be composed into pipelines."}\n')
    
    # .gitignore
    create_file(base_path, '.gitignore', """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# Logs
logs/
*.log

# Environment
.env
.env.local

# Data
data/
*.db
*.sqlite

# OS
.DS_Store
Thumbs.db

# Jupyter
.ipynb_checkpoints/

# DSPy cache
.dspy_cache/
""")
    
    # Note about remaining files
    print("\n" + "="*60)
    print("Setup complete!")
    print("="*60)
    print("\nNote: The following files need to be created from")
    print("      SETUP_CONTENT_PART2.md (too large for this script):")
    print("  - scripts/generate_context_map.py")
    print("  - src/__init__.py")
    print("  - src/modules/__init__.py")
    print("  - src/signatures/__init__.py")
    print("  - src/main_pipeline.py")
    print("  - evaluate.py")
    print("  - README.md")
    print("\nPlease refer to SETUP_CONTENT_PART2.md for their contents.")
    print("\nNext steps:")
    print("1. Create the remaining files from SETUP_CONTENT_PART2.md")
    print("2. Configure Cascade using CASCADE_CONFIGURATION.md")
    print("3. Run: python scripts/generate_context_map.py")
    print("4. Start development!\n")


if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else None
    setup_workspace(target)
