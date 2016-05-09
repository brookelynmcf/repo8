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
##      Algorithm #8
# •	Create park class(object):
# o	Attributes:
# o	Def __init__(self,  tourist_num = 0, lots : [], lots_total = 2 , tram):
# 	Self.lots = lots
# 	Self.tram = tram
# 	Self.tourists = tourist_num
# 	Self.lots_total = lots_total
# o	Methods:
# o	Def __str__(self):
# 	Return “{}{}…”.format(each lot instance, where the tram has stopped, and what direction it is going in)
# o	Def park_update(self):
# 	Return movement of tram to next stop
# •	Create ParkingLot class(Park):
# o	Attributes:
# o	Def __init__(self,  tourist_num = 0, lots : [], lots_total = 2 , tram, lot_number : int, wait_list = []):
# 	Park __init__(self, tourist_num, lots, lots_total, tram)
# 	Self.lot_number = lot_number
# 	Self.wait_list = wait_list
# o	Def __str__(self):
# 	Return “{}{}”.format(lot_number, wait_list)
# o	Def __repr__(self):
# 	Return ?
# o	Def register_tourist(self, tourist):
# 	Self.wait_list.append(tourist)
# •	Create Tram class(ParkingLot):
# o	Attributes:
# o	Def __init__(self,  tourist_num = 0, lots : [], lots_total = 2 , tram, lot_number : int, wait_list = [], current_lot, direction):
# 	ParkingLot.__init__(self, tourist, lots, lots_total, tram. Lot_number, wait_list)
# 	Self.current_lot = current_lot
# 	Self.direction = direction
# •	Create Tourist class(object):
# o	Def __init(self, start : int, destination : int)
# 	Self.start = start
# 	Self.stop = destination
# o	Def __str__(self):
# 	Return “{}”.format(tourist)
# •	Prompt function:
# o	Ask user if they would like to run the simulation
# 	If no
# 	Sys.exit(“Fine! I’ll ride the Tilt-a-Hurl by myself!”)
# o	Prompts user to input how many lots the park has
# o	Error handling:
# 	2 < =input <= 11
# 	Non integers
# o	Prompts user how many tourist
# o	Error handling:
# 	2<= input < = 20
# 	Non integers
# •	Current_state function:
# o	Prints state of park at current time
#
##
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
    """park object that makes a list of tourists (total), returns a str value of itself, creates a list of lots,calls on move function in tram to move the tram forward, calculates the amount of
    people that have arrived at their destination"""
    def __init__(self,lots = 2, tourist_num = 0 ):
        self.lots = self.__make_lots_list(lots)
        self.tourists = self.__make_tourist_list(tourist_num)
        self.tram = Tram(self.lots[0],self.lots,self.tourists)
        self.lots_total = len(self.lots)
        self.tourist_num = tourist_num
        self.arrived_tourist = []
    def __str__(self):
       return "Tram picked up {} passenger(s) at lot {}\nTram dropped off {} passenger(s) at lot {}".format(self.tram.current_lot.picked_up,self.tram.current_lot.lot_number,self.tram.current_lot.dropped_off,self.tram.current_lot.lot_number)
    def __make_lots_list(self,num_lot):
        """makes list of total lots"""
        lots_list = []
        for number in range(num_lot):
            lots_list.append(ParkingLot(number+1))
        return lots_list

    def __make_tourist_list(self,num_tourist):
        """makes list of total tourist in park, assigns a random starting lot and a random destination lot, error handling so start and end lot can not be the same"""
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
        """calculates tourist that have arrived at their random destination and creates a list of arrived tourist, which is a list of bool values. True being they arrived
        and False if they haven't arrived at their destination yet."""
        for person in self.tourists:
            if self.tram.current_lot.lot_number == person.destination.lot_number:
                person.arrived = True
                self.arrived_tourist.append(person.arrived)
    def step(self):
        """calls on method in tram class to move the tram forward"""
        self.tram.move()


class ParkingLot(object):
    """ParkingLot object contains a string representation of itself, a list of tourist waiting to get on the tram at each parking lot, a list of passangers that have been
    picked up and another list of passengers that have been dropped off"""
    def __init__(self, lot_number):
        self.lot_number = lot_number
        self.wait_list = []
        self.picked_up = 0
        self.dropped_off = 0
    def __str__(self):
        return " ==L{}({})".format(self.lot_number,len(self.wait_list))
    def __repr__(self):
        return self.__repr__()
    def register_tourist(self,tourist):
        """adds the tourist to the wait list that has been randomly generated at each parking lot"""
        self.wait_list.append(tourist)
    def remove_from_waitlist(self,tourist):
        """if the person is picked up by the tram, the person is then removed from the wait list"""
        for person in self.wait_list:
            if person.tourist_id == tourist.tourist_id:
                self.wait_list.remove(tourist)


class Tram(object):
    """the Tram class controls the direction of the tram(1 = to the right, -1 = to the left). It contains a list of lots, a list of tourists, a lits of tourists that are on the tram
    and at which lot the tram is currently at"""
    def __init__(self,current_lot,lots,tourists):
        self.current_lot = current_lot
        self.direction  = 1
        self.lots = lots
        self.tourists = tourists
        self.tram_tourists = []
        self.tourists_on_tram()
    def __str__(self):
        """formating for printing the tram and indicating the direction in which it is moving"""
        if self.direction == -1:
            return "<T({})".format(len(self.tram_tourists))
        elif self.direction == 1:
            return "T({})>".format(len(self.tram_tourists))
        elif self.direction == 0:
            return "T({})>".format(len(self.tram_tourists))
    def move(self):
        """function to move the train forward one lot in the positive direction stariting at lots index 0, calls on function keep track of people who are
        getting on and off the tram"""
        self.current_lot.picked_up = 0
        if self.current_lot == self.lots[0]:
            self.current_lot = self.lots[1]
            self.direction = 1
            self.tourists_on_tram()
            self.tourists_off_tram()
            return
        if self.current_lot == self.lots[len(self.lots)- 1]:
            self.tourists_on_tram()
            self.current_lot = self.lots[len(self.lots)-2]
            self.tourists_off_tram()
            self.direction = -1
            return
        currentlotindex = self.lots.index(self.current_lot)
        self.tourists_on_tram()
        self.current_lot = self.lots[currentlotindex+self.direction]
        self.tourists_off_tram()
    def tourists_on_tram(self):
        """creates a list of tourists who are currently on the tram, but must also not have arrived at their destination, and not already in the list, adds tourist to list if they
        meet all of these requirements"""
        for tourist in self.tourists:
            if tourist.start.lot_number == self.current_lot.lot_number and tourist not in self.tram_tourists and tourist.arrived == False:
                self.tram_tourists.append(tourist)
                self.current_lot.picked_up += 1
                self.current_lot.remove_from_waitlist(tourist)
    def tourists_off_tram(self):
        """creates a list of tourists getting off of the tram, must make a deep copy of the list so we can make changes to it with out altering the origional list"""
        copy_list = copy.deepcopy(self.tram_tourists)
        for tourist in copy_list:
            if tourist.destination.lot_number == self.current_lot.lot_number:
                for x in self.tram_tourists:
                    if x.tourist_id == tourist.tourist_id:
                        self.tram_tourists.remove(x)
                        self.current_lot.dropped_off += 1



class Tourist(object):
    """assigns each tourist a random start lot and a random destination lot, assigns a tourist id to each tourist"""
    def __init__(self, start_lot, dest_lot,tourist_id):
        self.start = start_lot
        self.destination = dest_lot
        self.arrived = False
        self.tourist_id = tourist_id


def get_number_lots(question):
    """input for user to choose the amount of total lots they would like in the park, and error handling for incorrect values"""
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
    """asks user how many total tourists they would like to initialise the park with, error handling for if the user enters a number less than 0 or greater than 20"""
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
    """method to print lots and their numbers, starting at index for the first one in the list so that the two equals signs are not included"""
    lot_str = ""
    for lot in park.lots:
        lot_str += str(lot)
    print(lot_str[3:])

input_tourists = get_number_tourists("How many tourists are in the park initially? (answer must be between 0 and 20)")
input_lots = get_number_lots("How many lots does the park have? (answer must be between 2 and 11)")
print("\n")

#creating an instance of park called mypark, and passing lots and tourist_num as parameters
mypark = Park(lots = input_lots,tourist_num= input_tourists)
#print a string representation of my park to indicate who what picked up at what lot
print(str(mypark))
#prints who was dropped off at what park
print_lot(mypark)
print("{:>}".format(str(mypark.tram)))



#creating spaces for when the tram moves
space = " "
while len(mypark.arrived_tourist) < len(mypark.tourists):
    question = input("Enter q to quit program").lower()
    if question == "q":
        break
    #tram moves
    mypark.step()
    #prints current data
    print(str(mypark))
    print_lot(mypark)
    #implements spacing to move the tram
    if mypark.tram.direction == 1:
        space += " "*7
        print(space+str(mypark.tram))
    if mypark.tram.direction == -1:
        space += space[:-7]
        print(space+str(mypark.tram))
    #calling on calc_arrived_tourist method to calculate the tourists that have arrived at their destination
    mypark.calc_arrived_tourist()



