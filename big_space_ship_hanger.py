def hanger():
    import pygame
    from add_text import draw_text 
    from save import load, room_item_save, room_item_load, save_invotary, invotary_load, save, invotory_spots_load, invotory_spots_save, save_loc
    from game_ship_fight import game_ship_run  # type: ignore
    from menu import menu
    from corridor_part import corridor # type: ignore
    from move_invotory_to_floor import invotory_to_map, room_to_invotory # type: ignore
    from moving_in_ship import moving_in_big_ship # type: ignore
    from text_language import Text_choice # type: ignore
    import time
    from walk import walk_imagie # type:ignore

    # Initialize Pygame
    pygame.init()

    save_loc(2)

    # Get screen dimensions for dynamic window size
    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w  # Get the current screen width
    screen_height = screen_info.current_h  # Get the current screen height

    # Set the window to fullscreen mode
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Load background image for the hanger (scale it to the required size)
    hanger_image = pygame.image.load('hanger_2.png')
    hanger_image = pygame.transform.scale(hanger_image, (877, 620))

    invotory_spots = [200,300,400]
    invotory_player_spots = [200,300,400]
    # Initialize room_item dictionary to hold items in the room
    room_item = {}
    # Initialize the inventory dictionary (items the player has)
    invotory = {}

    room_items_images={}
    invotory_images={}

    # Load saved room items and inventory items from files
    room_item = room_item_load("hanger_items")  # Load saved room items from file
    invotory = invotary_load()  # Load saved inventory items from file
    invotory_spots = invotory_spots_load()



    # Initial player position and spaceship position
    player_poss = [550, 200]  # Player's initial position
    space_ship_poss = [1030, 400]  # Space ship's position
    player_small_ship = load(player_ship={})  # Load player ship's data
    new_x = player_poss[0]  # Initialize new x position
    new_y = player_poss[1]  # Initialize new y position
    run = True  # Game loop flag
    invotory_player_spots_spot=0
    wait_for_invotory_spot = 0
    potato_time=0
    walk_time = 0
    flip = False
    frame = 0
    idle_stat = pygame.image.load('idle - 1.png')
    walk_stat = pygame.image.load('walk - 1.png')
    time.sleep(0.2)
    # Main game loop
    while run:
        # Draw the player (representing the player as a rectangle)
        player = pygame.draw.rect(screen, (190, 70, 70), pygame.Rect(player_poss[0]+25, player_poss[1], 50, 120))
        current_time = time.time()
        key = pygame.key.get_pressed()  # Get keys pressed

        
        wait_for_invotory_spot, new_x, new_y, invotory_player_spots_spot = moving_in_big_ship(current_time, wait_for_invotory_spot,
                                                                                               new_x, new_y, invotory_player_spots_spot, True)


        # Fill the screen with black before drawing objects
        screen.fill((0, 0, 0))
        corridor_way = pygame.draw.rect(screen, (70, 70, 70), pygame.Rect(550, 150, 50, 25))
        # Calculate the center positions for the hanger image
        middle_1 = (screen_width - 577) / 2
        middle_2 = (screen_height - 620) / 2

        # Restrict player movement to prevent going off-screen
        if middle_1 + 800 >= new_x - 50 / 2 and new_x + 50 / 2 >= middle_1 + 30:
            player_poss[0] = new_x  # Update x position if within bounds
        else:
            new_x = player_poss[0]
        if middle_2 - 30 <= new_y - 50 / 2 and new_y + 50 / 2 <= middle_2 + 480:
            player_poss[1] = new_y  # Update y position if within bounds
        else:
            new_y = player_poss[1]

        # Draw the background and spaceship
        pygame.draw.rect(screen, (70, 70, 70), pygame.Rect(0, 0, 250, screen_height))
        ship = pygame.draw.rect(screen, (70, 70, 70), pygame.Rect(space_ship_poss[0], space_ship_poss[1], 100, 180))

        # Blit the hanger image (background) onto the screen
        screen.blit(hanger_image, (middle_1, middle_2))

        invotory_player = pygame.draw.rect(screen, (10, 70, 70), pygame.Rect(25, invotory_player_spots[invotory_player_spots_spot]-75, 100, 100))
        # Draw all items in the inventory
        room_item, invotory, invotory_spots,  invotory_player, player_small_ship, potato_time = invotory_to_map(room_item, invotory, invotory_player_spots, invotory_spots,
                                                                                 invotory_player_spots_spot, player_poss,
                                                                                   invotory_player, invotory_images, screen, player_small_ship, True, current_time, potato_time)

        
        # Draw the player again but for user
        idle_stat,walk_stat, walk_time, flip, frame = walk_imagie(player_poss, screen ,current_time, walk_time, flip, frame, idle_stat, walk_stat)
        invotory, room_item, invotory_spots, pick_up = room_to_invotory(room_item, invotory, invotory_spots, screen, room_items_images,player,player_poss)

        # Save the updated room items and inventory
        room_item_save(room_item,"hanger_items")
        save_invotary(invotory)
        invotory_spots_save(invotory_spots)


        # Draw health and fuel bars for the spaceship
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(space_ship_poss[0] - player_small_ship['max_health'] / 2,
                                                          space_ship_poss[1] + 190, player_small_ship['max_health'] * 2, 20))
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(space_ship_poss[0] - player_small_ship['max_health'] / 2,
                                                          space_ship_poss[1] + 190, player_small_ship['health'] * 2, 20))

        pygame.draw.rect(screen, (190, 190, 190), pygame.Rect(space_ship_poss[0] - player_small_ship['max_fuel'] / 2,
                                                              space_ship_poss[1] + 220, player_small_ship['max_fuel'] * 2, 20))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(space_ship_poss[0] - player_small_ship['max_fuel'] / 2,
                                                         space_ship_poss[1] + 220, player_small_ship['fuel'] * 2, 20))


        if pick_up == True:
            draw_text(screen, Text_choice(0,8), (255,255,255), player_poss[0]  ,player_poss[1]-50) 
        

        # Check if player collides with spaceship and presses Enter
        if player.colliderect(ship):
            pygame.draw.rect(screen, (70, 70, 70), pygame.Rect(player_poss[0]-2.5  ,player_poss[1]-52.5, 100, 30))
            draw_text(screen, Text_choice(0,7), (255,255,255), player_poss[0]  ,player_poss[1]-50) 

        if player.colliderect(ship) and key[pygame.K_RETURN]:
            next = 1
            run = False  # Exit the game loop if player is inside the ship

        # Move spanner to the room if it's in inventory and "G" is pressed

        if player.colliderect(corridor_way) and key[pygame.K_w]:
            next = 2
            run = False  # Exit the game loop if player is inside the ship
        
        # Handle events (check for key presses)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  # If a key is pressed
                if event.key == pygame.K_ESCAPE:  # Check if it's the Escape key
                    run = False
                    next = 0  # Exit game if Escape is pressed

        # Update the display to show the changes
        pygame.display.update()

    # If game is over, go to menu or start the next game
    if next == 0:
        menu()  # Return to the main menu
    if next == 1:
        game_ship_run()  # Start the next game (ship fight)
    if next == 2:
        corridor()