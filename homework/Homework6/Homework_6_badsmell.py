#  The following file contains User Story 1 of sprint 1 which used to check that dates should not after the current dates in GedCom file
#  BadSmell 1: Long method
#  BadSemll 2: Unnecessary complexity which increase code length i.e, reduce number of methods

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

#bad smell : Unnecessary complexity
    def age(self):
        """ calculate age using the birth date """
        today = date.today()
        birthday = datetime.strptime(self.birt['date'], "%d %b %Y")
        return birthday

#bad smell : Unnecessary complexity
    def info(self):
        """ return Individual info """
        alive = True if self.deat is False else False
        death = 'NA' if self.deat is False else self.deat['date']
        child = 'NA' if len(self.famc) == 0 else self.famc
        spouse = 'NA' if len(self.fams) == 0 else self.fams
        return [self.id, self.name, self.sex, self.birt['date'],
                self.age(), alive, death, child, spouse]


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
        #bad smell : Long method
        if today - marr_date > timedelta(minutes=0):
            print(f"✔ ({family.id}): marrige take place before current date ")
            return True
        else:
            print(f"✘ ({family.id}): marrige didn't take place before current date ")

    else:
        print(f"✘ ({family.id}): marrige didn't take place ")


def divo(family: Family) -> bool:
    if family.div:
        div_date: datetime = datetime.strptime(family.div['date'], "%d %b %Y")
        #bad smell : Long method
        if today - div_date > timedelta(minutes=0):
            print(f"✔ ({family.id}): divorce take place before current date ")
            return True
        else:
            print(f"✘ ({family.id}): divorce didn't take place before current date ")

    else:
        print(f"✘ ({family.id}): divorce didn't take place ")


def birth(indi : Individual) -> bool:
    if indi.birt:
        birt_date: datetime = datetime.strptime(indi.birt['date'], "%d %b %Y")
        #bad smell : Long method
        if today - birt_date > timedelta(minutes=0):
            print(f"✔ ({indi.id}): birth take place before current date ")
            return True
        else:
            print(f"✘ ({indi.id}): birth didn't take place before current date ")

    else:
        print(f"✘ ({indi.id}): birth didn't take place ")


def death(indi : Individual) -> bool:
    if indi.deat:
        death_date: datetime = datetime.strptime(indi.deat['date'], "%d %b %Y")
        #bad smell : Long method
        if today - death_date > timedelta(minutes=0):
            print(f"✔ ({indi.id}): death take place before current date ")
            return True
        else:
            print(f"✘ ({indi.id}): death didn't take place before current date ")

    else:
        print(f"✘ ({indi.id}): death didn't take place ")


class TestApp(unittest.TestCase):
    def test_dates_before_current(self):
        family = Family(_id="I21", marr={'date': "15 JAN 2019"}) ##marrige date is before current date so result is true
        self.assertTrue(marriage(family))

        family = Family(_id="I22", div={'date': "15 JAN 2020"}) ##divorse date is before current date so result is true
        self.assertTrue(divo(family))

        Indi = Individual(_id="I23", birt={'date': "15 JAN 2021"}) ##Birth date is after current date so result is false
        self.assertFalse(birth(Indi))

        Indi = Individual(_id="I24", deat={'date': "15 JAN 2021"}) ##death date is after current date so result is false
        self.assertFalse(death(Indi))

        Indi = Individual(_id="I26", birt={'date': "15 JAN 2020"}) ##Birth date is before current date so result is true
        self.assertTrue(birth(Indi))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
