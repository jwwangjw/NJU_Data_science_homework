### 题目描述

一个已排序好的表 A，其包含 1 和其他一些素数.  当列表中的每一个 p<q 时，我们可以构造一个分数 p/q 。

那么第 k 个最小的分数是多少呢?  以整数数组的形式返回你的答案, 这里 answer[0] = p 且 answer[1] = q.

### 输入描述

```
一个已排序好的表 A和整数k。
A 的取值范围在 2 — 2000.
每个 A[i] 的值在 1 —30000.
K 取值范围为 1 —A.length * (A.length - 1) / 2
```
### 输出描述

```
以整数数组的形式返回
```

### 测试样例
#### 样例1: 输入-输出-解释
```
[1, 2, 3, 5]
3
```
```
[2, 5]
```
```
已构造好的分数,排序后如下所示:
1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
很明显第三个最小的分数是 2/5.
```
### 题目来源  
`LeetCode`