# 1-Spiral Memory
You come across an experimental new kind of memory stored on an infinite two-dimensional grid.  
Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then
counting up while spiraling outward. For example, the first few squares are allocated like this:  

17 16 15 14 13  
18  5  4  3 12  
19  6  1  2 11  
20  7  8  9 10  
21 22 23 24 25   

While this is very space-efficient (no squares are skipped), requested data must be carried back to
square 1 (the location of the only access port for this memory system) by programs that can only
move up, down, left, or right. They always take the shortest path: the Manhattan Distance between
the location of the data and square 1.  

For example:  
Data from square 1 is carried 0 steps, since it's at the access port.  
Data from square 12 is carried 3 steps, such as: down, left, left.  
Data from square 23 is carried only 2 steps: up twice.  
Data from square 1024 must be carried 31 steps.  

How many steps are required to carry the data from the square identified in your puzzle input all
the way to the access port?  
How to test your answer:  
If you input: 100000 Your Answer should be: 173  
If you input: 2345678 Your Answer should be: 1347  
  

# 2-Simple Number Finding
You are playing a card game with your friends. This game in China named “诈金花”. In this game, the
2, 3, 5 are some simple powerful numbers. Because the combination of 2,3,5 is less than any other combinations
but greater than the AAA, which is the king in this game. In today, you want to find if a number is a simple
number, in which their factors only include 2, 3 and 5.  
So your task is to find out whether a given number is an amazing number.  
  
E.g  
Input: 6  
Output: (2, 3)  
Explanation: 6 = 2 x 3  
Input: 14  
Output：None  
Explanation: 14 is not amazing since it includes another prime factor 7  

How to check your answer:  
If you test 1845281250, your program should give (2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5);  
If you test 3690562500, your program should give (2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5);  
If you test 1230187500, your program should give (2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5);  
If you test 10023750, your program should give None;  

# 3-Random Chinese Sentence Generator
Writing a programming which could generate random Chinese sentences based on one grammar.   
Your input grammar is:   

	simple_grammar = """ 
	sentence     =>  noun_phrase verb_phrase noun_phrase => Article Adj* noun 
	Adj          =>  蓝色的 |  好看的 | 小小的 |  年轻的  """ 
	Adj*         =>  null  | Adj Adj* 
	Article      =>  一个 | 这个 
	verb         =>  看着 | 听着 | 看见 
	noun         =>  女人 | 篮球 | 桌子 | 小猫
	verb_phrase  =>  verb noun_phrase

Your task is define a function called generate,  if we call generate(‘sentence’), you could see some sentences like: 
\>> generate(“sentence”)  
Output: 这个蓝色的女人看着一个小猫  
\>> generate(“sentence”)  
Output: 这个好看的小猫坐在一个女人  
