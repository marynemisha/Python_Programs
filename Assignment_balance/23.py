#Generate 100 random lottery tickets and pick two lucky tickets from it as a
# winner
import random
ticket=[]
for i in range(100):
    ticket.append(random.randint(100000,999999))
winner = random.sample(ticket, 2)
print("Winner1:", winner[0])
print("Winner2:", winner[1])