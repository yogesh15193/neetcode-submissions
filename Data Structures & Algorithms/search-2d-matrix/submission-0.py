class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        top_row=0
        bottom_row=rows-1
        flag=True
        while top_row<=bottom_row:
            middle_row=(top_row+bottom_row)//2
            if target>matrix[middle_row][-1]:
                top_row=middle_row+1
            elif target<matrix[middle_row][0]:
                bottom_row=middle_row-1
            else:
                break
        if not(top_row<=bottom_row):
            flag=False
            return False
        flag2=False
        if flag==True:
            middle_row=(top_row+bottom_row)//2
            left=0
            right=cols-1
            while(left<=right):
                mid=(left+right)//2
                mid_elem_value=matrix[middle_row][mid]
                if mid_elem_value>target:
                    right=mid-1
                elif mid_elem_value<target:
                    left=mid+1
                else :
                    flag2=True
                    break
                
        if flag2==False or flag==False:
            return False
        else:
            return True
