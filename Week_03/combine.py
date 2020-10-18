def combine(self, n: int, k: int) -> List[List[int]]:

    res=[]
    currentset=[]
        # lis=[i for in in range(n)]
    def recur(n,k,current_index,currentset,res):

            # nonlocal res
         if len(currentset)==k:
            res.append(currentset[:])
            return
         for num in range(current_index,n):

             currentset.append(num)
             recur(n,k,current_index+1,currentset,res)
             currentset.pop()
        

    recur(n,k,1,currentset,res)
    return res

