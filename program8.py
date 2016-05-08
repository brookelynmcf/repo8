########################################################################
##
## CS 101
## Program # 6
## Name Brooke McFarland
## Email blmz99@mail.umkc.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
import random
import copy

class Park(object):
    def __init__(self,lots = 2, tourist_num = 0 ):
        self.lots = self.__make_lots_list(lots)
        self.tourists = self.__make_tourist_list(tourist_num)
        self.tram = Tram(self.lots[0],self.lots,self.tourists)
        self.lots_total = len(self.lots)
        self.tourist_num = tourist_num
        self.arrived_tourist = []
        #self.wait_list = wait_list
    def __str__(self):
        lot = 0
        while lot <= lots_total:
            lot += 1
        print("{}==".format(lot))
    def step(self):
        pass
    def __make_lots_list(self,num_lot):
        lots_list = []
        for number in range(num_lot):
            lots_list.append(ParkingLot(number+1))
        return lots_list

    def __make_tourist_list(self,num_tourist):
        tourist_list = []
        for person in range(num_tourist):
            random_start_lot = random.choice(self.lots)
            k = copy.deepcopy(self.lots)
            for lot in k:
                if lot.lot_number == random_start_lot.lot_number:
                    k.remove(lot)
            random_dest_lot = random.choice(k)
            tourist_list.append(Tourist(random.choice(self.lots),random_dest_lot))
        return tourist_list
    def dest_tourist_list(self):
        for person in self.tourists:
            if self.tram.current_lot.lot_number == person.destination.lot_number:
                person.arrived = True
                self.arrived_tourist.append(person.arrived)
        return self.arrived_tourist


class ParkingLot(object):
    def __init__(self, lot_number):
        self.lot_number = lot_number
        #self.wait_list = wait_list
    def __str__(self):
        pass
    def __repr__(self):
        pass
    def register_tourist(self,tourist):
        return self.wait_list + tourist


class Tram(object):
    def __init__(self,current_lot,lots,tourists):
        self.current_lot = current_lot
        self.direction  = 0
        self.lots = lots
        self.tourists = tourists
        self.tram_tourists = []
    def __str__(self):
        pass
    def move(self):
        if self.current_lot == self.lots[0]:
            self.current_lot = self.lots[1]
            self.direction = 1
            self.tourists_on_or_off_tram()
            return
        if self.current_lot == self.lots[len(self.lots)- 1]:
            self.current_lot = self.lots[len(self.lots)-2]
            self.direction = -1
            self.tourists_on_or_off_tram()
            return
        currentlotindex = self.lots.index(self.current_lot)
        self.current_lot = self.lots[currentlotindex+self.direction]
        self.tourists_on_or_off_tram()
    def tourists_on_or_off_tram(self):
        for tourist in self.tourists:
            if tourist.start.lot_number == self.current_lot.lot_number and tourist not in self.tram_tourists:
                self.tram_tourists.append(tourist)
        for tourist in self.tram_tourists:
            if tourist.destination.lot_number == self.current_lot.lot_number:
                self.tram_tourists.remove(tourist)




class Tourist(object):
    def __init__(self, start_lot, dest_lot):
        self.start = start_lot
        self.destination = dest_lot
        self.arrived = False
    def __str__(self):
        pass
def get_number_lots(question):
    while True:
        try:
            answer = int(input(question))
        except ValueError:
            print("Please, enter an integer.")
            continue
        if answer <2 or answer > 11:
            print("The number you have used is out of the correct range.")
            continue
        else:
            return answer
def get_number_tourists(question):
    while True:
        try:
            answer = int(input(question))
        except ValueError:
            print("Please, enter an integer.")
            continue
        if answer < 0 or answer > 20:
            print("The number you have entered is not within the correct range.(0-20)")
            continue
        else:
            return answer

input_tourists = get_number_tourists("How many tourists are in the park initially? (answer must be between 0 and 20)")
input_lots = get_number_lots("How many lots does the park have? (answer must be between 2 and 11)")


mypark = Park(lots = input_lots,tourist_num= input_tourists)
arrived_list = mypark.dest_tourist_list()
while len(arrived_list) < len(mypark.tourists):
    mypark.tram.move()
    arrived_list = mypark.dest_tourist_list()
print("Fart")



