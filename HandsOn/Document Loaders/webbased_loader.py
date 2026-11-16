from langchain_community.document_loaders import WebBaseLoader

url = "https://www.example.com/"

loader = WebBaseLoader(web_paths=(url,))
documents = loader.load()

print(f"Loaded {len(documents)} document(s)")
for document in documents:
    print(f"\nSource: {document.metadata.get('source', url)}")
    print(document.page_content[:1000])
