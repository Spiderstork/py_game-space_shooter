import pygame
def moving_in_big_ship(current_time, wait_for_invotory_spot, new_x, new_y, invotory_player_spots_spot, check):
    key = pygame.key.get_pressed()  # Get keys pressed

    speed_player =  3  # Player movement speed


    # Player controls for movement (WASD keys)
    if check == True:
        if key[pygame.K_w]:
            new_y -= speed_player
        if key[pygame.K_s]:
            new_y += speed_player
    if key[pygame.K_d]:
        new_x += speed_player
    if key[pygame.K_a]:
        new_x -= speed_player
    


    # Player controls for movement (WASD keys)
    if key[pygame.K_UP] and invotory_player_spots_spot>0 and current_time - wait_for_invotory_spot > 0.2:
        invotory_player_spots_spot -=1
        wait_for_invotory_spot=current_time
    if key[pygame.K_DOWN] and invotory_player_spots_spot<2 and current_time - wait_for_invotory_spot > 0.2:
        invotory_player_spots_spot +=1
        wait_for_invotory_spot=current_time

    return wait_for_invotory_spot, new_x, new_y, invotory_player_spots_spot