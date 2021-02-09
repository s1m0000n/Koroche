from pydantic import BaseModel


class WordOccurences(BaseModel):
    lemma: str
    occurrences: int


class Statistics(BaseModel):
    total_symbols: int
    total_word_usages: int
    total_words: int
    top_word_occurrences: list[WordOccurences]


class SpellingCorrection(BaseModel):
    original_word: str
    fixed_word: str
    position_in_text: int
    diff_len: int



class SpellingCorrectionsList(BaseModel):
    corrections: list[SpellingCorrection]
    updated: str
