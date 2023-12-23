"""
Description:
Election: Each citizen gives his vote for one party
Party with the most number of votes forms a government.
    If several parties have the same most number of votes => Coalition govenrment

One businessman decided to invest in some parties so that his party will win!
    So they invest in propaganda company. It takes an 1 unit to change one citizen's views.
    it takes pi units to bribe the lider of i party 
        for i party to form a government that will benefit a businessman.
        Some parties aren't willing to cooperate with a businessman

It's known
    how many people will vote for a particular party

Help the businessman to win and spend the least amount of money possible
INPUT:
n - number of parties 1e5.
vi pi - number of citizens that will vot for i party and bribe for its leader 
        pi = -1 if won't cooperate

OUTPUT
min sum
number of party
n numbers = amount of votes for each party
Solution:
0. Sort parties by voters.O(nlogn) 
    count suffix sum of voters O(n) and find max pi
1. min sum => if less, cannot win. So bin search for sum
    sum is in [0, sum(vi) + max(pi)] ~ [0, 1e11] O(log(sum(vi) + pi))
2. for each sum check if its possible to win with any party
    iterate over parties O(n)
        if pi != -1 and sum > pi => can be bribed
            fi = vi + sum - pi - final number of votes for i party
            find how many parties have more than fi votes m   O(logn) if sorted
            and what number of voters shoud be agitated. suffix[n-m] - fi * m < remained sum O(1)
each bin search save what party can win
then O(n) to take votes from other parties            

O(nlogn + n*logn*log(sum(vi)))
"""
import unittest

class Party:
    def __init__(self, idp, vi, pi):
        self.idp = idp
        self.v = vi
        self.p = pi
    
    def canBribe(self, funds):
        return self.p != -1 and funds >= self.p
    
    def __str__(self):
        return f"Party {self.idp}: votes {self.v}, bribe {self.p}"
    
    def __repr__(self):
        return f"Party {self.idp}: votes {self.v}, bribe {self.p}"

def createVotesSuffix(parties):
    suffix = [0]
    for i in range(len(parties)):
        suffix.append(suffix[-1] + parties[-1 - i].v)
    
    return suffix[:0:-1]

def rivalStartPos(parties, votes):
    l = 0
    r = len(parties)

    while l < r:
        mid = (l + r) // 2
        if parties[mid].v < votes:
            l = mid + 1
        else:
            r = mid
    
    return l

def canWin(n, parties, vSuffix, funds):
    for i, party in enumerate(parties):
        if party.canBribe(funds):
            finalVotes = party.v + (funds - party.p)
            if finalVotes > parties[-1].v:
                return party

            firstRival = rivalStartPos(parties, finalVotes)
            mustAgitate = vSuffix[firstRival] - (finalVotes - 1) * (n - firstRival) - (i >= firstRival)
            if mustAgitate <= (funds - party.p):
                return party
    
    return None


def minFundsParty(n, parties, vSuffix):
    totalVotes = 0
    maxBribe = -1
    for party in parties:
        totalVotes += party.v
        if party.p > maxBribe:
            maxBribe = party.p
    
    l = 0
    r = totalVotes + maxBribe
    while l < r:
        mid = (l + r) // 2
        winParty = canWin(n, parties, vSuffix, mid)
        if winParty:
            r = mid
        else:
            l = mid + 1
    
    return l, canWin(n, parties, vSuffix, l)

def distributeVotes(n, parties, party, funds):
    finalVotes = party.v + (funds - party.p)
    funds -= party.p
    i = 0
    while i < len(parties) and parties[-1 - i].v >= finalVotes:
        if party is not parties[-1 - i]:
            delta = parties[-1 - i].v - (finalVotes - 1)
            parties[-1 - i].v -= delta
            funds -= delta
            party.v += delta
        i += 1
    
    i = 0
    while funds > 0:
        if party is not parties[-1 - i]:
            if parties[-1 - i].v >= funds:
                parties[-1 - i].v -= funds
                party.v += funds
                funds = 0
            else:
                delta = funds - parties[-1 - i].v
                parties[-1 - i].v -= delta
                funds -= delta
                party.v += delta
        i += 1


def chooseParty(n, parties):
    parties.sort(key=lambda party: (party.v, party.p)) # sorting by votes
    vSuffix = createVotesSuffix(parties)    # how many votes overall including last
    # print("Sorted")
    # for i, p in enumerate(parties):
    #     print(f"pos {i: >3} -> id{p.idp: >3}: votes{p.v: >3} bribe{p.p: >3} => suffix {vSuffix[i] - p.v * (n - i)}")

    #print(vSuffix)

    funds, party = minFundsParty(n, parties, vSuffix)
    
    #print("Min Party", funds, party)
    distributeVotes(n, parties, party, funds)

    # print("After distribution")
    # for i, p in enumerate(parties):
    #     print(f"pos {i: >3} -> id{p.idp: >3}: votes{p.v: >3} bribe{p.p: >3} => suffix {vSuffix[i] - p.v * (n - i)}")

    parties.sort(key=lambda p: p.idp)

    return funds, party

from copy import deepcopy

def main():
    n = int(input())
    parties = []
    for i in range(n):
        vi, pi = (int(x) for x in input().split())
        parties.append(Party(i + 1, vi, pi))
    
    before = deepcopy(parties)

    minFunds, party = chooseParty(n, parties)
    print(minFunds)
    print(party.idp)
    # for i, par in enumerate(parties):
    #     if par is party:
    #         print("winner", end=" ")
    #     print(f"{par.idp: >2}: brieb {par.p} now {par.v: >2} was {before[i].v: >2}")

    print(" ".join(str(party.v) for party in parties))

class H_test(unittest.TestCase):
    @staticmethod
    def createParties(params):
        parties = []
        for i, par in enumerate(params):
            parties.append(Party(i, *par))
        
        return parties

    def test_chooseParty(self):
        n = 3
        partyParams = [(7, -1), (2, 8), (1, 2)]
        parties = H_test.createParties(partyParams)
        minFunds, party = chooseParty(n, parties)
        partyId = 3; ansFunds = 6
        self.assertIs(party, parties[partyId - 1])
        self.assertEqual(minFunds, ansFunds)

        n = 3
        partyParams = [(1, 1), (5, 5), (6, 1)]
        parties = H_test.createParties(partyParams)
        minFunds, party = chooseParty(n, parties)
        partyId = 3; ansFunds = 1
        self.assertIs(party, parties[partyId - 1])
        self.assertEqual(minFunds, ansFunds)

        n = 3
        partyParams = [(1, 1), (5, 5), (6, -1)]
        parties = H_test.createParties(partyParams)
        minFunds, party = chooseParty(n, parties)
        partyId = 1; ansFunds = 5
        self.assertIs(party, parties[partyId - 1])
        self.assertEqual(minFunds, ansFunds)

        n = 3
        partyParams = [(1, 1), (5, 3), (6, -1)]
        parties = H_test.createParties(partyParams)
        minFunds, party = chooseParty(n, parties)
        partyId = 2; ansFunds = 4
        self.assertIs(party, parties[partyId - 1])
        self.assertEqual(minFunds, ansFunds)

        n = 3
        partyParams = [(6, 9), (4, 7), (2, 6)]
        parties = H_test.createParties(partyParams)
        minFunds, party = chooseParty(n, parties)
        partyId = 3; ansFunds = 9
        self.assertIs(party, parties[partyId - 1])
        self.assertEqual(minFunds, ansFunds)

        n = 1
        partyParams = [(239, 239)]
        parties = H_test.createParties(partyParams)
        minFunds, party = chooseParty(n, parties)
        partyId = 1; ansFunds = 239
        self.assertIs(party, parties[partyId - 1])
        self.assertEqual(minFunds, ansFunds)



if __name__ == "__main__":
    #unittest.main()
    main()