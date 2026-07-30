class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        similar_set=set()
        for pair in similarPairs:
            similar_set.add((pair[0],pair[1]))
            similar_set.add((pair[1],pair[0]))
        flag=True
        n=len(sentence1)
        m=len(sentence2)
        if(n!=m):
            flag=False
        if flag==True:
            for i in range(n):
                word_sent1=sentence1[i]
                word_sent2=sentence2[i]
                if (word_sent1,word_sent2) in similar_set:
                    pass
                elif word_sent1==word_sent2:
                    pass
                else:
                    flag=False
                    break
        return(flag)
        