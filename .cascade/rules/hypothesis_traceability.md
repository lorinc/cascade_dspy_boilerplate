# Rule: Hypothesis Traceability

## Enforcement Level: REQUIRED

All development work must be traceable to a hypothesis ID.

## Rule Statement

Every feature, experiment, or change MUST be associated with a hypothesis ID in the format `H-XXX`.

### Required Usage

1. **Commit Messages**
   - Format: `[H-XXX] Type: Description`
   - Types: `feat`, `fix`, `test`, `docs`, `refactor`, `perf`, `chore`
   - Example: `[H-001] feat: Add ChainOfThought to RAG module`

2. **Branch Names**
   - Feature branches: `feature/H-XXX-description`
   - Experiment branches: `experiment/H-XXX-description`
   - Example: `feature/H-001-add-cot-rag`

3. **Results Directories**
   - Format: `results/H-XXX_eval_YYYY-MM-DD/`
   - Example: `results/H-001_eval_2024-11-13/`

## Before Starting Work

Before implementing any new feature or experiment:

1. Check if a relevant hypothesis exists in `HYPOTHESES.md`
2. If yes, use that hypothesis ID
3. If no, ask the user to create a new hypothesis entry first

## Rationale

- Maintains clear R&D history
- Links code changes to experimental outcomes
- Enables tracing decisions back to original assumptions
- Facilitates learning from both successes and failures

## Reference

See `HYPOTHESES.md` for the current R&D plan and hypothesis structure.
