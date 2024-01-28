class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        unordered_map <int,int> temp;
        for(auto map : matches){
            int ele=map[1];
            temp[ele]++;
        }
        vector<vector<int>> ans;
        set<int> zero;
        set<int> one;
        for(auto ele: matches){
            int first=ele[0];
            int second=ele[1];
            if(temp.find(first)==temp.end()){
                zero.insert(first);}
            if(temp[second]==1){
                one.insert(second);
            }
        }
        vector<int> zero1 ;
         zero1.assign(zero.begin(),zero.end());
        vector<int> one1;
        one1.assign(one.begin(),one.end());
     
            
        ans.push_back(zero1);
        ans.push_back(one1);
        return ans;
        
        
        
        
    }
};