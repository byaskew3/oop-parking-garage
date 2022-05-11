import random
import time

class ParkingGarage:

    # constructor function
    def __init__(self, enteredGarage = False, tickets = random.sample(range(50), 10), parkingSpaces = random.sample(range(50), 10), currentTicket = {}):
        self.enteredGarage = enteredGarage
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket
    
    # methods
    def takeTicket(self):
        self.enteredGarage = True;
        if (len(self.tickets) > 0):
            newTicket = self.tickets.pop()
            newParking = self.parkingSpaces.pop()
            print(f'Your ticket number is #{newTicket}, please park at Parking Space #{newParking}!')
            self.currentTicket[newTicket] = 'false'
        else:
            print("Sorry we're full!")
    

    def payForParking(self):
        ticketNum = int(input('What is your ticket number? '))

        if (ticketNum in self.currentTicket):
            paidTicket = input("Type 'pay' to confirm payment. ")
            if (paidTicket.lower() == 'pay'):
                self.tickets.append(ticketNum)
                self.parkingSpaces.append(ticketNum)
                self.currentTicket[ticketNum] = 'true'
            else:
                print('Payment declined, please use another form of payment!')
                self.payForParking()
        else:
            print('Please check your ticket number again!')
            self.payForParking()
    

    def leaveGarage(self):
        if (self.enteredGarage):
            print('Verifying that your ticket is paid for...')
            time.sleep(2)
            for value in self.currentTicket.values():
                if (value == 'false'):
                    print("You haven't paid for your ticket yet!")
                else:
                    print('Thank you, have a nice day!😀')
        else:
            print('You need to enter the garage first...🤔')

christianGarage = ParkingGarage()

christianGarage.takeTicket()
christianGarage.payForParking()
christianGarage.leaveGarage()

