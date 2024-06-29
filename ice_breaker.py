from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import requests
import pprint

load_dotenv() 

gist_response = requests.get("https://gist.githubusercontent.com/kiransheshadri858/9c5679131afc1f538bf5f3525cf5822a/raw/03a30de9e6432b468f235f6fccf16d8de59aa097/aboutme")

information = gist_response.text

if __name__ == "__main__":

    summary_template = """
    Given the information {information} about a person, I want you to create:
    1. A detailed summary
    2. Reasons why they would be a grea data enignereing hire

    Don't say anything that I didn't tell you. Don't make anything up or embellish anything.
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain =  summary_prompt_template | llm

    res = chain.invoke(input={"information": information})

    pprint.pprint(res)