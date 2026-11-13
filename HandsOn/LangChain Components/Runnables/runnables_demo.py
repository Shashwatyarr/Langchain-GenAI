class nkliLLM:
    def __init__(self):
        print('LLM Created')
    def predict(self, prompt):
        return f"Predicted output for: {prompt}"

class NakliPromptTemplate:
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def format(self, **kwargs):
        return self.template.format(**kwargs)

class NakliLLMChain:
    def __init__(self, llm, prompt_template):
        self.llm = llm
        self.prompt_template = prompt_template

    def invoke(self, input_dict):
        formatted_prompt = self.prompt_template.format(**input_dict)
        return self.llm.predict(formatted_prompt)

llm=nkliLLM()
prompt_template = NakliPromptTemplate("Hello, {name}! How are you?", ["name"])
llm_chain = NakliLLMChain(llm, prompt_template)

llm_chain.invoke({"name": "Alice"})