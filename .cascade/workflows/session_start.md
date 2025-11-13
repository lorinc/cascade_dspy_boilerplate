# Workflow: Session Start Protocol

## When to Use

At the beginning of any new session or when the user starts working on the project.

## Workflow Steps

### Step 1: Read Project Log
```bash
# Read the dynamic status memory
cat .project_dev/PROJECT_LOG.md
```

**Purpose:** Understand the last-known state of the project.

### Step 2: Summarize Previous Work

Provide a concise summary including:
- What was done in the last session
- Key decisions that were made
- Results achieved
- Current state of the project

### Step 3: Identify Next Steps

Based on the project log, identify:
- Incomplete tasks from the previous session
- Logical next steps in the development process
- Any blockers or dependencies

### Step 4: Confirm or Adjust Plan

Present the summary and next steps to the user:
- Ask if the identified next steps are correct
- Allow the user to adjust priorities
- Clarify any ambiguities before proceeding

## Example Output

```
## Session Summary

### Previous Session (2024-11-12)
- Implemented H-001: ChainOfThought for RAG module
- Ran evaluation on dev set, achieved 78% accuracy
- Identified issue with retrieval quality

### Next Steps
1. Investigate retrieval quality issue
2. Run full evaluation on gold set
3. Update HYPOTHESES.md with results

Does this align with your priorities, or would you like to adjust?
```

## Session End Protocol

At the end of a session, update `PROJECT_LOG.md` with:
- **What We Tried:** Experiments or features attempted
- **Key Decisions:** Important decisions made
- **Results:** Key metrics or outcomes
- **Next Steps:** What to do in the following session

## Rationale

Maintains continuity between sessions and prevents lost context.
