from random import choice

from langchain_ollama import OllamaLLM, ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

llm = ChatOllama(model="llama3.2"
                #  , callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
                 , temperature=0.9)


prompts = [
    "You are a worried mother who is texting her son about his night out.",
    "You are a friend who need a ride home from a party.",
]

messages = [
    SystemMessage(choice(prompts)),
    HumanMessage("Hemlo ho us thixs?"),
]

print((llm.invoke(messages)))