# AI-Powered Proposal Generator 🌟

This Streamlit application leverages Google Vertex AI to generate and refine client proposals. The app is designed to be user-friendly, with a visually appealing interface and easy-to-use features for creating, reviewing, and editing AI-generated proposals.

## Features

- **Generate Proposals**: Automatically generate initial proposals based on client data.
- **Refine Proposals**: Enhance the generated proposals by providing additional context and refining details.
- **Review & Edit**: Review and manually edit the proposals to meet specific client needs.
- **Customizable Interface**: The app includes a modern, colorful interface with a customizable theme.

## Installation

### Prerequisites

- Python 3.7+
- Streamlit
- Google Vertex AI (Generative AI)
- dotenv

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/ai-proposal-generator.git
   cd ai-proposal-generator

install Dependencies
Use pip to install the necessary Python packages:
pip install -r requirements.txt

The requirements.txt should include:
streamlit
google-generativeai
python-dotenv

Set Up Environment Variables
Create a .env file in the root of your project and add your Google API key:

GOOGLE_API_KEY=your-google-api-key
Run the Application

Start the Streamlit application:
streamlit run app.py

Usage
1. Provide Client Information
Enter the client's name, select the industry, and specify any special requirements in the sidebar form.
2. Generate Proposal
Click "Generate Proposal" to create an initial proposal based on the client data.
3. Review & Edit Proposal
Navigate to the "Review Proposal" tab to edit and refine the generated proposal as needed.
4. Configure Settings
Use the "Settings" tab to configure AI parameters and other preferences (feature under development).
Customization
Background and Theme: The app's appearance can be easily customized by editing the CSS in the add_custom_css function inside app.py.
Google Vertex AI Model: The app uses the gemini-pro model by default. You can modify or expand the functionality by changing the model or adding more options.
Contributing
Feel free to submit issues or pull requests. Contributions are welcome!

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Streamlit
Google Vertex AI
