import random

def fortsätta():
    while(True):
        char = input("\nVill du spela igen? [y/n] ")
        if(char == "y"):
            return(True)
        elif(char == "n"):
            return(False)
        
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

mainloop = True
print("Välkommen till blackjack!")

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
    
        print("\nDina kort:", spelare, spelare_points)
            
        if standing:
            print("Dealerns kort: ", dealer, dealer_points)
        else:
            print("Dealerns kort: ", [dealer[0],'?'])
            
        if(standing):
            print("")
            if dealer_points > 21:
                print("Dealern är tjock!\nDu vinner! ")
            elif spelare_points == dealer_points:  
                print("Ingen vinner, du får pengarna tillbaka")               
            elif spelare_points > dealer_points:
                print("Du är närmast 21!\nGrattis du vinner!")                    
            else:
                print("Dealern är närmast 21!\nDu förlorar")
                    
            mainloop = fortsätta()
            gameloop = False
            break
        
        if(GIVräknare == 0 and spelare_points == 21 and spelare_points != dealer_points):
                print("\nBlackjack! Du är rik!")
                print("Dealerns kort: ", dealer, dealer_points)
                mainloop = fortsätta()
                gameloop = False
                break
            
        if spelare_points > 21:
            print("\nDu är tjock!\nDu förlorar!")
            mainloop = fortsätta()
            gameloop = False
            break
        
        '''
        Ifall man har 21 så får man fortfarande alternativet att ta ett nytt kort.
        Kan fixa det eller låta det vara
        '''
        
        while(True):
            val = input("\n[1] Hit\n[2] Stand\n\nVälj ett alternativ: ") 
            if val == '1':
                spelare.append(kort.pop())
                GIVräknare += 1
                break
            elif val == '2':
                standing = True
                while hand(dealer) <= 16:
                    dealer.append(kort.pop())
                break

