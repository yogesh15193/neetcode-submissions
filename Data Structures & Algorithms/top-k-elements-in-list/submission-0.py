class  Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        sorted_dict = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
        l1=(list(sorted_dict.keys()))
        return(l1[0:k])
    