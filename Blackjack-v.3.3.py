import random

def fortsätta():
    while(True):
        char = input("\nVill du spela igen? [y/n] ")
        if(char == "y"):
            return(True)
        elif(char == "n"):
            return(False)

def poängräknare(dp,sp):
    print("")
    if sp > 21:
        return("\nDu är tjock!\nDu förlorar!")
    elif dp > 21:
        return("Dealern är tjock!\nDu vinner!")
    elif sp == dp:  
        return("Ingen vinner, du får pengarna tillbaka")               
    elif sp > dp: #Denna elif egentligen inkomplett, men den ligger efter sp>21 och fungerar därför ändå
        return("Du är närmast 21!\nGrattis du vinner!")
    else:
        return("Dealern är närmast 21!\nDu förlorar")

    
                    
def hand(x):
    sum = 0
    
    ej_ess = [kort for kort in x if kort != 'A'] #Gör en lista för alla kort som inte är ess
    ess = [kort for kort in x if kort == 'A']    #Gör en lista för alla kort som ÄR ess
    
    for kort in ej_ess:
        if kort == 'J' or kort == 'Q' or kort == 'K': #Om kortet i listan ej_spader är J, Q eller K så läggs det till 10 poäng i sum
            sum += 10
        else:
            sum += int(kort)                   #Om kortet inte är J Q eller K så adderas kortets nummer till summan
            
    for kort in ess:
        if sum <= 10:
            sum += 11
        else:
            sum += 1
            
    return sum

'''
Funktion "hand" ger felaktig poäng vid handen "A, A, 10" eller liknande.
Första esset räknas som 11 och det andra som ett, båda borde räknas som
1, för att spelaren inte ska bli tjock.
'''

def förstagiv(d,s):
    random.shuffle(kort)

    s.append(kort.pop())
    d.append(kort.pop())
    s.append(kort.pop())
    d.append(kort.pop())
    return(d,s)
'''
Kan vara värt att nämna i redovisningen att vår funktion för att dela ut kort
fungerar på samma sätt som en riktig kortlek delar ut kort. Korten blandas i leken och delas
bara ut genom det översta, och inte att ett slumpmässigt kort i den oblandade leken delas ut.
'''
mainloop = True
print("Välkommen till:")

print("""\

██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗ █████╗  ██████╗██╗  ██╗██╗
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝     ██║██╔══██╗██╔════╝██║ ██╔╝██║
██████╔╝██║     ███████║██║     █████╔╝      ██║███████║██║     █████╔╝ ██║
██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ██   ██║██╔══██║██║     ██╔═██╗ ╚═╝
██████╔╝███████╗██║  ██║╚██████╗██║  ██╗╚█████╔╝██║  ██║╚██████╗██║  ██╗██╗
╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝

                                                                        
                    """)

while(mainloop):
    kort = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']*4
    dealer = []
    spelare = []
    förstagiv(dealer, spelare)
    
    gameloop = True
    standing = False
    GIVräknare = 0
    
    while(gameloop):
        spelare_points = hand(spelare)
        dealer_points = hand(dealer)
    
        print("\n\nDina kort:", spelare, spelare_points)
            
        if standing:
            print("Dealerns kort: ", dealer, dealer_points)
        else:
            print("Dealerns kort: ", [dealer[0],'?'])
        '''
        Denna if-sats ovan styr om dealern ska visa sitt dolda kort eller ej
        '''            
        if(standing or spelare_points > 21):
            print(poängräknare(dealer_points,spelare_points))        
            mainloop = fortsätta()
            gameloop = False
            break
        elif(GIVräknare == 3):
            print("\nDu har 5 kort på handen utan att var tjock!\nGrattis du vinner!")
            mainloop = fortsätta()
            gameloop = False
            break
        elif(GIVräknare == 0 and spelare_points == 21):
            if(spelare_points != dealer_points):
                print("\nBlackjack! Du är rik!")
                print("Dealerns kort: ", dealer, dealer_points)
                mainloop = fortsätta()
                gameloop = False
                break
            else:
                print("\n\nDina kort:", spelare, spelare_points)
                print("Dealerns kort: ", dealer, dealer_points)
                print("\nBåde du och dealern fick Blackjack!\nLika! Du får pengarna tillbaka!")        
                mainloop = fortsätta()
                gameloop = False
                break
        '''
        If-satsen ovan kontrollerar om spelaren eller dealern har vunnit/förlorat,
        och skriver därefter ut lämpliga textmeddelanden.
        '''
        
        '''
        Följande while-loop styr om spelaren vill ta ett ett kort till eller stanna.
        '''
        while(True):
            if(spelare_points != 21):
                val = input("\n[1] Hit\n[2] Stand\n\nVälj ett alternativ: ")
            else:
                val = '2'
            '''
            Ifall spelaren har 21 gör if-satsen ovan så att spelaren
            inte får alternativet att ta ett kort till.
            '''
            if val == '1':
                spelare.append(kort.pop())
                GIVräknare += 1
                break
            elif val == '2':
                standing = True
                while hand(dealer) <= 16:
                    dealer.append(kort.pop())
                break