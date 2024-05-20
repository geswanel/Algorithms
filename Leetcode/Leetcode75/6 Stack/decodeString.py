"""
k[encoded string]

stack saves k's and brackets
if isdigit
    put in stack
else if openbracket
    put in stack
elif closebracket
    pop openbracket and digit from stack
    and add string inside k times

2[a3[b]]

2[abc3[de]4[fg5[ee]]sdlj]


"""

class Solution:
    def decodeString(self, s: str) -> str:
        ans = []
        pos = 0
        while pos < len(s):
            if s[pos].isdigit():
                decodedStr, pos = self.decodeSubstr(s, pos)
                ans.append(decodedStr)
            else:
                ans.append(s[pos])
                pos += 1
        
        return "".join(ans)

    
    def decodeSubstr(self, s: str, pos: int):
        """
        Args:
            pos - pos of first digit
            rep - number of repetitions
        
        Return:
            decodedstr
            pos - position after closed bracket
        """
        rep, pos = self.buildRep(s, pos)
        pos += 1    # pos of first symbol inside brackets
        ans = []
        while s[pos] != "]":
            if s[pos].isdigit():
                decoded, pos = self.decodeSubstr(s, pos)
                ans.append(decoded)
            else:
                ans.append(s[pos])
                pos += 1
        
        return rep * "".join(ans), pos + 1
            
        
    
    def buildRep(self, s : str, pos: int):
        """
        Args:
            pos - position of first digit
            s - str
        
        Return:
            rep - number of repetition
            pos - position of openbracket
        """
        rep = []
        while s[pos].isdigit():
            rep.append(s[pos])
            pos += 1
        return int("".join(rep)), pos


"""
Stack based solution
push until ]
then pop until number
push result into stack again (wow) 
"""
class Solution2:
    def decodeString(self, s: str) -> str:
        st = []
        for i in range(len(s)):
            if s[i] == ']':
                decoded = []
                while not st[-1].isdigit():
                    decoded.append(st.pop())
                decoded.pop()

                rep = 0
                i = 0
                while len(st) > 0 and st[-1].isdigit():
                    rep = rep + int(st.pop()) * int(10 ** i)
                    i += 1
                
                st.append(rep * "".join(decoded[::-1]))
            else:
                st.append(s[i])
        
        return "".join(st)

print(Solution2().decodeString("2[abc]3[cd]ef"))