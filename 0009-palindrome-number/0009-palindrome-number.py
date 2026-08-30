class Solution:
    def isPalindrome(self, x: int) -> bool:
        # = list(input("Enter the word: "))
        b=list(str(x))
        reverse_word = b.copy()
        reverse_word.reverse()

        if b== reverse_word:
            return True
        else:
            return False