# RAG-Based AI-Powered FAQ System

## Overview
This project is a Retrieval-Augmented Generation (RAG)-based system that uses FastAPI as the backend framework. It allows users to upload documents, retrieve relevant documents using similarity search, and generate responses to queries using a language model (OpenAI's GPT-3.5).

## Features
1. **FastAPI Backend**:
   - REST API endpoints for document ingestion, vector indexing, and querying.
   - Health check endpoint to monitor service status.

2. **Document Storage & Vector Indexing**:
   - MongoDB for raw text document storage.
   - FAISS for vector-based similarity search.
   - Sentence Transformers for embedding generation.

3. **Retrieval-Augmented Generation (RAG)**:
   - Retrieves relevant documents based on a user query.
   - Uses OpenAI's GPT-3.5 to generate responses from retrieved documents.

4. **Frontend**:
   - Simple HTML+CSS+JavaScript interface for user interaction.
   - Users can input queries and view generated answers.

5. **Authentication**:
   - JWT-based authentication for secure endpoints.

## Prerequisites
- Python >= 3.8
- Node.js (optional for serving frontend)
- MongoDB installed and running

## Folder Structure
```plaintext
stu/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── db.py
│   │   ├── auth.py
│   │   ├── utils.py
│   │   └── config.py
│   ├── requirements.txt
│   └── README.md
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── .gitignore
```

## Setup Instructions

### Backend
1. **Navigate to the backend folder:**
   ```bash
   cd stu/backend
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables:**
   Create a `.env` file in `backend/app/` with the following content:
   ```env
   MONGO_URI=mongodb://localhost:27017
   OPENAI_API_KEY=your_openai_api_key
   ```

6. **Run the FastAPI server:**
   ```bash
   uvicorn app.main:app --reload
   ```
   The backend will be available at [http://localhost:8000](http://localhost:8000).

### Frontend
1. **Navigate to the frontend folder:**
   ```bash
   cd ../frontend
   ```

2. **Serve the HTML file:**
   - Open `index.html` directly in your browser.
   - Alternatively, use a lightweight server:
     - Using Python:
       ```bash
       python -m http.server 8080
       ```
     - Open your browser and go to [http://localhost:8080](http://localhost:8080).

## Endpoints

### 1. **Health Check**
- **URL**: `/health/`
- **Method**: GET
- **Description**: Check if the backend service is running.

### 2. **Upload Document**
- **URL**: `/documents/`
- **Method**: POST
- **Description**: Upload a document to the system.
- **Payload Example**:
  ```json
  {
      "content": "This is a sample document.",
      "metadata": {
          "author": "John Doe",
          "category": "Example"
      }
  }
  ```

### 3. **List Documents**
- **URL**: `/documents/`
- **Method**: GET
- **Description**: Retrieve a list of all stored documents.

### 4. **Query Document**
- **URL**: `/query/`
- **Method**: POST
- **Description**: Retrieve relevant documents and generate a response using the query.
- **Payload Example**:
  ```json
  {
      "query": "What is the content of the document?"
  }
  ```

### 5. **Secure Endpoint**
- **URL**: `/secure-endpoint/`
- **Method**: GET
- **Description**: Access a protected endpoint using JWT authentication.

## Usage

1. **Upload Documents**:
   Use the `/documents/` endpoint to upload documents for indexing.

2. **Ask a Query**:
   Use the frontend to submit a query or directly use the `/query/` endpoint to retrieve relevant answers.

3. **Authentication**:
   Generate a JWT token using the `/auth/token/` endpoint and use it to access secure endpoints.

## Dependencies
- **Backend**:
  - FastAPI
  - Pymongo
  - FAISS
  - Sentence Transformers
  - OpenAI
  - Bcrypt
  - Python JWT
- **Frontend**:
  - HTML, CSS, JavaScript

## Git Ignore Setup
Add the following `.gitignore` file to the project to exclude unnecessary files:
```gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]

# Virtual environment
venv/

# dotenv environment variable file
*.env

# Logs
*.log

# OS-specific files
.DS_Store
Thumbs.db

# IDE-specific files
.vscode/
.idea/
*.swp

# Node modules (if using Node.js)
node_modules/

# Python egg files
*.egg
*.egg-info/
```

## Future Improvements
1. Implement role-based access control for document management.
2. Cache frequent queries for faster response times.
3. Deploy the backend on a cloud platform (e.g., AWS, Azure, or Heroku).

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

---
Let me know if you have any issues or need additional assistance!
