import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Define the system prompt for context
SYSTEM_PROMPT = """
You are a helpful and friendly sustainability advisor. Your role is to guide users
towards eco-friendly living by suggesting practical, low-cost, and creative solutions.

Focus areas:
- Alternatives to common non-eco products
- How to recycle and dispose of household items properly
- Tips for reducing waste (plastic, food, electronics)
- Creative reuse and upcycling ideas
- Minimalist and sustainable shopping habits

Avoid technical jargon and luxury recommendations.
If asked something unrelated, politely redirect to sustainability.
"""

# Initialize the Gemini model
model = genai.GenerativeModel('models/gemini-1.5-flash')

# Classify user queries into sustainability categories
def classify_query(user_input: str) -> str:
    query = user_input.lower()
    if any(word in query for word in ["alternative", "replace", "swap", "substitute", "eco-friendly option"]):
        return "🔄 Sustainable Alternatives"
    elif any(word in query for word in ["recycle", "dispose", "trash", "reuse", "upcycle", "compost", "segregate"]):
        return "♻️ Recycling & Waste Management"
    else:
        return "🌱 Lifestyle & Tips"

# Generate bot response using Gemini
def get_bot_response(user_input: str):
    try:
        category = classify_query(user_input)
        full_prompt = f"{SYSTEM_PROMPT}\n\nUser: {user_input}\nBot:"
        response = model.generate_content(full_prompt)
        return category, response.text.strip()
    except Exception as e:
        return "❌ Error", f"Something went wrong: {str(e)}"

# Streamlit page config
st.set_page_config(page_title="EcoBot - Sustainability Assistant", page_icon="🌱", layout="centered")

# Add custom CSS
st.markdown("""
<style>
.stApp {
    background-color: #90EE90;
    color: Blue;
    font-family: 'Segoe UI', Tahoma, sans-serif;
}
.main-title {
    text-align: center;
    color: #2F4F2F;
    padding: 1rem 0;
    border-bottom: 3px solid #4CAF50;
    margin-bottom: 2rem;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    color: Black;
    margin-bottom: 2rem;
    font-size: 1.1rem;
}
.category-tag {
    background-color: #DFF5E1;
    color: #2F4F2F;
    padding: 0.4rem 0.9rem;
    border-radius: 15px;
    font-size: 0.9rem;
    font-weight: 600;
    display: inline-block;
    margin-bottom: 1rem;
}
.response-container {
    background-color: #FFFFFF;
    padding: 1.5rem;
    border-radius: 14px;
    border-left: 5px solid #4CAF50;
    margin: 1rem 0;
    color: #2F4F2F;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
}
.example-questions {
    background-color: #FFFBE6;
    padding: 1rem;
    border-radius: 10px;
    border: 1px solid #FFD54F;
    margin: 1rem 0;
    color: #5F5F5F;
}
.quick-tip {
    background-color: #EAF7E4;
    padding: 1rem;
    border-radius: 10px;
    border-left: 5px solid #81C784;
    margin: 1rem 0;
    color: #2F4F2F;
}
div.stButton > button {
    background-color: #ADD8E6;
    color: Black;
    border-radius: 8px;
    padding: 0.6rem 1rem;
    font-size: 1rem;
    font-weight: 500;
    border: none;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    justify-content: center;
    align-item: center;
}

</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-title">
    <h1>EcoWise - AI Assistant for Real Change. </h1>
</div>
<div class="subtitle">
    <p>Practical tips on eco-friendly living, recycling, and waste reduction.</p>
</div>
""", unsafe_allow_html=True)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# Example questions box
st.markdown("""
<div class="example-questions">
    <h4>Sample Questions You May Ask.</h4>
    <p>• "What are alternatives to plastic water bottles?"</p>
    <p>• "How can I recycle old electronics?"</p>
    <p>• "Ways to reduce food waste at home"</p>
    <p>• "Eco-friendly cleaning products I can make"</p>
</div>
""", unsafe_allow_html=True)

# Input and Ask button
col1, col2 = st.columns([5, 1])
with col1:
    user_input = st.text_input("Ask Your Question.", placeholder="Write your question here...")
with col2:
    ask_button = st.button("🚀 Submit", use_container_width=True,)

# Handle user input
if ask_button and user_input.strip():
    st.session_state.chat_history.append({"question": user_input})
    with st.spinner("🤖 Thinking..."):
        category, reply = get_bot_response(user_input)
    st.session_state.chat_history[-1].update({"category": category, "response": reply})

# Show current reply
if st.session_state.chat_history:
    latest = st.session_state.chat_history[-1]
    st.markdown(f'<div class="category-tag">{latest["category"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="response-container"><strong>🤖 EcoWise:</strong><br>{latest["response"]}</div>', unsafe_allow_html=True)

# Show recent history
if st.session_state.chat_history:
    st.divider()
    st.subheader("📝 Recent Questions")
    for chat in st.session_state.chat_history[-3:][::-1]:
        with st.expander(f"Q: {chat['question'][:50]}..."):
            st.markdown(f"**Category:** {chat['category']}")
            st.markdown(f"**Response:** {chat['response']}")

    if st.button("🗑️ Clear History"):
        st.session_state.chat_history.clear()
        st.rerun()

# Footer Tip
st.divider()
st.markdown("""
<div class="quick-tip">
    <h4>🌟 Pro Tip:</h4>
    <p>Small lifestyle changes create big environmental impact. Start with one habit and grow from there!</p>
</div>
""", unsafe_allow_html=True)
