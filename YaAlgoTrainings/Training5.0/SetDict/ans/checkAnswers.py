from unittest import TestCase

ans1 = None
with open("53I9.txt", 'r') as f:
    ans1 = [round(float(line.rstrip()), 3) for line in f.readlines()]

ans2 = None
with open("5319a.txt", 'r') as f:
    ans2 = [round(float(line.rstrip()), 3) for line in f.readlines()]

for i, ans in enumerate(ans1):
    if ans != ans2[i]:
        print(f"{i} error {ans} mine != {ans2[i]} right")