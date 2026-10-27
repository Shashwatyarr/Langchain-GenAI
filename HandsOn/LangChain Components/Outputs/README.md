# Structured Outputs and Notes

This folder is the central place for all generated work from the LangChain learning exercises.

The goal is to keep code, prompts, outputs, and notes separate and organized so every experiment can be reviewed later.

## Purpose

Store here:

- model outputs
- prompt results
- chat conversations
- embedding results
- logs and failures
- comparative experiments
- personal observation notes

This makes it easy to separate actual learning artifacts from the source scripts in `Models` and `Prompts`.

## Output categories

```text
Outputs/
├── README.md
├── ChatModels/
│   ├── README.md
│   ├── responses/
│   ├── prompts/
│   ├── logs/
│   └── notes/
├── Embeddings/
│   ├── README.md
│   ├── similarity/
│   ├── vectors/
│   ├── comparisons/
│   └── notes/
├── LLMs/
│   ├── README.md
│   ├── responses/
│   ├── summaries/
│   ├── comparisons/
│   └── notes/
├── Prompts/
│   ├── README.md
│   ├── templates/
│   ├── chat_history/
│   ├── experiments/
│   └── notes/
├── Notes/
│   ├── README.md
│   ├── output_template.md
│   └── experiment_notes/
└── Misc/
    └── experiments/
```

## How to record an output

Every output file should be stored with a short note explaining:

- what was tested
- which model or provider was used
- which prompt or template was used
- whether the result was successful or failed
- what observation was made

### Standard output note format

```markdown
# Experiment title

- Date: 2026-10-27
- Category: ChatModels / LLMs / Embeddings / Prompts
- Script: Models/ChatModels/chatmodel_groq.py
- Model: groq/llama-3.1-8b-instant
- Prompt type: system + user
- Result: success / failed / partial
- Notes: Good response quality, but output varied slightly by temperature.
```

This note can be saved as a `.md` file beside the output.

## Notes by category

### 1. ChatModels
Use this section for:

- chat model responses
- multi-turn conversations
- provider comparisons
- prompt + chat behavior testing
- logs of message formatting

Files should usually include:

- original prompt
- messages list
- final output
- notes about tone, accuracy, or failure

Example naming:

```text
chatmodel_groq_01_response.txt
chatmodel_google_01_conversation.txt
chatmodel_anthropic_compare_01.md
```

### 2. Embeddings
Use this section for:

- embedding generation
- similarity matrices
- nearest-neighbor checks
- vector comparisons
- semantic search experiments

Files should usually include:

- query text
- document text
- similarity score
- nearest result list
- interpretation

Example naming:

```text
embedding_similarity_doc_a_vs_b.json
semantic_search_demo_01.md
embedding_vector_sample_01.txt
```

### 3. LLMs
Use this section for:

- text generation experiments
- summarization examples
- completion outputs
- evaluation comparisons across providers

Files should usually include:

- input prompt
- model name
- temperature / max_tokens
- generated answer
- notes on quality or failure

Example naming:

```text
llm_summary_demo_01.txt
llm_response_groq_01.md
llm_compare_01.json
```

### 4. Prompts
Use this section for:

- prompt template test runs
- system/user message structure
- few-shot examples
- prompt engineering notes
- chat history logs

Files should usually include:

- prompt template name
- variables used
- final rendered prompt
- output received
- why the result was good or bad

Example naming:

```text
prompt_template_react_01.md
chat_prompt_history_01.txt
few_shot_prompt_demo_01.json
```

### 5. Notes
This folder is for the learning record.

Use it for:

- personal insights
- observations about model quality
- best practices learned
- mistakes to avoid
- summarised understanding of a topic

Keep note files short and practical.

Example naming:

```text
prompt_engineering_notes.md
embedding_experiment_summary.md
chat_model_debugging_notes.md
```

## File naming convention

Use a consistent pattern:

```text
<category>_<experiment>_<date>_<version>
```

Examples:

```text
chatmodel_groq_response_2026_10_27_v1.txt
embedding_similarity_test_2026_10_27_v2.json
prompt_template_qa_demo_2026_10_27_v1.md
llm_summary_compare_2026_10_27_v1.txt
```

## Best practices

- Save generated outputs in the correct category folder.
- Keep each output file focused on one experiment.
- Write a short note with every important result.
- Do not save API keys, secrets, or personal credentials in output files.
- Use .txt for plain output, .md for notes, .json for structured data, .csv for comparisons when needed.
- If an experiment failed, store the failure reason with the output.

## Example output record

```markdown
# Groq chat response test

- Date: 2026-10-27
- Category: ChatModels
- Script: Models/ChatModels/chatmodel_groq.py
- Model: groq/llama-3.1-8b-instant
- Prompt: Explain embeddings in simple language.
- Result: Success
- Notes: Response was concise and useful. Slight variation in wording was observed between runs.
```

## Learning purpose

This folder is not just for raw output storage. It is a record of how learning evolved over time.

It should contain:

- what was tried
- what worked
- what failed
- what was learned
- what should be improved next

## Final rule

If an output matters, it should be saved here with a clear category and a short note. Otherwise, it is difficult to reuse later for learning or debugging.
