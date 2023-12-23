#include "../../settings.h"

/*
Array chars - size ~ 2000 (n^2 is ok)
compress [a a a a] = [a, 4]
[a, a, a, ...] = [a, 1, 0]
*/

class Solution {
public:
    int compress(vector<char>& chars) {
        int insertId = 0;
        
        for (int curId = 0; curId < chars.size(); ++curId) {
            //Count repeated
            int cnt = 1;
            char curChar = chars[curId];
            while (curId + 1 < chars.size() && chars[curId + 1] == curChar) {
                curId++;
                cnt++;
            }
            //compress repeated
            chars[insertId++] = curChar;
            if (cnt > 1) {
                int maxDel = 1;
                while (cnt / maxDel > 9) {
                    maxDel *= 10;
                }
                while (maxDel > 0) {
                    chars[insertId++] = ('0' + cnt / maxDel);
                    cnt %= maxDel;
                    maxDel /= 10;
                }
            }
        }

        chars.resize(insertId);
    }
};