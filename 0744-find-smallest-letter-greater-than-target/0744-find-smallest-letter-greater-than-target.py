class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        alph="abcdefghijklmnopqrstuvwxyz"
        for i in letters:
            if alph.index(target)<alph.index(i):
                return i
                break
        else:
            return letters[0]