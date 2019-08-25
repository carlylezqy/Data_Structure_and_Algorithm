贪心 Greedy
### Big-$\mathcal{O}$
$$ T(n)=\mathcal{O}(f(n)) \quad \text { if } \quad \exists c>0 \quad \text { s.t. } \quad T(n)<c \cdot f(n) \quad \forall n \gg 2 $$
常系数、低次项从此可忽略：
+ $\mathcal{O}(f(n))=\mathcal{O}(c \cdot f(n)) $
+ $ \mathcal{O}\left(n^{a}+n^{b}\right)=\mathcal{O}\left(n^{a}\right), a \geq b>0$

+ Vector & Array
+ List & Linked List
+ Stack
+ Queue
+ (Binary) Tree

+ Graph as Matrix
1. undigraph (无向图)

||A|B|C|D|
|-|-|-|-|-|
|A||1|1||
|B|1||1|1|
|C|1|1|||
|D||1|||

2. digraph (有向图)

||A|B|C|D|
|-|-|-|-|-|
|A|||1||
|B|1||1|1|
|C|1||||
|D||1|||

3. network

||A|B|C|D|
|-|-|-|-|-|
|A|||3||
|B|7||9|2|
|C|4||||
|D||5|||

+ Graph as Vector <List>

    A -> &B|9 -> &C|3 -> &D|5
    A -> &B|9 -> &C|3 -> &D|5
    A -> &B|9 -> &C|3 -> &D|5

## Gnomesort: Naive + Improved

```C++
naiveGnomesort(S[], n)//single loop but O(n^2){
    for(int i=1; i<n;;)
        if(i<1 || S[i-1] <= S[i]) //GREEDY
            i++; //inefficient backtracking
        else swap(S[i-1], S[i]); i--;
}
improvedGnomesort(S[], n){ // nested loops and still O(n^2)
    for(int k=1; k<n; k++) //Since S[0, k) is always sorted, we can
        for(int i=k; 0<n && S[i-1] > S[i]; i--) //backtrack to k and rescan
            swap(S[i-1], S[i]);
}
```
## Bubblesort: Correctness
+ 不变性：经 $k$ 趟扫描交换后，最大的 $k$ 个元素必然就位
+ 单调性：经 $k$ 趟扫描交换后，问题规模缩减至 $n-k$
+ 正确性：经至多 $n$ 趟扫描后，算法必然终止，且能给出正确解答
### 1.Basic Version
拆分版
```C++
template <typename T>
void Vector<T> :: bubbleSort(Rank lo, Rank hi){
    while(lo < hi) //反复起泡
        bubble(lo, hi--); //理解算法后可整合为两重循环
} //各元素自大而小依次就位
template <typename T>
void Vector<T> :: bubble(Rank lo, Rank hi){
    while(++lo < hi) //自左向右，逐一检查各队相邻元素
        if(_elem[lo-1] > _elem[lo]) // 若逆序，则
            swap(_elem[lo-1], _elem[lo]); //交换
}

```
整合版
```C++
template <typename T> //0 <= lo < hi <= size
void Vector<T> :: bubbleSort(Rank lo, Rank hi){
    while(lo < --hi){ //逐趟起泡扫描
        for(Rank i = lo; i < hi; i++) //若相邻元素
            if(_elem[i] > _elem[i+1]) //逆序
                swap(_elem[i], _elem[i+1]);  //则交换
    }
}
```

+ $n-1$ 趟起泡扫描一定足够，但往往不必，比如...
+ [hi] 就位后，[lo, hi）可能已经有序——此时，应该可以...

### 2.提前终止
拆分版
```C++
template <typename T>
void Vector<T> :: bubbleSort(Rank lo, Rank hi){
    while(!bubble(lo, hi--)); //逐趟扫描交换，直至全序
}
template <typename T>
void Vector<T> :: bubble(Rank lo, Rank hi){
    bool sorted = true;
    while(++lo < hi) // 自左向右，逐一检查各对相邻元素
        if(_elem[lo-1] > _elem[lo]){ //若逆序，则
            sorted = false; //意味着尚未整体有序，并需要
            swap(_elem[lo-1], _elem[lo]); //交换
        }
    return sorted; //整体是否有序
}
```
乱序限于 $[0, \sqrt{n})$ ，仍需 $\mathcal{O}(n^{3/2})$ 时间——按理，$\mathcal{O}(n)$ 应已足矣。


整合版
```C++
template <typename T> //0 <= lo < hi <= size
void Vector<T> :: bubbleSort(Rank lo, Rank hi){
    for(bool sorted = false; i < hi-1; i++)
        if(_elem[i] > _elem[i+1]) //逆序则
            swap(_elem[i], _elem[i+1]),sorted = false; //交换——当然，至此还不能确定已整体有序
}
```

+ 有改进，但仍有继续改进的余地，比如...
+ [hi]就位后，尽管 [lo, hi) 未必有序，但某后缀 [last, hi) 可能有序——此时，应该可以...

省略无效起泡
```C++
template <typename T>
void Vector<T> :: bubbleSort(Rank lo, Rank hi){
    while(lo < (hi = bubble(lo, hi))); //逐趟扫描交换，直至全序
}
template <typename T>
void Vector<T> :: bubble(Rank lo, Rank hi){
    Rank last = lo;
    while(++lo < hi) //自左向右，逐一检查各队相邻元素
        if(_elem[lo-1] > _elem[lo]){ //若逆序，则
            last = lo;
            swap(_elem[lo-1], _elem[lo]); //交换
        }
    return last; //逆序对均在last以左
}
```

## Matrix Sorting
试证明一下元素，当先对每列元素进行排序，再对每行元素排序时，每列元素依然保持有序。

|5|8|7|3|5|
|-|-|-|-|-|-|
|1|5|2|8|8|
|0|9|4|6|2|
|6|3|1|4|7|

|a|x|
|b|y|
若相邻两个元素，在下列情况时依旧满足，则得证。
+ $a < x && b < y$ 时 $a < b && x < y$
+ $a > x && b < y$ 时 $x < b && a < y$

## Huffman: PFC Coding
"1/010/011/00" = "MAIN"
### Huffman: Unweighted Optimal Complete

    ald(T) * 4 = 2+3+3+1 = 9 (三层)
    "1/010/011/00" = "MAIN"

    ald(T) * 4 = 2+2+2+2 = 8 (两层)
    "01/10/11/00" = "MAIN"

    ald(T) * 4 = 2+3+3+1 = 9 (三层)
    "01/000/001/1" = "MAIN"

二叉树优化原则：在最深层拥有两个叶子的结点与最浅层拥有一个叶子节点的距离相差2以上时，两个叶子的结点的父节点可以与最浅层的节点互换以达到最优化（满二叉树）。

树在数据结构中占有非常重要的地位。本文从树的基本概念入手，给出完美(Perfect)二叉树，完全(Complete)二叉树和完满(Full)二叉树的区别。

### 树(Tree)

    A tree is a (possibly non-linear) data structure made up of nodes or vertices 
    and edges without having any cycle. The tree with no nodes is called the null 
    or empty tree. A tree that is not empty consists of a root node and potentially 
    many levels of additional nodes that form a hierarchy.

#### 满二叉树
