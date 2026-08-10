from text_toolkit.core import count_words
def test_count_words_simple():
    result=count_words("the cat sat on the mat")
    assert result == {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}


def test_count_words_empty_string():
    result = count_words("")
    assert result == {}


def test_count_words_case_sensitive():
    result = count_words("The the THE")
    assert result == {"The": 1, "the": 1, "THE": 1}