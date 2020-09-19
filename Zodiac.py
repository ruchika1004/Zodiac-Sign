#Application regarding Zodiac signs
next=True

while(next):

    print("""
1.Aries
2.Taurus
3.Gemini
4.Cancer
5.Leo
6.virgo
7.Libra
8.Scorpio
9.Sagittarius
10.Capricorn
11.Aquarius
12.Pisces
""")
    s=int(input("Please enter the Zodiac sign number:"))

    if s==1:
        print("""There is a hero deep inside of you, and you just might get a glimpse of that person today when you notice a 
    problem or danger that no one else notices. Your quick action will be essential for creating a safer environment for 
    the people you love, and it will also create a lot of positive buzz about you. Your profile is getting higher and as 
    the day goes on, your confidence will build. It might inspire you to try something that you've always been a bit too 
    intimidated to try before.""")

    elif s==2:
        print("""If drama erupts on the scene today, avoid it at all costs. Just keep your head down, mind your own business,
     and resist the urge to go find out what the fuss is about. Getting caught up in a power struggle right now is not 
     going to be a good move. Even if you try to stay objective, it simply won't be possible. It's much better to stick to 
     your own work and keep your eyes on your own paper. If someone asks you to get involved, you should tell them no and 
     accept the consequences.  """)

    elif s==3:
        print("""You need to pay closer attention to the numbers today, especially if you're reviewing any budgets, bank
     statements, or tax documents. This is not a day to gloss over details and just hope that everything turns out all right.
    Numbers could also be important socially. If you get some new cutie's phone number, make sure you have all the numbers 
    written down correctly! Little mistakes now could create big problems later, so double-check everything. """)

    elif s==4:
        print("""You could receive an inexpensive but impactful gift, and it will be no bargain basement purchase! It will be more
    like a gift of an idea, an inspiration that creates a spark in your mind. This spark could grow into a flame of new romantic
    feelings, it could become a brilliant new idea, or it could just fizzle out into a warm and pleasant feeling. But enjoy the 
    eureka moment because it's nice to be reminded that life is still full of surprises. """)

    elif s==5:
        print("""You will be exuding confidence today even if you don't feel particularly proud of what you have been doing. This type 
    of bravado will be very useful for you, so don't try to alter the positive opinions people will be forming of you by pointing 
    out your faults. That's nothing but self-sabotage. Focusing on your flaws will only drag you down and disappoint others. 
    People have faith in you, and you have to turn that into faith in yourself. """)

    elif s==6:
        print("""Are you worried that there is too much happening in your life right now? Think about those days that are filled with
     boredom and how difficult they can be, and then consider yourself lucky that you are being kept so active and busy right now. 
     Try to be grateful for your jam-packed schedule. There are many people who would trade places with you in an instant. The 
     grass is always greener on the other side of the fence. Be content with how things are right now. """)

    elif s==7:
        print("""It's time for you to build a few new hopes and give your subconscious something new to dream about at night. Take the 
    time to picture where you want to be and who you want to be with in five or ten years. And don't forget to include family and 
    friends in that beautiful scenario. Visualize the brightest future you can possibly imagine, and don't worry about falling short 
    of those expectations. It's important to keep your focus on the bright side. """)

    elif s==8:
        print("""You have mastered an immense challenge that few people could have handled, but you might be feeling like no one noticed!
     This resounding lack of praise could be disappointing, and it certainly is not appropriate. You deserve praise for your 
     accomplishments. You can always pat yourself on the back, you know, so why not? Give yourself a treat today and promise yourself 
     that the next time someone else does something wonderful, you'll be the one cheering the loudest. Lead by example. """)

    elif s==9:
        print("""You probably won't be in a very aggressive mood today. Mellow is more your style right now. But don't think that this 
    laid-back attitude won't have its advantages, because it certainly will! By being more approachable and relaxed, you will 
    unknowingly invite more people of all walks of life to talk to you. This could be the beginning of a very social time for you. 
    And if you are single and ready to mingle, get ready to meet a brand-new candidate! """)

    elif s==10:
        print("""There are a lot of things going on in your life already, so it's not an easy day for new beginnings. Instead of starting 
    yet another new project or trying yet another new activity, stick with the tried and true for now. There will be a much better 
    time to debut your newest ideas, and it's coming soon enough, so just hold your creative horses. In the meantime, keep busy with 
    your usual tasks. They will keep you happy. """)

    elif s==11:
        print("""Someone's words are not matching their actions, and it should cause you to think twice about taking their advice or 
    following in their footsteps. These contradictions in their character are a sure sign that they are not who you thought they were. 
    Take a break from expanding your social circle right now. You can have too many friends, you know. It's much better for you to 
    concentrate on fewer relationships than to spread yourself too thin. """)

    elif s==12: 
        print("""There might be a lot of drama going on in your life now, but none of it is centered around negative energy or anger, 
    which is good. There are just a few different people with differing agendas working against each other, and you're getting caught 
    up in the middle of it all. Choosing sides is a huge mistake, although staying completely neutral will be next to impossible. 
    Just try your best to get everyone to meet somewhere in the middle. If anyone can do it, you can. """)

    else:
        print("Please type the number in between 1-12")

    if input("Do you want to go again? (y/n)")=='y':
        next=True 
    else:
        next=False