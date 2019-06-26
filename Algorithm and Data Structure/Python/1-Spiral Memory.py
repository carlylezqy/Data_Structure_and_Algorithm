import numpy as np
def make_array(length):
    if length%2 == 0:
        length += 1
    index_x = index_y = int(length/2)
    border_x = border_y = int(length/2) + 1
    squares = np.zeros([length,length])
    squares[index_y,index_x] = 1
    print(squares)
    print("*******************")
    value = 2
    circle = 1
    while value < length**2 + 1:
        while index_x < border_x and index_y < border_y:
            index_x += 1
            squares[index_y, index_x] = value
            print('->',index_x,index_y)
            value += 1
        print(squares)
        while index_y > int((border_y + 1)/2) - circle and index_x == border_x:
            index_y -= 1
            squares[index_y, index_x] = value
            print('^',index_x,index_y)
            value += 1
        print(squares)
        print(index_x,border_x,index_y,border_y,"********")
        while index_x > int((border_y + 1)/2) - circle and index_y == int((border_y + 1)/2) - circle:
            index_x -= 1
            squares[index_y, index_x] = value
            print('<-',index_x,index_y)
            value += 1
        print(squares)
        while index_y < border_y and index_x == int((border_y + 1)/2) - circle:
            index_y += 1
            squares[index_y, index_x] = value
            print('.',index_x,index_y)
            value += 1
        border_x += 1
        border_y += 1
        circle += 1
        print(squares)
        print(circle)
        
    
make_array(7)