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
    bypass = False
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
    elif card_type == "a":
        card_type = "Avatar"
    elif card_type == "v":
        new_string = "Vacant"
    else:
        new_string = "%s" % card_type
        bypass = True

    if card_type != "Sucker" and card_type != "v" and bypass == False:
        new_string = "%s - %s" % (card_type, num)
    elif card_type == "Sucker" and bypass == False:
        new_string = "Sucker"
    else:
        toggle = True

    return(new_string)

def update(pos_1, pos_2, list_1):
    
    str_val_1 = list_1[pos_1]
    val_1 = str_value_1.split("-")
    str_val_2 = list_1[pos_2]
    val_2 = str_value_2.split("-")

    if val_1[0] == "0":
        return(None)
    elif val_2[0] == "0":
        if first_val[1] == "b" and second_val[1] == "Block":
            list_1[pos_2] = str_val_1
            list_1[pos_1] = "0-v"
        elif first_val[1] = "b" and second_val[1] == "Corner":
            list_1[pos_2] = str_val_1
            list_1[pos_1] = "0-v"
        elif first_val[1] == "p" and second_val[1] == "Punch":
            list_1[pos_2] = str_val_1
            list_1[pos_1] = "0-v"
        elif first_val[1] == "p" and second_val[1] == "Corner":
            list_1[pos_2] = str_val_1
            list_1[pos_1] = "0-v"
        elif first_val[1] == "k" and second_val[1] == "Corner":
            list_1[pos_2] = str_val_1
            list_1[pos_1] = "0-v"
        else:
            return(None)
    else:
        if first_val[1] == second_val[1]:
            list_1[pos_2] = str_val_1
            list_1[pos_1] = "0-v"
        elif first_val[1] == "c" and second_val[1] == "a":
            health = second_val[0] - first_val[0]
            string = "%s-a" % health
            list_1[pos_2] = string
            list_1[pos_1] = "0-v"
        elif first_val[1] == "k" and second_val[1] == "a":
            health = second_val[0] + first_val[0]
            string = "%s-a" % health
            list_1[pos_2] = string
            list_1[pos_1] = "0-v"
        
        


    
    

print("Welcome to Deck 'Em, a solitaire-style boxing game. Check it out on the App Store! ")
print("")

avatar = 21

blocks = ["2-b", "3-b", "4-b", "5-b", "5-b", "6-b", "6-b", "7-b", "7-b", "8-b", "9-b", "10-b"] # 12 total
champs = ["2-c", "3-c", "4-c", "5-c", "6-c", "7-c", "7-c", "8-c", "8-c", "9-c", "9-c", "10-c", "10-c", "11-c", "12-c", "13-c", "14-c", "15-c"] # 18 total
kits = ["2-k", "3-k", "4-k", "5-k", "5-k", "6-k", "6-k", "7-k", "7-k", "8-k", "9-k", "10-k"] # 12 total
punches = ["3-p", "3-p", "3-p", "3-p", "3-p", "5-p", "5-p", "5-p", "15-p", "15-p"] # 10 total
# Vacant spots are represented by '0-v'

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

round_list.append("0-Punch")
round_list.append("21-a")
round_list.append("0-Block")
round_list.append("0-Corner")

for i in range (0, 8):
    x = round_list[i]
    x = convert(x)
    show_list.append(x)

print(round_list)
print(show_list)
            
