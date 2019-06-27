import numpy as np

array = []
    
def make_array(length):
    squares = []
    if length%2 == 0:
        length += 1
    index_x = index_y = int(length/2)
    border_x = int(length/2) + 1
    border_y = int(length/2)
    squares = np.zeros([length,length])
    squares[index_y,index_x] = 1
    value = 2
        
    half_circle = 1

    while value < length*length:
        #print(value,length*length)
        while index_x < border_x and index_y == border_y:
            index_x += 1
            squares[index_y, index_x] = value
            #print('->',index_x,index_y)
            value += 1
        #print(squares)
        border_y -= half_circle
        half_circle += 1

        if value >= length*length:
            break

        while index_y > border_y  and index_x == border_x:
            index_y -= 1
            squares[index_y, index_x] = value
            #print('^',index_x,index_y)
            value += 1
        #print(squares)
        border_x -= half_circle
        while index_x > border_x and index_y == border_y:
            index_x -= 1
            squares[index_y, index_x] = value
            #print('<-',index_x, index_y)
            value += 1
        #print(squares)
        border_y += half_circle
        half_circle += 1
        while index_y < border_y and index_x == border_x:
            index_y += 1
            squares[index_y, index_x] = value
            #print('.', index_x, index_y)
            value += 1
        border_x += half_circle
        if  border_x >= length and border_y == length -1:
            border_x = length-1
    return(squares)
        
def find_line(squares,num):
    if squares is None:
        return None
    if num == 1:
        return 0
    for i in range(len(squares) -1 ,int(len(squares)/2) -1 ,-1):
        if squares[i,i] < num:
            return i + 1

def find_circle(squares,line,num):
    #print(range(len(squares) - line -1, line))
    for i in [len(squares) - line - 1, line]:
        for j in range(len(squares) - line - 1, line + 1):
            #print(i,j)
            if squares[j,i] == num:
                return(i,j)
            if squares[i,j] == num:
                return(j,i)

def effective_length(num):
    for value in range(1,999999,2):
        if num <= value**2:
            #print(num,value**2)
            return value

wannafind = 2345678

array = make_array(effective_length(wannafind))
#print(array)
#print(find_line(array,wannafind))
index = find_circle(array,find_line(array,wannafind),wannafind)
print(abs(int(len(array)/2)-index[0]) + abs(int(len(array)/2)-index[1]))
