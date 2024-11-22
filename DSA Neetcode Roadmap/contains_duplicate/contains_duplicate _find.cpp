class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::set<int> nums_set{};

        for (int i : nums) {
            if (nums_set.find(i) != nums_set.end()) {
                return true;
            }
            nums_set.insert(i);
        }
        return false;
    }
};