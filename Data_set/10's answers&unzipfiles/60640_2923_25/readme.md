### 题目描述

给定一个有 n 个整数的数组 a，下标从 1 开始。然后有 q 个询问，询问以 li,ri(li<=ri) 的形式给出，求数组 a 从 li 到 ri 的区间和。

这个问题很无聊，现在假设在询问开始之前，你有机会重新排列数组 a，使得这 q 个询问的结果的和最大，请求出这个最大值。

### 输入描述

```
第一行数组长度 n (1<=n<=2*10^5) 和查询数 q (1<=q<=2*10^5).
第二行 n 个正整数 ai (1<=ai<=2*10^5).
接下来 q 行,每行两个正整数 li 和 ri (1<=li<=ri<=n)
```

### 输出描述

```
输出一个整数表示这 q 个查询结果的和的最大值
```

### 测试样例

#### 样例1: 输入-输出

```
3 3
5 3 2
1 2
2 3
1 3
```

```
25
```

#### 样例2: 输入-输出

```
5 3
5 2 4 1 3
1 5
2 3
2 3
```

```
33
```

### 题目来源

CodeForces