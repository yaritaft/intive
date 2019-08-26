import unittest
from classes import HourRent,WeekRent,DayRent,Rent,FamilyRent

class TestRents(unittest.TestCase):
    def setUp(self):
        self.an_hour_rent=HourRent(5)
        self.a_day_rent=DayRent(4)
        self.a_week_rent=WeekRent(9)

    def test_hour_rent(self):
        self.assertEqual(25,self.an_hour_rent.fee())

    def test_week_rent(self):
        self.assertEqual(80,self.a_day_rent.fee())
    def test_day_rent(self):
        self.assertEqual(540,self.a_week_rent.fee())
    def test_hour_rent_with_type_error(self):
        self.assertRaises(TypeError,HourRent,"a")
    def test_day_rent_with_type_error(self):
        self.assertRaises(TypeError,DayRent,"a")
    def test_week_rent_with_type_error(self):
        self.assertRaises(TypeError,WeekRent,"a")
class TestFamilyRents(unittest.TestCase):
    def setUp(self):
        self.an_hour_rent=HourRent(5)
        self.a_day_rent=DayRent(4)
        self.a_week_rent=WeekRent(9)
        self.different_family_rents=FamilyRent((self.an_hour_rent,self.a_day_rent,self.a_week_rent))
        self.equal_family_rents=FamilyRent((self.an_hour_rent,self.an_hour_rent,self.an_hour_rent))
    def test_family_rent_different_rents(self):
        self.assertEqual(451.5,self.different_family_rents.total_fee())

    def test_family_rent_equal_rents(self):
        self.assertEqual(52.5,self.equal_family_rents.total_fee())
    def test_family_rent_less_amount_of_rents(self):
        self.assertRaises(ValueError,FamilyRent,(self.a_day_rent,))
    def test_family_rent_more_amount_of_rents(self):
        self.assertRaises(ValueError,FamilyRent,(self.a_day_rent,self.a_day_rent,self.a_day_rent,self.a_day_rent,self.a_day_rent,self.a_day_rent))
    def test_family_rent_no_list_of_rents(self):
        self.assertRaises(TypeError,FamilyRent,5)
    def test_family_rent_list_of_invalid_rents(self):
        self.assertRaises(ValueError,FamilyRent,(5,7))



if __name__=="__main__":
    unittest.main()