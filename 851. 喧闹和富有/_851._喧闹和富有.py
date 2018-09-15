
class Solution:
    def loudAndRich(self, richer, quiet):
        self.quiet=quiet
        self.answer=[None for i in range(0,len(quiet))]
        self.pre_con=[[] for i in range(0,len(quiet))]
        for i in richer:
            self.pre_con[i[1]].append(i[0])
        for i in range(0,len(quiet)):
            self.ans(i)
        return self.answer
    def ans(self,i):
        if self.answer[i]!=None:
            return self.answer[i]
        if len(self.pre_con[i])==0:
            self.answer[i]=i
            return i
        self.answer[i]=i
        for j in self.pre_con[i]:
            if self.quiet[self.answer[i]]>self.quiet[self.ans(j)]:
                self.answer[i]=self.ans(j)
        return self.answer[i]
        
    '''
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        answer=[]
        pre_stack=[]
        pre_con=[[] for i in range(0,len(quiet))]
        for i in richer:
            pre_con[i[1]].append(i[0])
        for i in range(0,len(quiet)):
            pre_stack.clear()
            answer.append(i)
            pre_stack.append(i)
            while len(pre_stack)>0:
                temp=pre_stack.pop()
                for j in pre_con[temp]:
                    pre_stack.append(j)
                if quiet[answer[i]]>quiet[temp]:
                    answer[i]=temp
        return answer
        '''
        

obj=Solution()
print(obj.loudAndRich([[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]],[3,2,5,4,6,1,7,0]))
        


