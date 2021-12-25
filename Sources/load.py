def load():
    
    filename = "Resources/saves.txt"

    try:
        openfile = open(filename, 'r')
    except OSError:
        print("ERROR: Could not open",filename)
        exit()

    saves = {}
    for line in openfile:
        line = line.strip()
        line = line.split()

        if len(line) < 3:
            print("ERROR: \"",line,"\" is not formatted correctly (name wins    losses)")
            exit()
        
        temp = [int(line[1]), int(line[2])]
        saves[line[0]] = temp

    openfile.close()

    return saves