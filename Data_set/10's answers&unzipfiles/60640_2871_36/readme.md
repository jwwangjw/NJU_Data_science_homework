### 题目描述

有 n 组学生参加训练比赛。每组学生的人数，要么是 1 人，要么是 2 人。

为了训练方便，教练决定将学生划分为 3 人团队。请判断能够形成的 3 人团队，最多有多少个。可能不会用到全部组的学生。对于 2 人的组，他们要么不参加任何团队，要么参加到同一个团队中。

### 输入描述

```
第一行包含单个整数 n (2 ≤ n ≤ 2·10^5)，表示组的数量。
第二行包含一个整数序列 (1 ≤ ai ≤ 2)，其中 ai 表示第 i 组中的人数。
```

### 输出描述

```
输出教练能够划分出的 3 人团队的最大数量
```

### 测试样例

#### 样例1: 输入-输出

```
4
1 1 2 1
```

```
1
```

#### 样例2: 输入-输出

```
2
2 2
```

```
0
```

#### 样例3: 输入-输出

```
7
2 2 2 1 1 1 1
```

```
3
```

#### 样例4: 输入-输出

```
3
1 1 1
```

```
1
```

### 题目来源

CodeForces
