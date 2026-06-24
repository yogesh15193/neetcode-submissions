class Solution:
    def simplifyPath(self, path: str) -> str:
        path_split=path.split('/')  
        #print("path",path_split)
        stack=[]
        output_str='/'
        flag_root=True  # assuming initially we at root
        for i in range(len(path_split)):
            if len(stack)==0:
                flag_root=True
            if path_split[i]=='' or path_split[i]=='.':
                pass
            elif (path_split[i]=='..' and len(stack)>0): # need to go to prev directory
                flag_root=False
                stack.pop()
            elif(path_split[i]=='..' and len(stack)==0 and flag_root==True): #we at root
                pass
            else:
                stack.append(path_split[i])
        #print(stack)
        return('/' + '/'.join(stack))
            
            