f = open("day17input.txt", "r")
input = f.read()

input = input.split(" ")
x = input[2].split("x=")[1].split(",")[0].split("..")
y = input[3].split("y=")[1].split(",")[0].split("..")
targetXRange = (int(x[0]), int(x[1]))
targetYRange = (int(y[0]), int(y[1]))

class Target():
    def __init__(self, xRange, yRange):
        self.x1 = min(xRange)
        self.x2 = max(xRange)
        self.y1 = min(yRange)
        self.y2 = max(yRange)
        
    def onTarget(self, x, y):
        if x >= self.x1 and x <= self.x2:
            if y >= self.y1 and y <= self.y2:
                return True
        return False

    def belowTarget(self, y):
        if y < self.y1:
            return True
        return False

class Probe():
    def __init__(self, xTraj, yTraj):
        self.x = 0
        self.y = 0

        self.dx = xTraj
        self.dy = yTraj
        
        self.highestY = 0
    
    def step(self):
        self.x += self.dx
        self.y += self.dy
        
        if self.y > self.highestY:
            self.highestY = self.y
        
        if self.dx != 0:
            self.dx += -(self.dx//abs(self.dx))
        self.dy -= 1
        
target = Target(targetXRange, targetYRange)

highY = []
velocities = []

for x in range(0,target.x2+1):
    for y in range(target.y1, 500):
        probe = Probe(x,y)

        while not(target.onTarget(probe.x,probe.y)) and not(target.belowTarget(probe.y)):
            probe.step()

        if target.onTarget(probe.x,probe.y):
            highY.append(probe.highestY)
            velocities.append([probe.x, probe.y])

if highY:
    print(max(highY))

if velocities:
    print(len(velocities))



