# Rule: DSPy Documentation Standards

## Enforcement Level: CRITICAL

This rule MUST be followed for all DSPy code. Violations should be immediately corrected.

## Rule Statement

All DSPy code must follow these documentation standards:

### 1. dspy.Signature Docstrings
- **MUST** be purely functional (task instructions for the LLM only)
- **MUST NOT** include Purpose, Role, or Assumptions sections
- **MUST** be concise and optimization-friendly (Teleprompters modify these)
- **Example:**
  ```python
  class SummarizeSignature(dspy.Signature):
      """Generate a concise 2-3 sentence summary of the document."""
      
      document = dspy.InputField(desc="The full text to summarize")
      summary = dspy.OutputField(desc="A 2-3 sentence summary")
  ```

### 2. dspy.Module Docstrings
- **MUST** include three sections:
  - **Purpose:** One sentence describing what the module does
  - **Role in execution:** One sentence describing where it fits in the pipeline
  - **Assumptions:** Bullet list of dependencies, constraints, expected inputs/outputs
- **Example:**
  ```python
  class RAGModule(dspy.Module):
      """
      Purpose: Retrieves relevant documents and generates an answer using RAG.
      
      Role in execution: Core QA module in the main pipeline, called after query preprocessing.
      
      Assumptions:
      - Requires a configured retriever (e.g., ColBERTv2)
      - Expects input: {"question": str}
      - Returns: {"answer": str, "sources": List[str]}
      - Minimum 3 documents retrieved per query
      """
  ```

### 3. Utility Functions
- **MUST** use standard Python docstrings with Purpose, Role, and Assumptions sections

## Rationale

- **dspy.Signature** docstrings are functional code sent to LLMs and optimized by Teleprompters
- **dspy.Module** docstrings provide human/AI context and are scraped for documentation
- This separation ensures optimization doesn't break documentation

## Reference

See `.project_dev/DOC_STANDARDS.md` for complete details and examples.
