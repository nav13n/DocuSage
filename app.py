import os
import chainlit as cl 
from chain import rag_chain
from langchain.schema.runnable import RunnableConfig


welcome_message = "Welcome! Ask anything about your stored documents and get AI-powered insights in seconds."

@cl.on_chat_start  
async def start_chat():
    await cl.Message(content=welcome_message).send()

    cl.user_session.set("runnable", rag_chain)


@cl.on_message 
async def main(message: cl.Message):
    runnable = cl.user_session.get("runnable")
    msg = cl.Message(content="")

    async for chunk in runnable.astream(
        message.content,
        config=RunnableConfig(callbacks=[
            cl.LangchainCallbackHandler()
        ]),
    ):
        await msg.stream_token(chunk)

    await msg.send()
