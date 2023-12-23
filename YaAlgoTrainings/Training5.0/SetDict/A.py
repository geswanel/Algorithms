"""
Description:
playlist so each song is liked by everybody
INPUT:
n - people in group
2n lines with desciptions of playlists for people. 2 lines for each member
    ki - number of liked tracks
    ki lines separated by space => track names
OUTPUT
number of tracks
sorted tracks

Solution:
1. use set and its intersections
"""
import unittest


def solution():
    pass

def main():
    n = int(input())
    tracks = []
    for _ in range(n):
        k = int(input())
        tracks.append(set(track for track in input().split()))
    
    playlist = set(tracks[0])
    for i in range(1, n):
        playlist.intersection_update(set(tracks[i]))
    
    print(len(playlist))
    print(" ".join(track for track in sorted(playlist)))


class A_Test(unittest.TestCase):
    pass


if __name__ == "__main__":
    main()