class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reverse=0
        original=x
        while x>0:
            last_digit=x%10
            reverse=(reverse*10)+last_digit
            x//=10
        
        if original==reverse:
            return True
        else:
            return False
