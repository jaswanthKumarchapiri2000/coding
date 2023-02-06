#code
t=int(input())
while(t):
    n=int(input())
    arr=list(map(int,input().split()))
    maxi=max(arr)
    helper=[0]*(maxi+1)
    ans=[]
    for i,ele in enumerate(arr):
        helper[ele]+=1
    for i,ele in enumerate(helper):
        helper[i]=[helper[i],i]
    helper.sort(key = lambda x : x[0] ,reverse=True)
    for i,j in helper:
        while(i>0):
            ans.append(j)
            i-=1
    for ele in ans:
        print(ele,end=' ')
    print(end='\n')
    t-=1