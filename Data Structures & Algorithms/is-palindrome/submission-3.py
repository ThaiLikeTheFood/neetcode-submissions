class Solution:
    def isPalindrome(self, s: str) -> bool:
        combinedString = "".join(filter(str.isalnum,s))
        TString = combinedString.lower()
        start = 0
        end = len(TString)-1
        while start != end and start<len(TString)-1:
            if(TString[start] != TString[end]):
                return False
            start+=1
            end-=1
        return True

        