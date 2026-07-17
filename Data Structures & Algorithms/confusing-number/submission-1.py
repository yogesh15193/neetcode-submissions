class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotation = {0:0, 1:1, 6:9, 8:8, 9:6, 2:-1, 3:-1, 4:-1, 5:-1, 7:-1}
        n=str(n)
        rotated_number=''
        flag=True
        flag_fuzzy_number=False
        for i in n:
            digit=int(i)
            if digit==2 or digit==3 or digit==4 or digit==5 or digit==7:
                flag=False
                return False
            if digit==6 or digit==9:
                flag_fuzzy_number=True
            rotated_result=str(rotation[digit])
            rotated_number=rotated_result+rotated_number

        if flag == True:
            rotated_number = int(rotated_number)
            if rotated_number != int(n):
                return True
            else:
                return False


        