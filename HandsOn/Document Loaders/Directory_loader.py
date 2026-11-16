#for multiple files in a directory
from pathlib import Path

from langchain_community.document_loaders import DirectoryLoader, TextLoader

directory = Path(__file__).resolve().parent

loader = DirectoryLoader(
    str(directory),
    glob="**/*.txt",
    loader_cls=TextLoader,
    loader_kwargs={"encoding": "utf-8"},
)

documents = loader.load()

print(f"Loaded {len(documents)} document(s)")
for document in documents:
    print(f"\nSource: {document.metadata['source']}")
    print(document.page_content)
