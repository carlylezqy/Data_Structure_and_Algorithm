# 高效列表(list)赋值法
list = [1, 2, 3, 4]
start = 0
end = len(list) - 1
a, b, c = list[start:end]
#print(b)

# 迭代器对象(イテレータオブジェクト)
season = ['Spring', 'Summer', 'Fall', 'Winter']
iter_season = iter(season)
rev_season = reversed(season)

#print(type(iter_season))
#print(type(rev_season))

#print(next(iter_season), next(rev_season))

for (i,j) in zip(iter_season, rev_season):
    print()
    #print(i, j)

import itertools
it = itertools.chain(season[:2], season[2:])
it2 = itertools.zip_longest([0, 1, 2, 3], season)
print(type(it))
for (i, j) in zip(it, it2):
    print(i, j[1])


# About more: https://www.sejuku.net/blog/23570


# numpy相关
## 快速创建指定大小的递进矩阵
import numpy as np

aH = 100
aW = 100
y = np.arange(aH).repeat(aW).reshape(aW, -1)
print(y)

## 矩阵拉伸

