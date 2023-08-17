## Files Overview

- `app.py`: This file sets up the Beam application, specifying the resources it requires and the Python packages it depends on. It also defines the REST API trigger for the application.

- `run.py`: This file is responsible for:
    - Loading documents from the `./data` directory.
    - Splitting the texts from the documents.
    - Generating embeddings for the split texts using the OpenAI API.
    - Creating a FAISS vector store from the embeddings.
    - Setting up a RetrievalQA system using `langchain`.
    - Defining a handler function that takes a query and returns a response from the QA system.

## Usage

1. Ensure you've set the `openai_api_key` variable in `run.py` to your OpenAI API key.
2. Run the Beam application.
3. Once the application is running, you can make a REST API call to the endpoint with a query, and the system will return a predicted response.

For example, calling the handler with the query "What is the meaning of life?" will return a response from the RetrievalQA system.

## Note

- Please ensure that the data directory (`./data`) contains your `.txt` files to be loaded by the DirectoryLoader.
- The `openai_api_key` should be kept confidential. Consider using environment variables or a configuration file to securely store and retrieve it.

## Contributing

Contributions are welcome! Please make sure to test your changes before submitting a pull request.
