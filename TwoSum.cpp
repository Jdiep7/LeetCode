#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

vector<int> twoSum(vector<int> nums, int target) {
  unordered_map<int, int> numMap;
  int n = nums.size();

  for (int i = 0; i < n; i++) {
    numMap[nums[i]] = i;
  }

  for (int i = 0; i < n; i++) {
    int complement = target - nums[i];
    if (numMap.count(complement) && numMap[complement] != i) {
      return {i, numMap[complement]};
    }
  }

  return {};
}

int main() { twoSum({5, 5, 5, 5, 5}, 10); }