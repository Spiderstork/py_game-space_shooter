def bridge():
    import pygame
    from save import  save_invotary, invotary_load, invotory_spots_load, invotory_spots_save, room_item_load , room_item_save, save_loc
    from menu import menu
    from move_invotory_to_floor import invotory_to_map, room_to_invotory # type: ignore
    from corridor_part import corridor # type: ignore
    from moving_in_ship import moving_in_big_ship # type: ignore
    from add_text import draw_text
    from text_language import Text_choice # type: ignore
    from walk import walk_imagie # type:ignore
    import time

    # Initialize Pygame
    pygame.init()

    save_loc(4)

    # Get screen dimensions for dynamic window size
    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w  # Get the current screen width
    screen_height = screen_info.current_h  # Get the current screen height

    # Set the window to fullscreen mode
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Load background image for the hanger (scale it to the required size)
    bridge = pygame.image.load('bridge_imagie.png')
    bridge = pygame.transform.scale(bridge, (877, 620))

    invotory_spots = [200,300,400]
    invotory_player_spots = [200,300,400]
    # Initialize room_item dictionary to hold items in the room
    room_item = {}
    # Initialize the inventory dictionary (items the player has)
    invotory = {}

    room_items_images={}
    invotory_images={}

    # Load saved room items and inventory items from files
    room_item = room_item_load("bridge_items")  # Load saved room items from file
    invotory = invotary_load()  # Load saved inventory items from file
    invotory_spots = invotory_spots_load()

    # Initial player position and spaceship position
    player_poss = [1070, 510]  # Player's initial position
   
    new_x = player_poss[0]  # Initialize new x position
    new_y = player_poss[1]  # Initialize new y position
    run = True  # Game loop 
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
        # Draw the player in background (representing the player as a rectangle)
        player = pygame.draw.rect(screen, (190, 70, 70), pygame.Rect(player_poss[0]+25, player_poss[1], 50, 150))
        current_time = time.time()

        wait_for_invotory_spot, new_x, new_y, invotory_player_spots_spot = moving_in_big_ship(current_time, wait_for_invotory_spot, new_x, new_y,
                                                                                               invotory_player_spots_spot, True)

        way_to_corridor = pygame.draw.rect(screen, (70, 70, 170), pygame.Rect(1175, 350, 50, 200))
        # Fill the screen with black before drawing objects
        screen.fill((0, 0, 0))

        # Calculate the center positions for the hanger image
        middle_1 = (screen_width - 577) / 2
        middle_2 = (screen_height - 620) / 2

        # Restrict player movement to prevent going off-screen
        if middle_1 + 720 >= new_x - 50 / 2 and new_x + 50 / 2 >= middle_1 + 80:
            player_poss[0] = new_x  # Update x position if within bounds
        else:
            new_x = player_poss[0]
        if middle_2<= new_y - 50 / 2 and new_y + 50 / 2 <= middle_2 + 400:
            player_poss[1] = new_y  # Update y position if within bounds
        else:
            new_y = player_poss[1]

        pygame.draw.rect(screen, (70, 70, 70), pygame.Rect(0, 0, 250, screen_height))

        

        # Blit the hanger image (background) onto the screen
        screen.blit(bridge, (middle_1, middle_2))

        invotory_player = pygame.draw.rect(screen, (10, 70, 70), pygame.Rect(25, invotory_player_spots[invotory_player_spots_spot]-75, 100, 100))
        # Draw all items in the inventory

        room_item, invotory, invotory_spots,  invotory_player, nothing, potato_time = invotory_to_map(room_item, invotory, invotory_player_spots, invotory_spots,
                                                                                 invotory_player_spots_spot, player_poss,
                                                                                   invotory_player, invotory_images, screen,False, False, current_time, potato_time)

        
        invotory, room_item, invotory_spots, pick_up = room_to_invotory(room_item, invotory, invotory_spots, screen, room_items_images,player,player_poss)

        # Save the updated room items and inventory
        room_item_save(room_item, "bridge_items")
        save_invotary(invotory)
        invotory_spots_save(invotory_spots)
        
        # Draw the player again but for user
        idle_stat,walk_stat, walk_time, flip, frame = walk_imagie(player_poss, screen ,current_time, walk_time, flip, frame, idle_stat, walk_stat)

        if pick_up == True:
            draw_text(screen, Text_choice(0,8), (255,255,255), player_poss[0]  ,player_poss[1]-50) 
        

        if player.colliderect(way_to_corridor):
            next = 1
            run = False 
        
        


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
        corridor()  