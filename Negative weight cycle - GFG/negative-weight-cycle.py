#User function Template for python3
class Solution:
    def isNegativeWeightCycle(self, n, edges):
        inf = 1000000000000000000
        d = [0 for i in range(n)]
        p = [-1 for i in range(n)]
        for i in range(n):
            x = -1
            for e in edges:
                if(d[e[0]] + e[2] < d[e[1]]):
                    d[e[1]] = d[e[0]] + e[2]
                    # p[e[1]] = e[0]
                    x = e[1]
        if(x == -1):
            return 0
        return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n)
		m = int(m)
		edges = []
		for _ in range(m):
			edges.append(list(map(int, input().split())))
		obj = Solution()
		ans = obj.isNegativeWeightCycle(n, edges)
		print(ans)

# } Driver Code Ends