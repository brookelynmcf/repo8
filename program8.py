########################################################################
##
## CS 101
## Program # 8
## Name Brooke McFarland
## Email blmz99@mail.umkc.edu
##
## PROBLEM : Simulate the dropping off and picking up of tourists.
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      lots must be greater than 2 and less than 11
##      Initial tourist count must be greater than or equal to 0 but less than 20
##      tram must stay within range of number of lots from user input
##      tram must move from left to right using positive and negative 1 for direction indicators
##      waitlist must eventually reach 0 if everyone has been picked up and dropped off at their final destination
##
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
    def __str__(self):
       return "Tram picked up {} passenger(s) at lot {}".format(len(self.tram.current_lot.wait_list),self.tram.current_lot.lot_number)
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
            random_tourist = Tourist(random_start_lot,random_dest_lot,person)
            tourist_list.append(random_tourist)
            random_start_lot.register_tourist(random_tourist)
        return tourist_list
    def calc_arrived_tourist(self):
        for person in self.tourists:
            if self.tram.current_lot.lot_number == person.destination.lot_number:
                person.arrived = True
                self.arrived_tourist.append(person.arrived)
    def step(self):
        self.tram.move()


class ParkingLot(object):
    def __init__(self, lot_number):
        self.lot_number = lot_number
        self.wait_list = []
    def __str__(self):
        return " ==L{}({})".format(self.lot_number,len(self.wait_list))
    def __repr__(self):
        return self.__repr__()
    def register_tourist(self,tourist):
        self.wait_list.append(tourist)
    def remove_from_waitlist(self,tourist):
        for person in self.wait_list:
            if person.tourist_id == tourist.tourist_id:
                self.wait_list.remove(tourist)


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
            self.tourists_on_or_off_tram()
            self.current_lot = self.lots[1]
            self.direction = 1
            return
        if self.current_lot == self.lots[len(self.lots)- 1]:
            self.tourists_on_or_off_tram()
            self.current_lot = self.lots[len(self.lots)-2]
            self.direction = -1
            return
        currentlotindex = self.lots.index(self.current_lot)
        self.tourists_on_or_off_tram()
        self.current_lot = self.lots[currentlotindex+self.direction]
    def tourists_on_or_off_tram(self):
        for tourist in self.tourists:
            if tourist.start.lot_number == self.current_lot.lot_number and tourist not in self.tram_tourists:
                self.tram_tourists.append(tourist)
                self.current_lot.remove_from_waitlist(tourist)
        for tourist in self.tram_tourists:
            if tourist.destination.lot_number == self.current_lot.lot_number:
                self.tram_tourists.remove(tourist)


class Tourist(object):
    def __init__(self, start_lot, dest_lot,tourist_id):
        self.start = start_lot
        self.destination = dest_lot
        self.arrived = False
        self.tourist_id = tourist_id
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

def print_lot(park):
    lot_str = ""
    for lot in park.lots:
        lot_str += str(lot)
    print(lot_str[3:])

input_tourists = get_number_tourists("How many tourists are in the park initially? (answer must be between 0 and 20)")
input_lots = get_number_lots("How many lots does the park have? (answer must be between 2 and 11)")
print("\n")


mypark = Park(lots = input_lots,tourist_num= input_tourists)
print(str(mypark))
print_lot(mypark)


while len(mypark.arrived_tourist) < len(mypark.tourists):
    mypark.step()
    print(str(mypark))
    print_lot(mypark)
    mypark.calc_arrived_tourist()
print("Fart")



