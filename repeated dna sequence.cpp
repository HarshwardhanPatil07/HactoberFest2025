#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        unordered_set<string> seen;
        unordered_set<string> repeated;
        int n = s.size();
        
        for (int i = 0; i <= n - 10; ++i) {
            string seq = s.substr(i, 10);
            if (seen.count(seq)) {
                repeated.insert(seq);
            } else {
                seen.insert(seq);
            }
        }
        
        return vector<string>(repeated.begin(), repeated.end());
    }
};
