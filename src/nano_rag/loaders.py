from pathlib import Path
from nano_rag.document import Document


def load_text(path: Path) -> Document:
    text = path.read_text(encoding="utf-8")
    return Document(text=text, source=path)
