from prompt_templates import memory_prompt_template
from langchain.chains import StuffDocumentsChain,LLMChain, ConversationalRetrievalChain
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate
from langchain.llms import ctransformers
from langchain.vectorstores import chroma
import chromadb
import yaml

with open("config.yml","r") as f:
    config = yaml.safe_load(f)

def create_llm(model_path=config["model_path"]["large"],model_type= config["model_type"]):
    llm = ctransformers(model_path, model_type)
    return llm
def create_embeddings(embeddings_path = config["embeddings_path"]):
    return HuggingFaceInstructEmbeddings(embeddings_path)

def create_chat_memory(chat_history):
    return ConversationBufferWindowMemory(memory_key="history", chat_memory=chat_history, k=3)

def create_prompt_from_template(template):
    return PromptTemplate.from_template(template)


def create_llm_chain():
    


def load_normal_chain():



class chatChain:
    def __init__ (self, chat_history, model_path=config["model_path"]["large"],model_type= config["model_type"]):
        self.memory = create_chat_memory(chat_history)
        llm = create_llm(model_path, model_type)
        chat_prompt= create_prompt_from_template(memory_prompt_template)
