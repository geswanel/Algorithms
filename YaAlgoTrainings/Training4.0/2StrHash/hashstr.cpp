#include <iostream>
#include <vector>
#include <string>


const int MOD = 1e6 + 3;

struct HashStruct {
    std::vector<int> hash;
    std::vector<int> pow;
};

HashStruct createHash(std::string& s, const int x) {
    std::vector<int> hash(s.size() + 1, 0);
    std::vector<int> x_power(s.size() + 1, 0);

    for (int i = 0; i < s.size() + 1; ++i) {
        hash[i] = (hash[i - 1] * x + 
            static_cast<int>(s[i - 1])) % MOD;
        x_power[i] = (x_power[i - 1] * x) % MOD;
    }

    return {hash, x_power};
}

bool isEqual(const HashStruct& lhs, const HashStruct& rhs) {
    return true;
}


int main() {

    return 0;
}