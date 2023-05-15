class grid:
    cell_size = 20
    input("Press Enter to start")
    for i in range(20):
        for j in range(20):
            if i == 0 or j == 0 or i == 19 or j == 19:
                print("0", end=" ")
            else:
                print("0", end=" ")
            if j == 19:
                print()