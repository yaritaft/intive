class Rent:
    """Super class Rent, every class inherits the way of calculating the fee, a cost attribute and an amount of time.
    Attributes:
        AMOUNT_OF_USAGE (int / float): Amount of time that the rent lasted. Can be hours, days or weeks depending on the subclass chose.
    """    
    def __init__(self,amount_of_usage):
        """Validate before creating an object. If the amount of time is int or float the object is created.
            Args:
                AMOUNT_OF_USAGE (int / float): Amount of time that the rent lasted. Can be hours, days or weeks depending on the subclass chose.
            Raises:
                TypeError: When the amount of usage is not a float or an int variable.
            Return:
                None
        """
        if (isinstance(amount_of_usage,int) or isinstance(amount_of_usage,float)):
            self.amount_of_usage=amount_of_usage
        else:
            raise(TypeError("The amount of usage must be an int or float variable but the type set is: {}.".format(type(amount_of_usage))))
    def fee(self):
        """Calculate fee for any type of rent by using polymorphism with cost. The formula is cost * amount of usage. If
            a new type of rent has a different formula, a fee method can be redefined in the subclass itself. In that way,
            the fee method will not be inherited from Rent.
            Args:
                None
            Return:
                Float / Int
        """
        return self.cost*self.amount_of_usage

class HourRent(Rent):
    """Hour rent represents a rent that is charged per hour, it is a subclass of Rent, it inherits the amount of usage attribute and fee method.
        Amount of usage in this case represents amount of hours per rent.
    Attributes:
        COST (int): Amount of money charged per hour.
    """   
    cost=5
    def __init__(self,amount_of_usage):
        """Create an hour rent.
            Args:
                AMOUNT_OF_USAGE (int / float): Number of HOURS that the rent lasted.
            Return:
                None
        """
        super().__init__(amount_of_usage)
class DayRent(Rent):
    """Day rent represents a rent that is charged per day, it is a subclass of Rent, it inherits the amount of usage attribute and fee method.
        Amount of usage in this case represents amount of days per rent.
    Attributes:
        COST (int): Amount of money charged per day.
    """   
    cost=20
    def __init__(self,amount_of_usage):
        """Create an Day rent.
            Args:
                AMOUNT_OF_USAGE (int / float): Number of DAYS that the rent lasted.
            Return:
                None
        """
        super().__init__(amount_of_usage)

class WeekRent(Rent):
    """Week rent represents a rent that is charged per week, it is a subclass of Rent, it inherits the amount of usage attribute and fee method.
        Amount of usage in this case represents amount of weeks per rent.
    Attributes:
        COST (int): Amount of money charged per week.
    """    
    cost=60
    def __init__(self,amount_of_usage):
        """Create an Week rent.
            Args:
                AMOUNT_OF_USAGE (int / float): Number of WEEKS that the rent lasted.
            Return:
                None
        """
        super().__init__(amount_of_usage)

class FamilyRent:
    """Group of rents. Group quantity between 3 and 5. It has a discount of 30%.
    Attributes:
        DISCOUNT (float): Percentaje of discount. This discount is applied to the total fee.
        FLOOR (int): Minimum amount of rents.
        TOP (int): Maximum amount of rents.
        RENTS (tuple): Tuple with all the rents involved in the family rent.
    """
    discount=0.3
    floor=3
    top=5
    
    @staticmethod
    def valid_rent(one_rent):
        """Validate if a rent given is a subclass of Rent class.
            Args:
                ONE_RENT (Rent Subclass): The type of the rent must be one subclass of Rent class. 
            Return:
                Bool
        """
        return type(one_rent) in Rent.__subclasses__()
    @staticmethod
    def validate_list_of_rents(rents):
        """Validate the list of rents. Validations applied: Quantity and type.
            Args:
                RENTS (tuple): Tuple of rents. Between 3 and 5 rents.
            Raises:
                TypeError: When the group of rents is not a tuple.
                ValueError: When at least one element of the group is not a Rent subclass.
            Return:
                Bool
        """
        if isinstance(rents,tuple):
            if all(FamilyRent.valid_rent(one_rent) for one_rent in rents):
                return all(FamilyRent.valid_rent(one_rent) for one_rent in rents)
            else:
                raise ValueError("At least one element of the group of rents is not a Rent subclass.")
        else:
            raise(TypeError("The type of variable provided to Family Rent is not a tuple."))
        

    def __init__(self,rents):
        """Create a family rent. A family rent is a group between 3 and 5 rents. These rents have to be validated in
            quantity and type before creating the object.
            Args:
                RENTS (tuple): Tuple with the group of rents.
            Raises:
                ValueError: When the group of rents is not between 3 and 5 rents.
            Return:
                None
        """
        if self.validate_list_of_rents(rents) and  (len(rents)>=self.floor) and (len(rents)<=self.top):
                self.rents=rents
        else:
            raise(ValueError("The amount of rents is not between 3 and 5. You loaded {}".format(len(rents))))
            
    def apply_discount_total(self,total):
        """Apply discounts by reducing the total amount given.
            quantity and type before creating the object.
            Args:
                TOTAL (int / float): Total amount of money that the rent will be charged.
            Return:
                Int / Float
        """
        return total - (total*self.discount)
    def total_fee(self):
        """Calculate the total fee of a family rent.
            Args:
                None
            Return:
                Int / Float
        """
        total=0
        for one_rent in self.rents:
            total+=one_rent.fee()
        total=self.apply_discount_total(total)
        return total