from pathlib import Path

from langchain_community.document_loaders import CSVLoader

csv_path = Path(__file__).resolve().parent / "sample.csv"
if not csv_path.is_file():
    raise FileNotFoundError(
        f"CSV file not found: {csv_path}. Place your CSV beside this script "
        "or update csv_path."
    )

loader = CSVLoader(
    file_path=str(csv_path),
    encoding="utf-8",
    csv_args={"delimiter": ","},
)
documents = loader.load()

print(f"Loaded {len(documents)} row(s)")
for document in documents:
    print(document.page_content)
