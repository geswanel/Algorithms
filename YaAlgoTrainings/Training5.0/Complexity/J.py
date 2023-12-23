"""
Placing pictures

Doc = seq of paragraphs
paragraph = seq of elements divided by space or newline(words and pictures)
paragraphs divided by blank line

word = *[a-zA-Z0-9.,:;!?-']
picture = "(image parname=parval par2=val2)"
    parameters divided by space or newline
    required params: width in pixels, height in pixels, layout (embedded, surrounded, floating)

Doc is place at infinity page width = w pixels
    point (0, 0)

Placing
    - paragraph one by one. First with top board at y = 0
        - elements by lines with h pixels height
        - picture
            - during picture placing => h can be higher, and lines can be divided into fragments
            - embedded => same as word. h = heigher. Stick to the top. If not first => space c before
            - surrounded => No spaces. Search for first fragment
                - top sticks to line top
                - bottom lines divided by fragments
            - floating => dx dy parameters. displacement of left top corner of picture related to 
            right top corner of previous element or paragraph start point
                - above words and other pictures. do not affect other elements
                - if overlaps edge => displaced so sticks to the edge
        - words
            - each symbol c pixels wide
            - before each word except first in fragment = space c pixels wide
            - if cannot be placed => search for next fragment
            - stick to the top of line
        - Top of next paragraph - bottom of surrounded edge or bottom of prev line of prev paragraph
        - using w, h, c = > find all coordinates of all images

        
INPUT:
w, h, c
1000 byte
next - document
"""
from abc import ABC, abstractmethod




def placeImages(w, h, c, lines):
    
    for line in lines:
        



def main():
    with open("input.txt", "r", encoding="utf-8") as f:
        w, h, c = (int(x) for x in f.readline().rstrip('\n').split())
        lines = [line.strip(' \n') for line in f.readlines()]


if __name__ == "__main__":
    main()