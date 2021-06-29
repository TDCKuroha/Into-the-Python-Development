
answer = input (f"\nWould you like to play the game? (Yes / No) : ")

if answer.lower() .strip() == "yes":

    answer = input (f"\nYou open your eyes, you cannot see anything because some" 
    f"lights point towards your face, then you realize \nthat you are tied up on a" 
    f"stretcher and there is someone who seems to be a doctor in front of you and then you ask...\n"
    f"\nWho you are? (A) / Where I am? (B) : ")

    if answer.lower() .strip() == "a":

        answer = input (f"\nYour savior! says the doctor.\n \nSo you say : I think I'm going to need a better explanation...\n"
        f"\nFine. You are just a test subject, you had an accident yesterday and by science you are alive " 
        f"again, \nbut unfortunately, I could not bring you back without collateral damage. After hearing this you ask : \n"
        f"\nHow did I die? (A) / What collateral damage are you talking about? (B) : ")

        if answer.lower() .strip() == "a":
            
            answer = input (f"\nI think it is not a very relevant question, but if you insist I can tell you : " 
            f"\nWhat is the last thing you remember before waking up here?\n"
            f"\nI don't remember anything. (A) / I remember having some candy at that party. (B) : ")

            if answer.lower() .strip() == "a": 

                answer = input (f'\nYou died in a very authentic way, according to the autopsy I performed on you, it was due to poisoning. '
                f'\nBut that is not the important thing, the important thing is that ... Unfortunately, '
                f'\nI could not bring you to life without endowing you with "certain skills" \n'
                f'\nWhat do you mean by "certain abilities" (A) / You mean I will have super powers? (B) : ')

                if answer.lower() .strip() == "a":  

                    answer = input (f"\nSuperhuman abilities, super powers whatever you want to call it today. \n"
                    f"\nI will have superpowers now! (A) / But why would having superpowers be collateral damage? (B) : ")

                    if answer.lower() .strip() == "a":

                        answer = input (f"\nSuperpowers seem cool to me. NICE!... PRESS ENTER. ")

                        answer = input (f'\nYou will be practically a superman, you will have super powers or' 
                            f'\nwhatever you call it, you will have super strength, improved speed, improved vision, '
                            f'\nyou have everything that we humans can wish for, you are what we would call a superior '
                            f'\nbeing or you would be like a "GOD" or so some would say but The only thing you cannot do is fly. \nDo you want this powers? \n'
                            f'\nACCEPT POWERS (OK) / I don not want to live with those powers. (NO) : ')

                        if answer.lower() .strip() == "ok":

                            answer = input (f"\nSounds good to me, I'll accept these powers! I think it will be something incredible. "
                                f"\nThe professor begins the phase of administration of doses of serum to prototype 0043 while doing it, screams "
                                f"\nof agonizing pain are heard, for some 10 minutes but after administering the serum, the doctor quickly puts "
                                f"\na metal collar on you and tells you that now You are going to use your life time for the good and you will be "
                                f"\na hereo of the city and that you will help him to end all possible crime during this year. \n"
                                f"\nYour plan works fine but I don't think this necklace was necessary, I was going to help you anyway. (HELP) / "
                                f"I won't be your slave, I didn't come back to life to be what you want. (ANGER) : ")

                            if answer.lower() .strip() == "help":

                                answer = input (f"\nYour plan is going well but I don't think this necklace was necessary, it was going to help you anyway. "
                                     f"\nOkay, I put the collar on you as a safety measure, when I trust you I'll take it off. Do you want to start your training? \n"
                                     f"\nYes. Let's do it (A) / No. I'll learn on my own (B) : ")

                                if answer.lower() .strip() == "a":

                                    answer = input (f"\nPerfect we are going to teach you the basics to use your powers, your training will start now. \n"
                                        f"\nTO BE CONTINUE... \n")
                                        
                                    print ("\nCLICK ENTER TO END THE GAME")

                                    input()

                                elif answer.lower() .strip() == "b":

                                    answer = input (f"\nAll right, if you need any help just ask me, I know you can master your skills quickly. \n"
                                        f"\nTO BE CONTINUE... \n")

                                    print ("\nCLICK ENTER TO END THE GAME")

                                    input()

                            elif answer.lower() .strip() == "anger":

                                answer = input (f"\nI will not be a slave of yours, I did not come back to life to be what you want. "
                                    f"\nI'm afraid this will stop! The teacher seeing your answer presses a button which activates the necklace, "
                                    f"\nit begins to electrocute you and make you wallow in pain. \n"
                                    f"\nTry to break the necklace (BREAK) / Attack the doctor (ATTACK) : ")

                                if answer.lower() .strip() == "break":

                                    answer = input (f'\nWith your superhuman strength it was more '
                                        f'\nthan easy to break the necklace and stop the electric shock. '
                                        f'\nWhen the teacher sees this he only says one word "damn it". '
                                        f'\nAttack the teacher (ATTACK) / Escape from the place (RUN) : ')

                                    if answer.lower() .strip() == "attack":

                                        answer = input (f"\nAfter attacking the professor and killing him, you realized what you had done and you "
                                            f"\nregret what makes you realize how dangerous you are, which will lead you to spend the time of your life "
                                            f"\nthat you have left on an island surrounded only by silver, animals and the immense sea while time passes while "
                                            f"\nyour life slowly comes to the end. \n")
                                            
                                        print ("")
                                        print ("*YOU WON* CLICK ENTER TO END THE GAME *YOU WON*")
                                        input()
                                            
                                    elif answer.lower() .strip() == "run":

                                        answer = input (f"\nWith the little time to live you had and with your superpowers, "
                                            f"\nyou decided to conquer humanity and enjoy everything before you perish. \n")

                                        print ("")
                                        print ("*YOU WON* CLICK ENTER TO END THE GAME *YOU WON*")
                                        input()

                                    else:

                                        print("Invalid choice, try again.")
                                        input()

                                elif answer.lower() .strip() == "attack":

                                    answer = input (f"\nWhile you were trying to attack the teacher, the electric shock was "
                                        f"\naffecting your internal organs which caused your death. GAME OVER \n")

                                    print ("CLICK ENTER TO END THE GAME. You Lose :( ")
                                    input()

                                else:

                                    print("Invalid choice, try again.")

                            else:

                                    print("Invalid choice, try again.")

                        elif answer.lower() .strip() == "no":

                                answer = input (f"\nI couldn't live that way, I don't want that, I can rather rest in peace. "
                                f"\nIf that's what you want, that's fine, you've made your decision! "
                                f"\n(The doctor operated on you so that you do not have the powers, therefore, you died. GAME OVER) \n")

                                print ("CLICK ENTER TO END THE GAME. You died. GAME OVER ")
                                input()

                        else:

                                print("Invalid choice, try again.")


                    elif answer.lower() .strip() == "b":

                        answer = input (f"\nBecause even if you have certain skills, I can bring you " 
                        f"\nback to life, but since you are only a prototype, "
                        f"\nyou will only live for 1 year at most. But tell me about the abilities, \n"
                        f"\nWhat powers do I have? (A) / That I will only have 1 year to live, but not solve that? (B) : ")

                        if answer.lower() .strip() == "a":

                            answer = input (f'\nYou will be practically a superman, you will have super powers or' 
                            f'\nwhatever you call it, you will have super strength, improved speed, improved vision, '
                            f'\nyou have everything that we humans can wish for, you are what we would call a superior '
                            f'\nbeing or you would be like a "GOD" or so some would say but The only thing you cannot do is fly. \nDo you want this powers? \n'
                            f'\nACCEPT POWERS (OK) / I don not want to live with those powers. (NO) : ')

                            if answer.lower() .strip() == "ok":

                                answer = input (f"\nSounds good to me, I'll accept these powers! I think it will be something incredible. "
                                f"\nThe professor begins the phase of administration of doses of serum to prototype 0043 while doing it, screams "
                                f"\nof agonizing pain are heard, for some 10 minutes but after administering the serum, the doctor quickly puts "
                                f"\na metal collar on you and tells you that now You are going to use your life time for the good and you will be "
                                f"\na hereo of the city and that you will help him to end all possible crime during this year. \n"
                                f"\nYour plan works fine but I don't think this necklace was necessary, I was going to help you anyway. (HELP) / "
                                f"\nI won't be your slave, I didn't come back to life to be what you want. (ANGER) : ")

                                if answer.lower() .strip() == "help":

                                    answer = input (f"\nYour plan is going well but I don't think this necklace was necessary, it was going to help you anyway. "
                                     f"\nOkay, I put the collar on you as a safety measure, when I trust you I'll take it off. Do you want to start your training? \n"
                                     f"\nYes. Let's do it (A) / No. I'll learn on my own (B) : ")

                                    if answer.lower() .strip() == "a":

                                        answer = input (f"\nPerfect we are going to teach you the basics to use your powers, your training will start now. \n"
                                        f"\nTO BE CONTINUE...")
                                        
                                        print ("CLICK ENTER TO END THE GAME")

                                        input()

                                    elif answer.lower() .strip() == "b":

                                        answer = input (f"\nAll right, if you need any help just ask me, I know you can master your skills quickly. \n"
                                        f"\nTO BE CONTINUE...")

                                        print ("CLICK ENTER TO END THE GAME")

                                        input()

                                elif answer.lower() .strip() == "anger":

                                    answer = input (f"\nI will not be a slave of yours, I did not come back to life to be what you want. "
                                    f"\nI'm afraid this will stop! The teacher seeing your answer presses a button which activates the necklace, "
                                    f"\nit begins to electrocute you and make you wallow in pain. \n"
                                    f"\nTry to break the necklace (BREAK) / Attack the doctor (ATTACK) : ")

                                    if answer.lower() .strip() == "break":

                                        answer = input (f'\nWith your superhuman strength it was more '
                                        f'\nthan easy to break the necklace and stop the electric shock. '
                                        f'\nWhen the teacher sees this he only says one word "damn it". '
                                        f'\nAttack the teacher (ATTACK) / Escape from the place (RUN) : ')

                                        if answer.lower() .strip() == "attack":

                                            answer = input (f"\nAfter attacking the professor and killing him, you realized what you had done and you "
                                            f"\nregret what makes you realize how dangerous you are, which will lead you to spend the time of your life "
                                            f"\nthat you have left on an island surrounded only by silver, animals and the immense sea while time passes while "
                                            f"\nyour life slowly comes to the end. \n")
                                            
                                            print ("")
                                            print ("*YOU WON* CLICK ENTER TO END THE GAME *YOU WON*")
                                            input()
                                            
                                        elif answer.lower() .strip() == "run":

                                            answer = input (f"\nWith the little time to live you had and with your superpowers, "
                                            f"\nyou decided to conquer humanity and enjoy everything before you perish. \n")

                                            print ("")
                                            print ("*YOU WON* CLICK ENTER TO END THE GAME *YOU WON*")
                                            input()

                                        else:

                                            print("Invalid choice, try again.")
                                            input()

                                    elif answer.lower() .strip() == "attack":

                                        answer = input (f"\nWhile you were trying to attack the teacher, the electric shock was "
                                        f"\naffecting your internal organs which caused your death. GAME OVER \n")

                                        print ("CLICK ENTER TO END THE GAME. You Lose :( ")
                                        input()

                                    else:

                                        print("Invalid choice, try again.")

                                else:

                                    print("Invalid choice, try again.")

                            elif answer.lower() .strip() == "no":

                                answer = input (f"\nI couldn't live that way, I don't want that, I can rather rest in peace. "
                                f"\nIf that's what you want, that's fine, you've made your decision! "
                                f"\n(The doctor operated on you so that you do not have the powers, therefore, you died. GAME OVER) \n")

                                print ("CLICK ENTER TO END THE GAME. You died. GAME OVER ")
                                input()

                            else:

                                print("Invalid choice, try again.")

                        elif answer.lower() .strip() == "b": 

                            answer = input (f"\nYes, but I will not force you to anything anyway, you can get the "
                            f"\nsuperpowers or go back to doing the cold cavader that you were \n"
                            f"\nYes, I want the powers! (A) / No. I could not live that way. (B) : ")

                            if answer.lower() .strip() == "a": 

                                answer = input (f"\nSounds good to me, I'll accept these powers! I think it will be something incredible. "
                                f"\nThe professor begins the phase of administration of doses of serum to prototype 0043 while doing it, screams "
                                f"\nof agonizing pain are heard, for some 10 minutes but after administering the serum, the doctor quickly puts "
                                f"\na metal collar on you and tells you that now You are going to use your life time for the good and you will be "
                                f"\na hero of the city and that you will help him to end all possible crime during this year. \n"
                                f"\n(Your plan works fine but I don't think this necklace was necessary, I was going to help you anyway. (HELP) " 
                                f"\nI won't be your slave, I didn't come back to life to be what you want. (ANGER) : ") 

                            elif answer.lower() .strip() == "b":

                                answer = input (f"\nI couldn't live that way, I don't want that, I can rather rest in peace. "
                                f"\nIf that's what you want, that's fine, you've made your decision! \n"
                                f"\n(The doctor operated on you so that you do not have the powers, therefore, you died. GAME OVER)")

                                print ("\nCLICK ENTER TO END THE GAME")

                        else:

                            print("Invalid choice, try again.")

                    else: 

                        print("Invalid choice, try again.")

                elif answer.lower() .strip() == "b":

                    answer = input (f"\nSuperhuman abilities, super powers whatever you want to call it today. \n"
                    f"\nGreat, I will have superpowers now! (A) / But why would having superpowers be collateral damage? (B) : ")

                    if answer.lower() .strip() == "a":

                        answer = input (f"\nSuperpowers seem cool to me. NICE!... PRESS ENTER. ")

                        answer = input (f'\nYou will be practically a superman, you will have super powers or' 
                            f'\nwhatever you call it, you will have super strength, improved speed, improved vision, '
                            f'\nyou have everything that we humans can wish for, you are what we would call a superior '
                            f'\nbeing or you would be like a "GOD" or so some would say but The only thing you cannot do is fly. \nDo you want this powers? \n'
                            f'\nACCEPT POWERS (OK) / I don not want to live with those powers. (NO) : ')

                        if answer.lower() .strip() == "ok":

                            answer = input (f"\nSounds good to me, I'll accept these powers! I think it will be something incredible. "
                                f"\nThe professor begins the phase of administration of doses of serum to prototype 0043 while doing it, screams "
                                f"\nof agonizing pain are heard, for some 10 minutes but after administering the serum, the doctor quickly puts "
                                f"\na metal collar on you and tells you that now You are going to use your life time for the good and you will be "
                                f"\na hereo of the city and that you will help him to end all possible crime during this year. \n"
                                f"\nYour plan works fine but I don't think this necklace was necessary, I was going to help you anyway. (HELP) / "
                                f"I won't be your slave, I didn't come back to life to be what you want. (ANGER) : ")

                            if answer.lower() .strip() == "help":

                                answer = input (f"\nYour plan is going well but I don't think this necklace was necessary, it was going to help you anyway. "
                                     f"\nOkay, I put the collar on you as a safety measure, when I trust you I'll take it off. Do you want to start your training? \n"
                                     f"\nYes. Let's do it (A) / No. I'll learn on my own (B) : ")

                                if answer.lower() .strip() == "a":

                                    answer = input (f"\nPerfect we are going to teach you the basics to use your powers, your training will start now. \n"
                                        f"\nTO BE CONTINUE...")
                                        
                                    print ("\nCLICK ENTER TO END THE GAME")

                                    input()

                                elif answer.lower() .strip() == "b":

                                    answer = input (f"\nAll right, if you need any help just ask me, I know you can master your skills quickly. \n"
                                        f"\nTO BE CONTINUE...")

                                    print ("\nCLICK ENTER TO END THE GAME")

                                    input()

                            elif answer.lower() .strip() == "anger":

                                answer = input (f"\nI will not be a slave of yours, I did not come back to life to be what you want. "
                                    f"\nI'm afraid this will stop! The teacher seeing your answer presses a button which activates the necklace, "
                                    f"\nit begins to electrocute you and make you wallow in pain. \n"
                                    f"\nTry to break the necklace (BREAK) / Attack the doctor (ATTACK) : ")

                                if answer.lower() .strip() == "break":

                                    answer = input (f'\nWith your superhuman strength it was more '
                                        f'\nthan easy to break the necklace and stop the electric shock. '
                                        f'\nWhen the teacher sees this he only says one word "damn it". '
                                        f'\nAttack the teacher (ATTACK) / Escape from the place (RUN) : ')

                                    if answer.lower() .strip() == "attack":

                                        answer = input (f"\nAfter attacking the professor and killing him, you realized what you had done and you "
                                            f"\nregret what makes you realize how dangerous you are, which will lead you to spend the time of your life "
                                            f"\nthat you have left on an island surrounded only by silver, animals and the immense sea while time passes while "
                                            f"\nyour life slowly comes to the end. \n")
                                            
                                        print ("")
                                        print ("*YOU WON* CLICK ENTER TO END THE GAME *YOU WON*")
                                        input()
                                            
                                    elif answer.lower() .strip() == "run":

                                        answer = input (f"\nWith the little time to live you had and with your superpowers, "
                                            f"\nyou decided to conquer humanity and enjoy everything before you perish. \n")

                                        print ("")
                                        print ("*YOU WON* CLICK ENTER TO END THE GAME *YOU WON*")
                                        input()

                                    else:

                                        print("Invalid choice, try again.")
                                        input()

                                elif answer.lower() .strip() == "attack":

                                    answer = input (f"\nWhile you were trying to attack the teacher, the electric shock was "
                                        f"\naffecting your internal organs which caused your death. GAME OVER \n")

                                    print ("CLICK ENTER TO END THE GAME. You Lose :( ")
                                    input()

                                else:

                                    print("Invalid choice, try again.")

                            else:

                                    print("Invalid choice, try again.")

                        elif answer.lower() .strip() == "no":

                                answer = input (f"\nI couldn't live that way, I don't want that, I can rather rest in peace. "
                                f"\nIf that's what you want, that's fine, you've made your decision! "
                                f"\n(The doctor operated on you so that you do not have the powers, therefore, you died. GAME OVER) \n")

                                print ("CLICK ENTER TO END THE GAME. You died. GAME OVER ")
                                input()

                        else:

                                print("Invalid choice, try again.")


                    elif answer.lower() .strip() == "b":

                        answer = input (f"\nBecause even if you have certain skills, I can bring you " 
                        f"\nback to life, but since you are only a prototype, "
                        f"\nyou will only live for 1 year at most. But tell me about the abilities, \n"
                        f"\nWhat powers do I have? (A) / That I will only have 1 year to live, but not solve that? (B) : ")

                        if answer.lower() .strip() == "a":

                            answer = input (f'\nYou will be practically a superman, you will have super powers or' 
                            f'\nwhatever you call it, you will have super strength, improved speed, improved vision, '
                            f'\nyou have everything that we humans can wish for, you are what we would call a superior '
                            f'\nbeing or you would be like a "GOD" or so some would say but The only thing you cannot do is fly. \nDo you want this powers? \n'
                            f'\nACCEPT POWERS (OK) / I don not want to live with those powers. (NO) : ')

                            if answer.lower() .strip() == "ok":

                                answer = input (f"\nSounds good to me, I'll accept these powers! I think it will be something incredible. "
                                f"\nThe professor begins the phase of administration of doses of serum to prototype 0043 while doing it, screams "
                                f"\nof agonizing pain are heard, for some 10 minutes but after administering the serum, the doctor quickly puts "
                                f"\na metal collar on you and tells you that now You are going to use your life time for the good and you will be "
                                f"\na hereo of the city and that you will help him to end all possible crime during this year. \n"
                                f"\nYour plan works fine but I don't think this necklace was necessary, I was going to help you anyway. (HELP) / "
                                f"I won't be your slave, I didn't come back to life to be what you want. (ANGER) : ")

                                if answer.lower() .strip() == "help":

                                    answer = input (f"\nYour plan is going well but I don't think this necklace was necessary, it was going to help you anyway. "
                                     f"\nOkay, I put the collar on you as a safety measure, when I trust you I'll take it off. Do you want to start your training? \n"
                                     f"\nYes. Let's do it (A) / No. I'll learn on my own (B) : ")

                                    if answer.lower() .strip() == "a":

                                        answer = input (f"\nPerfect we are going to teach you the basics to use your powers, your training will start now. \n"
                                        f"\nTO BE CONTINUE...")
                                        
                                        print ("CLICK ENTER TO END THE GAME")

                                        input()

                                    elif answer.lower() .strip() == "b":

                                        answer = input (f"\nAll right, if you need any help just ask me, I know you can master your skills quickly. \n"
                                        f"\nTO BE CONTINUE...")

                                        print ("CLICK ENTER TO END THE GAME")

                                        input()

                                elif answer.lower() .strip() == "anger":

                                    answer = input (f"\nI will not be a slave of yours, I did not come back to life to be what you want. "
                                    f"\nI'm afraid this will stop! The teacher seeing your answer presses a button which activates the necklace, "
                                    f"\nit begins to electrocute you and make you wallow in pain. \n"
                                    f"\nTry to break the necklace (BREAK) / Attack the doctor (ATTACK) : ")

                                    if answer.lower() .strip() == "break":

                                        answer = input (f'\nWith your superhuman strength it was more '
                                        f'\nthan easy to break the necklace and stop the electric shock. '
                                        f'\nWhen the teacher sees this he only says one word "damn it". '
                                        f'\nAttack the teacher (ATTACK) / Escape from the place (RUN) : ')

                                        if answer.lower() .strip() == "attack":

                                            answer = input (f"\nAfter attacking the professor and killing him, you realized what you had done and you "
                                            f"\nregret what makes you realize how dangerous you are, which will lead you to spend the time of your life "
                                            f"\nthat you have left on an island surrounded only by silver, animals and the immense sea while time passes while "
                                            f"\nyour life slowly comes to the end. \n")
                                            
                                            print ("")
                                            print ("*YOU WON* CLICK ENTER TO END THE GAME *YOU WON*")
                                            input()
                                            
                                        elif answer.lower() .strip() == "run":

                                            answer = input (f"\nWith the little time to live you had and with your superpowers, "
                                            f"\nyou decided to conquer humanity and enjoy everything before you perish. \n")

                                            print ("")
                                            print ("*YOU WON* CLICK ENTER TO END THE GAME *YOU WON*")
                                            input()

                                        else:

                                            print("Invalid choice, try again.")
                                            input()

                                    elif answer.lower() .strip() == "attack":

                                        answer = input (f"\nWhile you were trying to attack the teacher, the electric shock was "
                                        f"\naffecting your internal organs which caused your death. GAME OVER \n")

                                        print ("CLICK ENTER TO END THE GAME. You Lose :( ")
                                        input()

                                    else:

                                        print("Invalid choice, try again.")

                                else:

                                    print("Invalid choice, try again.")

                            elif answer.lower() .strip() == "no":

                                answer = input (f"\nI couldn't live that way, I don't want that, I can rather rest in peace. "
                                f"\nIf that's what you want, that's fine, you've made your decision! "
                                f"\n(The doctor operated on you so that you do not have the powers, therefore, you died. GAME OVER) \n")

                                print ("CLICK ENTER TO END THE GAME. You died. GAME OVER ")
                                input()

                            else:

                                print("Invalid choice, try again.")

                        elif answer.lower() .strip() == "b": 

                            answer = input (f"\nYes, but I will not force you to anything anyway, you can get the "
                            f"\nsuperpowers or go back to doing the cold cavader that you were \n"
                            f"\nYes, I want the powers! (A) / No. I could not live that way. (B) : ")

                            if answer.lower() .strip() == "a": 

                                answer = input (f"\nSounds good to me, I'll accept these powers! I think it will be something incredible. "
                                f"\nThe professor begins the phase of administration of doses of serum to prototype 0043 while doing it, screams "
                                f"\nof agonizing pain are heard, for some 10 minutes but after administering the serum, the doctor quickly puts "
                                f"\na metal collar on you and tells you that now You are going to use your life time for the good and you will be "
                                f"\na hereo of the city and that you will help him to end all possible crime during this year. \n"
                                f"\nYour plan works fine but I don't think this necklace was necessary, I was going to help you anyway. (HELP) / "
                                f"I won't be your slave, I didn't come back to life to be what you want. (ANGER) : ")

                            elif answer.lower() .strip() == "b":

                                answer = input (f"\nI couldn't live that way, I don't want that, I can rather rest in peace. "
                                f"\nIf that's what you want, that's fine, you've made your decision! \n"
                                f"\n(The doctor operated on you so that you do not have the powers, therefore, you died. GAME OVER)")

                                print ("\nCLICK ENTER TO END THE GAME")

                        else:

                            print("Invalid choice, try again.")

                    else: 

                        print("Invalid choice, try again.")
    
            elif answer.lower() .strip() == "b":

                answer = input (f'\nYou were at a typical promiscuous teen party, what did you think those candies were? '
                f'\nBut that is not the important thing, the important thing is that ... Unfortunately, I could not bring you to life without '
                f'\nendowing you with "certain skills" that we say. But that is not the important thing, the important thing is that ... '
                f'\nUnfortunately, I could not bring you to life without endowing you with "certain skills" that we say. \n'
                f'\nWhat do you mean by "certain abilities" (A) / You mean I will have super powers? (B) : ')

                if answer.lower() .strip() == "a": 

                    answer = input (f"\nSuperhuman abilities, super powers whatever you want to call it today. \n"
                    f"\nGreat, I will have superpowers now! (A) / But why would having superpowers be collateral damage? (B) : ")

            else:

                print("Invalid choice, try again.") 

        elif answer.lower() .strip() == "b":

            answer = input (f'\nSadly, I could not bring you to life without endowing you with "certain abilities" to say the least.\n ' 
            f'\nWhat do you mean by "certain abilities" (A) / You mean I will have super powers? (B) : ')

            if answer.lower() .strip() == "a":

                        answer = input (f'\nYou will be practically a superman, you will have super powers or' 
                            f'\nwhatever you call it, you will have super strength, improved speed, improved vision, '
                            f'\nyou have everything that we humans can wish for, you are what we would call a superior '
                            f'\nbeing or you would be like a "GOD" or so some would say but The only thing you cannot do is fly. \nDo you want this powers? \n'
                            f'\nACCEPT POWERS (OK) / I don not want to live with those powers. (NO) : ')

                        if answer.lower() .strip() == "ok":

                            answer = input (f"\nSounds good to me, I'll accept these powers! I think it will be something incredible. "
                                f"\nThe professor begins the phase of administration of doses of serum to prototype 0043 while doing it, screams "
                                f"\nof agonizing pain are heard, for some 10 minutes but after administering the serum, the doctor quickly puts "
                                f"\na metal collar on you and tells you that now You are going to use your life time for the good and you will be "
                                f"\na hereo of the city and that you will help him to end all possible crime during this year. \n"
                                f"\nYour plan works fine but I don't think this necklace was necessary, I was going to help you anyway. (HELP) "
                                f"\nI won't be your slave, I didn't come back to life to be what you want. (ANGER) : ")

                            if answer.lower() .strip() == "help":

                                answer = input (f"\nYour plan is going well but I don't think this necklace was necessary, it was going to help you anyway. "
                                     f"\nOkay, I put the collar on you as a safety measure, when I trust you I'll take it off. Do you want to start your training? \n"
                                     f"\nYes. Let's do it (A) / No. I'll learn on my own (B) : ")

                                if answer.lower() .strip() == "a":

                                    answer = input (f"\nPerfect we are going to teach you the basics to use your powers, your training will start now. \n"
                                        f"\nTO BE CONTINUE...")
                                        
                                    print ("CLICK ENTER TO END THE GAME")

                                    input()

                                elif answer.lower() .strip() == "b":

                                    answer = input (f"\nAll right, if you need any help just ask me, I know you can master your skills quickly. \n"
                                        f"\nTO BE CONTINUE...")

                                    print ("CLICK ENTER TO END THE GAME")

                                    input()

                            elif answer.lower() .strip() == "anger":

                                answer = input (f"\nI will not be a slave of yours, I did not come back to life to be what you want. "
                                    f"\nI'm afraid this will stop! The teacher seeing your answer presses a button which activates the necklace, "
                                    f"\nit begins to electrocute you and make you wallow in pain. \n"
                                    f"\nTry to break the necklace (BREAK) / Attack the doctor (ATTACK) : ")

                                if answer.lower() .strip() == "break":

                                    answer = input (f'\nWith your superhuman strength it was more '
                                        f'\nthan easy to break the necklace and stop the electric shock. '
                                        f'\nWhen the teacher sees this he only says one word "damn it". '
                                        f'\nAttack the teacher (ATTACK) / Escape from the place (RUN) : ')

                                    if answer.lower() .strip() == "attack":

                                        answer = input (f"\nAfter attacking the professor and killing him, you realized what you had done and you "
                                            f"\nregret what makes you realize how dangerous you are, which will lead you to spend the time of your life "
                                            f"\nthat you have left on an island surrounded only by silver, animals and the immense sea while time passes while "
                                            f"\nyour life slowly comes to the end. \n")
                                            
                                        print ("")
                                        print ("*YOU WON* CLICK ENTER TO END THE GAME *YOU WON*")
                                        input()
                                            
                                    elif answer.lower() .strip() == "run":

                                        answer = input (f"\nWith the little time to live you had and with your superpowers, "
                                            f"\nyou decided to conquer humanity and enjoy everything before you perish. \n")

                                        print ("")
                                        print ("*YOU WON* CLICK ENTER TO END THE GAME *YOU WON*")
                                        input()

                                    else:

                                        print("Invalid choice, try again.")
                                        input()

                                elif answer.lower() .strip() == "attack":

                                    answer = input (f"\nWhile you were trying to attack the teacher, the electric shock was "
                                        f"\naffecting your internal organs which caused your death. GAME OVER \n")

                                    print ("CLICK ENTER TO END THE GAME. You Lose :( ")
                                    input()

                                else:

                                    print("Invalid choice, try again.")

                            else:

                                    print("Invalid choice, try again.")

                        elif answer.lower() .strip() == "no":

                                answer = input (f"\nI couldn't live that way, I don't want that, I can rather rest in peace. "
                                f"\nIf that's what you want, that's fine, you've made your decision! "
                                f"\n(The doctor operated on you so that you do not have the powers, therefore, you died. GAME OVER) \n")

                                print ("CLICK ENTER TO END THE GAME. You died. GAME OVER ")
                                input()

                        else:

                                print("Invalid choice, try again.")

            if answer.lower() .strip() == "a":  

                    answer = input (f"\nSuperhuman abilities, super powers whatever you want to call it today. \n"
                    f"\nI will have superpowers now! (A) / But why would having superpowers be collateral damage? (B) : ")

                    if answer.lower() .strip() == "a":

                        answer = input (f"\nSuperpowers seem cool to me. NICE!... PRESS ENTER. ")

                        answer = input (f'\nYou will be practically a superman, you will have super powers or' 
                            f'\nwhatever you call it, you will have super strength, improved speed, improved vision, '
                            f'\nyou have everything that we humans can wish for, you are what we would call a superior '
                            f'\nbeing or you would be like a "GOD" or so some would say but The only thing you cannot do is fly. \nDo you want this powers? \n'
                            f'\nACCEPT POWERS (OK) / I don not want to live with those powers. (NO) : ')

                        if answer.lower() .strip() == "ok":

                            answer = input (f"\nSounds good to me, I'll accept these powers! I think it will be something incredible. "
                                f"\nThe professor begins the phase of administration of doses of serum to prototype 0043 while doing it, screams "
                                f"\nof agonizing pain are heard, for some 10 minutes but after administering the serum, the doctor quickly puts "
                                f"\na metal collar on you and tells you that now You are going to use your life time for the good and you will be "
                                f"\na hereo of the city and that you will help him to end all possible crime during this year. \n"
                                f"\nYour plan works fine but I don't think this necklace was necessary, I was going to help you anyway. (HELP) "
                                f"\nI won't be your slave, I didn't come back to life to be what you want. (ANGER) : ")

                            if answer.lower() .strip() == "help":

                                answer = input (f"\nYour plan is going well but I don't think this necklace was necessary, it was going to help you anyway. "
                                     f"\nOkay, I put the collar on you as a safety measure, when I trust you I'll take it off. Do you want to start your training? \n"
                                     f"\nYes. Let's do it (A) / No. I'll learn on my own (B) : ")

                                if answer.lower() .strip() == "a":

                                    answer = input (f"\nPerfect we are going to teach you the basics to use your powers, your training will start now. \n"
                                        f"\nTO BE CONTINUE...")
                                        
                                    print ("CLICK ENTER TO END THE GAME")

                                    input()

                                elif answer.lower() .strip() == "b":

                                    answer = input (f"\nAll right, if you need any help just ask me, I know you can master your skills quickly. \n"
                                        f"\nTO BE CONTINUE...")

                                    print ("CLICK ENTER TO END THE GAME")

                                    input()

                            elif answer.lower() .strip() == "anger":

                                answer = input (f"\nI will not be a slave of yours, I did not come back to life to be what you want. "
                                    f"\nI'm afraid this will stop! The teacher seeing your answer presses a button which activates the necklace, "
                                    f"\nit begins to electrocute you and make you wallow in pain. \n"
                                    f"\nTry to break the necklace (BREAK) / Attack the doctor (ATTACK) : ")

                                if answer.lower() .strip() == "break":

                                    answer = input (f'\nWith your superhuman strength it was more '
                                        f'\nthan easy to break the necklace and stop the electric shock. '
                                        f'\nWhen the teacher sees this he only says one word "damn it". '
                                        f'\nAttack the teacher (ATTACK) / Escape from the place (RUN) : ')

                                    if answer.lower() .strip() == "attack":

                                        answer = input (f"\nAfter attacking the professor and killing him, you realized what you had done and you "
                                            f"\nregret what makes you realize how dangerous you are, which will lead you to spend the time of your life "
                                            f"\nthat you have left on an island surrounded only by silver, animals and the immense sea while time passes while "
                                            f"\nyour life slowly comes to the end. \n")
                                            
                                        print ("")
                                        print ("*YOU WON* CLICK ENTER TO END THE GAME *YOU WON*")
                                        input()
                                            
                                    elif answer.lower() .strip() == "run":

                                        answer = input (f"\nWith the little time to live you had and with your superpowers, "
                                            f"\nyou decided to conquer humanity and enjoy everything before you perish. \n")

                                        print ("")
                                        print ("*YOU WON* CLICK ENTER TO END THE GAME *YOU WON*")
                                        input()

                                    else:

                                        print("Invalid choice, try again.")
                                        input()

                                elif answer.lower() .strip() == "attack":

                                    answer = input (f"\nWhile you were trying to attack the teacher, the electric shock was "
                                        f"\naffecting your internal organs which caused your death. GAME OVER \n")

                                    print ("CLICK ENTER TO END THE GAME. You Lose :( ")
                                    input()

                                else:

                                    print("Invalid choice, try again.")

                            else:

                                    print("Invalid choice, try again.")

                        elif answer.lower() .strip() == "no":

                                answer = input (f"\nI couldn't live that way, I don't want that, I can rather rest in peace. "
                                f"\nIf that's what you want, that's fine, you've made your decision! "
                                f"\n(The doctor operated on you so that you do not have the powers, therefore, you died. GAME OVER) \n")

                                print ("CLICK ENTER TO END THE GAME. You died. GAME OVER ")
                                input()

                        else:

                                print("Invalid choice, try again.")


                    elif answer.lower() .strip() == "b":

                        answer = input (f"\nBecause even if you have certain skills, I can bring you " 
                        f"\nback to life, but since you are only a prototype, "
                        f"\nyou will only live for 1 year at most. But tell me about the abilities, \n"
                        f"\nWhat powers do I have? (A) / That I will only have 1 year to live, but not solve that? (B) : ")

                        if answer.lower() .strip() == "a":

                            answer = input (f'\nYou will be practically a superman, you will have super powers or' 
                            f'\nwhatever you call it, you will have super strength, improved speed, improved vision, '
                            f'\nyou have everything that we humans can wish for, you are what we would call a superior '
                            f'\nbeing or you would be like a "GOD" or so some would say but The only thing you cannot do is fly. \nDo you want this powers? \n'
                            f'\nACCEPT POWERS (OK) / I don not want to live with those powers. (NO) : ')

                            if answer.lower() .strip() == "ok":

                                answer = input (f"\nSounds good to me, I'll accept these powers! I think it will be something incredible. "
                                f"\nThe professor begins the phase of administration of doses of serum to prototype 0043 while doing it, screams "
                                f"\nof agonizing pain are heard, for some 10 minutes but after administering the serum, the doctor quickly puts "
                                f"\na metal collar on you and tells you that now You are going to use your life time for the good and you will be "
                                f"\na hereo of the city and that you will help him to end all possible crime during this year. \n"
                                f"\nYour plan works fine but I don't think this necklace was necessary, I was going to help you anyway. (HELP) / "
                                f"\nI won't be your slave, I didn't come back to life to be what you want. (ANGER) : ")

                                if answer.lower() .strip() == "help":

                                    answer = input (f"\nYour plan is going well but I don't think this necklace was necessary, it was going to help you anyway. "
                                     f"\nOkay, I put the collar on you as a safety measure, when I trust you I'll take it off. Do you want to start your training? \n"
                                     f"\nYes. Let's do it (A) / No. I'll learn on my own (B) : ")

                                    if answer.lower() .strip() == "a":

                                        answer = input (f"\nPerfect we are going to teach you the basics to use your powers, your training will start now. \n"
                                        f"\nTO BE CONTINUE...")
                                        
                                        print ("CLICK ENTER TO END THE GAME")

                                        input()

                                    elif answer.lower() .strip() == "b":

                                        answer = input (f"\nAll right, if you need any help just ask me, I know you can master your skills quickly. \n"
                                        f"\nTO BE CONTINUE...")

                                        print ("CLICK ENTER TO END THE GAME")

                                        input()

                                elif answer.lower() .strip() == "anger":

                                    answer = input (f"\nI will not be a slave of yours, I did not come back to life to be what you want. "
                                    f"\nI'm afraid this will stop! The teacher seeing your answer presses a button which activates the necklace, "
                                    f"\nit begins to electrocute you and make you wallow in pain. \n"
                                    f"\nTry to break the necklace (BREAK) / Attack the doctor (ATTACK) : ")

                                    if answer.lower() .strip() == "break":

                                        answer = input (f'\nWith your superhuman strength it was more '
                                        f'\nthan easy to break the necklace and stop the electric shock. '
                                        f'\nWhen the teacher sees this he only says one word "damn it". '
                                        f'\nAttack the teacher (ATTACK) / Escape from the place (RUN) : ')

                                        if answer.lower() .strip() == "attack":

                                            answer = input (f"\nAfter attacking the professor and killing him, you realized what you had done and you "
                                            f"\nregret what makes you realize how dangerous you are, which will lead you to spend the time of your life "
                                            f"\nthat you have left on an island surrounded only by silver, animals and the immense sea while time passes while "
                                            f"\nyour life slowly comes to the end. \n")
                                            
                                            print ("")
                                            print ("*YOU WON* CLICK ENTER TO END THE GAME *YOU WON*")
                                            input()
                                            
                                        elif answer.lower() .strip() == "run":

                                            answer = input (f"\nWith the little time to live you had and with your superpowers, "
                                            f"\nyou decided to conquer humanity and enjoy everything before you perish. \n")

                                            print ("")
                                            print ("*YOU WON* CLICK ENTER TO END THE GAME *YOU WON*")
                                            input()

                                        else:

                                            print("Invalid choice, try again.")
                                            input()

                                    elif answer.lower() .strip() == "attack":

                                        answer = input (f"\nWhile you were trying to attack the teacher, the electric shock was "
                                        f"\naffecting your internal organs which caused your death. GAME OVER \n")

                                        print ("CLICK ENTER TO END THE GAME. You Lose :( ")
                                        input()

                                    else:

                                        print("Invalid choice, try again.")

                                else:

                                    print("Invalid choice, try again.")

                            elif answer.lower() .strip() == "no":

                                answer = input (f"\nI couldn't live that way, I don't want that, I can rather rest in peace. "
                                f"\nIf that's what you want, that's fine, you've made your decision! "
                                f"\n(The doctor operated on you so that you do not have the powers, therefore, you died. GAME OVER) \n")

                                print ("CLICK ENTER TO END THE GAME. You died. GAME OVER ")
                                input()

                            else:

                                print("Invalid choice, try again.")


        else:

             print("Invalid choice, try again.")  

    elif answer.lower() .strip() == "b":    

        answer = input (f"\nAgain among the living says the doctor.\n \nSo you say : I think I'm going to need a better explanation...\n"
        f"\nFine. You are just a test subject, you had an accident yesterday and by science you are alive " 
        f"again, \nbut unfortunately, I could not bring you back without collateral damage. After hearing this you ask : \n"
        f"\nHow did I die? (A) / What collateral damage are you talking about? (B) : ")

        if answer.lower() .strip() == "a": 

            answer = input (f"\nI think it is not a very relevant question, but if you insist I can tell you : " 
            f"\nWhat is the last thing you remember before waking up here?\n"
            f"\nI don't remember anything. (A) / I remember having some candy at that party. (B) : ")

            if answer.lower() .strip() == "a": 

                answer = input (f'\nYou died in a very authentic way, according to the autopsy I performed on you, it was due to poisoning. '
                f'\nBut that is not the important thing, the important thing is that ... Unfortunately, '
                f'\nI could not bring you to life without endowing you with "certain skills" \n'
                f'\nWhat do you mean by "certain abilities" (A) / You mean I will have super powers? (B) : ')

                if answer.lower() .strip() == "a":  

                    answer = input (f"\nSuperhuman abilities, super powers whatever you want to call it today. \n"
                    f"\nI will have superpowers now! (A) / But why would having superpowers be collateral damage? (B) : ")

                    if answer.lower() .strip() == "a":

                        answer = input (f"\nSuperpowers seem cool to me. NICE!... PRESS ENTER. ")

                        answer = input (f'\nYou will be practically a superman, you will have super powers or' 
                            f'\nwhatever you call it, you will have super strength, improved speed, improved vision, '
                            f'\nyou have everything that we humans can wish for, you are what we would call a superior '
                            f'\nbeing or you would be like a "GOD" or so some would say but The only thing you cannot do is fly. \nDo you want this powers? \n'
                            f'\nACCEPT POWERS (OK) / I don not want to live with those powers. (NO) : ')

                        if answer.lower() .strip() == "ok":

                            answer = input (f"\nSounds good to me, I'll accept these powers! I think it will be something incredible. "
                                f"\nThe professor begins the phase of administration of doses of serum to prototype 0043 while doing it, screams "
                                f"\nof agonizing pain are heard, for some 10 minutes but after administering the serum, the doctor quickly puts "
                                f"\na metal collar on you and tells you that now You are going to use your life time for the good and you will be "
                                f"\na hereo of the city and that you will help him to end all possible crime during this year. \n"
                                f"\nYour plan works fine but I don't think this necklace was necessary, I was going to help you anyway. (HELP) / "
                                f"I won't be your slave, I didn't come back to life to be what you want. (ANGER) : ")

                            if answer.lower() .strip() == "help":

                                answer = input (f"\nYour plan is going well but I don't think this necklace was necessary, it was going to help you anyway. "
                                     f"\nOkay, I put the collar on you as a safety measure, when I trust you I'll take it off. Do you want to start your training? \n"
                                     f"\nYes. Let's do it (A) / No. I'll learn on my own (B) : ")

                                if answer.lower() .strip() == "a":

                                    answer = input (f"\nPerfect we are going to teach you the basics to use your powers, your training will start now. \n"
                                        f"\nTO BE CONTINUE... \n")
                                        
                                    print ("\nCLICK ENTER TO END THE GAME")

                                    input()

                                elif answer.lower() .strip() == "b":

                                    answer = input (f"\nAll right, if you need any help just ask me, I know you can master your skills quickly. \n"
                                        f"\nTO BE CONTINUE... \n")

                                    print ("\nCLICK ENTER TO END THE GAME")

                                    input()

                            elif answer.lower() .strip() == "anger":

                                answer = input (f"\nI will not be a slave of yours, I did not come back to life to be what you want. "
                                    f"\nI'm afraid this will stop! The teacher seeing your answer presses a button which activates the necklace, "
                                    f"\nit begins to electrocute you and make you wallow in pain. \n"
                                    f"\nTry to break the necklace (BREAK) / Attack the doctor (ATTACK) : ")

                                if answer.lower() .strip() == "break":

                                    answer = input (f'\nWith your superhuman strength it was more '
                                        f'\nthan easy to break the necklace and stop the electric shock. '
                                        f'\nWhen the teacher sees this he only says one word "damn it". '
                                        f'\nAttack the teacher (ATTACK) / Escape from the place (RUN) : ')

                                    if answer.lower() .strip() == "attack":

                                        answer = input (f"\nAfter attacking the professor and killing him, you realized what you had done and you "
                                            f"\nregret what makes you realize how dangerous you are, which will lead you to spend the time of your life "
                                            f"\nthat you have left on an island surrounded only by silver, animals and the immense sea while time passes while "
                                            f"\nyour life slowly comes to the end. \n")
                                            
                                        print ("")
                                        print ("*YOU WON* CLICK ENTER TO END THE GAME *YOU WON*")
                                        input()
                                            
                                    elif answer.lower() .strip() == "run":

                                        answer = input (f"\nWith the little time to live you had and with your superpowers, "
                                            f"\nyou decided to conquer humanity and enjoy everything before you perish. \n")

                                        print ("")
                                        print ("*YOU WON* CLICK ENTER TO END THE GAME *YOU WON*")
                                        input()

                                    else:

                                        print("Invalid choice, try again.")
                                        input()

                                elif answer.lower() .strip() == "attack":

                                    answer = input (f"\nWhile you were trying to attack the teacher, the electric shock was "
                                        f"\naffecting your internal organs which caused your death. GAME OVER \n")

                                    print ("CLICK ENTER TO END THE GAME. You Lose :( ")
                                    input()

                                else:

                                    print("Invalid choice, try again.")

                            else:

                                    print("Invalid choice, try again.")

                        elif answer.lower() .strip() == "no":

                                answer = input (f"\nI couldn't live that way, I don't want that, I can rather rest in peace. "
                                f"\nIf that's what you want, that's fine, you've made your decision! "
                                f"\n(The doctor operated on you so that you do not have the powers, therefore, you died. GAME OVER) \n")

                                print ("CLICK ENTER TO END THE GAME. You died. GAME OVER ")
                                input()

                        else:

                                print("Invalid choice, try again.")


                    elif answer.lower() .strip() == "b":

                        answer = input (f"\nBecause even if you have certain skills, I can bring you " 
                        f"\nback to life, but since you are only a prototype, "
                        f"\nyou will only live for 1 year at most. But tell me about the abilities, \n"
                        f"\nWhat powers do I have? (A) / That I will only have 1 year to live, but not solve that? (B) : ")

                        if answer.lower() .strip() == "a":

                            answer = input (f'\nYou will be practically a superman, you will have super powers or' 
                            f'\nwhatever you call it, you will have super strength, improved speed, improved vision, '
                            f'\nyou have everything that we humans can wish for, you are what we would call a superior '
                            f'\nbeing or you would be like a "GOD" or so some would say but The only thing you cannot do is fly. \nDo you want this powers? \n'
                            f'\nACCEPT POWERS (OK) / I don not want to live with those powers. (NO) : ')

                            if answer.lower() .strip() == "ok":

                                answer = input (f"\nSounds good to me, I'll accept these powers! I think it will be something incredible. "
                                f"\nThe professor begins the phase of administration of doses of serum to prototype 0043 while doing it, screams "
                                f"\nof agonizing pain are heard, for some 10 minutes but after administering the serum, the doctor quickly puts "
                                f"\na metal collar on you and tells you that now You are going to use your life time for the good and you will be "
                                f"\na hereo of the city and that you will help him to end all possible crime during this year. \n"
                                f"\nYour plan works fine but I don't think this necklace was necessary, I was going to help you anyway. (HELP) / "
                                f"\nI won't be your slave, I didn't come back to life to be what you want. (ANGER) : ")

                                if answer.lower() .strip() == "help":

                                    answer = input (f"\nYour plan is going well but I don't think this necklace was necessary, it was going to help you anyway. "
                                     f"\nOkay, I put the collar on you as a safety measure, when I trust you I'll take it off. Do you want to start your training? \n"
                                     f"\nYes. Let's do it (A) / No. I'll learn on my own (B) : ")

                                    if answer.lower() .strip() == "a":

                                        answer = input (f"\nPerfect we are going to teach you the basics to use your powers, your training will start now. \n"
                                        f"\nTO BE CONTINUE...")
                                        
                                        print ("CLICK ENTER TO END THE GAME")

                                        input()

                                    elif answer.lower() .strip() == "b":

                                        answer = input (f"\nAll right, if you need any help just ask me, I know you can master your skills quickly. \n"
                                        f"\nTO BE CONTINUE...")

                                        print ("CLICK ENTER TO END THE GAME")

                                        input()

                                elif answer.lower() .strip() == "anger":

                                    answer = input (f"\nI will not be a slave of yours, I did not come back to life to be what you want. "
                                    f"\nI'm afraid this will stop! The teacher seeing your answer presses a button which activates the necklace, "
                                    f"\nit begins to electrocute you and make you wallow in pain. \n"
                                    f"\nTry to break the necklace (BREAK) / Attack the doctor (ATTACK) : ")

                                    if answer.lower() .strip() == "break":

                                        answer = input (f'\nWith your superhuman strength it was more '
                                        f'\nthan easy to break the necklace and stop the electric shock. '
                                        f'\nWhen the teacher sees this he only says one word "damn it". '
                                        f'\nAttack the teacher (ATTACK) / Escape from the place (RUN) : ')

                                        if answer.lower() .strip() == "attack":

                                            answer = input (f"\nAfter attacking the professor and killing him, you realized what you had done and you "
                                            f"\nregret what makes you realize how dangerous you are, which will lead you to spend the time of your life "
                                            f"\nthat you have left on an island surrounded only by silver, animals and the immense sea while time passes while "
                                            f"\nyour life slowly comes to the end. \n")
                                            
                                            print ("")
                                            print ("*YOU WON* CLICK ENTER TO END THE GAME *YOU WON*")
                                            input()
                                            
                                        elif answer.lower() .strip() == "run":

                                            answer = input (f"\nWith the little time to live you had and with your superpowers, "
                                            f"\nyou decided to conquer humanity and enjoy everything before you perish. \n")

                                            print ("")
                                            print ("*YOU WON* CLICK ENTER TO END THE GAME *YOU WON*")
                                            input()

                                        else:

                                            print("Invalid choice, try again.")
                                            input()

                                    elif answer.lower() .strip() == "attack":

                                        answer = input (f"\nWhile you were trying to attack the teacher, the electric shock was "
                                        f"\naffecting your internal organs which caused your death. GAME OVER \n")

                                        print ("CLICK ENTER TO END THE GAME. You Lose :( ")
                                        input()

                                    else:

                                        print("Invalid choice, try again.")

                                else:

                                    print("Invalid choice, try again.")

                            elif answer.lower() .strip() == "no":

                                answer = input (f"\nI couldn't live that way, I don't want that, I can rather rest in peace. "
                                f"\nIf that's what you want, that's fine, you've made your decision! "
                                f"\n(The doctor operated on you so that you do not have the powers, therefore, you died. GAME OVER) \n")

                                print ("CLICK ENTER TO END THE GAME. You died. GAME OVER ")
                                input()

                            else:

                                print("Invalid choice, try again.")

                        elif answer.lower() .strip() == "b": 

                            answer = input (f"\nYes, but I will not force you to anything anyway, you can get the "
                            f"\nsuperpowers or go back to doing the cold cavader that you were \n"
                            f"\nYes, I want the powers! (A) / No. I could not live that way. (B) : ")

                            if answer.lower() .strip() == "a": 

                                answer = input (f"\nSounds good to me, I'll accept these powers! I think it will be something incredible. "
                                f"\nThe professor begins the phase of administration of doses of serum to prototype 0043 while doing it, screams "
                                f"\nof agonizing pain are heard, for some 10 minutes but after administering the serum, the doctor quickly puts "
                                f"\na metal collar on you and tells you that now You are going to use your life time for the good and you will be "
                                f"\na hero of the city and that you will help him to end all possible crime during this year. \n"
                                f"\n(Your plan works fine but I don't think this necklace was necessary, I was going to help you anyway. (HELP) " 
                                f"\nI won't be your slave, I didn't come back to life to be what you want. (ANGER) : ") 

                            elif answer.lower() .strip() == "b":

                                answer = input (f"\nI couldn't live that way, I don't want that, I can rather rest in peace. "
                                f"\nIf that's what you want, that's fine, you've made your decision! \n"
                                f"\n(The doctor operated on you so that you do not have the powers, therefore, you died. GAME OVER)")

                                print ("\nCLICK ENTER TO END THE GAME")

                        else:

                            print("Invalid choice, try again.")

                    else: 

                        print("Invalid choice, try again.")

            

        elif answer.lower() .strip() == "b":

            answer = input (f"\nEven if you have certain skills, I can bring you " 
                        f"\nback to life, but since you are only a prototype, you will only live for 1 year at most. \n"
                        f"\nBut tell me about the abilities, What powers do I have? (A) "
                        f"\nThat I will only have 1 year to live, but not solve that? (B) : ")

            if answer.lower() .strip() == "a":

                answer = input (f'\nYou will be practically a superman, you will have super powers or' 
                f'\nwhatever you call it, you will have super strength, improved speed, improved vision, '
                f'\nyou have everything that we humans can wish for, you are what we would call a superior '
                f'\nbeing or you would be like a "GOD" or so some would say but The only thing you cannot do is fly. \nDo you want this powers? \n'
                f'\nACCEPT POWERS (OK) / I don not want to live with those powers. (NO) : ')

                if answer.lower() .strip() == "ok":

                    answer = input (f"\nSounds good to me, I'll accept these powers! I think it will be something incredible. "
                    f"\nThe professor begins the phase of administration of doses of serum to prototype 0043 while doing it, screams "
                    f"\nof agonizing pain are heard, for some 10 minutes but after administering the serum, the doctor quickly puts "
                    f"\na metal collar on you and tells you that now You are going to use your life time for the good and you will be "
                    f"\na hereo of the city and that you will help him to end all possible crime during this year. \n"
                    f"\nYour plan works fine but I don't think this necklace was necessary, I was going to help you anyway. (HELP) " 
                    f"\nI won't be your slave, I didn't come back to life to be what you want. (ANGER) : ")

                    if answer.lower() .strip() == "help":

                        answer = input (f"\nYour plan is going well but I don't think this necklace was necessary, it was going to help you anyway. "
                        f"\nOkay, I put the collar on you as a safety measure, when I trust you I'll take it off. Do you want to start your training? \n"
                        f"\nYes. Let's do it (A) / No. I'll learn on my own (B) : ")

                        if answer.lower() .strip() == "a":

                            answer = input (f"\nPerfect we are going to teach you the basics to use your powers, your training will start now. "
                            f"TO BE CONTINUE... \n")

                            print ("\nCLICK ENTER TO END THE GAME")
                            input ()

                        elif answer.lower() .strip() == "b":

                            answer = input (f"\nAll right, if you need any help just ask me, I know you can master your skills quickly. "
                            f"TO BE CONTINUE... \n")

                            print ("\nCLICK ENTER TO END THE GAME")
                            input ()

            elif answer.lower() .strip() == "b":

                answer = input (f"\nYes, but I will not force you to anything anyway, you can get the super" 
                f"\npowers or go back to doing the cold cavader that you were \n"
                f"\nYes, I want the powers! (A) / No. I could not live that way. (B) : ")

                if answer.lower() .strip() == "a": 

                    answer = input (f"\nSounds good to me, I'll accept these powers! I think it will be something incredible. "
                                f"\nThe professor begins the phase of administration of doses of serum to prototype 0043 while doing it, screams "
                                f"\nof agonizing pain are heard, for some 10 minutes but after administering the serum, the doctor quickly puts "
                                f"\na metal collar on you and tells you that now You are going to use your life time for the good and you will be "
                                f"\na hero of the city and that you will help him to end all possible crime during this year. \n"
                                f"\nYour plan works fine but I don't think this necklace was necessary, I was going to help you anyway. (HELP)  "
                                f"\nI won't be your slave, I didn't come back to life to be what you want. (ANGER) : ")
                                
                    if answer.lower() .strip() == "help":

                        answer = input (f"\nYour plan is going well but I don't think this necklace was necessary, it was going to help you anyway. "
                                     f"\nOkay, I put the collar on you as a safety measure, when I trust you I'll take it off. Do you want to start your training? \n"
                                     f"\nYes. Let's do it (A) / No. I'll learn on my own (B) : ")

                        if answer.lower() .strip() == "a":

                            answer = input (f"\nPerfect we are going to teach you the basics to use your powers, your training will start now. "
                                        f"TO BE CONTINUE...\n")

                            print ("\nCLICK ENTER TO END THE GAME")


                        elif answer.lower() .strip() == "b":

                                answer = input (f"\nAll right, if you need any help just ask me, I know you can master your skills quickly. "
                                        f"TO BE CONTINUE...\n")

                                print ("\nCLICK ENTER TO END THE GAME")

                    elif answer.lower() .strip() == "anger":

                         answer = input (f"\nI will not be a slave of yours, I did not come back to life to be what you want. "
                                    f"\nI'm afraid this will stop! The teacher seeing your answer presses a button which activates the necklace, "
                                    f"\nit begins to electrocute you and make you wallow in pain. \n"
                                    f"\nTry to break the necklace (BREAK) / Attack the doctor (ATTACK) : ")

                         if answer.lower() .strip() == "break":

                            answer = input (f'\nWith your superhuman strength it was more than easy to break the necklace and stop the electric shock. '
                                        f'\nWhen the teacher sees this he only says one word "damn it". \n'
                                        f'\nAttack the teacher (ATTACK) / Escape from the place (RUN) ')

                            if answer.lower() .strip() == "attack":

                                answer = input (f"\nAfter attacking the professor and killing him, you realized what you had done and you "
                                            f"\nregret what makes you realize how dangerous you are, which will lead you to spend the time of your life "
                                            f"\nthat you have left on an island surrounded only by silver, animals and the immense sea while time passes while "
                                            f"\nyour life slowly comes to an end. ")

                                print ("\n*YOU WON* CLICK ENTER TO END THE GAME *YOU WON*")

                            elif answer.lower() .strip() == "run":

                                answer = input (f"\nWith the little time to live you had and with your superpowers, "
                                f"\nyou decided to conquer humanity and enjoy everything before you perish." )

                                print ("\n*YOU WON* CLICK ENTER TO END THE GAME *YOU WON*")

                            else:   

                                print("Invalid choice, try again.")
                                 

                elif answer.lower() .strip() == "b":

                    answer = input (f"\nI couldn't live that way, I don't want that, I can rather rest in peace. \n"
                                f"\nIf that's what you want, that's fine, you've made your decision! \n"
                                f"\n(The doctor operated on you so that you do not have the powers, therefore, you died. GAME OVER) ")

                    print ("\nCLICK ENTER TO END THE GAME")
                    input()
                            
    else:

        print("Invalid choice, try again.")

elif answer.lower() .strip() == "no":

    print("\nApparently you don't want to play, see you later then. ")

    print("\nPRESS ENTER TO END THE GAME. ")

    input()

else:
    print("\nInvalid choice, try again. ")

    print("\nPRESS ENTER TO END THE GAME. \n")

    input()

