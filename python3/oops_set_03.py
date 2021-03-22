class Train:
    def __init__(self,name,seats,fare):
        self.name= name
        self.seats= seats
        self.fare= fare
    def getStatus(self):
        print(f"The name of the train is {self.name}.")    
        print(f"The seats are available in the trin is {self.seats}.")    
    def getFare(self):
        print(f"The prize of ticket is: Rs{self.fare}")    
    def bookTicket(self):
        if(self.seats>0):
            print(f"The ticket number has been booked! seat no is {self.seats}")
            self.seats= self.seats-1
        else:
            print("Sorry seat has been already booked")

t = Train("Rajdhani Express (444034)", 4, 150)
t.bookTicket()
t.getStatus()
t.getFare()
t.bookTicket()
t.bookTicket()
t.bookTicket()
t.bookTicket()
