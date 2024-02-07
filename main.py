answer_yes = ["Y", "Yes", "y", "yes"]
answer_no = ["N", "No", "n", "no"]

print("Welcome to this Text BAsed Adventure Game, to respond to decisions use: Y, Yes, N, or no. Other responses will not work and the game will either stop or you will have to re-input your desicion.")

##print("a group of jr high kids get transported to different workd - adults w/ roles and buisnesses and have to figure shit out gotta get back home w/o revealing identity")


print("On a late Tuesday morning in March you're walking into school. You anxiosly wait for the bell to ring for your first period class. You have a test in second but haven't studied at all. You wish that you could just be done with school.Do you wish you could just be done with school? (Y/N)")

ans1 = input("->")

if ans1 in answer_yes:
    print("\nYou blink your eyes and the school is gone. You're sitting in a glass office building behind a desk. You start to look around, should you go explore? (Y/N)\n")

    ans2 = input("->")

    if ans2 in answer_yes:
        print("\nYou stand up and begin walking throughh the plain walls. You're surrounded by adults in fancy clothes. Theres a mirror at the end of the hall an you seem completley unrecognizable. You're we're fancy clothes and have aged to be an adult.DO you sccream? (Y/N)")

    elif ans2 in answer_no:
        print("\nGood choice, you keep your composier and wander into a random hallway. At the end of the hall there is a glowing light. You walk into as, you have nothing to lose considering you don't know where or who you are. It teleports you into your second period class where you fail your exam. ")

    else:
        print("\nBad input. Game Over!")

elif ans1 in answer_no:
    print("\nThe bell rings and your first period class ends. Do you skip your second period? (Y/N)\n")

    ans3 = input("->")

    if ans3 in answer_yes:
        print("\nThe principal catches you on the way out and you get sent to detention. Game Over!")

    elif ans3 in answer_no:
        print("\nYou go to class and you end up aceing your test. Congrats! You win!")

    else:
        print("\nBad input. Game Over!")

else:
    print("\nBad input. Game Over!")