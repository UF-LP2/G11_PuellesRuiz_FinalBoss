from os.path import exists
import pytest
import sys
sys.path.append(r".\G11_PuellesRuiz_FinalBoss")
from src.ships import Ship

def test_ship1(): 
    barco1=Ship(50,1)
    assert (barco1.is_worth_it()>=20 )== True
def test_ship2():
    barco2=Ship(20,1)
    with pytest.raises(Exception):
        barco2.is_worth_it()


