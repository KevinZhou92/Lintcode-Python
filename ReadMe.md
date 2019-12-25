# 记录刷题心得
## 语言
## 算法
### Depth First Search
#### DFS + Memorization and Dynamic Programming
记忆化搜索和动态规划虽然分别叫做Top-Down和Bottom-Up的方法, 但本质都是现将问题化简到更小的子问题直至base case, 然后通过base case的值不断反推回去, 这个过程中cache子问题的最优解, 这样递归到相同子问题时可以直接返回已经缓存的子问题最优解