import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from langchain.chains import LLMChain
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('.env')

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# Get Groq API key
groq_api_key = os.environ['GROQ_API_KEY']
model = 'llama3-8b-8192'
# Initialize Groq Langchain chat object and conversation
groq_chat = ChatGroq(
        groq_api_key=groq_api_key, 
        model_name=model
)

system_prompt = 'You are a friendly conversational chatbot. you are an AI Assistant to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, Assistant is able to generate human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand. Assistant is constantly learning and improving, and its capabilities are constantly evolving. It is able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. Additionally, Assistant is able to generate its own text based on the input it receives, allowing it to engage in discussions and provide explanations and descriptions on a wide range of topics.Overall, Assistant is a powerful tool that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether you need help with a specific question or just want to have a conversation about a particular topic, Assistant is here to assist.'
conversational_memory_length = 5
memory = ConversationBufferWindowMemory(k=conversational_memory_length, memory_key="chat_history", return_messages=True)

# Construct a chat prompt template using various components
prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content=system_prompt
        ),  # This is the persistent system prompt that is always included at the start of the chat.

        MessagesPlaceholder(
            variable_name="chat_history"
        ),  # This placeholder will be replaced by the actual chat history during the conversation. It helps in maintaining context.

        HumanMessagePromptTemplate.from_template(
            "{human_input}"
        ),  # This template is where the user's current input will be injected into the prompt.
    ]
)

# Create a conversation chain using the LangChain LLM (Language Learning Model)
conversation = LLMChain(
    llm=groq_chat,  # The Groq LangChain chat object initialized earlier.
    prompt=prompt,  # The constructed prompt template.
    verbose=False,   # TRUE Enables verbose output, which can be useful for debugging.
    memory=memory,  # The conversational memory object that stores and manages the conversation history.
)

#Message handler for Slack
@app.message(".*")
def message_handler(message, say, logger):
    print(message)
    
    output = conversation.predict(human_input = message['text'])   
    say(output)



# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()