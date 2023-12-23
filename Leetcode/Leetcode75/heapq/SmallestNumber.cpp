#include <set>
#include <algorithm>
#include <iterator>

using namespace std;

class SmallestInfiniteSet {
public:
    SmallestInfiniteSet() {
        for (int i = 1; i <= MAX_INT; ++i) {
            numbers.insert(i);
        }
    }
    
    int popSmallest() {
        int res = *numbers.begin();
        numbers.erase(numbers.begin());
        return res;
    }
    
    void addBack(int num) {
        numbers.insert(num);
    }
private:
    set<int> numbers;
    const int MAX_INT = 1000;
};

int main() {
    return 0;
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet* obj = new SmallestInfiniteSet();
 * int param_1 = obj->popSmallest();
 * obj->addBack(num);
 */