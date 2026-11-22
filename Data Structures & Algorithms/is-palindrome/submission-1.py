class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters from the left
            while left < right and not s[left].isalnum():
                left += 1
            # Skip non-alphanumeric characters from the right
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare lowercase characters; if they don't match, fail fast
            if s[left].lower() != s[right].lower():
                return False

            # Move both pointers inward together
            left += 1
            right -= 1

        # If we checked everything without a mismatch, it's a palindrome
        return True