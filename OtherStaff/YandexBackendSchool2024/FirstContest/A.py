"""
Description:
Nickname
>= 8 chars
at least 1 digit
at least 1 upper and 1 lower case letter
INPUT:
Nickname - sequence of digits and letters
OUTPUT
YES if suitable for nickname, NO otherwise
Solution:
Just check conditions
"""
import unittest


def isValidNickname(nickname: str):
    if len(nickname) < 8:
        return False

    haveDigit = False
    haveUpper = False
    haveLower = False
    for char in nickname:
        if char.isdigit():
            haveDigit = True
        elif char.isupper():
            haveUpper = True
        elif char.islower():
            haveLower = True
    
    return haveDigit and haveUpper and haveLower

def main():
    nickname = input()
    print("YES" if isValidNickname(nickname) else "NO")


class A_Test(unittest.TestCase):
    def test_isValidNickname(self):
        nickname = "nickname"
        self.assertFalse(isValidNickname(nickname))

        nickname = "nIckname"
        self.assertFalse(isValidNickname(nickname))

        nickname = "nickname1"
        self.assertFalse(isValidNickname(nickname))
        
        nickname = "NICKNAME1"
        self.assertFalse(isValidNickname(nickname))

        nickname = "nI1"
        self.assertFalse(isValidNickname(nickname))

        nickname = "nI13123nK1"
        self.assertTrue(isValidNickname(nickname))


if __name__ == "__main__":
    #unittest.main()
    main()