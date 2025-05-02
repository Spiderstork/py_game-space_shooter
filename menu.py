# ahhhhhhhhhhhhh what have i done DEAR GOD SAVES US ALL HOW AM I GONNA DO
def menu():
    import pygame
    from add_text import draw_text , middle
    import time
    from big_space_ship_hanger import hanger # type: ignore
    from game_ship_fight import game_ship_run  # type: ignore
    from save import load_loc
    from new_game_start_up import new_game # type: ignore
    from corridor_part import corridor # type: ignore
    from bridge_code import bridge # type: ignore
    from text_language import Text_choice # type: ignore
    from contols import controls # type: ignore
    # Initialize Pygame
    pygame.init()

    # Load music
    try:
        pygame.mixer.init()
        pygame.mixer.music.load('western music.mp3')  # Replace with your music file path
        # Play the music
        pygame.mixer.music.play()
    except:
        pass

    logo = pygame.image.load("logo.png")  # Load bad_guy image from file
    logo = pygame.transform.scale(logo , (230, 240))  # Resize bad_guy image to fit

    # Get screen dimensions for dynamic window size
    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w  # Get the current screen width
    screen_height = screen_info.current_h  # Get the current screen height

    # Set the window to fullscreen mode
    screen = pygame.display.set_mode((screen_width, screen_height))

    option = [1.422, 1.3, 1.2, 1.1]
    option_list_decider = 0
    spot = screen_height / option[option_list_decider]
    hold = 0
    run = True
    while run:
        current_time = time.time()
        key = pygame.key.get_pressed()
        if (key[pygame.K_DOWN] or key[pygame.K_s])and current_time-hold>0.2 and option_list_decider<3:
            option_list_decider  += 1  
            hold=current_time

        if (key[pygame.K_UP] or key[pygame.K_w]) and current_time-hold>0.2 and option_list_decider > 0:
            option_list_decider -= 1
            hold=current_time

        if key[pygame.K_RETURN] and current_time-hold>0.2 :     
            if option_list_decider == 0 :
                start_screen = int(load_loc())
                next = start_screen
                run = False
            
            if option_list_decider == 1 :
                new_game()
                start_screen = int(load_loc())
                next = start_screen
                run = False

            if option_list_decider == 2 :
                next = 5
                run = False

            if option_list_decider == 3 :
                next = 0
                run = False

        screen.fill((140, 140, 140))

        text_200="A"
        for n in range(9):
            text_200+="A"
        spot = screen_height / option[option_list_decider]
        center = middle(text_200,screen_width)
        
        pygame.draw.rect(screen, (187, 214, 235 ), pygame.Rect(center , spot, 190,50))
        
        center = middle(Text_choice(0,0),screen_width)
        draw_text(screen, Text_choice(0,0), (255,255,255), center  , screen_height//10)   
    
        center = middle(Text_choice(0,1),screen_width)
        draw_text(screen, Text_choice(0,1), (255,255,255), center , screen_height/1.4)  

        center = middle(Text_choice(0,2),screen_width)
        draw_text(screen, Text_choice(0,2), (255,255,255), center , screen_height/1.3)   

        center = middle(Text_choice(0,3),screen_width)
        draw_text(screen, Text_choice(0,3), (255,255,255), center  , screen_height/1.2)

        center = middle(Text_choice(0,4),screen_width)
        draw_text(screen, Text_choice(0,4),(255,255,255), center, screen_height/1.1 )
        
        middle_1= (screen_width - 230)//2
        middle_2 = (screen_height - 240) // 2
        screen.blit(logo, (middle_1 + 5, middle_2))

        # --- Handle Events ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                next = 0
                run = False  # Exit the game loop if the window is closed

        # Update the display
        pygame.display.update()

    if next == 0:
        pygame.quit()

    if next == 1:
        game_ship_run()
    
    if next == 2:
        hanger()
    
    if next == 3:
        corridor()

    if next == 4:
        bridge()

    if next == 5:
        controls()

    