class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> myMap;
        for (int i = 0; i < nums.size(); i++) {
            // myMap[nums[i]] = i;
            myMap.insert({nums[i], i});
        }
        for (int i = 0; i < nums.size(); i++) {
            int difference = target - nums[i];
            auto mapElement = myMap.find(difference);
            if (mapElement != myMap.end() && (mapElement->second != i)) {
                if (i > mapElement->second) {
                    return {mapElement->second, i};
                }
                else {
                    return {i, mapElement->second};
                }
            }
        }
        return {};
    }
};