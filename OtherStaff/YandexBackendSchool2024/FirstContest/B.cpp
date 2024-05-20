/*
Description:

Input:

Output:

Solution:

*/

#include <iostream>
#include <string>
#include <cctype>
#include <cassert>

using namespace std;

class KeyTrainer {
public:
    void typeChar(char c) {
        typed.insert(cursor, 1, c);
        cursor++;
    }

    void left() {
        if (cursor > 0) {
            cursor--;
        }
    }

    void right() {
        if (cursor < typed.length()) {
            cursor++;
        }
    }

    void bspace() {
        if (cursor > 0) {
            typed.erase(cursor - 1, 1);
            cursor--;
        }
    }

    void delChar() {
        if (cursor < typed.length()) {
            typed.erase(cursor, 1);
        }
    }

    string getTyped() const {
        return typed;
    }

private:
    string typed;
    int cursor = 0;
};


bool isTyped(string a, string log) {
    KeyTrainer kt;
    int i = 0;
    while (i < log.length()) {
        if (isalpha(log[i])) {
            kt.typeChar(log[i]);
            i++;
        } else {
            int j = log.find('>', i);
            string command = log.substr(i + 1, j - i - 1);
            if (command == "bspace") {
                kt.bspace();
            } else if (command == "left") {
                kt.left();
            } else if (command == "right") {
                kt.right();
            } else if (command == "delete") {
                kt.delChar();
            }

            i = j + 1;
        }
    }
    // cout << "str " << kt.getTyped() << "\n";
    return kt.getTyped() == a;
}


void unitTest() {
    {
        string line = "abc";
        string log = "abd<bspace><left><delete>bcd<left><left><delete><right><bspace>c";
        assert(isTyped(line, log));
    }

    {
        string line = "programming";
        string log = "programming<left><left><right><delete>";
        assert(!isTyped(line, log));
    }

    {
        string line = "hellochild";
        string log = "helto<left><bspace>l<delete>ochilds<bspace>";
        assert(isTyped(line, log));
    }
}


int main() {
    unitTest();
    string a, b;
    cin >> a >> b;
    //cout << a << " " << b;
    if (isTyped(a, b)) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }
    return 0;
}