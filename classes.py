class Rent:
    def __init__(self,amount_of_usage):
        if (isinstance(amount_of_usage,int) or isinstance(amount_of_usage,float)):
            self.amount_of_usage=amount_of_usage
        else:
            raise(TypeError("The amount of usage must be an int or float variable but the type set is: {}.".format(type(amount_of_usage))))
    def fee(self):
        return self.cost*self.amount_of_usage

class HourRent(Rent):
    cost=5
    def __init__(self,amount_of_usage):
        super().__init__(amount_of_usage)
class DayRent(Rent):
    cost=20
    def __init__(self,amount_of_usage):
        super().__init__(amount_of_usage)

class WeekRent(Rent):
    cost=60
    def __init__(self,amount_of_usage):
        super().__init__(amount_of_usage)

class FamilyRent:
    discount=0.3
    floor=3
    top=5
    
    @staticmethod
    def valid_rent(one_rent):
        return type(one_rent) in Rent.__subclasses__()
    @staticmethod
    def validate_list_of_rents(list_of_rents):
        if isinstance(list_of_rents,tuple):
            if all(FamilyRent.valid_rent(one_rent) for one_rent in list_of_rents):
                return all(FamilyRent.valid_rent(one_rent) for one_rent in list_of_rents)
            else:
                raise ValueError("At least one element of the list of rents is not a Rent subclass.")
        else:
            raise TypeError("The list of rents is not a tuple.")
        

    def __init__(self,rents):#ADD HERE TRY AND EXCEPT if we are not receiving a list
        try:
            if self.validate_list_of_rents(rents):
                if (len(rents)>=self.floor) and (len(rents)<=self.top):#Apply controls to class type, every element should be hour, day or week rent and amount of rents
                    self.rents=rents
                else:
                    raise(ValueError("The amount of rents is not between 3 and 5. You loaded {}".format(len(rents))))
                    
        except TypeError:
            raise(TypeError("The type of variable provided to Family Rent is not a tuple or a list."))
    def apply_discounts_total(self,total):
        return total - (total*self.discount)
    def total_fee(self):
        total=0
        for one_rent in self.rents:
            total+=one_rent.fee()
        total=self.apply_discounts_total(total)
        return total