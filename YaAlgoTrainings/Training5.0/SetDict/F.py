"""
Description:
map of word abbreviations
word can be shortened if it starts with any abbreviation
the shortest abbreviation chosen
INPUT:
words from map separated by space; n <= 1000. len <= 100
text; n <= 1e5; len(sum) <= 1e6

all letters a-z
OUTPUT:
print changed text
Solution:
For each word start with prefixes and check every prefix on existance in the map
in python is too slow I think. Because it's hard to create prefixes in O(1)
"""
import unittest


def replaceWords(text, abbr):
    for i, word in enumerate(text):
        length = 0
        while length <= len(word) and word[0:length] not in abbr:
            length += 1
        text[i] = word[0:length]
    
    return text

def main():
    abbr = {word for word in input().split()}
    text = [word for word in input().split()]
    print(" ".join(replaceWords(text, abbr)))


class F_Test(unittest.TestCase):
    pass


if __name__ == "__main__":
    main()