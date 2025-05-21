from random import randint
class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
    def book(self, fro, to):
        print(f"The ticket for train no {self.trainNo} is booked from {fro} to {to}")
    def getStatus(self):
        print(f"The train no {self.trainNo} is running on time.")
    def getFare(self, fro, to):
        print(f"Ticket fare in train no {self.trainNo} from {fro} to {to} is {randint(111, 5656)}")
    
booker = Train(12345)
booker.book("Lahore", "Karachi")
booker.getStatus()
booker.getFare("Lahore", "Karachi")