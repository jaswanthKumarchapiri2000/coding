//{ Driver Code Starts
//Initial Template for C++
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++
class Solution
{
  public:
  int maxWeightCell(int N, vector<int> Edge)
  {
      // code here
      int ans=0;
      int ans2;
      if( N==1) return 0;
      unordered_map <int,int> d ;
      for (int i=0 ; i< N ;i++){
          if (Edge[i]!=-1){
              d[Edge[i]]=d[Edge[i]]+i;
        
          }
          }
      for (int i=0 ; i< N ;i++){
          if(Edge[i]!=-1){
              int sum=d[Edge[i]];
              if(sum>ans){
                  ans=sum;
                  ans2=Edge[i];
              }
              if(sum==ans){
                  ans2=max(ans2,Edge[i]);
              }
          }
          
          }
    return ans2;
      
      
  }
};

//{ Driver Code Starts.
int main(){
   int tc;
   cin >> tc;
   while(tc--){
      int N;
      cin >> N;
      vector<int> Edge(N);
      for(int i=0;i<N;i++){
        cin>>Edge[i];
      }
      Solution obj;
      int ans=obj.maxWeightCell(N, Edge);
      cout<<ans<<endl;
   }
   return 0;
}
// } Driver Code Ends