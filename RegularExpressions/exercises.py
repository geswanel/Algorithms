import re

# exercise 1
def ex_1(line):
    print("Exercise 1 - check if string contains only 0-9a-zA-Z")
    # pattern = r"^[0-9a-zA-Z]*$"
    # return bool(re.search(pattern, line))
    charReg = re.compile(r'[^a-zA-Z0-9]')
    ans = charReg.search(line)   # find any symbol that is not from validated
    return not bool(string)

def ex_2(line):
    #reg = re.compile(r'ab*')
    # ans = reg.match(line)
    # return ans
    pattern = r"^a(b*)$"
    if re.search(pattern, line):
        return "Matched"
    else:
        return "Not Matched"

print(ex_2("abb"))