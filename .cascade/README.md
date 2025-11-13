# Cascade Configuration

This directory contains rules and workflows for the Cascade AI assistant.

## Structure

```
.cascade/
├── rules/          # Non-negotiable constraints that must always be followed
└── workflows/      # Step-by-step processes and procedures
```

## Rules

Rules are **enforced constraints** that the AI must follow:

- **`dspy_documentation.md`** - DSPy-specific documentation standards (CRITICAL)
- **`hypothesis_traceability.md`** - All work must be traceable to hypothesis IDs
- **`check_existing_code.md`** - Consult CODE_CONTEXT.md before implementing new code

## Workflows

Workflows are **procedural guides** for common tasks:

- **`session_start.md`** - Protocol for starting a new session
- **`pre_implementation_checklist.md`** - Checklist before implementing new features

## Relationship to .project_dev/

The `.project_dev/` directory contains the **source of truth** for development standards:
- `DEV_NORMS.md` - Branching, commits, PR process
- `TDD_PROCESS.md` - Test-driven development approach
- `DOC_STANDARDS.md` - Complete documentation standards
- `CODE_CONTEXT.md` - Auto-generated code map
- `PROJECT_LOG.md` - Session-to-session development log

The `.cascade/` directory **references** these files and provides:
- Enforcement rules for critical standards
- Procedural workflows for common tasks
- Quick reference for the AI assistant

## Usage

Cascade automatically reads rules and workflows from this directory. You can:
- Add new rules for additional constraints
- Add new workflows for common procedures
- Update existing rules/workflows as standards evolve

## Maintenance

- Keep rules concise and enforceable
- Keep workflows actionable and step-by-step
- Reference `.project_dev/` files for detailed documentation
- Update when project standards change
