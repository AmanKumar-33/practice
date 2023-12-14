// writing another program on the Sort colors problem
// https://leetcode.com/problems/sort-colors/
#include<bits/stdc++.h>
using namespace std;
#include<vector>


void Sort_color(vector<int>& nums){
    vector<int> count(3,0);
    for(int n : nums){
        count[n]++;
    }
    for(int i =0;i<nums.size();i++){
        if(count[0] >0){
            nums[i] =0;
            count[0]--;
        }
        else if(count[1] >0){
            nums[i] =0;
            count[1]--;
        }
        else
            nums[i] =2;
            
        }
    }