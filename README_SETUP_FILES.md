# DSPy Workspace Setup Files - Overview

This directory contains everything needed to set up a complete DSPy development workspace following the 3-pillar framework.

## 📦 What's Included

### Setup Files (Drop these into any empty folder)

1. **`QUICK_SETUP.md`** ⚡
   - TL;DR version for AI assistants
   - Checklist format
   - Quick reference

2. **`SETUP_INSTRUCTIONS.md`** 📋
   - Complete setup guide
   - Folder structure overview
   - Verification steps

3. **`SETUP_CONTENT_PART1.md`** 📄
   - Core project files content
   - `.project_dev/` files
   - Configuration files
   - Test data

4. **`SETUP_CONTENT_PART2.md`** 📄
   - Scripts and source code
   - `evaluate.py` content
   - `generate_context_map.py` content
   - README template

5. **`CASCADE_CONFIGURATION.md`** 🎯
   - Cascade/Windsurf setup
   - 4 Memories configuration
   - Reference to `.cascade/` directory for rules and workflows

6. **`setup_workspace.py`** 🤖
   - Automated setup script
   - Creates folders and most files
   - Python-based automation

## 🚀 Quick Start for AI Assistants

**If you're an AI assistant setting up a workspace:**

1. Read `QUICK_SETUP.md` first
2. Create all folders
3. Read `SETUP_CONTENT_PART1.md` and create all files
4. Read `SETUP_CONTENT_PART2.md` and create remaining files
5. Read `CASCADE_CONFIGURATION.md` and configure Cascade
6. Verify setup is complete

## 🚀 Quick Start for Humans

**If you're a human setting up a workspace:**

### Option 1: Automated (Partial)
```bash
# Copy setup files to your new project directory
cp SETUP_*.md CASCADE_CONFIGURATION.md setup_workspace.py /path/to/new/project/

# Run the setup script
cd /path/to/new/project/
python setup_workspace.py

# Manually create remaining files from SETUP_CONTENT_PART2.md
# Configure Cascade using CASCADE_CONFIGURATION.md
```

### Option 2: Manual with AI Assistant
```bash
# Copy all setup files to your new project directory
cp *.md setup_workspace.py /path/to/new/project/

# Open the project in Cascade/Windsurf
# Point your AI assistant to QUICK_SETUP.md
# Say: "Please set up the workspace following QUICK_SETUP.md"
```

### Option 3: Fully Manual
1. Read `SETUP_INSTRUCTIONS.md`
2. Create folders manually
3. Copy file contents from `SETUP_CONTENT_PART1.md` and `SETUP_CONTENT_PART2.md`
4. Configure Cascade using `CASCADE_CONFIGURATION.md`

## 📁 What Gets Created

After setup, your workspace will have:

```
your_project/
├── .cascade/              # Cascade AI configuration
│   ├── rules/             # Enforced constraints
│   └── workflows/         # Procedural guides
├── .project_dev/          # AI context files (5 files)
├── config/                # Configuration (2 files)
├── logs/                  # Local logs (gitignored)
├── results/               # Evaluation results
├── scripts/               # Automation scripts (1 file)
├── src/                   # Source code (4 files)
│   ├── modules/
│   └── signatures/
├── test_data/             # Test datasets (2 files)
├── .gitignore
├── evaluate.py
├── HYPOTHESES.md
└── README.md
```

**Total:** 10 folders, 23+ files (plus rules and workflows in `.cascade/`)

## 🎯 The 3-Pillar Framework

### Pillar 1: System of Record
- `.project_dev/` directory with AI context
- `DEV_NORMS.md`, `TDD_PROCESS.md`, `DOC_STANDARDS.md`
- Auto-generated `CODE_CONTEXT.md`
- Session log in `PROJECT_LOG.md`

### Pillar 2: Hypothesis-Driven Development
- `HYPOTHESES.md` for R&D planning
- Structured experiment tracking
- Learning capture from failures

### Pillar 3: Reproducible Test Harness
- `evaluate.py` for E2E evaluation
- Version-controlled results in `results/`
- Test datasets in `test_data/`
- Full observability and traceability

## 🔧 Cascade Integration

The setup includes configuration for:
- **4 Memories:** Static Norms, Code Context, Dynamic Status, Hypothesis (manual configuration)
- **Rules & Workflows:** Automatically loaded from `.cascade/` directory
  - Rules in `.cascade/rules/` (DSPy docs, hypothesis traceability, code context)
  - Workflows in `.cascade/workflows/` (session start, pre-implementation checklist)

## 📚 File Descriptions

### Setup Files

| File | Purpose | Size |
|------|---------|------|
| `QUICK_SETUP.md` | Quick reference checklist | Short |
| `SETUP_INSTRUCTIONS.md` | Complete setup guide | Medium |
| `SETUP_CONTENT_PART1.md` | Core files content | Large |
| `SETUP_CONTENT_PART2.md` | Scripts and code content | Large |
| `CASCADE_CONFIGURATION.md` | Cascade setup details | Large |
| `setup_workspace.py` | Automated setup script | Medium |

### Reference Files (in `coding_tool_context/`)

| File | Purpose |
|------|---------|
| `windsurf_workspace_concept.md` | Original 3-pillar framework concept |
| `windsurf_workspace_init.md` | Original Windsurf artifacts spec |
| `dspy_patterns.md` | DSPy best practices |
| `pydantic_patterns.md` | Pydantic patterns |

## ✅ Verification

After setup, verify:

1. **Folders exist:**
   ```bash
   ls -la | grep -E "project_dev|config|logs|results|scripts|src|test_data"
   ```

2. **Files have content:**
   ```bash
   wc -l .project_dev/*.md config/*.json
   ```

3. **Scripts are executable:**
   ```bash
   chmod +x scripts/generate_context_map.py evaluate.py
   ```

4. **Cascade is configured:**
   - Check memories in Cascade settings
   - Verify `.cascade/` directory exists with rules and workflows
   - Cascade automatically loads rules and workflows from `.cascade/`

## 🎓 Usage After Setup

1. **Start a session:**
   ```
   Say to AI: "Let's start"
   ```

2. **Add a hypothesis:**
   ```
   Edit HYPOTHESES.md and add H-001
   ```

3. **Start development:**
   ```
   Say to AI: "Let's add [feature]"
   ```

4. **Run evaluation:**
   ```bash
   python evaluate.py --config config/dev_config.json --test_set test_data/dev_set.jsonl
   ```

5. **End session:**
   ```
   Say to AI: "Let's wrap up"
   ```

## 🐛 Troubleshooting

**Problem:** Files are empty after creation
**Solution:** Ensure you copied full content from SETUP_CONTENT files

**Problem:** Cascade doesn't see memories
**Solution:** Verify file paths are absolute and files exist

**Problem:** Scripts won't execute
**Solution:** Make executable with `chmod +x` or run with `python`

**Problem:** evaluate.py fails
**Solution:** Install dependencies: `pip install dspy-ai openai`

## 📖 Further Reading

- Original concept: `coding_tool_context/windsurf_workspace_concept.md`
- DSPy patterns: `coding_tool_context/dspy_patterns.md`
- Windsurf artifacts: `coding_tool_context/windsurf_workspace_init.md`

## 🤝 Contributing

This setup framework is designed to be:
- **Portable:** Drop into any empty folder
- **Complete:** Everything needed to start
- **Documented:** Clear instructions for AI and humans
- **Extensible:** Easy to customize for your needs

## 📝 License

[Your license here]

---

**Ready to set up a workspace?**

1. Copy these files to your new project directory
2. Point your AI assistant to `QUICK_SETUP.md`
3. Say: "Please set up the workspace"
4. Start building!
