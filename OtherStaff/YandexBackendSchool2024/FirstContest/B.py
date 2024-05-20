"""
Description:
Keyboard trainer

a - string to type ~ 1000. latin + control keys (delete, bspace, left, right)
b - log of sequence of printed keys or control key

By log check if a string is typed

INPUT:
a
b

OUTPUT
Yes or No

Solution:
1. list of symbols + cursor position
    - cursor points after char that will be deleted by bspace 
    - and points on char that will be deleted by delete
2. process control keys
"""
class KeyTrainer:
    def __init__(self):
        self.log = []
        self.cursor = 0
    
    def typeChar(self, ch):
        self.log.insert(self.cursor, ch)
        self.cursor += 1
    
    def left(self):
        self.cursor -= 1
        if self.cursor < 0:
            self.cursor = 0
    
    def right(self):
        self.cursor += 1
        if self.cursor > len(self.log):
            self.cursor = len(self.log)
    
    def bspace(self):
        if self.cursor > 0:
            self.log.pop(self.cursor - 1)
            self.cursor -= 1
    
    def delete(self):
        if self.cursor < len(self.log):
            self.log.pop(self.cursor)
    
    def getTypedStr(self):
        return "".join(self.log)


def isTyped(toType: str, logged: str):
    kt = KeyTrainer()
    i = 0
    while i < len(logged):
        if logged[i].isalpha():
            kt.typeChar(logged[i])
            i += 1
        else:
            # log[i] == '<'
            comEnd = logged.find('>', i)
            command = logged[i + 1:comEnd]
            if command == "bspace":
                kt.bspace()
            elif command == "delete":
                kt.delete()
            elif command == "left":
                kt.left()
            elif command == "right":
                kt.right()
            i = comEnd + 1

    return kt.getTypedStr() == toType


def main():
    toType = input()
    logged = input()
    if isTyped(toType, logged):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()