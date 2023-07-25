#User function Template for python3


#Function to return a list containing the level order traversal in spiral form.
#Function to find the height of the tree.
def getHeight(root):
    
    #base case for recursion.
    if root is None:
        return 0
    
    #finding height of left subtree recursively.
    lh = getHeight(root.left)
    
    #finding height of right subtree recursively.
    rh = getHeight(root.right)
    
    #taking the maximum as height of tree.
    if lh>rh:
        return lh+1
    else:
        return rh+1


#Function to do level order traversal of tree in spiral form.
def printLevel(result,node, lvl, flg):
    
    #base case for recursion.
    if node is None:
        return
    
    #if level is 1, we push the data in the list.
    if lvl==1:
        result.append(node.data)
    
    elif(lvl > 1):
        
        #if flg is true, we call the spiral function recursively for the
        #left subtrees first and then for right subtrees.
        if flg:
            printLevel(result,node.left, lvl-1, flg)
            printLevel(result,node.right, lvl-1, flg)
        
        #else we call for right subtrees first and then left subtrees.
        else:
            printLevel(result,node.right, lvl-1, flg)
            printLevel(result,node.left, lvl-1, flg)

#Function to return a list containing the level order traversal in spiral form.
def findSpiral(root):

    result = []
    if root is None:
        return result
    h = getHeight(root)
    ltr = False
    #for each level, we do the spiral traversal.
    for i in range(1, h+1):
        printLevel(result,root, i, ltr)
        ltr = not ltr
        
    #returning the list.
    return result
        








#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3



#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None



    
# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        result = findSpiral(root)
        for value in result:
            print(value,end = " ")
        print()
        
        

# } Driver Code Ends