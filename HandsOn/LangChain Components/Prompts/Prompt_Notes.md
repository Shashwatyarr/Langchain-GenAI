# Prompt Notes in LangChain

## 1. What is a prompt?

A prompt is the text or message structure sent to an LLM. It tells the model:

- what task to perform,
- what context to use,
- what format to return,
- and what behavior to follow.

In LangChain, prompts are usually built as structured inputs rather than as plain raw strings.

Example:

```python
prompt = "Summarize the following text in 3 bullet points:\n\n{text}"
```

This is simple, but in production we usually prefer prompt templates so values can be injected safely and consistently.

## 2. Why prompt templates matter

Prompt templates help us:

- reuse the same instruction pattern,
- insert runtime values dynamically,
- keep code cleaner,
- reduce formatting mistakes,
- build more maintainable RAG and chatbot apps.

Instead of hardcoding values into a prompt, we define placeholders like `{question}` or `{context}`.

## 3. Basic prompt template example

```python
from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in simple words for a beginner."
)

prompt = template.format(topic="neural networks")
print(prompt)
```

This produces a prompt string with the topic inserted at runtime.

## 4. Chat prompt templates

For chat-based models, prompts are usually built as message sequences with roles like:

- `system`
- `user`
- `assistant`
- `tool`

LangChain provides `ChatPromptTemplate` for this pattern.

```python
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful technical assistant."),
    ("user", "Explain {topic} in 3 short points.")
])

messages = chat_template.invoke({"topic": "LangChain prompts"})
print(messages)
```

This is the recommended style for modern chat models.

## 5. System, user, and assistant roles

Prompt design becomes clearer when we separate input roles:

- `system`: defines behavior, tone, and rules
- `user`: asks the actual question or provides task data
- `assistant`: used for conversational history or prior outputs

Example:

```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert Python tutor."),
    ("user", "Explain decorators with a simple example."),
])
```

This makes the instruction stack more structured than a single raw paragraph.

## 6. Prompt variables and partials

Prompt templates can accept multiple variables and can also use partial values.

```python
from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["question", "language"],
    template="Answer in {language}: {question}"
)

print(template.format(question="What is recursion?", language="English"))
```

In some cases, you may want to fill part of the prompt in advance:

```python
from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["question"],
    template="Answer this question in a concise way: {question}"
)

partial = template.partial(instruction="Use only 2 sentences.")
print(partial.format(question="What is prompt engineering?"))
```

This is useful when repeated instructions are shared across many requests.

## 7. Prompt engineering best practices

### Be clear
Use direct, unambiguous instructions.

Bad:

```text
Tell me about AI.
```

Better:

```text
Explain AI in beginner-friendly language for a high school student in 5 bullet points.
```

### Give output constraints
Tell the model exactly what format you want.

Example:

```text
Return only JSON with keys: summary, key_points, and risk_level.
```

### Add context
Include only the most relevant context. Too much irrelevant information can confuse model behavior.

### Separate instructions from data
For chat models, keep instructions in the system message and user content in the user message.

### Use examples when needed
Few-shot prompting is useful for structured output or custom formatting.

Example:

```python
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate

examples = [
    {"input": "I loved the product", "output": "Positive"},
    {"input": "It was slow and buggy", "output": "Negative"},
]

example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="Input: {input}\nOutput: {output}"
)

few_shot = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Input: {text}\nOutput:",
    input_variables=["text"],
)

print(few_shot.format(text="The app was very fast and easy to use"))
```

## 8. Combining prompts with models

A prompt is not useful by itself; it is passed to a model.

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a concise technical writer."),
    ("user", "Write a short summary of {topic}.")
])

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

response = model.invoke(prompt.format_messages(topic="vector databases"))
print(response.content)
```

This flow is typical in LangChain:

```text
PromptTemplate -> Model -> Response
```

## 9. Practical prompt design checklist

Before finalizing a prompt, check:

- Is the instruction specific?
- Is the output format defined clearly?
- Is the model told what not to do?
- Are variables named clearly?
- Is the prompt reusable across cases?
- Is the context concise and relevant?

## 10. Summary

Prompts are the interface between user input and model behavior. In LangChain, prompt templates make it easier to:

- create reusable instructions,
- inject variable values,
- structure chat messages properly,
- and maintain scalable LLM application logic.

Good prompts are not random text; they are deliberate instructions that guide the model toward the desired behavior and output.

## 11. Quick example to remember

```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer clearly and briefly."),
    ("user", "Explain {topic} in 2 sentences."),
])

result = prompt.format_messages(topic="retrieval augmented generation")
print(result)
```

This is the basic building block used in many LangChain apps.
