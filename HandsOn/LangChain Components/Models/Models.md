# LangChain Models — Detailed Notes

## 1. What is a model in LangChain?

A model is the component that performs the AI work in a LangChain application. Depending on the model type and provider, it can:

- Generate or transform text.
- Interpret a sequence of chat messages.
- Return structured data or request a tool call.
- Convert text into numerical vectors called embeddings.

LangChain gives an application a common interface for working with models from different providers. The provider integration still determines which models, options, and capabilities are available. Keeping provider-specific setup at the model boundary makes the rest of an application easier to reuse.

At a high level:

```text
Input or messages -> model -> generated response, structured data, or vectors
```

Models do not automatically know private, current, or application-specific information. Supply relevant context in the input or use retrieval when the application needs external knowledge.

## 2. Main model categories

### 2.1 Chat models

A chat model accepts a sequence of messages and returns a response. Messages generally have roles such as:

| Role | Typical purpose |
| --- | --- |
| `system` | Set the assistant's behavior, boundaries, or response style. |
| `user` | Provide a request, question, or data to work on. |
| `assistant` | Represent an assistant response or a prior conversational turn. |
| `tool` | In tool-enabled workflows, provide the result returned by a tool. |

Chat models are commonly used for:

- Conversation and question answering.
- Summarization, rewriting, and translation.
- Classification and information extraction.
- Reasoning over context supplied in the prompt.
- Structured output and tool calling, when supported by the model and provider.

The model's output is usually an AI message (for example, a LangChain `AIMessage`) rather than a plain string. Its `.content` contains the response content; additional metadata may include token usage, finish information, or tool calls, depending on the integration.

### 2.2 Text-completion models

Some integrations expose models that take a plain text prompt and return a text completion. These are often called LLMs or completion models in LangChain terminology.

For new applications, chat models are commonly used because they represent instructions and conversation turns explicitly. Use a completion-style model when the chosen provider/model offers that interface or when working with an existing completion-based application.

### 2.3 Embedding models

An embedding model maps text to a vector: a list of numbers representing aspects of the text's meaning. Texts with related meanings tend to have vectors that are close under a similarity measure.

Embeddings are useful for:

- Semantic search, where a query can match conceptually related wording.
- Indexing document chunks for retrieval-augmented generation (RAG).
- Clustering or deduplicating text.
- Finding related items.

An embedding model does **not** generate a conversational answer. A vector store or another similarity-search system stores and searches the vectors; a retriever can then return relevant source documents to a chat model.

## 3. Calling a chat model

Install the integration package for the provider you choose. For example, the OpenAI integration is distributed as `langchain-openai`:

```bash
pip install langchain-openai
```

Configure credentials using the provider's recommended environment-variable or secret-management mechanism. Do not put API keys directly in source code or commit them to version control.

```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
)

reply = model.invoke("Explain embeddings in one sentence.")
print(reply.content)
```

`invoke()` runs the model once and returns its response object. Access `.content` when the application needs the text, but keep the full response when it needs metadata or tool-call information.

### Providing role-based messages

For chat applications, explicitly separating instructions from user input makes the request easier to understand and maintain:

```python
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

messages = [
    SystemMessage(content="You are a concise science tutor."),
    HumanMessage(content="Explain gravity using an everyday example."),
]

reply = model.invoke(messages)
print(reply.content)
```

In larger workflows, a prompt template can create these messages from runtime values and be composed with the model.

## 4. Common ways to run a model

LangChain model integrations generally implement the Runnable interface. Common operations include:

| Operation | Purpose |
| --- | --- |
| `invoke(input)` | Run one input and return one result. |
| `batch(inputs)` | Run a collection of inputs and return their results. |
| `stream(input)` | Yield output chunks as they are produced, when streaming is supported. |
| `ainvoke(input)` | Asynchronously run one input. |
| `abatch(inputs)` | Asynchronously run a collection of inputs. |
| `astream(input)` | Asynchronously yield output chunks when supported. |

Example of streaming text from a chat model:

```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

for chunk in model.stream("Give three tips for clear technical writing."):
    if chunk.content:
        print(chunk.content, end="", flush=True)
print()
```

Streaming support and the exact contents of chunks can vary by integration and model. When streaming tool calls or multimodal output, handle the relevant response fields rather than assuming every chunk is plain text.

## 5. Model configuration and generation options

Configuration is provider- and model-dependent. Common options include:

- **Model name:** Selects the provider's model and its available capabilities.
- **Temperature:** Where supported, influences variation in generated responses. Lower values often suit tasks that benefit from consistency; this does not guarantee correctness or fully deterministic output.
- **Maximum output tokens:** Limits the size of the generated response, where the integration exposes this option.
- **Timeout and retries:** Affect how long a call can wait and how transient failures are handled.
- **Streaming:** Requests incremental output if the provider and model support it.
- **Provider credentials and endpoint:** Identify and authenticate with the service.

Use option names and valid values documented for the installed integration version. A setting supported by one provider or model may be ignored or rejected by another.

## 6. Embeddings in practice

The following example creates a query vector and document vectors using the OpenAI integration:

```python
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

query_vector = embeddings.embed_query("How do embeddings support semantic search?")
document_vectors = embeddings.embed_documents([
    "Embeddings represent text as numerical vectors.",
    "A retriever can search for documents relevant to a query.",
])

print(len(query_vector))
print(len(document_vectors))
```

Use `embed_query()` for a search query and `embed_documents()` for a set of documents. Some providers use different embedding behavior for queries and documents; follow the integration's guidance.

### Embeddings and retrieval flow

```text
Documents
  -> split into chunks
  -> create document embeddings
  -> store vectors and source text in a vector store

User query
  -> create query embedding
  -> search for similar document vectors
  -> retrieve relevant text
  -> provide that text to a chat model as context
```

For useful semantic search, the query and indexed documents should use compatible embedding models and vector dimensions. If the embedding model changes, existing vectors may need to be regenerated and re-indexed.

## 7. Structured output and tool calling

Some chat models can return data that follows a schema or request that an application call a tool. LangChain integrations may expose helpers such as structured-output methods or tool-binding methods for this purpose.

- Check that both the selected model and provider integration support the feature.
- Define and validate the expected data shape in application code.
- Treat tool calls as requests, not as proof that an action is safe or authorized.
- Validate tool arguments and enforce application permissions before executing a tool.
- Handle incomplete, invalid, or refused model output explicitly.

Structured output reduces ambiguity but does not remove the need for validation. Model output is generated data and should not be trusted automatically.

## 8. Choosing a model

Choose a model based on the actual requirements rather than on its name alone:

1. **Capability:** Does the task need chat, vision, tool calling, structured output, a long context window, or embeddings?
2. **Quality:** Does it perform adequately on representative examples from the application?
3. **Latency:** Is its response time suitable for the user experience?
4. **Cost:** Consider both input and output usage, expected request volume, and embedding/indexing costs.
5. **Context and output limits:** Can it handle the required input and produce the required response size?
6. **Availability and data handling:** Check provider availability, regional requirements, retention settings, and organizational policies.
7. **Operational fit:** Consider quotas, rate limits, retry behavior, monitoring, and fallback requirements.

Evaluate models with a small, representative test set before selecting one for production. A model that performs well on a demonstration may behave differently on real inputs.

## 9. Models in a LangChain workflow

Models commonly compose with other LangChain components:

```text
Prompt template -> chat model -> output parser
```

For example:

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a concise study assistant."),
    ("user", "Explain {topic} in two sentences."),
])

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
chain = prompt | model

reply = chain.invoke({"topic": "semantic search"})
print(reply.content)
```

For a RAG workflow, a retriever first supplies relevant source text, and the chat model uses it as context. The model itself does not perform vector search unless the application connects it to a retrieval or tool workflow.

## 10. Reliability, security, and good practices

- Keep API keys out of source files, notebooks, logs, and version control.
- Validate user input and model output according to the application's requirements.
- Give the model only the context needed for the task; avoid sending unnecessary sensitive data to an external provider.
- Treat retrieved text as data, not trusted instructions. A document can contain misleading or adversarial instructions.
- Do not rely on a model response as the sole authorization check for sensitive actions.
- Handle provider errors, timeouts, rate limits, and malformed output explicitly.
- Add suitable limits for input size, output size, retries, and request duration.
- Monitor token usage, latency, error rates, and quality while respecting privacy requirements.
- Pin or record dependency versions for reproducibility and verify examples against the installed LangChain integration version.

## 11. Common misconceptions

| Misconception | More accurate view |
| --- | --- |
| “The model knows everything in my application.” | The model only has its training and the information supplied or made available at runtime. |
| “A lower temperature makes every answer correct.” | Temperature influences variation where supported; it is not a correctness setting. |
| “Embeddings are answers.” | Embeddings are vectors used for comparison and retrieval, not conversational responses. |
| “A chat model automatically searches my documents.” | Retrieval must be implemented and connected to the workflow. |
| “Structured output is always valid.” | Validate the result and handle errors even when using a schema-oriented feature. |
| “All providers support the same options.” | Capabilities, option names, limits, and behavior vary by provider and model. |

## 12. Quick revision

- **Chat model:** Takes messages and produces a response; used for conversation and generation tasks.
- **Completion model:** Takes a text prompt and produces a text completion.
- **Embedding model:** Converts text into vectors for semantic comparison and retrieval.
- **`invoke()`:** Runs one model input.
- **`batch()`:** Runs multiple inputs.
- **`stream()`:** Yields incremental output when supported.
- **RAG:** Retrieves relevant text and supplies it as context to a generative model.
- **Key principle:** Select the model for the task, verify provider capabilities, and validate generated output.

> LangChain and provider APIs evolve. Check the documentation for the versions installed in your project before relying on specific model names, configuration options, or integration methods.
