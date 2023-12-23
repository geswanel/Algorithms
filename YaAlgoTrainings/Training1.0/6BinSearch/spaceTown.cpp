/*
n modules are identical
each module is a rectangle
module - living compartment axb + protection around
Protection d meters -> (a + 2d)(b + 2d) - module area
d - integer - all modules have the same protection thickness
field of size wxh. Module orientation is the same - regular grid - parallel to the sides of the field
Determine the maximum layer thickness based on the given parameters

It turns out there is a field wxh
There are n modules whose length is a+2d and b+2d. It is necessary to find d for which the condition is met

w / (a + 2d) * h/ (b + 2d) >= n - i.e. you can fit n modules

d = 0 then the modules can be placed according to the condition

Right binary search d is needed since from 0 to max everything is fine
*/


#include "binary2.h"
#include <iostream>
#include <limits>


using T = unsigned long long;

struct ModuleParams {
    T n;
    T a;
    T b;
    T w;
    T h;
};

std::istream& operator>>(std::istream& in, ModuleParams& params) {
    in >> params.n >> params.a >> params.b >> params.w >> params.h;
    return in;
}

bool checkModulePlacing(const T& d, const ModuleParams& params) {
    return (params.w / (params.a + 2 * d)) * (params.h / (params.b + 2 * d)) >= params.n ||
        (params.w / (params.b + 2 * d)) * (params.h / (params.a + 2 * d)) >= params.n;
}

int main() {
    ModuleParams params;
    std::cin >> params;
    T ans = rBinSearch<T, ModuleParams>((T)0, std::max(params.w, params.h), params, checkModulePlacing);
    std::cout << ans;
    return 0;
}