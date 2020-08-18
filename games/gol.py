import random, time, copy

WIDTH = 60
HEIGHT  = 20


nextcells = []

for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append("#")
        else:
            column.append(" ")
    nextcells.append(column)

# printing space between cells
while True:
    print("\n\n\n\n\n")
    currentcells = copy.deepcopy(nextcells)

#printing the current cells
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(nextcells[x][y], end="")
        print()

    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT
            
            numNeighbors = 0
            if currentcells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1
            if currentcells[x][aboveCoord] == '#':
                numNeighbors +=1
            if currentcells[rightCoord][aboveCoord] == '#':
                numNeighbors +=1
            if currentcells[leftCoord][y] == '#':
                numNeighbors +=1
            if currentcells[rightCoord][y] == '#':
                numNeighbors +=1
            if currentcells[leftCoord][belowCoord] == '#':
                numNeighbors +=1
            if currentcells[rightCoord][belowCoord] == '#':
                numNeighbors +=1
            if currentcells[x][belowCoord] == '#':
                numNeighbors +=1
            #game of life rules
            if currentcells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                nextcells[x][y] = '#'
            elif currentcells[x][y] == " " and numNeighbors == 3:
                nextcells[x][y] = '#'
            else:
                nextcells[x][y] = ' '

    time.sleep(10)