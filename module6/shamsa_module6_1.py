
# import all req. libraries 
from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

# ---------- SETTINGS ----------
EMBED_MODEL = "nomic-embed-text"
PERSIST_DIR = "db"

# ---------- STEP 1: Load document ----------
docs = Docx2txtLoader("my_file.docx").load()

# ---------- STEP 2: Split text ----------
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# ---------- STEP 3: Embeddings (Ollama) ----------
embeddings = OllamaEmbeddings(
    model=EMBED_MODEL,
    base_url="http://127.0.0.1:11434"
)

# ---------- STEP 4: Store in Chroma ----------
db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=PERSIST_DIR
)
# NOTE: No need for db.persist() anymore (auto-persist)

# ---------- STEP 5: Retriever ----------
retriever = db.as_retriever(search_kwargs={"k": 3})

query = input("Enter your question: ")

# New LangChain way:
results = retriever.invoke(query)

# ---------- STEP 6: Show results ----------
for i, doc in enumerate(results, 1):
    print(f"\nResult {i}:")
    print(doc.page_content)


#Should install all these in Terminal :

#pip install -U langchain langchain-community langchain-ollama chromadb docx2txt
#pip install -U langchain langchain-community chromadb docx2txt ollama


