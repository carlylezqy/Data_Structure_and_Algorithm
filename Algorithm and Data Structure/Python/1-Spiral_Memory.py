import numpy as np

class SpiralMemory:
    squares = []
    length = 0
    number = 0
    def __init__(self,number):
        self.number = number
        self.length = self.default_length()
        if self.length%2 == 0:
            self.length += 1
        self.squares = self.make_array(self.length)
        #print(self.squares)

    def default_length(self,min=1,max=999999):
        # 根据待查找数，匹配斜向元素的平方对应的最大索引
        # 返回推荐的SpiralMemory数组的最大长度
        # max：支持创建的最大奇数索引
        for value in range(min,max,2):
            if self.number <= value**2:
                return value

    def make_array(self,length):
        index_x = index_y = int(length/2)
        border_x = int(length/2) + 1
        border_y = int(length/2)
        self.squares = np.zeros([length,length])
        self.squares[index_y,index_x] = 1
        value = 2
            
        half_circle = 1

        while value < length*length:
            #print(value,length*length)
            while index_x < border_x and index_y == border_y:
                index_x += 1
                self.squares[index_y, index_x] = value
                #print('->',index_x,index_y)
                value += 1
            #print(self.squares)
            border_y -= half_circle
            half_circle += 1

            if value >= length*length:
                break

            while index_y > border_y  and index_x == border_x:
                index_y -= 1
                self.squares[index_y, index_x] = value
                #print('^',index_x,index_y)
                value += 1
            #print(self.squares)
            border_x -= half_circle
            while index_x > border_x and index_y == border_y:
                index_x -= 1
                self.squares[index_y, index_x] = value
                #print('<-',index_x, index_y)
                value += 1
            #print(self.squares)
            border_y += half_circle
            half_circle += 1
            while index_y < border_y and index_x == border_x:
                index_y += 1
                self.squares[index_y, index_x] = value
                #print('.', index_x, index_y)
                value += 1
            border_x += half_circle
            if  border_x >= length and border_y == length -1:
                border_x = length-1
        return(self.squares)
    
    def find(self):
        if(self.number == 0):
            return None
        index = self.find_circle(self.find_line())
        #print(index)
        return self.distance(index)

    def find_line(self):
        if self.squares is None:
            return None
        if self.number == 1:
            return 0
        for i in range(self.length -1 ,int(self.length/2) -1 ,-1):
            if self.squares[i,i] < self.number:
                return i + 1

    def find_circle(self,line):
        #print(range(len(self.squares) - line -1, line))
        for i in [self.length - line - 1, line]:
            for j in range(self.length - line - 1, line + 1):
                #print(i,j)
                if self.squares[j,i] == self.number:
                    return(i,j)
                if self.squares[i,j] == self.number:
                    return(j,i)

    def distance(self,index):
        return abs(int(self.length/2)-index[0]) + abs(int(self.length/2)-index[1])

wannafind = 2345678
print(SpiralMemory(wannafind).find())
