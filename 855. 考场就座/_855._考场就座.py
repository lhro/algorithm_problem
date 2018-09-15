import math

class ExamRoom:

    def __init__(self, N):
        """
        :type N: int
        """
        self.max_index=N-1
        self.seat_list=[]
        

    def seat(self):
        """
        :rtype: int
        """
        if len(self.seat_list)==0:
            self.seat_list.append(0)
            return 0
        #断言：self.seat_list有序，降序
        
        better_index=self.max_index
        better_distance=self.max_index-self.seat_list[0]-1

        for i in range(1,len(self.seat_list)):
            if int((self.seat_list[i-1]+self.seat_list[i])/2)-self.seat_list[i]-1>=better_distance:
                better_index=int((self.seat_list[i-1]+self.seat_list[i])/2)
                better_distance=better_index-self.seat_list[i]-1

        if self.seat_list[-1]-1>=better_distance:
            better_index=0
            better_distance=self.seat_list[-1]-1

        self.seat_list.append(better_index)
        self.seat_list.sort()
        self.seat_list.reverse()
        return better_index

        

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        try:
            self.seat_list.remove(p)
        except ValueError:
            pass
        
print('hello')
obj = ExamRoom(4)
for i in range(4):
    print('i=',i,obj.seat())
