/*
DxE hole
AxBxC brick
Can brick be pushed into the hole?

Variants:
AxB
AxC
BxC
*/

#include <iostream>


int main() {
    int A, B, C, D, E;
    std::cin >> A >> B >> C >> D >> E;
    
    if (A <= D && B <= E || A <= E && B <= D ||
        A <= D && C <= E || A <= E && C <= D ||
        C <= D && B <= E || C <= E && B <= D) {
        std::cout << "YES\n";
    } else {
        std::cout << "NO\n";
    }

    return 0;
}