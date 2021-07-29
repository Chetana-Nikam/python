class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats avaible in the train are {self.seats}")

    def fareInfo(self):
        print(f"The prise of ticket is {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket is booked ! and your seat no is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Train is full !!")

    # def cancelTicket(self, seatNo):
        
    #     l = []
    #     for i in range(1, self.seats+1):
    #         l.append(i)
    #         self.seatNo = seatNo

    #         print(f"Your ticket is successfully canceled {self.seatNo}")
    #         print("Noe available seats are givenn belo: ")
    #         print(l)


            
intercity = Train("intercity express: 10023", 90, 300)
intercity.getStatus()
intercity.fareInfo()
intercity.bookTicket()

