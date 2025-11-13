# DSPy Workspace Setup Instructions

**For AI Assistant (Cascade/Windsurf):** Read this file and all companion files in this directory, then execute the setup.

## Quick Start

1. **Read all setup files:**
   - `SETUP_INSTRUCTIONS.md` (this file)
   - `SETUP_CONTENT_PART1.md` - Core project files
   - `SETUP_CONTENT_PART2.md` - Scripts and evaluation
   - `CASCADE_CONFIGURATION.md` - Cascade/Windsurf setup

2. **Create folder structure:**
   ```
   .cascade/rules/
   .cascade/workflows/
   .project_dev/
   config/
   logs/
   results/
   scripts/
   src/modules/
   src/signatures/
   test_data/
   ```

3. **Create all files** as specified in SETUP_CONTENT_PART1.md and SETUP_CONTENT_PART2.md

4. **Configure Cascade** using CASCADE_CONFIGURATION.md

## Folder Structure

```
project_root/
├── .cascade/
│   ├── README.md
│   ├── rules/
│   │   ├── dspy_documentation.md
│   │   ├── hypothesis_traceability.md
│   │   └── check_existing_code.md
│   └── workflows/
│       ├── session_start.md
│       └── pre_implementation_checklist.md
├── .project_dev/
│   ├── DEV_NORMS.md
│   ├── TDD_PROCESS.md
│   ├── DOC_STANDARDS.md
│   ├── CODE_CONTEXT.md
│   └── PROJECT_LOG.md
├── config/
│   ├── dev_config.json
│   └── prod_config.json
├── logs/
│   └── .gitignore
├── results/
│   └── .gitkeep
├── scripts/
│   └── generate_context_map.py
├── src/
│   ├── modules/
│   │   └── __init__.py
│   ├── signatures/
│   │   └── __init__.py
│   ├── __init__.py
│   └── main_pipeline.py
├── test_data/
│   ├── dev_set.jsonl
│   └── gold_set.jsonl
├── .gitignore
├── evaluate.py
├── HYPOTHESES.md
└── README.md
```

## Setup Order

1. Create all folders (including `.cascade/`)
2. Create all files in `.cascade/` (rules and workflows)
3. Create all files in `.project_dev/`
4. Create config files
5. Create source code structure
6. Create test data
7. Create scripts
8. Create root files (.gitignore, README.md, etc.)
9. Configure Cascade memories (rules and workflows auto-load from `.cascade/`)

## Verification

After setup, verify:
- [ ] All folders exist (including `.cascade/`)
- [ ] All files have content (not empty)
- [ ] `.cascade/` directory contains rules and workflows
- [ ] `scripts/generate_context_map.py` is executable
- [ ] Cascade memories are configured
- [ ] Cascade automatically loads rules and workflows from `.cascade/`

## Next Steps

After setup:
1. Run `python scripts/generate_context_map.py` to populate CODE_CONTEXT.md
2. Add your first hypothesis to HYPOTHESES.md
3. Start development with the `Start_Day_Session` workflow
