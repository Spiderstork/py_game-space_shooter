import pygame
import copy
import math
import random

# Function to handle speed changes via key presses
def speed_keys(speed, y_speed_size,player_ship):
    key = pygame.key.get_pressed()

    # Speed control: S to decrease, W to increase
    if key[pygame.K_s]:
        if speed < 0 and player_ship["fuel"]>0: # Prevent the speed from going below zero
            y_speed_size -= 2  # Decrease the speed meter size
            speed += 0.1  # Increase the speed (negative to move down)
            player_ship["fuel"]-=0.05
           
    elif key[pygame.K_w]:
        if speed >  -player_ship["max_speed"] and player_ship["fuel"]>0:  # Prevent speed from going below -10
            y_speed_size += 2  # Increase the speed meter size
            speed -= 0.1  # Decrease the speed (negative to move up)
            player_ship["fuel"]-=0.05
           

    return speed, y_speed_size

# Function to handle rotation of the player using A and D keys
def angle_keys(angle):
    key = pygame.key.get_pressed()

    # Control rotation: A to rotate counter-clockwise, D to rotate clockwise
    if key[pygame.K_a]:
        angle += 5  # Rotate counter-clockwise
    elif key[pygame.K_d]:
        angle -= 5  # Rotate clockwise

    return angle

def bullet_coretion(angle, bullets, player_pos,num,speed,time,last_time,player_ship):
    key = pygame.key.get_pressed()

    if key[pygame.K_SPACE] and time-last_time > 0.2 and player_ship["bulets"]>10:
        bull_speed = -speed + 6  
        dy = math.cos(math.radians(angle)) * bull_speed  # Vertical movement
        dx = math.sin(math.radians(angle)) * bull_speed  # Horizontal movement

        #
        #       key is a tuple      stores a tuple what contains deep copys of a player postion to avoid the player postion being affecting the bullets poss
        #                           why are the other two deepcopys dont know
        bullets['bullet', num] = copy.deepcopy(player_pos), dx, dy
        num += 1
        last_time = time
        player_ship["bulets"]-=10
        time = 0
    
    return num, last_time


def screen_check(new_x,new_y,rotated_height , rotated_width ,screen_width,screen_height,player_pos):
    # Check if the player moves off the screen horizontally
    if 250 <= new_x - rotated_width / 2 and new_x + rotated_width / 2 <= screen_width:
        player_pos[0] = new_x  # Update x position if within bounds
    # Check if the player moves off the screen vertically
    if 0 <= new_y - rotated_height / 2 and new_y + rotated_height / 2 <= screen_height:
        player_pos[1] = new_y  # Update y position if within bounds

def bad_guy_maker(bad_guy_ship,current_time, bad_guy_make_time, screen_height, screen_width, bad_guy_ship__num):
    if current_time - bad_guy_make_time > 15:
        make_not_make=random.randint(0,2)
        if make_not_make<=1 and len(bad_guy_ship)<3:
            bad_guy_ship__num+=1
            bad_guy_ship[bad_guy_ship__num]={
                "pos":[screen_width // 2, screen_height // 1.8],
                "health":100,
                "max_health":100,
                "angle":25,
                "rotated_bad_image":1,
                "rotated_bad_rect":1,
                "time":0,
                "add_angle":0,
                "speed": random.randint(-5,-2)
                }

        bad_guy_make_time=current_time
    return bad_guy_make_time , bad_guy_ship__num ,bad_guy_ship

def ai_movement(player_pos, original_bad_guy_image,bad_guy_ship,current_time):

    for ship in bad_guy_ship:
        if current_time - bad_guy_ship[ship]["time"]>3:
            bad_guy_ship[ship]["time"]=current_time
            bad_guy_ship[ship]["add_angle"]=random.randint(-100,100)
            
        #   --- Calculate Movement ---
        # Calculate vertical and horizontal movement (dx, dy) based on angle and speed
        by = math.cos(math.radians(bad_guy_ship[ship]["angle"]+bad_guy_ship[ship]["add_angle"]))  * bad_guy_ship[ship]["speed"]  # Vertical movement
        bx = math.sin(math.radians(bad_guy_ship[ship]["angle"]+bad_guy_ship[ship]["add_angle"]))  * bad_guy_ship[ship]["speed"]  # Horizontal movement

        # Calculate the potential new position for the bad_guy
        new_bad_x = bad_guy_ship[ship]["pos"][0] + bx
        new_bad_y = bad_guy_ship[ship]["pos"][1] + by

        diff_x = bad_guy_ship[ship]["pos"][1] - player_pos[1] 
        diff_y = bad_guy_ship[ship]["pos"][0] - player_pos[0]
        bad_guy_ship[ship]["angle"] = math.atan2(diff_y ,diff_x)
        bad_guy_ship[ship]["angle"] *= 180  
        bad_guy_ship[ship]["angle"] /= 3.14159265359

        # --- Rotate bad guy Image ---
        # Rotate the bad guy image based on the current angle
        bad_guy_ship[ship]["rotated_bad_image"] = pygame.transform.rotate(original_bad_guy_image, bad_guy_ship[ship]["angle"]+bad_guy_ship[ship]["add_angle"])
        bad_guy_ship[ship]["rotated_bad_rect"]  = bad_guy_ship[ship]["rotated_bad_image"].get_rect(center=(bad_guy_ship[ship]["pos"][0], bad_guy_ship[ship]["pos"][1]))

        bad_guy_ship[ship]["pos"][0]=new_bad_x 
        bad_guy_ship[ship]["pos"][1]=new_bad_y

    return bad_guy_ship 


def output_bars(player_ship, bad_guy_ship, screen , player_bar_postions,player_bar_color, y_speed_size, screen_height):
    if player_ship["health"] > 0:
        for ship in bad_guy_ship:
            pygame.draw.rect(screen, (255,0,0), pygame.Rect(bad_guy_ship[ship]["pos"][0]-50, bad_guy_ship[ship]["pos"][1]+50, bad_guy_ship[ship]["max_health"],10))
            pygame.draw.rect(screen, (0,255,0), pygame.Rect(bad_guy_ship[ship]["pos"][0]-50, bad_guy_ship[ship]["pos"][1]+50, bad_guy_ship[ship]["health"],10))
    else:
        screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (70,70,70), pygame.Rect(0, 0, 250, screen_height))
    #   --- speed ---
    max_player_speed = player_ship["max_speed"]*20
    pygame.draw.rect(screen, (40,40,40), pygame.Rect(player_bar_postions["speed_pos"][0], player_bar_postions["speed_pos"][1] - max_player_speed, 50, max_player_speed))
    pygame.draw.rect(screen, player_bar_color["speed_color"], pygame.Rect(player_bar_postions["speed_pos"][0], player_bar_postions["speed_pos"][1] - y_speed_size, 50, y_speed_size))

    #   --- fuel ---
    pygame.draw.rect(screen, (40,40,40), pygame.Rect(player_bar_postions["fuel_pos"][0], player_bar_postions["fuel_pos"][1] - player_ship["max_fuel"] , 50, player_ship["max_fuel"]))
    pygame.draw.rect(screen, player_bar_color["fuel_color"], pygame.Rect(player_bar_postions["fuel_pos"][0], player_bar_postions["fuel_pos"][1] - player_ship["fuel"], 50, player_ship["fuel"]))
    #   --- good bullets ---
    pygame.draw.rect(screen, (40,40,40), pygame.Rect(player_bar_postions["bullet_amount_pos"][0], player_bar_postions["bullet_amount_pos"][1], player_ship["max_bulets"] ,50 ))
    pygame.draw.rect(screen, player_bar_color["bullet_amount_color"], pygame.Rect(player_bar_postions["bullet_amount_pos"][0], player_bar_postions["bullet_amount_pos"][1], player_ship["bulets"] ,50 ))

    #   --- player health ---
    pygame.draw.rect(screen,(255,0,0), pygame.Rect(player_bar_postions["health_pos"][0], player_bar_postions["health_pos"][1], player_ship["max_health"], 50))   
    pygame.draw.rect(screen, player_bar_color["health_color"], pygame.Rect(player_bar_postions["health_pos"][0], player_bar_postions["health_pos"][1], player_ship["health"], 50))    


def bad_guy_bullet_creation(bad_guy_ship, current_time, bad_time,bad_bullets,num):
    for ship in bad_guy_ship:
        if current_time - bad_time > 0.5:
            if random.randint(0,100)>80: 
                bull_speed = bad_guy_ship[ship]["speed"] * 2
                dy = math.cos(math.radians(bad_guy_ship[ship]["angle"]+bad_guy_ship[ship]["add_angle"])) * -bull_speed  # Vertical movement
                dx = math.sin(math.radians(bad_guy_ship[ship]["angle"]+bad_guy_ship[ship]["add_angle"])) * -bull_speed  # Horizontal movement

                #
                #           key is a tuple          deep copys player postion to avoid it beign effected by the player later on
                #
                bad_bullets['bullet', num] = copy.deepcopy(bad_guy_ship[ship]["pos"]), dx, dy
                num += 1
                bad_time= current_time
    return bad_bullets, num, bad_time 


