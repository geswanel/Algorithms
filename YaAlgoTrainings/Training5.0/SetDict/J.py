"""
Description:
n devices connected to each other
1 device has an update that should be uploaded to others
P2P protocol to deliver a file to all devices
    1. File divided into k pieces with the same size.
        uploading is happening during a timeslot that takes 1 minute
        during a timeslot each device can transfer or receive 1 piece of update
            Actions: pass and receive, pass or receive, nothing
    2. Before timeslot.
        Requests:
            1. Each device chooses missing and rarest piece of update with minimum id
            2. Each device makes a request to another device with this piece
                with least pieces downloaded
                with least device id
        Response:
            1. Each device decides which request to process
                Device A chooses a device B with most value
                    Value of B for A is the number of pieces received by A from B
                        if there are several devices with the smae value
                            the device with least received pieces and with least device id
    3. During a timeslot => transfering and receiving pieces

For each device check how many timeslots needed to download an update
INPUT:
n, k  #n ~100, k ~ 200
OUTPUT
n - 1 - number of timeslots to download
Solution:
Carefully implement algorithm
1. class Device
        static updateSize 
        pieces: set - uploaded pieces
        values: dict deviceId: value
        requests: set   - ids of devices who made a request
    dict piece: cnt => how many devices have a piece
2. Functions
    Choose missing part
    Make requests
    Identify to who response
    process responses and receives
"""
import unittest

class Device:
    processor = None
    def __init__(self, idd):
        self.idd = idd
        self.pieces = set()
        self.devValue = dict()
        self.requests = set()
        self.devToSend = None
        self.pieceToReceive = None
        self.updatedTimeslot = 0
    
    def chooseMissing(self):
        rarity = self.processor.n + 1
        # missing | rarest | min id
        for i in range(self.processor.k):
            if i not in self.pieces and \
                    self.processor.cntPieceLoaded[i] < rarity:
                rarity = self.processor.cntPieceLoaded[i]
                self.pieceToReceive = i

    def makeRequest(self):
        # has the piece | has least pieces | min id
        if self.pieceToReceive is not None:
            leastPieces = self.processor.k + 1
            reqReciever = None
            for d in self.processor.devices:
                if d is not self and \
                    self.pieceToReceive in d.pieces and \
                        len(d.pieces) < leastPieces:
                    leastPieces = len(d.pieces)
                    reqReciever = d
            reqReciever.requests.add(self.idd)
    
    def identifyRecipient(self):
        # most value | least received pieces | leased id
        if self.requests:
            maxValue = -1
            leastPieces = self.processor.k + 1
            devToSendId = self.processor.n
            for reqId in self.requests:
                val = self.devValue.get(reqId, 0)
                dLoadedPieces = len(self.processor.devices[reqId].pieces)
                if val > maxValue:
                    devToSendId = reqId
                    leastPieces = dLoadedPieces
                    maxValue = val
                elif val == maxValue and dLoadedPieces < leastPieces:
                    leastPieces = dLoadedPieces
                    devToSendId = reqId
                elif val == maxValue and dLoadedPieces == leastPieces and reqId < devToSendId:
                    devToSendId = reqId
            self.requests.clear()
            self.devToSend = self.processor.devices[devToSendId]
    
    def processTimeslot(self):
        if self.devToSend:
            reciever = self.devToSend
            sendedPiece = reciever.pieceToReceive
            reciever.pieces.add(sendedPiece)
            reciever.devValue[self.idd] = reciever.devValue.get(self.idd, 0) + 1
            if len(reciever.pieces) == self.processor.k:
                reciever.updatedTimeslot = self.processor.timeSlot

            self.processor.cntPieceLoaded[sendedPiece] += 1
            if self.processor.cntPieceLoaded[sendedPiece] == self.processor.n:
                self.processor.cntCompletion += 1

            reciever.pieceToReceive = None
            self.devToSend = None



class P2PAlgorithm:
    def __init__(self, n, k):
        self.n = n
        Device.processor = self
        self.devices = [Device(i) for i in range(n)]
        self.devices[0].pieces.update(j for j in range(k))
        self.k = k
        self.cntPieceLoaded = {j: 1 for j in range(k)}  # pieceId: cnt of devices with piece
        self.cntCompletion = 0 if n > 1 else k  # how many pieces completed loading
        self.timeSlot = 0

    def updateDevices(self):
        while self.cntCompletion < self.k:
            self.chooseMissing()
            self.makeRequests()
            self.identifyRecipients()
            self.processTimeslot()
    
    def chooseMissing(self):
        for d in self.devices:
            d.chooseMissing()
    
    def makeRequests(self):
        for d in self.devices:
            d.makeRequest()
    
    def identifyRecipients(self):
        for d in self.devices:
            d.identifyRecipient()
    
    def processTimeslot(self):
        self.timeSlot += 1
        for d in self.devices:
            d.processTimeslot()
    
    def getStat(self):
        return " ".join(str(d.updatedTimeslot) for d in self.devices[1:])



def main():
    n, k = (int(x) for x in input().split())
    processor = P2PAlgorithm(n, k)
    processor.updateDevices()
    print(processor.getStat())


if __name__ == "__main__":
    main()