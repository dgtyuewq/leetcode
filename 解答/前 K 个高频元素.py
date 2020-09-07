class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dit = {}    #將列表轉為字典
        nums.sort()     #將列表排序
        for i in nums:  #計算列表元素數量
            dit[i] = dit.get(i,0)+1
        dit = sorted(dit.items(), key=lambda dit:dit[1], reverse=True)  #排序列表元素
        res = []
        for x in range(k):
            res.append(dit[x][0])
        return res
