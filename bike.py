class Bike(object):
    def __init__(self,price,max_speed,miles):
        self.price=price
        self.max_speed=max_speed
        self.miles=miles
    def displayInfo(self):
        print self.price,self.max_speed,self.miles
    def ride(self):
        self.miles+=10
        print "Riding",self.miles
    def reverse(self):
        print "Reversing",self.miles
   
bmx=Bike(100,"25Mph",10)
bmx.displayInfo()
bmx.ride()
bmx.reverse()


