def controls():
    import pygame
    from add_text import draw_text , middle
    from text_language import Text_choice_controls # type: ignore
    from menu import menu
    import time
    # Initialize Pygame
    pygame.init()

    # Get screen dimensions for dynamic window size
    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w  # Get the current screen width
    screen_height = screen_info.current_h  # Get the current screen height
    # Set the window to fullscreen mode
    screen = pygame.display.set_mode((screen_width, screen_height))
    time.sleep(0.5)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  # If a key is pressed
                next = 0
                run = False
        screen.fill((140, 140, 140))

        center = middle(Text_choice_controls(0,0),screen_width)
        draw_text(screen, Text_choice_controls(0,0), (255,255,255), center/2  , screen_height//10)

        center = middle(Text_choice_controls(0,11),screen_width)
        draw_text(screen, Text_choice_controls(0,11), (255,255,255), center*1.5  , screen_height//10)


        center = middle(Text_choice_controls(0,5),screen_width)

        spot = 550
        for n in range(11):
            if n == 0:
                continue
            else:
                draw_text(screen, Text_choice_controls(0,n), (255,255,255), center/2 , (screen_height/1) - spot )  
                spot-=50

        spot = 550  
        for n in range(17):
            if n<12:
                continue
            else:
                draw_text(screen, Text_choice_controls(0,n), (255,255,255), center*1.5 , (screen_height/1) - spot )  
                spot-=50

        # Update the display
        pygame.display.update()

    if next == 0:
        time.sleep(0.5)
        menu()
