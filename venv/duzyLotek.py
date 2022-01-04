import random
import time
print("Witaj w dużym lotku")
time.sleep(1)

selectedNumbers = []
textNumerals = ['pierwszą', 'drugą', 'trzecią', 'czwartą', 'piątą', 'szóstą']
for i in range (0,len(textNumerals)):
        print("Podaj " + textNumerals[i] + " liczbę od 0 do 49: ", end='')
        userNumber = int(input())
        while userNumber < 0 or userNumber > 49:
            print("Podaj liczbę w przedziale 0 - 49")
            userNumber = int(input())
        if userNumber in selectedNumbers:
            print("Ta liczba już została wybrana, podaj inną liczbę")
            userNumber = int(input())
        else:
            selectedNumbers.append(userNumber)
print("Wybrałeś liczby: " +str( selectedNumbers))
# tu rozpoczyna się losowanie liczb przez komputer
drawnNumbers = []
for j in range (6):
    j = random.randint(0,49)
    drawnNumbers.append(j)
print("Komputer wylosował liczby: " +str (drawnNumbers))

A = set(selectedNumbers)
B = set(drawnNumbers)
guessedNumbers = A.intersection(B)
print("Trafiłeś liczby: " + str(guessedNumbers))