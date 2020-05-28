class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.islower():
            return True
        if word.isupper():
            return True
        elif word[0].isupper() and word[1:].islower():
            return True
        else:
            return False