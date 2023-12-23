#pragma once

#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>

template<typename T>
std::ostream& operator<<(std::ostream& out, const std::vector<T>& v) {
    out << "{";
    for (int i = 0; i < v.size(); i++)
    {
        out << v[i] << ", ";
    }
    out << "}";
    return out;
}

template<typename T>
std::ostream& operator<<(std::ostream& out, const std::set<T>& v) {
    out << "{";
    for (const T& val : v) {
        out << val << ", ";
    }
    out << "}";
    return out;
}

template<typename T>
std::ostream& operator<<(std::ostream& out, const std::unordered_set<T>& v) {
    out << "{";
    for (const T& val : v) {
        out << val << ", ";
    }
    out << "}";
    return out;
}

template<typename Key, typename Value>
std::ostream& operator<<(std::ostream& out, const std::map<Key, Value>& m) {
    out << "{";
    for (const auto& val : m) {
        out << '(' << val.first << ", " << val.second << "), ";
    }
    out << "}";
    return out;
}

template<typename Key, typename Value>
std::ostream& operator<<(std::ostream& out, const std::unordered_set<Key, Value>& m) {
    out << "{";
    for (const auto& val : m) {
        out << '(' << val.first << ", " << val.second << "), ";
    }
    out << "}";
    return out;
}
