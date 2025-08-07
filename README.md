EcoWise – Your Sustainability Assistant
EcoWise is an AI-powered Sustainability Advisor Chatbot built using Streamlit and Google Gemini API.


✅ Features
Eco-Friendly Alternatives – Suggests sustainable swaps for common items.
Recycling & Waste Management – Guides proper disposal, recycling, and composting.
Creative Reuse & Upcycling – Ideas to repurpose household items.
Sustainable Lifestyle Tips – Minimalist and waste-reducing practices.
Interactive UI – Built with Streamlit, includes clean design, custom CSS, and animations.

🛠️ Tech Stack
Python 3.10+
Streamlit – Interactive web UI
Google Gemini API – AI-powered responses
dotenv – Environment variable management

📂 Project Structure

Sustainability_bot/
│── app.py                             # Main Streamlit application
│── .env                               # Environment variables (API Key)
│── requirements.txt                   # Dependencies
│── README.md                          # Project documentation

⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/yourusername/ecowise.git
cd ecowise

3. Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate

5. Install Dependencies
pip install -r requirements.txt

7. Set Up API Key
Create a .env file in the project root and add:
GEMINI_API_KEY=your_google_gemini_api_key

▶️ Run the App
streamlit run app.py
The app will open in your browser at:
http://localhost:8501

✅ Example Questions
"What are alternatives to plastic water bottles??"
"How can I recycle old electronics?"
"Ways to reduce food waste at home"
"Eco-friendly cleaning products I can make"





