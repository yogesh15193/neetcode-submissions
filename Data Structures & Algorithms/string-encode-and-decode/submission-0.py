class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_added_length=[]
        for i in strs:
            length_str=len(i)
            i=str(length_str)+'#'+i
            print(i)
            encoded_added_length.append(i)
        print(encoded_added_length)
        return("".join(encoded_added_length))


    def get_length(self,encoded_string, start_index):
        i=start_index
        length=[]
        if i==len(encoded_string):
            return("Decode complete")
        else:
            for i in range(i,len(encoded_string)):
                if encoded_string[i]!='#':    
                    length.append(encoded_string[i])
                else:
                    break
        return("".join(length),i)
    
    def decode(self, s: str) -> List[str]:
        decoded_list=[]
        index=0
        i=0    
        while(i<len(s)):
            length,index=self.get_length(s,i)
            print("length, index", length, index)
            length=int(length) 
            index=int(index)
            extract_str_length=length+index
            print("extraction length", extract_str_length)
            word_extracted=s[index+1:extract_str_length+1]
            decoded_list.append(word_extracted)
            index=index+length
            i=extract_str_length+1
            print("word extracted", word_extracted)
            print("next index",i)

        return(decoded_list)


