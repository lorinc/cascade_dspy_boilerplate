# Rule: Check Existing Code Before Implementation

## Enforcement Level: REQUIRED

Prevent code duplication by consulting existing code maps before implementation.

## Rule Statement

Before implementing any new function, class, or `dspy.Signature`, you MUST:

1. **Read** `.project_dev/CODE_CONTEXT.md`
2. **Search** for similar functionality
3. **Decide:**
   - If similar functionality exists → Propose reuse or extension
   - If no similar functionality exists → Proceed with implementation

## What CODE_CONTEXT.md Contains

- All `dspy.Module` classes with full docstrings (Purpose, Role, Assumptions)
- All `dspy.Signature` names (docstrings excluded as they're functional)
- All utility functions with signatures and docstrings

## Actions Required

### If Similar Functionality Exists
- **Propose reuse** instead of reimplementation
- **Extend existing modules** rather than creating duplicates
- **Explain** why reuse is preferred

### If No Similar Functionality Exists
- **Proceed** with implementation
- **Follow** DOC_STANDARDS.md for documentation
- **Regenerate** CODE_CONTEXT.md after adding new modules:
  ```bash
  python scripts/generate_context_map.py
  ```

## Rationale

- Prevents code duplication
- Maintains consistency across the codebase
- Reduces maintenance burden
- Leverages existing tested functionality

## Reference

See `.project_dev/CODE_CONTEXT.md` for the current code map.
