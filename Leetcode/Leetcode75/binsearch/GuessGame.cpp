/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */
int guess(int num);

class Solution {
public:
    int guessNumber(int n) {
        int l = 1, r = n;
        
        while (true) {
            int mid = r / 2 + l / 2 + (r % 2 + l % 2) / 2;
            switch (guess(mid)) {
                case 1:
                    l = mid + 1;
                    break;
                case -1:
                    r = mid;
                    break;
                case 0:
                    return mid;
            }
        }
    }
};