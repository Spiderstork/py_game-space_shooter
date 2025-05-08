def game_ship_run():
    import pygame
    import pygame.image
    import math
    from game_funtions import speed_keys, angle_keys, screen_check,bullet_coretion ,ai_movement,output_bars , bad_guy_maker , bad_guy_bullet_creation
    from add_text import draw_text
    from save import save , load , save_loc ,load_bad_guy, save_bad_guy
    from menu import menu
    from big_space_ship_hanger import hanger #type: ignore
    from text_language import Text_choice # type: ignore
    import time


    # Initialize Pygame
    pygame.init()

    save_loc(1)

    # Load music
    try:
        pygame.mixer.init()
        pygame.mixer.music.load('western music.mp3')
        # Play the music
        pygame.mixer.music.play()
    except:
        pass

    # Get screen dimensions for dynamic window size
    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w  # Get the current screen width
    screen_height = screen_info.current_h  # Get the current screen height

    # Set the window to fullscreen mode
    screen = pygame.display.set_mode((screen_width, screen_height))

    # --- Player Setup ---
    # Load the player image
    player_image = pygame.image.load('space_imagie.png')  # Load player image from file
    player_image = pygame.transform.scale(player_image, (50, 50))  # Resize player image to fit
    original_player_image = player_image  # Store the original image for future rotations

    big_ship_image = pygame.image.load('the_big_ship.png')  # Load player image from file
    big_ship_image = pygame.transform.scale( big_ship_image, (906, 500))  # Resize player image to fit

    # Set initial player position (center of the screen)
    player_pos = [screen_width // 2, screen_height // 1.5]

    # --- bad_guy Setup ---
    # Load the bad_guy image
    bad_guy_image = pygame.image.load('bad_guy_space__ship.png')  # Load bad_guy image from file
    bad_guy_image = pygame.transform.scale(bad_guy_image , (30, 40))  # Resize bad_guy image to fit
    original_bad_guy_image = bad_guy_image # Store the original image for future rotations
    # Set initial bad_guy position (center of the screen)

    # --- Player Speed and Rotation ---
    speed = 0  # Initial speed value (no movement)
    angle = -90  # Initial rotation angle (facing upwards)

    #
    #   --- sets up speeds and user ships specs if never played before ---
    #

    bullet_refill_interval = 2 # seconds between bullet refills


    player_ship = {}
    bad_guy_ship={}

    player_ship = load(player_ship)
    bad_guy_ship = load_bad_guy(bad_guy_ship)
    
    

    # --- bullet Setup ---
    # Initial size and color for the bullet
    y_bullet_size = 1
    bullet_color = (0, 0, 255)  # Red color
    bullets={}

    y_speed_size = 1

    player_bar_postions={
        "health_pos":[0, 120], # Position at the bottom left
        "fuel_pos" : [10, screen_height],
        "bullet_amount_pos" : [0, 60],
        "speed_pos" : [100, screen_height]

    }
    player_bar_color={
        "health_color":(0, 255, 0),
        "fuel_color" : (0, 255, 0) ,
        "bullet_amount_color" : (0, 0, 255),
        "speed_color" : (255, 0, 0) 
    }

    # --- bad_bullet Setup ---
    # Initial size and color for the bullet
   
    bad_bullet_color = (255, 0, 0)  # Red color
    bad_bullets={}

    delete=[]
    # --- FPS Clock ---
    clock = pygame.time.Clock()

    # Game loop flag
    run = True
    num=0
    last_time=0
    bullet_time = 0
    bad_time=0
    delete_bad_guy=[]
    delete_bullet=[]
    bad_guy_make_time=0
    bad_guy_ship__num=1
    time.sleep(0.5)
    # Main game loop
    while run:
            key = pygame.key.get_pressed()
            if key[pygame.K_p]:
                # --- bad_guy Setup ---
                # Load the bad_guy image
                bad_guy_image = pygame.image.load('doge.png')  # Load bad_guy image from file
                bad_guy_image = pygame.transform.scale(bad_guy_image , (30, 40))  # Resize bad_guy image to fit
                original_bad_guy_image = bad_guy_image # Store the original image for future rotations
                # Set initial bad_guy position (center of the screen)
            current_time = time.time()
            bad_guy_make_time , bad_guy_ship__num , bad_guy_ship  = bad_guy_maker(bad_guy_ship,current_time, bad_guy_make_time,
                                                                                  screen_height, screen_width, bad_guy_ship__num)

            # --- Handle Key Inputs ---
            # Update speed and speed meter size based on key inputs
            speed, y_speed_size = speed_keys(speed, y_speed_size,player_ship)

            # Update rotation angle based on key inputs
            if  player_ship["fuel"]>0:
                angle= angle_keys(angle)

            num , last_time= bullet_coretion(angle,bullets,player_pos,num,speed,current_time,last_time,player_ship)

            # --- Calculate Movement ---
            # Calculate vertical and horizontal movement (dx, dy) based on angle and speed
            dy = math.cos(math.radians(angle)) * speed  # Vertical movement
            dx = math.sin(math.radians(angle)) * speed  # Horizontal movement

            # Calculate the potential new position for the player
            new_x = player_pos[0] + dx
            new_y = player_pos[1] + dy

            # --- Rotate Player Image ---
            # Rotate the player image based on the current angle
            rotated_image = pygame.transform.rotate(original_player_image, angle)
            rotated_width = rotated_image.get_width()  # Get the width of the rotated image
            rotated_height = rotated_image.get_height()  # Get the height of the rotated image

            bad_guy_ship = ai_movement( player_pos, original_bad_guy_image, bad_guy_ship,current_time)

            bad_bullets, num, bad_time = bad_guy_bullet_creation(bad_guy_ship, current_time, bad_time,bad_bullets,num)

            # --- Check Player Position ---
            # Ensure the player doesn't move off the screen
            screen_check(new_x, new_y, rotated_height, rotated_width, screen_width, screen_height, player_pos)

            # Get the rectangle for the rotated player image and center it at the player's position
            rotated_rect = rotated_image.get_rect(center=(player_pos[0], player_pos[1]))

            # --- Rendering ---
            # Fill the screen with a black background
            screen.fill((0, 0, 0))

            the_big_one = screen.blit(big_ship_image, ((screen_width-906+250)//2,(screen_height-500)//2))

            if current_time - bullet_time > bullet_refill_interval and player_ship["bulets"]<110:
                player_ship["bulets"] += 10
                bullet_time = current_time  # Reset the bullet refill timer to the current time

            for d in bullets:
                # d = key
                # 0 = bullet postion
                # 1 and 0 are  x and y pos
                bullets[d][0][1]-=bullets[d][2]
                bullets[d][0][0]-=bullets[d][1]
                shoot_shoot_thing=pygame.draw.circle(screen, bullet_color, (bullets[d][0][0], bullets[d][0][1]), 5)

                #   check if player bullets have hit bad guys
                for ship in bad_guy_ship:
                    bad_guy_ship[ship]["rotated_bad_rect"]
                    if shoot_shoot_thing.colliderect(bad_guy_ship[ship]["rotated_bad_rect"]):
                        bad_guy_ship[ship]["health"]-=10
                        if d in delete_bullet:
                            pass
                        else:
                            delete_bullet.append(d) # stores the bullet to be delleted

            # delete bullets what have hit bad guys
            for bull in delete_bullet:
                del bullets[bull]
            delete_bullet=[]

            #   check if any bad guy have 0 health
            for ship in bad_guy_ship:
                if bad_guy_ship[ship]["health"]<=0:
                    delete_bad_guy.append(ship) # stores to be deleted


            #   dellets bad guys
            for ship in delete_bad_guy:
                del bad_guy_ship[ship]
            delete_bad_guy=[]

            if player_ship["health"] > 0:
                for d in bad_bullets:
                    # d = key
                    # 0 = bullets pos of enemy
                    # 1 and 0 are  y and x
                    bad_bullets[d][0][1]-=bad_bullets[d][2]
                    bad_bullets[d][0][0]-=bad_bullets[d][1]
                    bull = pygame.draw.circle(screen, bad_bullet_color, (bad_bullets[d][0][0], bad_bullets[d][0][1]), 5)

                    #   check if player bullets have hit bad guys
                    if bull.colliderect(rotated_rect):
                        player_ship["health"]-=5
                        delete_bullet.append(d) # stores the bullet to be delleted

            # dellet bullets what have are no longer needed
            for bull in delete_bullet:
                del bad_bullets[bull]
            delete_bullet=[]

            if player_ship["health"] > 0:
                # Draw the rotated player image at the calculated position
                screen.blit(rotated_image, rotated_rect.topleft)
                for ship in bad_guy_ship:
                    screen.blit(bad_guy_ship[ship]["rotated_bad_image"], bad_guy_ship[ship]["rotated_bad_rect"].topleft)


            # --- Handle Events ---
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:  # If a key is pressed
                    if event.key == pygame.K_ESCAPE:  # Check if it's the Escape key

                        if player_ship["health"] <=5 or player_ship["fuel"]  <= 5:
                            run = False
                            next = 1

                        else:
                            save(player_ship)
                            save_bad_guy(bad_guy_ship)
                            run = False
                            next = 1


            output_bars(player_ship, bad_guy_ship, screen , player_bar_postions,player_bar_color, y_speed_size, screen_height)


            #   check if any player have 0 health
            if player_ship["health"]<=0:
                bad_guy_ship={}
                bad_guy_ship__num=1
                bad_bullets={}
                draw_text(screen, Text_choice(0,5), (255,255,255), screen_width/2 , screen_height/2)
                draw_text(screen, Text_choice(0,6), (255,255,255), screen_width/2.205 , screen_height/1.85)

                key = pygame.key.get_pressed()
                if key[pygame.K_RETURN]:
                    player_ship = load(player_ship)
                    bad_guy_ship = load_bad_guy(bad_guy_ship)

            key = pygame.key.get_pressed()
            if key[pygame.K_RETURN] and the_big_one.colliderect(rotated_rect) and player_ship["health"]>0:
                save(player_ship)
                save_bad_guy(bad_guy_ship)
                next = 2
                run = False  # Exit the game loop if the window is closed

            # --- Update the Display ---
            pygame.display.flip()  # Update the screen with the new content

            # --- Frame Rate Control ---
            clock.tick(60)  # Maintain a frame rate of 60 frames per second

    if next == 1:
        menu()
    elif next == 2:
        hanger()
