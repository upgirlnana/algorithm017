

```python
动态规划解题思路

动态规划主要分为两个核心部分，一是确定DP 状态，二是确定DP 转移方程。

DP 状态：
「DP 状态」的确定主要有两大原则：最优子结构和无后效性。
最优子结构：
将原有问题化分为一个个子问题，即为子结构。而对于每一个子问题，其最优值均由「更小规模的子问题的最优值」推导而来，即为最优子结构。
因此DP状态设置之前，需要将原有问题划分为一个个子问题，且需要确保子问题的最优值由「更小规模子问题的最优值」推出，此时子问题的最优值即为DP状态的定义。
无后效性：
而对于无后效性，顾名思义，就是我们只关心子问题的最优值，不关心子问题的最优值是怎么得到的。
例如只能挑选长度 <= k 的连续区间。此时若我们定义 f[i] 表示「以 i 为右端点的长度 <= k 的最大连续区间和」，则 f[i + 1] 的取值不仅取决于 f[i] 的数值，还取决于 f[i] 是如何得到的。
因为如果 f[i] 取得最优值时区间长度 = k，则 f[i + 1] 不能从 f[i]  转移得到，即 f[i] 的状态定义有后效性。
最后，最优子结构就是DP 状态最优值由更小规模的 DP 状态最优值推出，此处 DP 状态即为子问题。而「无后效性就是无论 DP 状态是如何得到的，都不会影响后续 DP 状态的取值。
2.
DP 转移方程
有了DP 状态之后，我们需要用分情况讨论的思想来枚举所有小状态向大状态转移的可能性即可推出DP转移方程。
以最大子序列之和为例：
定义f[i] 之后，考虑状态 f[i] 如何从 f[1] ~ f[i - 1] 这些更小规模的状态转移而来，以及在边界时有无特殊的条件限制。例如在跳格子问题中，只能想右或者向下方向跳跃，在第一行的时候，只能往右，在第一列的时候，只能向下，诸如此类的条件要具体的分析。
个人认为在动态规划中，最终要还是转移方程这步最关键，往往也叫难推出来，目前认为自己好多方法都是用暴力方法解决，动态规划的内容掌握的还不够牢固。
```
