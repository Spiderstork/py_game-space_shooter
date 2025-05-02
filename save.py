import pygame

def save(player_ship):

    f = open("game_save.txt","w")
    for n in player_ship:
        f.write(str(player_ship[n]))
        f.write("/")
    f.close




def load(player_ship):

    # prep to have key names for all atributes
    player_ship_dict={
        1 :"max_speed",
        2:"bulets" ,
        3:"max_bulets",
        4:"fuel" ,
        5:"max_fuel",
        6:"health",
        7:"max_health",
        8:"refill_speed"
    }

    try:
        with open("game_save.txt","r") as f:
            for line in f:
                # Split the line by "/" to get individual values
                stats = line.strip().split("/")
                for n in range(len(stats)):
                    player_ship[player_ship_dict[n+1]]=float(stats[n])
    except KeyError:
        pass
    except ValueError:
        pass
    except FileNotFoundError:
        pass
    
    f.close

    return player_ship

def save_bad_guy(bad_guy_ship):
    f = open("bad_guy_save.txt","w")
    for n in bad_guy_ship:
        for d in bad_guy_ship[n]:
            if d == "pos":
                f.write(str(bad_guy_ship[n][d][0]))
                f.write("/")
                f.write(str(bad_guy_ship[n][d][1]))
            else:
                f.write(str(bad_guy_ship[n][d]))
            f.write("/")
        f.write("\n")
    f.close


def load_bad_guy(bad_guy_ship):
    bad_guy_ship_dict={
                1:"pos",
                2:"health",
                3:"max_health",
                4:"angle",
                5:"rotated_bad_image",
                6:"rotated_bad_rect",
                7:"time",
                8:"add_angle",
                9:"speed",
                }
    
    bad_guy_ship = {}  # Ensure this is defined
    specific_ship = 0
    with open("bad_guy_save.txt", "r") as f:
    
        for line in f:
            specific_ship += 1
            bad_guy_ship[specific_ship] = {}
        
            stats = line.strip().split("/")
          
            for n in range(len(stats)):
                try:
                    if stats[n+1] == "":
                        continue
                except:
                    break

                if n+1 < 2:
                   ship_pos=[]
                   ship_pos.append(float(stats[n]))
                   ship_pos.append(float(stats[n+1]))
                   bad_guy_ship[specific_ship][bad_guy_ship_dict[n+1]]=ship_pos
                   
                elif n+1 == 5:
                    bad_guy_ship[specific_ship][bad_guy_ship_dict[n+1]]= stats[n+1]

                elif n+1 == 6:
                    bad_guy_ship[specific_ship][bad_guy_ship_dict[n+1]]= stats[n+1]

                else:
                    bad_guy_ship[specific_ship][bad_guy_ship_dict[n+1]]= float(stats[n+1])
    f.close
    return  bad_guy_ship 

#
#   --- location ---
#
def save_loc(num):
    f = open("location.txt","w")
    f.write(str(num))
    f.close

def load_loc():
    with open("location.txt","r") as f:
        for line in f:
            loc = line
    f.close
    return(loc)

def room_item_save(room_items,map):
    f = open(map,"w")
    for n in room_items:
        f.write(n)
        f.write("/")
        for d in room_items[n]:
            if d == "pos":
                f.write(str(room_items[n][d][0]))
                f.write("/")
                f.write(str(room_items[n][d][1]))

            elif d == "size":
                f.write(str(room_items[n][d][0]))
                f.write("/")
                f.write(str(room_items[n][d][1]))
            else:
                f.write(str(room_items[n][d]))
            f.write("/")
        f.write("\n")
    f.close

def room_item_load(map):
    # Initialize room_item dictionary
    room_item = {}

    # Open the file and read line by line
    with open(map, 'r') as f:
        for line in f:
            line = line.strip() 
            if not line:
                continue  # Skip empty lines

            # Split the line by / to get the parts (item_name, image_path, x_position, y_position)
            item_data = line.split('/')

            if len(item_data) < 4:
                continue  # Skip lines that don't have enough data

            item_name = item_data[0].strip()  # Item name 
            image_path = item_data[1].strip()  # Image file path
            x_position = float(item_data[2].strip())  # X position
            y_position = float(item_data[3].strip())  # Y position

            x_size = float(item_data[4].strip())  # X position
            y_size = float(item_data[5].strip())  # Y position


            # Add the item to the room_item dictionary
            room_item[item_name] = {
                "imagie": image_path,
                "pos": [x_position, y_position],
                "size": [x_size, y_size]
            }

    return room_item

def save_invotary(invotary):
    f = open("player_invotary","w")
    for n in invotary:
        f.write(n)
        f.write("/")
        for d in invotary[n]:
            if d == "pos":
                f.write(str(invotary[n][d][0]))
                f.write("/")
                f.write(str(invotary[n][d][1]))

            elif d == "size":
                f.write(str(invotary[n][d][0]))
                f.write("/")
                f.write(str(invotary[n][d][1]))

            else:
                f.write(str(invotary[n][d]))
            f.write("/")
        f.write("\n")
    f.close

def invotary_load():
    # Initialize room_item dictionary
    invotary = {}

    # Open the file and read line by line
    with open("player_invotary", 'r') as f:
        for line in f:
            line = line.strip()  # Remove leading/trailing whitespace
            if not line:
                continue  # Skip empty lines

            # Split the line by '/' to get the parts (item_name, image_path, x_position, y_position)
            item_data = line.split('/')

            if len(item_data) < 4:
                continue  # Skip lines that don't have enough data

            item_name = item_data[0].strip()  # Item name
            image_path = item_data[1].strip()  # Image file path 
            x_position = float(item_data[2].strip())  # X position
            y_position = float(item_data[3].strip())  # Y position

            x_size = float(item_data[4].strip())  # X position
            y_size = float(item_data[5].strip())  # Y position


            # Add the item to the room_item dictionary
            invotary[item_name] = {
                "imagie": image_path,
                "pos": [x_position, y_position],
                "size": [x_size, y_size]
            }


    return invotary


def invotory_spots_save(invotory_spots):
    f = open("invotory_spots","w")
    for n in invotory_spots:
        f.write(str(n))
        f.write("/")
    f.close

def invotory_spots_load():
    invotory_spots=[]
    f = open("invotory_spots","r")
    for line in f:
        item_data = line.split('/')
        for n in item_data:
            if n=="":
                continue
            else:
                invotory_spots.append(int(n))
    f.close

    return invotory_spots
