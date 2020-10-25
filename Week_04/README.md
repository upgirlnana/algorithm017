

```python
1.
贪心算法：可以很直白的理解就是‘只顾眼前’、‘目光短浅’，只考虑当前的情况，不考虑之前的和之后的
情况，每个步骤都是如此，若贪心算法能够获得最优解，则说明贪心算法是当前解决这个问题
个问题的最优解。
2.动态规划
动态规划在算法计算的过程中会考虑之前的状态，综合之前和当前的信息dp[i]=dp[i-1]
+operation，动态规划与贪心算法相比较，贪心算法的每一步相当于是计算的局部最优，而
动态规划计算的则是当前状态之前的最优的一个结果。
3.
二分查找模板
def (nums):
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)/2
        if nums[mid]==target:
            return
        elif nums[mid]>target:
            high=mid-1
        else:
            low=mid+1
二分查找的关键：单调，注意边界
4.旋转数组中次序变化的地方：确定left=0，right=len(nums)-1,如果nums[mid]>nums[left]h
,则数组前半块有序，后半块无序，如果nums[left]>nums[mid]，数组前半块无序，后半块有序。
遍历至left和right指的是同一个元素时，这个位置就是发生旋转的地方。
def search(self, nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] >nums[left]: # 左边有序
            left=mid+1
        elif nums[mid] < nums[left]:  # 左边是有序
            right = mid - 1
        elif nums[mid] ==nums[right]==nums[left]:
            return mid


```
