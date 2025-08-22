# 📘 Library Assistant (OpenAI Agents SDK)

This project is a Library Assistant built using the OpenAI Agents SDK.
It can:

# 🔎 Search for books

📖 Check book availability (for registered members only)

🕒 Provide library timings

🚫 Ignore non-library related queries

# ⚙️ Requirements

Python 3.9+
OpenAI Python SDK with Agents support
An OpenAI API Key

# 📦 Installation

Clone this repository:

git clone https://github.com/your-username/library-assistant.git
cd library-assistant


Create and activate a virtual environment (recommended):

python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Linux/Mac


Install dependencies:

pip install openai

# 🔑 API Key Setup

Set your OpenAI API Key as an environment variable:
Windows (PowerShell):
setx OPENAI_API_KEY "sk-xxxxxxxxxxxxxxxx"

Linux / Mac:
export OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxx"

# ▶️ Run the Project

Run the main script:
python main.py
The assistant will start and handle your library queries.

# 🛠️ Tech Stack

Language: Python
Framework: OpenAI Agents SDK
Features Used:
. Agen
. Runner / Runner.run_sync
. @function_tool
. @input_guardrail
. RunContextWrapper
. dynamic_instruction
. BaseModel
. ModelSettings

# 📚 Example Use

User: "What are today’s library timings?"
Assistant: "The library is open from 9 AM to 6 PM today."

User: "Tell me a joke!"
Assistant: "Sorry, I only answer library-related questions."

# 👨‍💻 Author
Developed as part of an OpenAI Agents SDK practice project.

# 🤝 Contribution
I welcome contributions! Feel free to submit issues or pull requests.

# 📢 Connect
📧 Email: nanum3773@gmail.com

💼 LinkedIn: Anum Rajput

💻 GitHub: Anum Rajput

🐦 X (Twitter): @Anumrajput88

# ⭐ Star this repository if you find it inspiring!
Happy coding!
