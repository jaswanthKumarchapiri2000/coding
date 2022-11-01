# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        d={}
        mi,ma=0,0
        def helper(node,val,level):
            if not node:
                return 
            try:
                d[val].append((node.val,level))
            except:
                d[val]=[(node.val,level)]
            
            helper(node.left,val-1,level+1)
            helper(node.right,val+1,level+1)
        helper(root,0,0)
        print(d)
        for i in (sorted(d)):
            d[i].sort(key=lambda x:[x[1],x[0]])
            print(d[i])
            x=[]
            for k in d[i]:
                x.append(k[0])
            ans.append(x)
            
        return ans
       
        