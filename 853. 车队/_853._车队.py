
class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        if len(position)==0:
            return 0
        if len(position)==1:
            return 1
        distance=[]
        raw_time=[]
        for i in range(0,len(position)):
            distance.append(target-position[i])
            raw_time.append(distance[i]/speed[i])
        d_t=dict(zip(distance,raw_time))
        distance.sort()
        sum=1
        now_time=d_t[distance[0]]
        for i in range(1,len(distance)):
            if now_time>=d_t[distance[i]]:
                pass
            else:
                sum=sum+1
                now_time=d_t[distance[i]]
        return sum

