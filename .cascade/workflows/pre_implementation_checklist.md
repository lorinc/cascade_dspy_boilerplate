# Workflow: Pre-Implementation Checklist

## When to Use

Before generating any code or implementation plan for new features or changes.

## Workflow Steps

### Step 1: Read Development Standards

Read the following files to understand project standards:

```bash
# Development norms
cat .project_dev/DEV_NORMS.md

# Testing approach
cat .project_dev/TDD_PROCESS.md

# Documentation rules
cat .project_dev/DOC_STANDARDS.md
```

**Purpose:** Ensure you understand:
- Branching strategy and commit standards
- Test-driven development process
- DSPy-specific documentation rules

### Step 2: Check Existing Code

Read the code context map:

```bash
# Existing modules and functions
cat .project_dev/CODE_CONTEXT.md
```

**Purpose:** Identify existing functionality to avoid duplication.

### Step 3: Verify Hypothesis Association

Check the hypothesis log:

```bash
# Current R&D plan
cat HYPOTHESES.md
```

**Actions:**
- If a relevant hypothesis exists → Use that H-XXX ID
- If no relevant hypothesis exists → Ask user to create one first

### Step 4: Plan Implementation

Based on the above context:
- Identify what needs to be implemented
- Determine if existing code can be reused
- Plan the test-first approach (TDD)
- Ensure all work follows documentation standards

## Checklist Summary

- [ ] Read DEV_NORMS.md
- [ ] Read TDD_PROCESS.md
- [ ] Read DOC_STANDARDS.md
- [ ] Read CODE_CONTEXT.md
- [ ] Verify hypothesis ID exists or create new one
- [ ] Plan test cases first
- [ ] Identify reusable existing code

## Rationale

Ensures all implementations:
- Follow project standards
- Don't duplicate existing code
- Are traceable to hypotheses
- Use test-driven development
- Have proper documentation
