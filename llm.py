from langchain.llms import CTransformers
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

MODEL_PATH = "models/llama-2-7b-chat.ggmlv3.q4_1.bin"

def load_llm():
    """ Loads the Llama 2 7B 4-bit quantized llm """

    # download the model if it doesn't exist
    if not os.path.exists(MODEL_PATH):
        os.system("wget https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q4_1.bin -P models")
    
    # load the model
    llm = CTransformers(model=MODEL_PATH, model_type='llama')
    return llm


def construct_prompt():
    """ Construct the scientific assistant prompt """
    
    template = """You are a helpful scientific assistant. Your task is to answer scientific related questions providing the needed information. Don't answer questions in any field other than scientific fields. Be kind while talking with users by replying to hello and other kind messages.
    Question: {question}
    Answer:
    """
    prompt_template = PromptTemplate(template=template, input_variables=["question"])
    return prompt_template


def create_chain(llm, prompt):
    """ Creates the chain given the llm and prompt template """
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    return llm_chain


def construct_chain():
    """ Constructs the chain itself """
    llm = load_llm()
    prompt = construct_prompt()
    return create_chain(llm, prompt)


def generate_answer(chain, question):
    """ Running inference given a question """
    return chain.run(question)