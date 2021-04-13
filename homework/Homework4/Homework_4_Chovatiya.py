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

    def age(self):
        """ calculate age using the birth date """
        today = date.today()
        birthday = datetime.strptime(self.birt['date'], "%d %b %Y")
        return birthday

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


def AreIndividualsUnique(individuals: List[Individual]):
    names_bdays = {}
    same_data = []
    for individual in individuals:
        if individual.name in names_bdays:
            if names_bdays[individual.name] == individual.birt["date"]:
                same_data.append([individual.id, individual.name, individual.birt["date"]])
        else:
            names_bdays[individual.name] = individual.birt["date"]

    return same_data
    

class TestApp(unittest.TestCase):
    def test_AreIndividualsUnique(self):

        indi1: Individual = Individual(_id="I1", name="John Doe1", birt={'date':"14 Oct 1990"})
        indi2: Individual = Individual(_id="I2", name="John Doe2", birt={'date':"14 Oct 1990"})
        indi3: Individual = Individual(_id="I3", name="John Doe3", birt={'date':"15 Oct 1990"})
        indi4: Individual = Individual(_id="I4", name="John Doe4", birt={'date':"17 Oct 1990"})
        
        individuals = List[Individual] = [indi1, indi2, indi3, indi4]

        self.assertTrue(AreIndividualsUnique(individuals), [["I2", "John Doe1", "14 Oct 1990"]])
    
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2 )