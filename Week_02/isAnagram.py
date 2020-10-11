def isAnagram(self,s:str,t:str):
    if len(s)!=len(t):
        return False
    return(True if sorted(s)==sorted(t) else False)



