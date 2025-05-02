from save import save, save_loc, save_bad_guy, save_invotary, room_item_save, invotory_spots_save
import pygame
def new_game():
    max_speed=7
    bulet=110
    max_bulets=110
    fuel = 100
    max_fuel = 100
    health = 100
    max_health = 100
    bullet_refill_interval = 2 # seconds between bullet refills
    player_ship = {
        "max_speed" : max_speed,
        "bulets" : bulet,
        "max_bulets" : max_bulets,
        "fuel" : fuel,
        "max fuel":max_fuel,
        "health": health,
        "max_health": max_health,
        "refill_speed": bullet_refill_interval
    }
    save(player_ship)
    save_bad_guy(bad_guy_ship={})
    save_loc(4)
    save_invotary(invotary={})

    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w  # Get the current screen width
    screen_height = screen_info.current_h  # Get the current screen height

    room_item = {}


    # Define the spanner and fuel can item data including their positions
    room_item["spanner"] = {
        "imagie": "spanner.png",  # Scale image
        "pos": [(screen_width-577)/1.2, (screen_height-620)/1.2],  # Position of spanner
        "size": [40,40]
    }
    room_item["fuel_can"] = {
        "imagie": "fuel_can.png",  # Scale image
        "pos": [(screen_width-577)/1.1, (screen_height-620)/1.1],  # Position of fuel can
        "size" : [50,50]
    }
    # Initialize the inventory dictionary (items the player has)
    room_item_save(room_item,"hanger_items")
    room_item={}
    room_item_save(room_item, "corridor_items")
    room_item_save(room_item, "bridge_items")
    invotory_spots = [200,300,400]
    invotory_spots_save(invotory_spots)
