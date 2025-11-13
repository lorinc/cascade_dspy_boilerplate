# Cascade/Windsurf Configuration Guide

**IMPORTANT:** After creating all files from SETUP_CONTENT_PART1.md and SETUP_CONTENT_PART2.md, configure Cascade with the following memories, rules, and workflows.

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

## Part 2: Cascade Rules

Rules are high-level instructions that govern AI behavior at all times.

### Rule 1: Read Before Writing

**Name:** `Read Before Writing`

**Content:**
```
Before generating any code or plan, you MUST read the contents of the Static Norms Memory and the Code Context Memory. This ensures you understand the project standards and existing code before making changes.
```

---

### Rule 2: Context-First

**Name:** `Context-First`

**Content:**
```
Before implementing any new function, class, or dspy.Signature, you MUST consult the Code Context Memory. If similar functionality exists, propose its reuse. Do not re-implement existing logic. Always check CODE_CONTEXT.md first.
```

---

### Rule 3: DSPy Documentation Standard

**Name:** `DSPy Documentation Standard`

**Content:**
```
CRITICAL: Adhere strictly to DOC_STANDARDS.md for DSPy-idiomatic documentation:

- dspy.Signature docstrings MUST be purely functional (concise task instructions for the LLM)
- dspy.Signature docstrings are NOT for human/AI context - they are optimized by Teleprompters
- dspy.Module docstrings MUST include: Purpose, Role in execution, and Assumptions
- dspy.Module docstrings are the designated place for human/AI context
- Utility functions use standard Python docstrings (Purpose, Role, Assumptions)
- Commit message format: [H-XXX] Type: Description
- Branch naming: feature/H-XXX-description
- Follow test-driven development process from TDD_PROCESS.md
```

---

### Rule 4: Traceability

**Name:** `Traceability`

**Content:**
```
Every new feature or experiment MUST be associated with an ID from the Hypothesis Memory (HYPOTHESES.md). Use the format H-XXX in all commits, branches, and results directories. This ensures all work is traceable to a specific hypothesis.
```

---

### Rule 5: Status Aware

**Name:** `Status Aware`

**Content:**
```
At the beginning of any new session, you MUST read the Dynamic Status Memory (PROJECT_LOG.md) to understand the last-known state. Summarize what was done previously and what the next steps are before proceeding with new work.
```

---

## Part 3: Cascade Workflows

Workflows are automated multi-step processes for common tasks.

### Workflow 1: Start_Day_Session

**Name:** `Start Day Session`

**Trigger:** User starts a new session or says "Let's start" / "Good morning"

**Steps:**

1. Read `Dynamic Status Memory` (`.project_dev/PROJECT_LOG.md`)
2. Read `Hypothesis Memory` (`HYPOTHESES.md`)
3. Summarize for the user:
   - "Welcome back. Here is the last-known status: [Summary of last entry in PROJECT_LOG.md]"
   - "The current open hypotheses are: [List hypotheses with 'Pending' or 'In Progress' status]"
   - "What is our objective today?"

**Implementation:**
```
STEP 1: Read file .project_dev/PROJECT_LOG.md
STEP 2: Read file HYPOTHESES.md
STEP 3: Provide summary to user with:
  - Last session summary
  - Open hypotheses
  - Ask for today's objective
```

---

### Workflow 2: Start_New_Feature

**Name:** `Start New Feature`

**Trigger:** User asks to build a new feature (e.g., "Let's add a summarization module")

**Steps:**

1. Ask: "Which Hypothesis ID from HYPOTHESES.md does this feature test?" (User provides ID, e.g., H-002)
2. Read `Static Norms Memory` (specifically `TDD_PROCESS.md` and `DOC_STANDARDS.md`)
3. Read `Code Context Memory` (`.project_dev/CODE_CONTEXT.md`)
4. Confirm: "Understood. Per TDD_PROCESS.md, I will first create a new test file in test_data/ and add a failing test to evaluate.py for Hypothesis H-XXX. Please confirm."
5. Proceed with TDD loop

**Implementation:**
```
STEP 1: Ask user for Hypothesis ID
STEP 2: Read .project_dev/TDD_PROCESS.md
STEP 3: Read .project_dev/DOC_STANDARDS.md
STEP 4: Read .project_dev/CODE_CONTEXT.md
STEP 5: Propose test-first approach
STEP 6: Wait for confirmation
STEP 7: Implement TDD loop
```

---

### Workflow 3: Run_Full_Experiment

**Name:** `Run Full Experiment`

**Trigger:** User wants to validate a completed POC (e.g., "Let's run the full evaluation")

**Steps:**

1. Ask: "Which Hypothesis ID are we evaluating?" (User provides H-XXX)
2. Confirm: "I will now run the full test harness against the gold set and save the results to a new, version-controlled directory."
3. Execute command:
   ```bash
   python evaluate.py --config config/dev_config.json \
     --test_set test_data/gold_set.jsonl \
     --output_dir results/H-XXX_eval_$(date +%Y-%m-%d)
   ```
4. Wait for completion
5. Summarize: "Evaluation complete. The outputs are in results/H-XXX_eval_YYYY-MM-DD/. The metrics.json file shows: [Key metrics]. How should we update HYPOTHESES.md?"

**Implementation:**
```
STEP 1: Ask user for Hypothesis ID
STEP 2: Confirm action
STEP 3: Run command: python evaluate.py --config config/dev_config.json --test_set test_data/gold_set.jsonl --output_dir results/H-XXX_eval_$(date +%Y-%m-%d)
STEP 4: Read results/H-XXX_eval_*/metrics.json
STEP 5: Summarize results and ask how to update HYPOTHESES.md
```

---

### Workflow 4: Update_Code_Context

**Name:** `Update Code Context`

**Trigger:** User asks "Update the code context" or after a new module is merged

**Steps:**

1. Confirm: "Updating the code context map..."
2. Execute command: `python scripts/generate_context_map.py`
3. Verify: "The script has successfully scanned all src/modules/ for dspy.Module classes and extracted their docstrings (Purpose, Role, Assumptions). Per DOC_STANDARDS.md, dspy.Signature docstrings were NOT included as they are functional LLM instructions."
4. Confirm: "The CODE_CONTEXT.md file in the Code Context Memory is now up-to-date with the latest src/ directory."

**Implementation:**
```
STEP 1: Announce action
STEP 2: Run command: python scripts/generate_context_map.py
STEP 3: Verify script extracted Module docstrings and ignored Signature docstrings
STEP 4: Confirm completion
```

---

### Workflow 5: End_Day_Session

**Name:** `End Day Session`

**Trigger:** User says "Let's wrap up" / "End session" / "That's all for today"

**Steps:**

1. Prompt user: "Okay. To update the PROJECT_LOG.md, please summarize:
   - What did we try today?
   - What were the key decisions or results?
   - What is the next step for tomorrow?"
2. Wait for user's answers
3. Format the answers with a timestamp
4. Append to `.project_dev/PROJECT_LOG.md`
5. Confirm: "The project log is updated. Session concluded."

**Implementation:**
```
STEP 1: Ask user for session summary (what tried, decisions, next steps)
STEP 2: Format response with timestamp
STEP 3: Append to .project_dev/PROJECT_LOG.md
STEP 4: Confirm completion
```

---

## Configuration Instructions for Cascade/Windsurf

### How to Set Up Memories:

1. Open Cascade/Windsurf settings
2. Navigate to "Memories" or "Context" section
3. Create 4 new memories as specified above
4. For each memory, add the file paths listed
5. Save and verify the memories are active

### How to Set Up Rules:

1. Open Cascade/Windsurf settings
2. Navigate to "Rules" or "Instructions" section
3. Create 5 new rules as specified above
4. Copy the content exactly as written
5. Set rules to "Always Active"
6. Save and verify rules are enabled

### How to Set Up Workflows:

1. Open Cascade/Windsurf settings
2. Navigate to "Workflows" or "Automations" section
3. Create 5 new workflows as specified above
4. For each workflow, define:
   - Trigger phrase or condition
   - Sequential steps to execute
   - Expected outputs
5. Test each workflow after creation
6. Save and verify workflows are active

---

## Verification Checklist

After configuration, verify:

- [ ] All 4 memories are created and pointing to correct files
- [ ] All 5 rules are active and enabled
- [ ] All 5 workflows are created and functional
- [ ] Test "Start Day Session" workflow by saying "Let's start"
- [ ] Test "Update Code Context" workflow by saying "Update the code context"
- [ ] Verify AI reads PROJECT_LOG.md at session start
- [ ] Verify AI checks CODE_CONTEXT.md before implementing new code
- [ ] Verify AI asks for Hypothesis ID when starting new features

---

## Alternative: Manual Configuration

If Cascade/Windsurf doesn't have a UI for memories/rules/workflows, you can:

1. **Create a `.cascade/` or `.windsurf/` directory** in the project root
2. **Create configuration files:**
   - `memories.json` - List of file paths to always load
   - `rules.md` - Markdown file with all rules
   - `workflows.json` - JSON defining workflow triggers and steps

3. **Reference these in your IDE settings** or workspace configuration

Example `memories.json`:
```json
{
  "memories": [
    {
      "name": "Static Norms Memory",
      "files": [
        ".project_dev/DEV_NORMS.md",
        ".project_dev/TDD_PROCESS.md",
        ".project_dev/DOC_STANDARDS.md"
      ]
    },
    {
      "name": "Code Context Memory",
      "files": [".project_dev/CODE_CONTEXT.md"]
    },
    {
      "name": "Dynamic Status Memory",
      "files": [".project_dev/PROJECT_LOG.md"]
    },
    {
      "name": "Hypothesis Memory",
      "files": ["HYPOTHESES.md"]
    }
  ]
}
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
