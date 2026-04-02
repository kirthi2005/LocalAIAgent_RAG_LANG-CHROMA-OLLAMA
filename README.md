
# Building a Local AI Agent using Python, Ollama, RAG, Langchain and ChromaDB  

## Steps involved
  1. downlaod ollama
  
  2.  **Create virtual environment:** Python -m venv .venv ./venv/Scripts/activate
  
  3.  **Install all the required dependencies mentioned in requirements.txt:** pip install -r requirements.txt
  
  4.   **Pull Ollama models we are going to use:** ollama pull llama3.2
  
  5.  **Pull Ollama models we are going to use:** ollama pull mxbai-embed-large
     
  6.  **To run main.py:** python .\main.py 
  
 ## Error & Solution 
  Getting Error: Import "langchain_ollama.llms" could not be resolved. checking 
    i. its installed or not: pip list | findstr langchain 
    ii. python -c "from langchain_ollama import OllamaLLM; print('OK')" 
    iii. Press Ctrl + Shift + P. Type "Python: Select Interpreter". Choose the one that explicitly points to c:\ai\RAG_LANG_CHROMA_OLLAMA.venv\Scripts\python.exe. (this step resolved the issue. before global python path was selected)
  
  In command prompt check what are the ollama models available ollama list NAME ID SIZE MODIFIED mxbai-embed-large:latest 468836162de7 669 MB 2 hours ago llama3.2:latest a80c4f17acd5 2.0 GB 2 hours ago
  
 ## gitignore  
  **Create .gitignore file and add following folders/files:**.venv/ pycache/ *.pyc # Ignore your ChromaDB folder (usually better to rebuild locally) chroma_db/ .env run: 

  ## git commands
    *git init
    *git add . 
    *git commit -m "RAG project with LangChain and Chroma using Ollama"
    *git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
    *git branch -M main
    *git push -u origin main
