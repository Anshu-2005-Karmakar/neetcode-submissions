class Solution:
    def isPalindrome(self, s: str) -> bool:
        words = s.split()
        temp = ""
        for word in words :
            for ch in word :
                if ch.isalnum():
                    temp += ch.lower()
        i = 0 
        j = len(temp) - 1
        palin = True
        while i < j :
            if temp[i] != temp[j]:
                palin = False 
                break
            i += 1
            j -= 1 
        if palin :
            return True
        else :
            return False
o = Solution()
s = "Was it a car or a cat I saw?"
o.isPalindrome(s)

        