### 题目描述

小 Polo 有一个 n × m 的整数矩阵，现在小 Polo 可以进行一种操作：在矩阵的一些元素上增加或减少 d。请帮助小 Polo 计算，至少需要多少次这样的操作使得矩阵的每个元素都相等。

### 输入描述

```
第一行为题意所述 n, m 和 d (1 ≤ n, m ≤ 100, 1 ≤ d ≤ 10^4)
接下来 n 行，每行 m 个整数，共同表示这个矩阵 (1 ≤ aij ≤ 10^4)
```

### 输出描述

```
如果结果存在，输出最少需要的操作数，否则输出 -1
```

### 测试样例

#### 样例1: 输入-输出

```
2 2 2
2 4
6 8
```

```
4
```

#### 样例2: 输入-输出

```
1 2 7
6 7
```

```
-1
```

### 题目来源

CodeForces