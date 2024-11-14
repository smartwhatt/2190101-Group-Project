from random import choice

from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate

from typing import List
from pydantic import BaseModel, Field


class Evaluation(BaseModel):
    """
    Evaluation model for assessing the drunk level and confidence of a person being texted.

    Attributes:
        drunk_level (float): The drunk level of the person you are texting, rated from 0 to 10 where 0 is sober and 10 is "you need to go home" level drunk.
        confidence (float): The confidence level that the person you are texting is drunk at the specified drunk level, ranging from 0 to 1.
    """

    drunk_level: float = Field(
        description="The drunk level of the person you are texting rate from 0 to 10 where 0 is sober and 10 is you need to go home level drunk",
        ge=0,
        le=10,
    )
    confidence: float = Field(
        description="The confidence level that the person you are texting is drunk at the drunk level rate range from 0 to 1",
        ge=0,
        le=1,
    )


def get_chat_model():
    """
    Creates a chat model instance and generates a conversation based on predefined prompts.

    Returns:
        tuple: A tuple containing the chat model instance, the generated messages, and the selected role.
    """

    llm = ChatOllama(model="llama3.2", temperature=0.9)

    prompts = [
        ("worried mother who is texting her son about his night out", "Mother"),
        ("friend who need a ride home from a party", "John"),
    ]

    chat_template = ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template(
                "You're a {role}. Text a message to check in on your friend."
            ),
            HumanMessage("Hi"),
        ]
    )

    role = choice(prompts)

    messages = chat_template.format_messages(role=role[0])

    messages.append(llm.invoke(messages))

    return llm, messages, role


def get_evaluation(messages: List[str]):
    llm = ChatOllama(model="llama3.2", temperature=0.9).with_structured_output(
        Evaluation
    )

    return llm.invoke("\n".join(messages))
