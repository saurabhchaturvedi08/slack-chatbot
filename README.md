# Slack Chatbot with LangChain & Groq Integration

This project demonstrates a Slack chatbot built using [Slack Bolt](https://slack.dev/bolt-python/), [LangChain](https://python.langchain.com/), and [Groq](https://www.groq.com/). The chatbot leverages Slack's Socket Mode to receive messages, processes conversation context using LangChain's conversation memory, and generates responses using Groq’s LLM (e.g., `llama3-8b-8192`).

## Features

- **Slack Integration:** Uses Slack Bolt to connect and listen for messages via Slack Socket Mode.
- **Advanced Language Modeling:** Integrates LangChain with Groq's chat API for natural language responses.
- **Conversational Memory:** Maintains conversation context with LangChain’s `ConversationBufferWindowMemory`.
- **Custom Prompt Templates:** Utilizes a dynamic chat prompt composed of system instructions and user input.
- **Environment-Based Configuration:** Uses a `.env` file to securely manage API tokens and keys.

## Prerequisites

- Python 3.7 or higher
- A Slack App with:
  - A Bot Token (`SLACK_BOT_TOKEN`)
  - An App Token for Socket Mode (`SLACK_APP_TOKEN`)
- A Groq API key (`GROQ_API_KEY`)

## Setup & Installation

1. **Clone the Repository:**

   - git clone https://github.com/yourusername/your-repo.git
   - cd your-repo

2. **Create a Virtual Environment & Activate It:**

   - python3 -m venv venv
   - source venv/bin/activate # On Windows use `venv\Scripts\activate`

3. **Install Dependencies:**

   - Run : pip install -r requirements.txt

4. **Configure Environment Variables: Create a .env file in the project root and add the following:**

   - SLACK_BOT_TOKEN=your-slack-bot-token
   - SLACK_APP_TOKEN=your-slack-app-token
   - GROQ_API_KEY=your-groq-api-key

5. **RUN THE CHATBOT**
   - python app.py

- Your Slack app should now connect via Socket Mode. Once active, any message sent in Slack that matches the specified pattern will be processed by the chatbot, which will generate a response using the Groq model and send it back to the channel
