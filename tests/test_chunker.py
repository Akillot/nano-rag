from nano_rag.chunker import chunk_words


def test_sentence_slicing_into_chunks():
    text = "Praha je hlavní město a největší město České republiky dnes"
    result = chunk_words(text, size=4, overlap=1)
    assert result == ['Praha je hlavní město', 'město a největší město', 'město České republiky dnes']
