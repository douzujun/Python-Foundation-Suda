# -*- coding: utf-8 -*-

class WordsFrequency:

    def __init__(self, book):
        self.freq = {}
        for b in book:
            self.freq[b] = self.freq.get(b, 0) + 1

    def get(self, word: str) -> int:
        return self.freq.get(word, 0)


# Your WordsFrequency object will be instantiated and called as such:
wordsFrequency = WordsFrequency(["i", "have", "an", "apple", "he", "have", "a", "pen"])
print(wordsFrequency.get("you") )


