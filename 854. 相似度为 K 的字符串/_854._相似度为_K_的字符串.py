class Solution:
    def __init__(self):
        self.memo=dict()

    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        A=list(A)
        B=list(B)
        sum=999999999
        if len(A)<=1:
            return 0
        if A[-1]==B[-1]:
            return self.kSimilarity(A[:-1],B[:-1])
        for i in range(0,len(A)-1):
            if A[i]==B[-1]:
                A_copy=A[:-1]
                A_copy[i]=A[-1]
                if str(A_copy) in self.memo:
                    temp=self.memo[str(A_copy)]
                else:
                    temp=self.kSimilarity(A_copy,B[:-1])
                    self.memo[str(A_copy)]=temp
                sum=min((sum,temp))

        return sum+1

obj=Solution()
print(obj.kSimilarity('abc','bca'))
