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

class Packet():
    def __init__(self, string, parent = PacketHolder):
        self.string = string
        self.parent = parent

        if self.parent == PacketHolder:
            self.parent.subPackets.append(self)

        if '1' not in self.string:
            parent.subPackets.remove(self)
        else:
            self.create()
        
    def create(self):
        self.version = self.string[:3]
        self.typeID = self.string[3:6]
        
        self.values = []
        self.subPackets = []

        # Literal Value
        if binaryToInt(self.typeID) == 4:
            leftOver = self.getValues(self.string[6:])
            self.parent.subPackets.append(Packet(leftOver))
        
        # Operator
        else:
            lengthTypeID = self.string[6:7]
            
            # next 15 bits encode the total length in bits of the sub-packets in the packet
            if lengthTypeID == '0':
                totalLengthOfSubPackets = binaryToInt(self.string[7:22])
                self.subPackets.append(Packet(self.string[22:22+totalLengthOfSubPackets]))
                self.parent.subPackets.append(Packet(self.string[22+totalLengthOfSubPackets:]))
            # Next 11 bits are the number of subpackets contained in the packet
            else:
                pass

    def getValues(self, string):
        stop = False
        while not stop:
            if string[0] == '0':
                stop = True
            self.values.append(string[1:5])
            string = string[5:]
        leftOver = string
        return leftOver
            



def parsePacket(packetString):
    pass

print(hexToBinary('D2FE28'))
print(Packet('00111000000000000110111101000101001010010001001000000000').subPackets)