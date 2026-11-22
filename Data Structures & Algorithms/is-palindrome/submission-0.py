class Solution:
    def isPalindrome(self, s: str) -> bool:
        mystr = "".join(letter.lower() for letter in s if letter.isalnum())
        return mystr[::-1] == mystr