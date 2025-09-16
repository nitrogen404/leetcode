class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vovels = set('aeiouAEIOU')
        words = sentence.split()
        result = []
        for i, word in enumerate(words):
            if word[0] in vovels:
                goat_word = word + "ma"
            else:
                goat_word = word[1:] + word[0] + "ma"
            goat_word += 'a' * (i + 1)
            result.append(goat_word)
        return " ".join(result)
