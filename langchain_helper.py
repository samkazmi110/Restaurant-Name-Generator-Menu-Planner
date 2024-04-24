from langchain.llms import OpenAI
from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate
import os

# Define a global variable to hold the OpenAI instance
llm = None

def initialize_openAPI_key(openapi_key):
    os.environ["OPENAI_API_KEY"] = openapi_key

# Initialize the OpenAI instance after setting the API key
    global llm
    llm = OpenAI(temperature=0.7)

def generate_resturant_name(cuisine):
    # Chain 1 : Generate Restaurant Name
    prompt_template_name = PromptTemplate(
    input_variables=["cuisine"],
    template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for the restaurant.",
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="name")

    # Chain 2 : Generate Restaurant Items
    prompt_template_items = PromptTemplate(
    input_variables=["name"],
    template="I want to open a restaurant for {name} food. Suggest only 10 items for the restaurant and return it as comma separated list.",
    )

    items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="items")

    chain = SequentialChain (
    chains=[name_chain, items_chain],
    input_variables = ["cuisine"],
    output_variables = ["name", "items"],
    verbose=True,
    )

    return chain({"cuisine": cuisine})


