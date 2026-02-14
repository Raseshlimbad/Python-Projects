# CodeFixer - AI Code Reviewer

![Preview Image](./Images/image.png)

## Overview
The **CodeFixer - AI Code Reviewer** is a Streamlit-based application that leverages Google's Generative AI models to review Python code. The app analyzes the submitted code, identifies bugs, errors, or areas of improvement, and provides fixed code snippets along with explanations for the corrections.

## Features
- Submit Python code for review.
- Get detailed feedback on bugs, errors, and improvements.
- Receive corrected code snippets with explanations.
- Friendly and interactive user interface powered by Streamlit.

## Prerequisites
Before setting up the project, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)

## Setup Guide
Follow these steps to set up and run the application:

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd GenAI-App-AI_Code_Reviewer
   ```

2. **Create a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   - Ensure the `.env` file is present in the root directory.
   - Add your Gemini API key in the following format:
     ```
     GEMINI_API_KEY=your-api-key
     ```

5. **Run the Application**
   ```bash
   streamlit run Code_review_PA.py
   ```

6. **Access the App**
   - Open your browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

## File Structure
```
GenAI-App-CodeFixer/
├── Code_review_PA.py          # Main application script
├── .env                       # Environment variables file
├── requirements.txt           # Dependencies file
└── README.md                  # Project documentation
```

## Notes
- Ensure your API key is valid and has the necessary permissions to access the Generative AI models.
- The app is designed to work with the `gemini-2.5-flash` model. Update the model name in the code if required.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- [Google GenAI](https://pypi.org/project/google-genai/) for providing the Generative AI SDK.
- [Streamlit](https://streamlit.io/) for the interactive web app framework.