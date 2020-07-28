### 题目描述

给定两个长度为 n 的数组 a 和 b。现在你可以为数组 a 的连续一段 [l, r] 加上 k。

例如，如果 a = [3,7,1,4,1,2] 并选择（l = 3，r = 5，k = 2），则数组a将变为 [3,7,3,6,3,2]。

您最多可以执行一次此操作。 你能使数组 a 等于数组 b 吗？

### 输入描述

```
第一行为测试数据的个数 t (1≤t≤20)
接下来每三行为一个测试数据：
- 第一行为数组的长度 n (1≤n≤100000) 
- 第二行为数组 a (1≤ai≤1000)
- 第三行为数组 b (1≤bi≤1000)
```

### 输出描述

```
如果能，输出 YES，否则输出 NO
```

### 测试样例

#### 样例1: 输入-输出

```
4
6
3 7 1 4 1 2
3 7 3 6 3 2
5
1 1 1 1 1
1 2 1 3 1
2
42 42
42 42
1
7
6
```

```
YES
NO
YES
NO
```

#### 样例2: 输入-输出

```
2
1
2
1
1
1
1
```

```
NO
YES
```

### 题目来源

CodeForces