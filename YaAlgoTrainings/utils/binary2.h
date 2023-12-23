#pragma once

template<typename T, typename P>
T lBinSearch(T l, T r, const P& params, bool (*checkFunc)(const T&, const P&)) {
    while (l < r) {
        T m = (l + r) / 2;
        if (checkFunc(m, params)) {
            r = m;
        } else {
            l = m + 1;
        }
    }
    return l;
}

template<typename T, typename P>
T rBinSearch(T l, T r, const P& params, bool (*checkFunc)(const T&, const P&)) {
    while (l < r) {
        T m = (l + r + 1) / 2;
        if (checkFunc(m, params)) {
            l = m;
        } else {
            r = m - 1;
        }
    }
    return l;
}