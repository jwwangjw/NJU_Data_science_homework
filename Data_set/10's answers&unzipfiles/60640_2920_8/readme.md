### 题目描述

给你一个非递减正整数序列 a 和一个整数 k，你需要把这个序列分成 k 个非空子序列，每个子序列的价值为这个序列的最大值减去最小值。请选出一个最佳分割方法，使得所有子序列的价值和最小。

### 输入描述

```
第一行为序列长度 n 和子序列数 k (1≤k≤n≤3⋅10^5)
第二行为 n 个正整数表示序列元素 (1≤ai≤10^9, ai≥ai−1)
```

### 输出描述

```
输出一个整数表示最小价值和
```

### 测试样例

#### 样例1: 输入-输出

```
6 3
4 8 15 16 23 42
```

```
12
```

#### 样例2: 输入-输出

```
4 4
1 3 3 7
```

```
0
```

### 题目来源

CodeForces
