class Solution:
    def decodeString(self, s: str) -> str:
        s=list(s)
        stack=[]
        for i in s:
            if i!=']': # no closing bracket
                stack.append(i)
            else:
                temp_list=[]
                while stack[-1]!='[':
                    temp_list.append(stack.pop())
                temp_str = ''.join(reversed(temp_list))
                
                opening_bracket=stack.pop()
                number_str=''
                while len(stack)>0:
                    d=stack.pop()
                    number_flag=False
                    try:
                        number_before_opening_bracket=int(d)
                    except:
                        number_flag=True
                        stack.append(d)
                    if number_flag==True:
                        break
                    number_str=number_str+str(number_before_opening_bracket)
                number_str = int("".join(reversed(number_str))) 
                
                temp_str=number_str*temp_str
                stack.append(temp_str)
        return(''.join(stack))
                        