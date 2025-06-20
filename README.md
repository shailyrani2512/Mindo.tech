# Mindo.tech
# Mindo.tech - Multi-LLM Prompt Generator 🔮

A dynamic web application built using Flask that allows users to generate AI responses using multiple Large Language Models (LLMs) — including Google Gemini, OpenAI GPT-4, Anthropic Claude, and Groq's LLaMA models — all integrated via [LiteLLM](https://github.com/BerriAI/litellm).

## 🌟 Features

- ✍️ Input prompts with `{placeholder}` variables
- 🔄 Fill dynamic values via JSON
- 🧠 Choose from multiple output formats: JSON, paragraph, one-word, custom
- 🤖 Switch between LLMs (Gemini, GPT-4, Claude, LLaMA) from a dropdown
- 📋 Copy generated output with a click
- ⚡ Spinner loading animation
- 🔐 API keys secured per provider using LiteLLM

## 🔧 Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **LLM Middleware**: [LiteLLM](https://github.com/BerriAI/litellm)
- **LLMs Integrated**:  
  - Google Gemini (via Generative Language API)  
  - OpenAI GPT-4  
  - Anthropic Claude  
  - Groq (Meta LLaMA)

---

## 📂 Folder Structure

mindo_llm/
│
├── templates/
│ └── index.html # Frontend UI
├── app.py # Flask backend
├── requirements.txt # Python dependencies
└── README.md # Project documentation

yaml
Copy
Edit

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/shailyrani2512/Mindo.tech
cd mindo_llm
2. Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On Mac/Linux
3. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
4. Configure API Keys
In app.py, set your API keys:

python
Copy
Edit
API_KEYS = {
    "gemini": "<your-google-api-key>",
    "groq": "<your-groq-api-key>",
    "anthropic": "<your-anthropic-api-key>",
    "openai": "<your-openai-api-key>"
}
5. Run the App
bash
Copy
Edit
python app.py
Then go to http://localhost:5000 in your browser.

📝 Usage Instructions
Enter a prompt using {placeholder} style (e.g., Hello {name})

Provide dynamic values in JSON (e.g., { "name": "Alice" })

Choose a format: json, paragraph, one-word, or customize

Pick your preferred LLM from the dropdown

Click Generate and get your AI-powered response

Copy to clipboard if needed

📦 Dependencies
See requirements.txt:

nginx
Copy
Edit
flask
requests
litellm
Install with:

bash
Copy
Edit
pip install -r requirements.txt
📸 Screenshots
![image](https://github.com/user-attachments/assets/e9887428-fb77-4a91-b323-020bc43ee3bd)

Main UI of the LLM prompt generator

📜 License
MIT License. Feel free to use and contribute.

👩‍💻 Author
Shaily Rani
GitHub: @shailyrani2512

🙌 Acknowledgements
LiteLLM

Google Generative Language API

Groq API

OpenAI API

Anthropic Claude

yaml
Copy
Edit

---
