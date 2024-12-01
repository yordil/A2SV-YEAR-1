class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        int len = arr.size();
       //ool flag = false;
        for(int i = 0 ; i < len ; i++){
            for(int j = 0 ; j < len ; j++){
                if( i == j)
                    continue;
                if(arr.at(i) == 2* arr.at(j))
                   return true;
            }
        }
                   return false;  // O(n^2) time complexity
        
    }
};