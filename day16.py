from typing import Pattern

f = open("day16input.txt", "r")
input = f.read()

hexCharInBinary = {
'0' : '0000',
'1' : '0001',
'2' : '0010',
'3' : '0011',
'4' : '0100',
'5' : '0101',
'6' : '0110',
'7' : '0111',
'8' : '1000',
'9' : '1001',
'A' : '1010',
'B' : '1011',
'C' : '1100',
'D' : '1101',
'E' : '1110',
'F' : '1111',
}

def hexToBinary(hexString):
    binaryString = ''
    for char in hexString:
        binaryString += hexCharInBinary[char]
    return binaryString

def binaryToInt(binaryString):
    out = 0
    worth = 1
    for char in binaryString[::-1]:
        if char == '1':
            out += worth
        worth *= 2
    return out

class PacketHolder():
    subPackets = []

    def versionSum():
        out = 0
        for packet in PacketHolder.subPackets:
            out += packet.versionSum()
        return out

    def evaluate():
        for packet in PacketHolder.subPackets:
            packet.evaluate()
        return PacketHolder.subPackets[0].value


class Packet():
    def __init__(self, string, parent = PacketHolder):
        self.string = string
        self.parent = parent

        self.parent.subPackets.append(self)

        if '1' not in self.string:
            self.parent.subPackets.remove(self)
        else:
            self.create()

    def create(self):
        self.version = binaryToInt(self.string[:3])
        self.typeID = binaryToInt(self.string[3:6])
        
        self.value = 0
        self.subPackets = []

        # Literal Value
        if self.typeID == 4:
            leftOver = self.getLiteralLeftover(self.string[6:])
            Packet(leftOver, parent=self.parent)
        
        # Operator
        else:
            lengthTypeID = self.string[6:7]
            
            # next 15 bits encode the total length in bits of the sub-packets in the packet
            if lengthTypeID == '0':
                totalLengthOfSubPackets = binaryToInt(self.string[7:22])
                Packet(self.string[22:22+totalLengthOfSubPackets], parent=self)
                Packet(self.string[22+totalLengthOfSubPackets:], parent=self.parent)
            # Next 11 bits are the number of subpackets contained in the packet
            else:
                numSubPackets = binaryToInt(self.string[7:18])
                Packet(self.string[18:], parent = self)
                if len(self.subPackets) > numSubPackets:
                    for i in range(numSubPackets,len(self.subPackets)):
                        self.parent.subPackets.append(self.subPackets[numSubPackets])
                        self.subPackets.pop(numSubPackets)

    def getLiteralValue(self, string):
        stop = False
        value = ''
        while not stop:
            if string[0] == '0':
                stop = True
            value += string[1:5]
            string = string[5:]
        value = binaryToInt(value)
        return value

    def getLiteralLeftover(self, string):
        stop = False
        while not stop:
            if string[0] == '0':
                stop = True
            string = string[5:]
        return string
    
    def evaluate(self):
        if self.typeID == 4:
            self.value = self.getLiteralValue(self.string[6:])

        # Sum of all packets
        elif self.typeID == 0:
            out = 0
            for packet in self.subPackets:
                packet.evaluate()
                out += packet.value
            self.value = out
        
        # Product of packets
        elif self.typeID == 1:
            product = 1
            for packet in self.subPackets:
                packet.evaluate()
                product *= packet.value
            self.value = product

        # Minimum packet value
        elif self.typeID == 2:
            valueList = []
            for packet in self.subPackets:
                packet.evaluate()
                valueList.append(packet.value)
            self.value = min(valueList)

        # Maximum
        elif self.typeID == 3:
            valueList = []
            for packet in self.subPackets:
                packet.evaluate()
                valueList.append(packet.value)
            self.value = max(valueList)

        # >
        elif self.typeID == 5:
            self.subPackets[0].evaluate()
            self.subPackets[1].evaluate()
            if self.subPackets[0].value > self.subPackets[1].value:
                self.value = 1
        elif self.typeID == 6:
            self.subPackets[0].evaluate()
            self.subPackets[1].evaluate()
            if self.subPackets[0].value < self.subPackets[1].value:
                self.value = 1
        elif self.typeID == 7:
            self.subPackets[0].evaluate()
            self.subPackets[1].evaluate()
            if self.subPackets[0].value == self.subPackets[1].value:
                self.value = 1

    def versionSum(self):
        out = self.version
        for packet in self.subPackets:
            out += packet.versionSum()
        return out

def parsePacket(packetString):
    pass

Packet(hexToBinary(input))
print(PacketHolder.evaluate())
