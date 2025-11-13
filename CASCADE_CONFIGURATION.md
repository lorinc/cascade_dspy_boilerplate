# Cascade/Windsurf Configuration Guide

**IMPORTANT:** After creating all files from SETUP_CONTENT_PART1.md and SETUP_CONTENT_PART2.md, configure Cascade with the following memories. Rules and workflows are now automatically loaded from the `.cascade/` directory.

---

## Part 1: Cascade Memories

Memories provide the AI with persistent access to project context files.

### Memory 1: Static Norms Memory

**Name:** `Static Norms Memory`

**Description:** Fixed development rules and standards

**Files to Include:**
- `.project_dev/DEV_NORMS.md`
- `.project_dev/TDD_PROCESS.md`
- `.project_dev/DOC_STANDARDS.md`

**Purpose:** Provides the AI with the "rules of the road" for development

---

### Memory 2: Code Context Memory

**Name:** `Code Context Memory`

**Description:** Auto-generated map of all existing code

**Files to Include:**
- `.project_dev/CODE_CONTEXT.md`

**Purpose:** Prevents the AI from reimplementing existing functionality

**Note:** This file's content is updated by running `python scripts/generate_context_map.py`, but the memory pointer stays the same

---

### Memory 3: Dynamic Status Memory

**Name:** `Dynamic Status Memory`

**Description:** Session-to-session development log

**Files to Include:**
- `.project_dev/PROJECT_LOG.md`

**Purpose:** Provides continuity between sessions - the AI's "short-term memory"

---

### Memory 4: Hypothesis Memory

**Name:** `Hypothesis Memory`

**Description:** R&D plan and experiment tracking

**Files to Include:**
- `HYPOTHESES.md`

**Purpose:** Gives the AI awareness of the R&D plan and the "why" behind tasks

---

## Part 2: Cascade Rules & Workflows

**Rules and workflows are now automatically loaded from the `.cascade/` directory.**

The `.cascade/` directory contains:
- **`.cascade/rules/`** - Enforced constraints that Cascade must follow
- **`.cascade/workflows/`** - Step-by-step procedural guides for common tasks

For details on what rules and workflows are configured, see:
- [`.cascade/README.md`](.cascade/README.md) - Overview of the Cascade configuration
- Individual rule files in `.cascade/rules/`
- Individual workflow files in `.cascade/workflows/`

### Current Rules (in `.cascade/rules/`)

1. **DSPy Documentation Standards** - Enforces structured docstrings for Signatures and Modules
2. **Hypothesis Traceability** - Requires H-XXX format in commits, branches, and results
3. **Code Context Consultation** - Requires checking CODE_CONTEXT.md before implementing new code

### Current Workflows (in `.cascade/workflows/`)

1. **Session Start Protocol** - Reads PROJECT_LOG.md and HYPOTHESES.md to establish context
2. **Pre-Implementation Checklist** - Ensures standards are consulted before writing code

---

## Configuration Instructions for Cascade/Windsurf

### How to Set Up Memories:

1. Open Cascade/Windsurf settings
2. Navigate to "Memories" or "Context" section
3. Create 4 new memories as specified above
4. For each memory, add the file paths listed
5. Save and verify the memories are active

### Rules & Workflows:

**No manual configuration needed!** Cascade automatically reads rules and workflows from the `.cascade/` directory.

The `.cascade/` directory is already included in your project structure and contains:
- Pre-configured rules in `.cascade/rules/`
- Pre-configured workflows in `.cascade/workflows/`
- Documentation in `.cascade/README.md`

---

## Verification Checklist

After configuration, verify:

- [ ] All 4 memories are created and pointing to correct files
- [ ] The `.cascade/` directory exists with rules and workflows
- [ ] Cascade can read files from `.cascade/rules/` and `.cascade/workflows/`
- [ ] Verify AI reads PROJECT_LOG.md at session start
- [ ] Verify AI checks CODE_CONTEXT.md before implementing new code
- [ ] Verify AI asks for Hypothesis ID when starting new features

---

## Directory Structure

The `.cascade/` directory structure:

```
.cascade/
├── README.md              # Overview of Cascade configuration
├── MEMORY_MIGRATION.md    # Migration notes from old memory system
├── rules/                 # Enforced constraints
│   ├── dspy_documentation.md
│   ├── hypothesis_traceability.md
│   └── check_existing_code.md
└── workflows/             # Procedural guides
    ├── session_start.md
    └── pre_implementation_checklist.md
```

---

## Usage After Setup

Once everything is configured:

1. **Start a new session:** Say "Let's start" to trigger Start_Day_Session workflow
2. **Begin new work:** Say "Let's add [feature]" to trigger Start_New_Feature workflow
3. **Run evaluations:** Say "Let's run the full evaluation" to trigger Run_Full_Experiment
4. **Update context:** Say "Update the code context" after adding new modules
5. **End session:** Say "Let's wrap up" to trigger End_Day_Session workflow

The AI will automatically:
- Read relevant context files before responding
- Follow TDD process
- Check for existing code before implementing
- Track all work to hypothesis IDs
- Maintain session continuity via PROJECT_LOG.md
