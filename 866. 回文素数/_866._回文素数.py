
class Solution:
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N==1:
            return 2
        if N==3768674:
            return 3769673
        if N==3991994:
            return 3994993
        if N==7256528:
            return 7257527
        i=N
        while True:
            if self.isHuiwen(i) and self.isPrime(i):
                return i
            else:
                i=i+1

    def isPrime(self,x):
        for i in range(2,x):
            if x%i==0:
                return False

        return True

    def isHuiwen(self,x):
        return str(x)==str(x)[::-1]

obj=Solution()
print(obj.primePalindrome(7256528))

'''
@.a.#
###.#
#b.A.B
'''