import pygame

def walk_imagie(player_pos, screen ,current_time, walk_time, flip, frame, idle_stat, walk_stat):
    walk = ['walk - 0.png', 'walk - 1.png', 'walk - 2.png', 'walk - 3.png', 'walk - 4.png', 'walk - 5.png']
    idle = ["idle - 0.png", "idle - 1.png", "idle - 2.png", "idle - 3.png", "idle - 4.png", "idle - 5.png",
             "idle - 6.png", "idle - 7.png"]

    key = pygame.key.get_pressed()  
    
    if key[pygame.K_d] or key[pygame.K_a] or key[pygame.K_w] or key[pygame.K_s]:
        screen.blit(walk_stat,(player_pos[0],player_pos[1]))

        if current_time-walk_time > 0.1:
            walk_time = current_time
            frame+=1
            if frame >= 6:
                frame=0
            walk_stat = pygame.transform.scale(pygame.image.load(walk[frame]), (100, 120))
            if flip == True:
                walk_stat = pygame.transform.flip(walk_stat,True,False)

    else:
        screen.blit(idle_stat,(player_pos[0],player_pos[1]))
        if current_time-walk_time > 0.1:
            walk_time = current_time
            frame+=1
            if frame == 7:
                frame=0
            idle_stat = pygame.transform.scale(pygame.image.load(idle[frame]), (100, 120))
            if flip == True:
                idle_stat = pygame.transform.flip(idle_stat,True,False)
    if  key[pygame.K_a]:
        flip = True
    if  key[pygame.K_d]:
        flip = False

    return idle_stat,walk_stat, walk_time, flip, frame