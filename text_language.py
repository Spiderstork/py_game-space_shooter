def Text_choice(language,choice):
    languages = [
        ["__INTERGALATIC_SPACE_DELIVERY__","CONTINUE","NEW GAME","CONTROLS","QUIT","YOU DIED","ENTER TO RESTART","ENTER","E","G = Drop","F = Fix","F = Fuel"]
        ]
    
    return languages[language][choice]
    
def Text_choice_controls(language,choice):
    languages = [
        ["PLAYER","W = UP","S = DOWN","D = RIGHT","A = LEFT","E = PICK UP","G = DROP","F = USE","G = Drop","Up arrow = ivotory up","Down arrow = ivotory down"
         ,"SPACE_SHIP","W = Increase speed","S = Decrease speed", "D = Turn Right", "A = Turn Left","space = Shoot"]
         
        ]
    
    return languages[language][choice]
    