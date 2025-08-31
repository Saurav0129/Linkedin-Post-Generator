# LinkedIn Post Generator

This project is an AI-powered LinkedIn post generator built with Streamlit. It crafts engaging content by leveraging a dataset of posts from top influencers and a large language model (LLM) to generate new content based on user preferences.

**Live App:** [LinkedIn Post Generator](https://linkedin-post-generator-byinfluencer-style.streamlit.app/)

## Features

- **Influencer Style Emulation**: Generate posts in the style of top LinkedIn influencers like Ankur Warikoo, Kunal Shah, and Justin Welsh.
- **Content Customization**: Choose the desired post length (short, medium, long), language (English or Hinglish), and topic (tag).
- **Engagement-Based Generation**: Prioritize post generation based on the engagement level (high, medium, or low) of the original data.
- **Secure API Key Management**: Utilizes Streamlit's secrets management to securely handle API keys.

## App Preview

### Main Interface
The application provides an intuitive interface where users can:
- Select the preferred influencer style
- Choose post length and language
- Pick engagement level for content inspiration
- Generate multiple post variations

### Sample Generated Content
The app generates professional LinkedIn posts that maintain the authentic voice and style of the selected influencer while incorporating your specified topic and preferences.
<img width="791" height="761" alt="image" src="https://github.com/user-attachments/assets/27cd6ef4-ba91-4715-b48e-c1763c412cd2" />


## Project Structure

```
linkedin-post-generator/
│
├── app.py                 # Main Streamlit application file
├── preprocess.py          # Data cleaning and preprocessing utility
├── few_shots.py          # Data loading and filtering class
├── post_generator.py     # Core LLM post generation logic
├── llm_helper.py         # LLM initialization and API management
├── requirements.txt      # Project dependencies
├── README.md            # Project documentation
│
├── .streamlit/
│   └── secrets.toml     # API keys configuration
│
└── data/
    ├── raw_posts.json      # Original dataset of LinkedIn posts
    └── preprocessed.json   # Processed data with metadata
```

### File Descriptions

- **`app.py`**: The main Streamlit application file that runs the user interface.
- **`preprocess.py`**: A utility script to clean and preprocess the raw data, adding features like line_count, language, and tags.
- **`few_shots.py`**: A Python class that handles data loading, filtering, and retrieval of preprocessed posts based on various criteria.
- **`post_generator.py`**: The core logic that uses the LLM to generate new posts based on the few-shot examples provided.
- **`llm_helper.py`**: Initializes the LLM (ChatGroq) and securely provides the API key from Streamlit's secrets.
- **`data/`**: This directory contains the raw and preprocessed data files.
  - **`raw_posts.json`**: The initial dataset of manually extracted LinkedIn posts.
  - **`preprocessed.json`**: The processed data used by the application, with added metadata like tags and line counts.

## Getting Started

### Prerequisites

- Python 3.8+
- Git
- Groq API key

### Installation

1. **Clone this repository:**
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your Streamlit secrets for the LLM API key:**
   
   - Create a `.streamlit` directory in the project's root folder
   - Inside `.streamlit`, create a file named `secrets.toml`
   - Add your Groq API key to the file in the following format:
   
   ```toml
   [api_keys]
   GROQ_API_KEY = "your_groq_api_key"
   ```

5. **Run the preprocessing script:**
   ```bash
   python preprocess.py
   ```

### Running the Application

To start the Streamlit app, run the following command from your project's root directory:

```bash
streamlit run app.py
```

The app will open in your web browser at `http://localhost:8501`, and you can begin generating posts!

## Usage

1. **Select Influencer Style**: Choose from Ankur Warikoo, Kunal Shah, or Justin Welsh
2. **Configure Settings**: 
   - Post length (Short/Medium/Long)
   - Language (English/Hinglish)
   - Engagement level preference
3. **Enter Topic**: Specify the subject matter for your post
4. **Generate**: Click to create your customized LinkedIn post
5. **Refine**: Generate multiple variations and select the best one

## Technical Details

- **Frontend**: Streamlit for the web interface
- **LLM**: ChatGroq for content generation
- **Data Processing**: Custom preprocessing pipeline for influencer post analysis
- **Security**: Streamlit secrets management for API key protection

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Credits

This project was built with inspiration from the content of the following LinkedIn influencers. Their unique writing styles and insightful posts served as the foundation for the dataset and the AI's learning process:

- **Ankur Warikoo** - Entrepreneur and educator
- **Kunal Shah** - Founder of CRED
- **Justin Welsh** - Solo entrepreneur and content creator

Special thanks to their amazing content that made this project possible.

## Disclaimer

This tool is designed to inspire and assist with content creation. Always review and personalize generated content before posting to maintain authenticity and ensure it aligns with your personal brand and voice.

---

**⭐ If you found this project helpful, please consider giving it a star!**

