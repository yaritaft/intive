class Rent:
    def __init__(self,amount_of_usage):
        self.amount_of_usage=amount_of_usage
    def fee(self):
        return self.cost*self.amount_of_usage

class HourRent(Rent):
    cost=5
    def __init__(self,amount_of_usage):
        Rent.__init__(self,amount_of_usage)
class DayRent(Rent):
    cost=20
    def __init__(self,amount_of_usage):
        Rent.__init__(self,amount_of_usage)

class WeekRent(Rent):
    cost=60
    def __init__(self,amount_of_usage):
        Rent.__init__(self,amount_of_usage)

class FamilyRent:
    discount=0.3
    floor=3
    top=5
    def __init__(self,rents):#ADD HERE TRY AND EXCEPT if we are not receiving a list
        if (len(rents)>=self.floor) and (len(rents)<=self.top):#Apply controls to class type, every element should be hour, day or week rent and amount of rents
            self.rents=rents
        else:
            print("error")
    def apply_discounts_total(self,total):
        return total - (total*self.discount)
    def total_fee(self):
        total=0
        for one_rent in self.rents:
            total+=one_rent.fee()
        total=self.apply_discounts_total(total)
        return total

#Mencionar que al principio iba a usar polimorfmismo y terminé no usandolo porque no era necesario ya que el metodo era el mismo sisempre con distinta variable de clase.

a=HourRent(5)
b=DayRent(4)
c=WeekRent(9)
print(a.fee())
print(b.fee())
print(c.fee())
d=FamilyRent((a,b,c))
print(d.total_fee())

