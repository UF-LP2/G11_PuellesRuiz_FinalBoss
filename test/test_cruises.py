from os.path import exists
import pytest
import sys
sys.path.append(r".\G11_PuellesRuiz_FinalBoss")
from src.cruise import Cruise

def test_cruise(): 
    crucero1=Cruise(20, 2000, 15)
    assert (crucero1.is_worth_it()>=20) == True
def test_cruise2():
    crucero2=Cruise(45,10,1)
    with pytest.raises(Exception):
        crucero2.is_worth_it()
