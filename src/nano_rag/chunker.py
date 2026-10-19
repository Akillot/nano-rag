def chunk_words(text: str, size: int, overlap: int) -> list[str]:
    if overlap >= size:
        raise ValueError("overlap should be smaller than size")

    if overlap < 0:
                raise ValueError("overlap should not be negative")
    
    words = text.split()
    step = size - overlap
    chunks = []

    for start in range(0, len(words), step):
        piece = words[start : start + size]
        chunks.append(" ".join(piece))

        if start + size >= len(words):
            break
    
    return chunks
 