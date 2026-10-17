def chunk_words(text: str, size: int, overlap: int) -> list[str]:
    words = text.split()
    step = size - overlap
    chunks = []

    for start in range(0, len(words), step):
        piece = words[start : start + size]
        chunks.append(" ".join(piece))

        if start + size >= len(words):
            break
        
    return chunks
    