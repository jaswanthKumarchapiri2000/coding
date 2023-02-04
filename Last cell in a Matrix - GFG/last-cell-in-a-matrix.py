#User function Template for python3

class Solution:
    def endPoints(self, matrix, R, C):
        #code here
        i,j=0,0
        dir='right'
        while(0<=i<R and 0<=j<C):
            prev=(i,j)
            if matrix[i][j]==0:
                if dir=='right':
                    j+=1
                elif dir=='down':
                    i+=1
                elif dir=='up':
                    i-=1
                else:
                    j-=1
            else:
                matrix[i][j]=0
                if dir=='right':
                    dir='down'
                    i+=1
                elif dir=='down':
                    dir='left'
                    j-=1
                elif dir=='up':
                    j+=1
                    dir='right'
                else:
                    dir='up'
                    i-=1
        return prev
            
        
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        ob = Solution()
        ans = ob.endPoints(matrix,r,c)
        print('(',ans[0],', ',ans[1],')',sep ='')

# } Driver Code Ends