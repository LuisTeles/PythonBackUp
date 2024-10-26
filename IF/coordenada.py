# Read coordinates and convert them to integers
coordenadaX = int(input("Coordenada X: "))
coordenadaY = int(input("Coordenada Y: "))

# Check the position based on the coordinates
if coordenadaX == 0 and coordenadaY == 0:
    print("Origem")
elif coordenadaX == 0:
    print("Eixo Y")
elif coordenadaY == 0:
    print("Eixo X")
elif coordenadaX > 0 and coordenadaY > 0:
    print("Q1")
elif coordenadaX < 0 and coordenadaY > 0:
    print("Q2")
elif coordenadaX < 0 and coordenadaY < 0:
    print("Q3")
else:
    print("Q4")
