#include<iostream>
#include<vector>
using namespace std;

double average(const vector<int>& nums) {
    int sum = 0;
    for (int num : nums) {
        sum += num;
    }
    return sum / nums.size();  // Potential bug if nums.size() == 0
}
