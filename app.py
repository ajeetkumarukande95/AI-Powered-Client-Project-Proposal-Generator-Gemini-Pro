import streamlit as st
import os
import google.generativeai as geneai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class GoogleVertexAIService:
    def __init__(self):
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if self.api_key:
            geneai.configure(api_key=self.api_key)
        # Use the provided model IDs
        self.model_1 = geneai.GenerativeModel("gemini-pro")
        self.model_2 = geneai.GenerativeModel("gemini-pro")

    def generate_proposal(self, client_data):
        prompt = self._create_initial_prompt(client_data)
        try:
            response = self._generate_text(self.model_1, prompt)
            refined_prompt = self._create_refined_prompt(client_data, response.text)
            refined_response = self._generate_text(self.model_2, refined_prompt)
            return refined_response.text.strip()
        except Exception as e:
            print(f"Error generating proposal: {e}")
            return "An error occurred while generating the proposal."

    def _generate_text(self, model, prompt):
        try:
            response = model.generate_content(prompt)
            return response
        except Exception as e:
            print(f"Error in generate_content call: {e}")
            raise

    def _create_initial_prompt(self, client_data):
        return (
            f"Generate a base proposal for {client_data['client_name']} in the {client_data['industry']} industry. "
            f"The client has specific requirements: {client_data['requirements']}. "
            "Provide a foundational proposal that can be further refined."
        )

    def _create_refined_prompt(self, client_data, initial_proposal):
        return (
            f"Refine the following proposal for {client_data['client_name']} in the {client_data['industry']} industry. "
            f"The client has specific requirements: {client_data['requirements']}. "
            f"Initial proposal: {initial_proposal}. "
            "Enhance this proposal with more contextually accurate details and ensure it addresses all client needs precisely."
        )

# Sidebar input form for client data
def proposal_input():
    st.sidebar.header("📝 Client Information")
    client_name = st.sidebar.text_input("Client Name")
    industry = st.sidebar.selectbox("Industry", ["Tech", "Finance", "Healthcare", "Education", "Other"])
    requirements = st.sidebar.text_area("Special Requirements")

    client_data = {
        "client_name": client_name,
        "industry": industry,
        "requirements": requirements
    }
    
    return client_data

# Function to generate proposal using Google Generative AI
def proposal_generation(client_data):
    st.header("🚀 Generate Proposal")
    
    if st.button("Generate Proposal"):
        with st.spinner("Generating proposal... 🤖"):
            google_service = GoogleVertexAIService()
            proposal = google_service.generate_proposal(client_data)
            st.session_state['proposal'] = proposal
            st.success("Proposal generated successfully! 🎉")
            st.write(proposal)

# Function to review and edit generated proposal
def proposal_review():
    st.header("✏️ Review and Edit Proposal")
    
    if 'proposal' in st.session_state:
        proposal = st.text_area("Edit Proposal", st.session_state['proposal'], height=400)
        st.session_state['proposal'] = proposal
        st.success("Proposal updated successfully! 👍")
    else:
        st.warning("No proposal to review. Please generate a proposal first. 🕵️‍♂️")

# Function to handle application settings (placeholder)
def settings():
    st.header("⚙️ Settings")
    st.write("Here you can configure your AI parameters and other preferences.")
    # Implement settings form here as needed

# Main application logic
def main():
    st.title("AI-Powered Proposal Generator 🌟")

    # Sidebar navigation
    menu = ["Create Proposal", "Review Proposal", "Settings"]
    choice = st.sidebar.selectbox("Menu", menu)

    client_data = proposal_input()
    st.session_state['client_data'] = client_data

    if choice == "Create Proposal":
        proposal_generation(client_data)
    elif choice == "Review Proposal":
        proposal_review()
    elif choice == "Settings":
        settings()

if __name__ == '__main__':
    main()
