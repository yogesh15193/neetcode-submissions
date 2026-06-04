class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_1={}
        for i in strs:
            key="".join(sorted(i)) # word gets sorted here
            if key not in dict_1:
                dict_1[key]=[]
            dict_1[key].append(i)
        result=[]
        for k,v in dict_1.items():
            result.append(v)
        return result
