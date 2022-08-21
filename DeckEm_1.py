import random

def format_8(list_8):
    for i in range (0, 2):
        message = ""
        for j in range (0, 4):
            num = 2 * i + j
            val = list_8[num]
            message = "%s%s   " % (message, val)
        print(message)
    return(None)

def convert(string):
    list_1 = string.split("-")
    num = int(list_1[0])
    card_type = list_1[1]
    if card_type == "b":
        card_type = "Block"
    elif card_type == "c":
        card_type = "Champ"
    elif card_type == "k":
        card_type = "MedKit"
    elif card_type == "p":
        if num == 3:
            card_type = "Lucky"
        elif num == 5:
            card_type = "Haymaker"
        elif num == 15:
            card_type = "Sucker"
        else:
            print("Something went wrong.")
    else:
        print("Something went wrong")

    if card_type != "Sucker":
        new_string = "%s - %s" % (card_type, num)
    else:
        new_string = "Sucker"

    return(new_string)

def update(pos_1, pos_2, list_1):
    update_list = []
    for i in range (0, 8):
        update_list.append(0)
    
    value_1 = list_1[pos_1]
    value_1 = value_1.split("-")
    value_2 = list_1[pos_2]
    value_2 = value_2.split("-")

    if value_1 = "None":
        print(None)
    

    
    

print("Welcome to Deck 'Em, a solitaire-style boxing game. Check it out on the App Store! ")
print("")

avatar = 21

blocks = ["2-b", "3-b", "4-b", "5-b", "5-b", "6-b", "6-b", "7-b", "7-b", "8-b", "9-b", "10-b"] # 12 total
champs = ["2-c", "3-c", "4-c", "5-c", "6-c", "7-c", "7-c", "8-c", "8-c", "9-c", "9-c", "10-c", "10-c", "11-c", "12-c", "13-c", "14-c", "15-c"] # 18 total
kits = ["2-k", "3-k", "4-k", "5-k", "5-k", "6-k", "6-k", "7-k", "7-k", "8-k", "9-k", "10-k"] # 12 total
punches = ["3-p", "3-p", "3-p", "3-p", "3-p", "5-p", "5-p", "5-p", "15-p", "15-p"] # 10 total

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

shuffle_list = total_list
random.shuffle(shuffle_list)

show_list = []
round_list = []

for i in range (0, 4):
    x = shuffle_list[i]
    round_list.append(x)
    x = convert(x)
    show_list.append(x)

round_list.append(0)
round_list.append(0)
round_list.append("21-a")

print(round_list)
print(show_list)
            
