import unittest
import datetime
from datetime import datetime, timedelta,date
from typing import Optional, Dict, List

class Individual:
    """ holds an Individual record """
    def __init__(self, _id=None, name=None, sex=None, birt=None, alive=True, deat=False):
        """ store Individual info """
        self.id = _id
        self.name = name
        self.sex = sex
        self.birt : Dict[str, str]= birt
        self.alive = alive
        self.deat: Optional[bool, Dict[str, str]] = deat
        self.famc: List[str] = []
        self.fams: List[str] = []

class Family:
    """ holds a Family record """
    
    def __init__(self, _id=None, marr=None, husb=None, wife=None, div=False,birt=None, deat=False):
        """ store Family info """
        self.id = _id
        self.marr = marr
        self.husb = husb
        self.wife = wife
        self.birt : Dict[str, str]= birt
        self.deat: Optional[bool, Dict[str, str]] = deat
        self.chil: List[str] = []
        self.div: Optional[bool, Dict[str, str]] = div

"""today = datetime.today()"""
today: datetime = datetime.now()
year=timedelta(minutes=0)
def marriage(family: Family) -> bool:
    if family.marr:
        marr_date: datetime = datetime.strptime(family.marr['date'], "%d %b %Y")
        return True if today - marr_date > timedelta(minutes=0)else False
    else:
        return False

def divo(family: Family) -> bool:
    if family.div:
        div_date: datetime = datetime.strptime(family.div['date'], "%d %b %Y")
        return True if today - div_date > timedelta(minutes=0)else False
    else:
        return False

def birth(indi : Individual) -> bool:
    if indi.birt:
        birth_date: datetime = datetime.strptime(indi.birt['date'], "%d %b %Y")
        return True if today - birth_date > timedelta(minutes=0) else False
    else:
        return False

def death(indi : Individual) -> bool:
    if indi.deat:
        death_date: datetime = datetime.strptime(indi.deat['date'], "%d %b %Y")
        return True if today - death_date > timedelta(minutes=0) else False
    else:
        return False

class TestApp(unittest.TestCase):
    def test_dates_before_current(self):
        family = Family(marr={'date': "15 JAN 2019"}) ##marrige date is before current date so result is true 
        self.assertTrue(marriage(family))

        family = Family(div={'date': "15 JAN 2020"}) ##divorse date is before current date so result is true
        self.assertTrue(divo(family))

        Indi = Family(birt={'date': "15 JAN 2021"}) ##Birth date is after current date so result is false
        self.assertFalse(birth(Indi))

        Indi = Family(deat={'date': "15 JAN 2021"}) ##death date is after current date so result is false
        self.assertFalse(death(Indi))

        Indi = Family(birt={'date': "15 JAN 2020"}) ##Birth date is before current date so result is true
        self.assertTrue(birth(Indi))        


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
