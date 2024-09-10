# Jobsflow.ai Chat Application

This project is a Streamlit-based chat application that allows users to interact with the Jobsflow.ai website content using AI-powered responses.

## Features

- Chat interface for asking questions about Jobsflow.ai
- AI-powered responses using Google's Generative AI (Gemini Pro)
- Document retrieval using FAISS vector store
- Data preprocessing and embedding generation

## Installation

1. Clone the repository:
    
    ```bash
    git clone https://github.com/Birat-Poudel/Chat-With-Website.git
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:
   
   Create a `.env` file in the root directory and add your Google API key:

    ```
    GOOGLE_API_KEY=your_api_key_here
    ```

4. Run the Streamlit application:

    ```
    streamlit run app.py
    ```
## Project Structure

- `app.py`: Main Streamlit application
- `build_vector.py`: Vector store building function
- `config.yml`: Configuration file for embeddings and vector store
- `data_preprocessing.py`: Data loading and preprocessing
- `embeddings.py`: Embedding model initialization
- `model.py`: Google Generative AI model setup
- `retrieve_documents.py`: Document retrieval function
- `scraping.py`: Web scraping script for Jobsflow.ai content
- `vector_store.py`: FAISS vector store implementation

## Configuration

Adjust the `config.yml` file to modify:

- Embedding model
- Vector store parameters

## Data

The application uses scraped data from the Jobsflow.ai website, stored in `scraped_data.json`.

## Dependencies

See `requirements.txt` for a full list of dependencies.