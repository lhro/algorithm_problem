
class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        at=[[0 for j in range(0,len(A))] for i in range(0,len(A[0]))]
        for m in range(0,len(A)):
            for n in range(0,len(A[0])):
                at[n][m]=A[m][n]
        return at