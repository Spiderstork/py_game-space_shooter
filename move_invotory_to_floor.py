import pygame
from save import save
from add_text import draw_text
from text_language import Text_choice # type: ignore
import random

def invotory_to_map(room_item, invotory, invotory_player_spots, invotory_spots, invotory_player_spots_spot, player_poss, invotory_player, invotory_images, screen,
                     player_small_ship, useable, current_time, potato_time):  
    if_return_able = 0
    key = pygame.key.get_pressed() 
    del_invotory=[]
    for item in invotory:
        
        #   show the user items in the invotory 
        invotory_images[item]=pygame.transform.scale(pygame.image.load(invotory[item]["imagie"]),(invotory[item]["size"][0], invotory[item]["size"][1]))
        invotory_item = screen.blit(invotory_images[item], (invotory[item]["pos"][0], invotory[item]["pos"][1]))

        #   check if the user is squre invotory thing is covering the the tool
        if invotory_player.colliderect(invotory_item ):
            draw_text(screen, Text_choice(0,9), (255,255,255), 50,850) 

            #   adds text if tool can be used
            if useable == True:
                if item=="spanner":
                    draw_text(screen, Text_choice(0,10), (255,255,255), 50,800)
                elif item=="fuel_can":
                    draw_text(screen, Text_choice(0,11), (255,255,255), 50,800)

        #check if user is pressing g and is over a tool to drop it
        if key[pygame.K_g]:
            if invotory_player.colliderect(invotory_item ):
                room_item[item] = invotory[item]
                room_item[item]["pos"][0] = player_poss[0]
                room_item[item]["pos"][1] = player_poss[1]+75
                del_invotory.append(item)
                invotory_spots.append(invotory_player_spots[invotory_player_spots_spot])

        # check if user is other tool and f is pressed to use the tool to repair the ship
        if useable == True:
            if key[pygame.K_f]:
                if invotory_player.colliderect(invotory_item) and item =="spanner" and player_small_ship["health"]<player_small_ship["max_health"]:
                    player_small_ship["health"] += 0.05
                    save(player_small_ship)
                elif invotory_player.colliderect(invotory_item) and item =="fuel_can" and player_small_ship["fuel"]<player_small_ship["max_fuel"]:
                    player_small_ship["fuel"] += 0.05
                    save(player_small_ship)
                
    
    if key[pygame.K_p] and current_time-potato_time > 1 :
        room_item[str(random.randint(1,9999999999999))] = {
            "imagie": "potato.png",  # Scale image
            "pos": [player_poss[0], player_poss[1]+75],  
            "size" : [50,50]
            }     
        potato_time = current_time
 

              
    for item in del_invotory:
        del invotory[item]

    # if the player ship chanhges it returns it to the main program
    if useable == True:
        if_return_able = player_small_ship
    return room_item, invotory, invotory_spots,  invotory_player, if_return_able, potato_time








def room_to_invotory(room_item, invotory, invotory_spots, screen, room_items_images,player,player_poss):
    key = pygame.key.get_pressed()
    # Initialize item and object movers for collision detection
    item_mover = []
    object_mover = []


        
    # Draw all room items on the screen and store their positions for collision detection
    for item in room_item:
        room_items_images[item]=pygame.transform.scale(pygame.image.load(room_item[item]["imagie"]),(room_item[item]["size"][0],room_item[item]["size"][1]))
        object = screen.blit(room_items_images[item], (room_item[item]["pos"][0], room_item[item]["pos"][1]))
        item_mover.append(item)
        object_mover.append(object)

    # Check for collisions between the player and room items

    pick_up = False
    for item in range(len(item_mover)):
        if player.colliderect(object_mover[item]):
            pick_up = True

        if player.colliderect(object_mover[item]) and key[pygame.K_e]:
            if len(invotory_spots) >= 1 :
                invotory[item_mover[item]] = room_item[item_mover[item]]  # Add item to inventory
                invotory[item_mover[item]]["pos"][0] = 100 - invotory[item_mover[item]]["size"][1] # Set new position in inventory
                invotory[item_mover[item]]["pos"][1] = invotory_spots[0] - invotory[item_mover[item]]["size"][0]
                del invotory_spots[0]
                del room_item[item_mover[item]]  # Remove item from room

    return invotory, room_item, invotory_spots,pick_up