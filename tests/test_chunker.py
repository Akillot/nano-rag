import pytest
from nano_rag.chunker import chunk_words


def test_sentence_slicing_into_chunks():
    text = "Praha je hlavní město a největší město České republiky dnes"
    result = chunk_words(text, size=4, overlap=1)
    assert result == ['Praha je hlavní město', 'město a největší město', 'město České republiky dnes']


def test_value_error_raises_when_overlap_equals_size():
    text = "a b c"
    with pytest.raises(ValueError, match="overlap should be smaller than size"):
        chunk_words(text, size=4,overlap=4) 
