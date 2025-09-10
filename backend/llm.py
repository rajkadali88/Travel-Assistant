from langchain_ollama import ChatOllama


llm  = ChatOllama(base_url="http://host.docker.internal:11434",model="llama3.2:1b",streaming=True)


