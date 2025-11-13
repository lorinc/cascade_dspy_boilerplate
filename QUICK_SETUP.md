# Quick Setup Guide - TL;DR

**For AI Assistant:** This is your checklist. Execute all steps to set up the complete DSPy workspace.

---

## Step 1: Create All Folders

Execute these commands:

```bash
mkdir -p .cascade/rules
mkdir -p .cascade/workflows
mkdir -p .project_dev
mkdir -p config
mkdir -p logs
mkdir -p results
mkdir -p scripts
mkdir -p src/modules
mkdir -p src/signatures
mkdir -p test_data
```

---

## Step 2: Create All Files

Read `SETUP_CONTENT_PART1.md` and create:
- `.project_dev/DEV_NORMS.md`
- `.project_dev/TDD_PROCESS.md`
- `.project_dev/DOC_STANDARDS.md`
- `.project_dev/CODE_CONTEXT.md`
- `.project_dev/PROJECT_LOG.md`
- `HYPOTHESES.md`
- `config/dev_config.json`
- `config/prod_config.json`
- `logs/.gitignore`
- `results/.gitkeep`
- `test_data/dev_set.jsonl`
- `test_data/gold_set.jsonl`
- `.gitignore`

Read `SETUP_CONTENT_PART2.md` and create:
- `scripts/generate_context_map.py`
- `src/__init__.py`
- `src/modules/__init__.py`
- `src/signatures/__init__.py`
- `src/main_pipeline.py`
- `evaluate.py`
- `README.md`

**IMPORTANT:** Copy the exact content from the setup files. Do not create empty files.

---

## Step 3: Make Scripts Executable

```bash
chmod +x scripts/generate_context_map.py
chmod +x evaluate.py
```

---

## Step 4: Configure Cascade

Read `CASCADE_CONFIGURATION.md` and configure:

### 4.1 Create 4 Memories:
1. **Static Norms Memory** → `.project_dev/DEV_NORMS.md`, `TDD_PROCESS.md`, `DOC_STANDARDS.md`
2. **Code Context Memory** → `.project_dev/CODE_CONTEXT.md`
3. **Dynamic Status Memory** → `.project_dev/PROJECT_LOG.md`
4. **Hypothesis Memory** → `HYPOTHESES.md`

### 4.2 Rules & Workflows:
**Automatically loaded from `.cascade/` directory** - No manual configuration needed!
- Rules are in `.cascade/rules/`
- Workflows are in `.cascade/workflows/`
- See `.cascade/README.md` for details

---

## Step 5: Verify Setup

Check that:
- [ ] All folders exist (including `.cascade/`)
- [ ] All files exist and have content (not empty)
- [ ] Scripts are executable
- [ ] Cascade memories are configured
- [ ] `.cascade/` directory contains rules and workflows

---

## Step 6: Initial Test

Run the context map generator:

```bash
python scripts/generate_context_map.py
```

Expected output:
```
✓ Generated .project_dev/CODE_CONTEXT.md
  - 1 modules
  - 0 signatures
  - 1 functions
```

---

## What You've Built

A complete DSPy development workspace with:

✅ **System of Record** - AI context management via `.project_dev/`
✅ **Hypothesis-Driven Development** - R&D tracking via `HYPOTHESES.md`
✅ **Reproducible Test Harness** - Evaluation framework via `evaluate.py`
✅ **Cascade Integration** - Memories, rules, and workflows for AI assistance

---

## Next Steps

1. Add your first hypothesis to `HYPOTHESES.md`
2. Start a session by saying "Let's start" to the AI
3. Begin development following the TDD process
4. Run evaluations and track results
5. Update PROJECT_LOG.md at end of each session

---

## File Manifest

**Total Files:** 23
**Total Folders:** 8

### Documentation (5):
- `.project_dev/DEV_NORMS.md`
- `.project_dev/TDD_PROCESS.md`
- `.project_dev/DOC_STANDARDS.md`
- `.project_dev/CODE_CONTEXT.md`
- `.project_dev/PROJECT_LOG.md`

### Configuration (2):
- `config/dev_config.json`
- `config/prod_config.json`

### Source Code (5):
- `src/__init__.py`
- `src/modules/__init__.py`
- `src/signatures/__init__.py`
- `src/main_pipeline.py`
- `evaluate.py`

### Test Data (2):
- `test_data/dev_set.jsonl`
- `test_data/gold_set.jsonl`

### Scripts (1):
- `scripts/generate_context_map.py`

### Project Files (4):
- `HYPOTHESES.md`
- `README.md`
- `.gitignore`
- `logs/.gitignore`

### Placeholders (1):
- `results/.gitkeep`

### Cascade Config:
- 4 Memories (manual configuration)
- `.cascade/` directory with rules and workflows (automatic)

---

## Troubleshooting

**Q: Files are empty after creation**
A: Make sure to copy the full content from SETUP_CONTENT_PART1.md and SETUP_CONTENT_PART2.md

**Q: Cascade doesn't recognize memories**
A: Verify file paths are correct and files exist. Check Cascade settings.

**Q: Scripts won't run**
A: Make them executable with `chmod +x` or run with `python scripts/generate_context_map.py`

**Q: evaluate.py fails**
A: Install dependencies: `pip install dspy-ai openai`

**Q: Missing API key**
A: Set environment variable: `export OPENAI_API_KEY="your-key"`

---

## Support

For detailed information, refer to:
- `SETUP_INSTRUCTIONS.md` - Full setup guide
- `SETUP_CONTENT_PART1.md` - Core files content
- `SETUP_CONTENT_PART2.md` - Scripts and code content
- `CASCADE_CONFIGURATION.md` - Cascade setup details
- Original concept docs in `coding_tool_context/`
