cmake_minimum_required(VERSION 3.14)
project(CS101)

set(CMAKE_CXX_STANDARD 14)

include_directories(Week_0)

add_executable(CS101
        Week_0/1-A+B问题.cpp
        Week_0/2-栈排序.cpp
        Week_0/2-栈排序.out
        Week_0/2-栈排序.xlsx
        Week_0/3-直方图最大面积.cpp
        Week_0/3-直方图最大面积.out
        Week_0/3-直方图最大面积.xlsx
        Week_0/4.cpp
        Week_0/4-最大红矩形.out
        Week_0/bits/stdc++.h
        Week_0/bits/stdc++.out)
