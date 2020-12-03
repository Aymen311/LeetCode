class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max = nums[0];
        int first_max = nums[0] ; 
        for(int i=1; i<nums.size(); i++){
            first_max = std::max(first_max + nums[i], nums[i]);
            max = std::max(max, first_max);
            
        }
        return max ; 
    }
};
