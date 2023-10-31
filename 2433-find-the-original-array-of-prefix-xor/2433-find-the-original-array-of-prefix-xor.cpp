class Solution {
public:
    vector<int> findArray(vector<int>& pref) {
        
        vector<int> ans ;
        int temp=0,prev=0;
        for(auto ele:pref){
            // cout << temp <<" next "<< prev<<  "end ";
            temp=prev^ele;
            prev=prev^temp;
            
            ans.push_back(temp);
            
        }
        // for(auto ele: ans){
        //     cout<<ele;
        // }
        return ans;
        
    }
};