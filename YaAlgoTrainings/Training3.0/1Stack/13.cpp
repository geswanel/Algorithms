/*
Evaluate the expression in postfix notation

If encountering an operation, take the previous 2 operands and perform the operation

Solution using a stack
Operands are pushed onto the stack
Operation pops 2 operands, performs the operation, and pushes the result back into the stack
In the end, the stack will contain the answer
*/


#include "../../utils/Stack.h"
#include <iostream>
#include <string>

int executeOperation(const int& operand1, const int& operand2, const char& operation) {
    switch (operation)
    {
    case '+':
        return operand1 + operand2;
        break;
    case '-':
        return operand1 - operand2;
        break;
    case '*':
        return operand1 * operand2;
        break;
    default:
        return 0;
    }
}

int calculatePostfixExpression(std::istream& in) {
    Stack<int> operands;

    std::string value;
    while (in >> value) {
        if (value != "") {
            if ('0' <= value[0] && value[0] <= '9') {
                operands.push(std::stoi(value));
            } else if (value[0] == '+' || value[0] == '-' || value[0] == '*') {
                int operand2 = operands.back();
                operands.pop();
                int operand1 = operands.back();
                operands.pop();
                operands.push(executeOperation(operand1, operand2, value[0]));
            }
        }
    }

    return operands.back();
}

int main() {
    std::cout << calculatePostfixExpression(std::cin);
    return 0;
}
