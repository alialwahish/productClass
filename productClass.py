class Product(object):
    def __init__(self,price,itemName,weight,brand):
        self.price=price
        self.itemName=itemName
        self.weight=weight
        self.brand=brand
        self.status="for sale"
        
    def sell(self):
        self.status="sold"
        return self
    def addTax(self,tax):
      
        self.price+=self.price*tax
        
        return self
    def Return(self,reason):
        if reason == "defective":
            self.price=0
            self.status=reason
        elif reason == "retrndInBox":
            self.status=reason
        elif reason == "opnBxRtrnd":
            self.status="used"
            self.price=self.price*.2
        else:
            print  self.itemName,"item cannot be returned for that reason"
    def displayInfo(self):
        print "Price:",self.price,"$ Item Name:",self.itemName," Weight:",self.weight,"lb Brand:",self.brand," Status:",self.status
grocery = Product(10,"tomato",0.2,"usa")
fruit = Product(3,"orange",0.4,"italy")
shelf=Product(5,"Protien Bar",0.5,"Matrix")
fruit.addTax(0.15)
shelf.Return("defective")
grocery.displayInfo()
fruit.displayInfo()
shelf.displayInfo()
