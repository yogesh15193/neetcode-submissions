class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        flag=True
        for i in range(len(words)):
            for j in range(len(words)):
                i_exists = j < len(words[i])
                j_exists = i < len(words[j])
                if i_exists != j_exists:
                    return False
                elif not i_exists and not j_exists:
                    pass
                elif len(words[i]) > len(words) or len(words[j])>len(words):
                    return False
                    flag=False
                    break
                else:
                    if words[i][j]!=words[j][i]:
                        return False
                        flag=False
                        break
        return flag
        