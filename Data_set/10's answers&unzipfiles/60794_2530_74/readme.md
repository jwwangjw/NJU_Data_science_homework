### 题目描述

字符串S和 T 只包含小写字符。在S中，所有字符只会出现一次。

S 已经根据某种规则进行了排序。我们要根据S中的字符顺序对T进行排序。更具体地说，如果S中x在y之前出现，那么返回的字符串中x也应出现在y之前。

返回任意一种符合条件的字符串T。

### 输入描述

```
两行分别是字符串S和 T。S的最大长度为26，其中没有重复的字符。T的最大长度为200。S和T只包含小写字符。
```
### 输出描述

```
返回排好序的字符串T
```

### 测试样例
#### 样例1: 输入-输出-解释
```
cba
abcd
```
```
cbad
```
```
S中出现了字符 "a", "b", "c", 所以 "a", "b", "c" 的顺序应该是 "c", "b", "a". 
由于 "d" 没有在S中出现, 它可以放在T的任意位置. "dcba", "cdba", "cbda" 都是合法的输出。
```
### 题目来源  
`LeetCode`