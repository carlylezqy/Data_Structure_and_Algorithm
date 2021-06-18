## bst bbst

堆https://www.jianshu.com/p/6b526aa481b1

### 二叉搜索树 (Binary Search Tree)，是指一棵空树或者具有下列性质的二叉树：
1. 若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值；
2. 若任意节点的右子树不空，则右子树上所有节点的值均大于它的根节点的值；
3. 任意节点的左、右子树也分别为二叉查找树；
4. 没有键值相等的节点。

二叉查找树相比于其他数据结构的优势在于查找、插入的时间复杂度较低。为 $ O(\log n) $。二叉查找树是基础性数据结构，用于构建更为抽象的数据结构，如集合、多重集、关联数组等。
改进版二叉树：AVL树、红黑树等。

```C++
Status SearchBST(BiTree T, KeyType key, BiTree f, BiTree &p) {
    // 在根指针T所指二元查找树中递归地查找其关键字等于key的数据元素，若查找成功，
    // 则指针p指向该数据元素节点，并返回TRUE，否则指针指向查找路径上访问的最后
    // 一个节点并返回FALSE，指针f指向T的双亲，其初始调用值为NULL
    if (!T) { // 查找不成功
        p = f;
        return false;
    } else if (key == T->data.key) { // 查找成功
        p = T;
        return true;
    } else if (key < T->data.key) // 在左子树中继续查找
        return SearchBST(T->lchild, key, T, p);
    else // 在右子树中继续查找
        return SearchBST(T->rchild, key, T, p);
}
```

## Hashtable Dictionary Map
beauty = dict # Python dictionary (hashtable)
({"沉鱼":"西施", "落雁":"昭君", "闭月":"貂蝉", "羞花":"玉环"})

15 -> 156 -> 861 -> 109 -> 579 (mod 47)
散列表索引建立方法：取模 (mod 一般为素数)

## Priority Queue ~ Heap (优先级队列)
## Huffman: Stack + Queue
## Minimum Spanning Tree (最小生成树、最小支撑树) 
使用最少的线段（最小代价）联通各个节点。
最小线段限制：一条线段不能连接三个点。
最大线段限制：(n-1) 破拆环路。

## Prim: Cut + Cross

## Kruskal: Sorting by Weight

## Union-Find (并查集)

## Quick-Find
## Slowly-Find

## Path Compression