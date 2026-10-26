# GenAI Learning Lab

A hands-on learning repository for building generative AI applications with Python and LangChain. It collects small, focused examples and notes covering language models, chat models, prompts, embeddings, and related components.

> **Learning project:** Examples are intended for experimentation and may need updates as provider APIs, model IDs, and LangChain integrations change. Check the provider's current documentation before running an example.

## Contents

- [Repository layout](#repository-layout)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Configure provider credentials](#configure-provider-credentials)
- [Run an example](#run-an-example)
- [Topics covered](#topics-covered)
- [Troubleshooting](#troubleshooting)
- [Security](#security)

## Repository layout

```text
GenAI/
├── HandsOn/
│   └── LangChain Components/
│       ├── Models/
│       │   ├── ChatModels/       # Chat models from several providers
│       │   ├── EmbeddedModels/   # Embeddings and similarity examples
│       │   ├── LLMs/             # Text-generation examples
│       │   ├── Models.md         # Model concepts and usage notes
│       │   └── requirements.txt  # Python dependencies for the examples
│       └── Prompts/              # Prompt templates, message history, and UI
└── Notes/                        # Additional LangChain reference notes
```

## Prerequisites

- Python 3.10 or newer is recommended.
- `pip` and a virtual environment.
- Credentials for the provider used by the example you want to run.
- For local Hugging Face models, enough disk space and memory for the selected model; a compatible accelerator may improve performance.

Examples make calls to third-party model providers, which may require an account, network access, and a paid plan or available quota.

## Setup

Run these commands in PowerShell from the repository root:

```powershell
cd "HandsOn\LangChain Components"
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r "Models\requirements.txt"
```

If PowerShell blocks virtual-environment activation, you can run the environment's Python directly instead:

```powershell
.\.venv\Scripts\python.exe -m pip install -r "Models\requirements.txt"
```

The prompt UI uses Streamlit, which is not currently listed in `Models\requirements.txt`. Install it in the same virtual environment if you want to run that UI:

```powershell
pip install streamlit
```

## Configure provider credentials

Create a local `.env` file in `HandsOn\LangChain Components\` (the directory containing `Models` and `Prompts`). Add only the credentials needed for your chosen example, using the environment variable names expected by that provider or script. For example:

```dotenv
GROQ_API_KEY=your_groq_api_key
GEMINI_API_KEY=your_google_ai_api_key
```

Do not use these placeholder values as real credentials. Replace them locally, and never commit `.env` files or paste API keys into source code. The repository's `.gitignore` excludes `.env` files.

Some integrations use provider-standard environment variable names or authentication methods of their own. Consult the relevant provider's documentation and the selected example if a credential is not picked up.

## Run an example

From the `HandsOn\LangChain Components` directory, activate the virtual environment you created above and run a script. For example:

```powershell
python "Models\LLMs\llm_demo.py"
python "Models\ChatModels\chatmodel_groq.py"
python "Models\EmbeddedModels\Embedding_model.py"
```

To launch the prompt-template Streamlit app:

```powershell
streamlit run "Prompts\prompt_ui.py"
```

Individual examples may use different providers, model IDs, hardware, and credentials. Choose the matching environment setup for each script. Use `Ctrl+C` to stop a running terminal app or Streamlit server.

## Topics covered

- **Language and chat models:** calling providers, sending chat messages, and reading model responses.
- **Prompt construction:** reusable prompt templates, role-based messages, and conversation history.
- **Embeddings:** converting text into vectors and exploring semantic similarity.
- **Provider integrations:** examples using integrations such as Google Gemini, Groq, Anthropic, and Hugging Face.
- **Learning notes:** written explanations in `Models\Models.md`, `Prompts\Prompt_Notes.md`, and the `Notes` folder.

## Troubleshooting

- **Authentication or API-key error:** confirm the correct variable name, that the `.env` file is in the documented location, and that the key is active and has access to the selected provider/model.
- **Unknown or unavailable model:** model IDs and provider availability change over time. Check the provider's current model catalog and update the example's model ID as needed.
- **Missing Python module:** activate the intended virtual environment and install `Models\requirements.txt`. Install optional packages such as Streamlit separately when needed.
- **Local model download or memory error:** check available disk space and RAM/VRAM, or try a smaller compatible model.
- **Streamlit command not found:** verify Streamlit was installed in the active virtual environment and run `python -m streamlit run "Prompts\prompt_ui.py"`.

## Security

- Keep API keys and other credentials private; do not commit `.env` files.
- If a credential is accidentally committed or shared, revoke it with its provider and create a replacement. Removing a file in a later commit does not remove it from earlier Git history.
- Review provider pricing, privacy policies, and data handling before sending sensitive content to an external model.
