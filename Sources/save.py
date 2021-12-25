def save(user, result, u_icon, saves):
    
    filename = "Resources/saves.txt"

    try:
        openfile = open(filename, 'w')
    except OSError:
        print("ERROR: Could not open",filename)
        exit()

    try:
        s = saves[user]
        if u_icon == result: # user won
            s[0] += 1 # up wins
        elif result == 'C': # tie
            s[1] += 1 # up losses
            s[0] += 1 # up wins
        else: # up losses
            s[1] += 1 # up losses
        saves[user] = s
    except KeyError:
        if u_icon == result:
            saves[user] = [1, 0]
        else:
            saves[user] = [0, 1]

    for key in saves.keys():
        openfile.write(key)
        openfile.write('\t')
        openfile.write(str(saves[key][0]))
        openfile.write('\t')
        openfile.write(str(saves[key][1]))

    openfile.close()

    return