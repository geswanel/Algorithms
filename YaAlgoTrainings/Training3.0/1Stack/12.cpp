/*
Bracket sequence containing (){}[] brackets.
Determine if it is correct.

Encode brackets with codes from 0-5
/3 and %3 determine the type of bracket
/3 = 0 - opening
/3 = 1 - closing
%3 = 0 - round
%3 = 1 - curly
%3 = 2 - square

Solution using a stack
- Opening brackets are pushed onto the stack
- Closing brackets remove the corresponding opening bracket from the stack (in essence, we remove correct sequences from the sequence, leaving it correct)
*/


#include "../../utils/Stack.h"

#include <iostream>
#include <unordered_map>

const std::unordered_map<char, int> bracketsCodes = {
    {'(', 0}, {')', 3},
    {'{', 1}, {'}', 4}, 
    {'[', 2}, {']', 5}};

bool isRightBrackets(const std::string& brackets) {
    Stack<char> bracketsStack;

    for (const char& bracket : brackets) {
        if (bracketsCodes.at(bracket) / 3 == 0) {
            bracketsStack.push(bracket);
        } else {
            try {
                if (bracketsCodes.at(bracket) % 3 != bracketsCodes.at(bracketsStack.back()) % 3) {
                    return false;
                }
                bracketsStack.pop();
            } catch(EmptyException e) {
                return false;
            }
        }
    }
    return bracketsStack.size() == 0;
}

int main() {
    std::string brackets;
    std::cin >> brackets;

    std::cout << (isRightBrackets(brackets) ? "yes" : "no");


    return 0;
}