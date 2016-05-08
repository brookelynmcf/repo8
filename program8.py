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

class Park(object):
    def __init__(self,lots = 2, tourist_num = 0 ):
        self.lots = lots
        self.tram = tram
        self.tourist = tourist
        self.lots_total = lots_total
        self.tourist_num = tourist_num
        self.wait_list = wait_list
    def __str__(self):
        lot = 0
        while lot <= lots_total:
            lot += 1
        print("{}==".format(lot))
    def step(self):
        pass

class ParkingLot(object):
    def __init__(self, lot_number):
        self.lot_number = lot_number
    def __str__(self):
        pass
    def __repr__(self):
        pass
    def register_tourist(self,tourist):
        return self.wait_list + tourist

class Tram(object):
    def __init__(self,current_lot,lots):
        self.current_lot = current_lot
        self.direction = direction
        self.lots = lots
        self.tourist = tourists
    def __str__(self):
        pass
    def move(self):
        pass

class Tourist(object):
    def __init__(self, start_lot, dest_lot):
        self.start = start_lot
        self. destination = dest_lot
        self.arrived = bool
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

input_tourists = get_number_tourists("How many tourists are in the park initially? (answer must be between 0 and 20)")
input_lots = get_number_lots("How many lots does the park have? (answer must be between 2 and 11)")



