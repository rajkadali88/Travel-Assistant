# ✈️ Travel Assistant

Plan your trip effortlessly with AI-powered suggestions for flights and hotels.  
This project uses a local LLM via **Ollama**, containerized with **Docker**, and features a modular architecture for scalable deployment.

---

## 🚀 Features

- 🌍 Input origin, destination, travel dates, budget, and number of travelers
- ✈️ Get realistic flight options based on location and budget
- 🏨 Receive hotel recommendations tailored to your preferences
- 🧠 LLM-powered agents using Ollama for contextual travel advice
- 🐳 Fully containerized backend and frontend for easy deployment

---


---

## ⚙️ Tech Stack

| Layer       | Technology             |
|------------|------------------------|
| Backend     | FastAPI, Python, Ollama |
| Frontend    | Streamlit              |
| AI Engine   | Local LLM via Ollama   |
| Containerization | Docker + Docker Compose |

---

## 🛠️ Setup Instructions
##  Prerequisites

Before running the application, make sure the following dependencies are installed on your system:

-  **Docker**  
  Required to build and run the containerized backend and frontend services.  
  [Download Docker Desktop](https://www.docker.com/products/docker-desktop)

-  **Ollama**  
  Used to run local LLMs like LLaMA2 or Mistral for generating responses.  
  [Install Ollama](https://ollama.com/download)

After installing Ollama, make sure the desired model is pulled and running:

```bash
ollama run llama2

```
You can replace llama2 with any supported model like mistral, gemma,...etc. in app/config.py 

### 1. Clone the repo
```bash
git clone https://github.com/your-username/Travel_Assistant.git
cd Travel_Assistant
docker-compose up --build 

```

- Access the frontend at: http://localhost:8501
- Backend API at: http://localhost:8000