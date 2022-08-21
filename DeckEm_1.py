def format_8(list_8):
    for i in range (0, 2):
        message = ""
        for j in range (0, 4):
            num = 2 * i + j
            val = list_8[num]
            message = "%s%s   " % (message, val)
        print(message)
    return(None)

print("Welcome to Deck 'Em, a solitaire-style boxing game. Check it out on the App Store! ")

avatar = 21



blocks = [2, 3, 4, 5, 5, 6, 6, 7, 7, 8, 9, 10] # 12 total
champs = [2, 3, 4, 5, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 12, 13, 14, 15] # 18 total
kits = [2, 3, 4, 5, 5, 6, 6, 7, 7, 8, 9, 10] # 12 total
punches = [3, 3, 3, 3, 3, 5, 5, 5, 15, 15] # 10 total

total_list = []
for i in range (0, 12):
    value = blocks[i]
    total_list.append(value)
for i in range (0, 18):
    value = champs[i]
    total_list.append(value)
for i in range (0, 12):
    value = kits[i]
    total_list.append(value)
for i in range (0, 10):
    value = punches[i]
    total_list.append(value)


            
