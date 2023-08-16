from os.path import exists
import pytest
import sys
sys.path.append(r".\G11_PuellesRuiz_FinalBoss")

from src.ship import Cargo

def test_cargo(): 
    cargo1=Cargo(15, 1, 5000, 40)
    assert (cargo1.is_worth_it()>=20) == True
def test_cargo2():
    cargo2=Cargo(55, 1.5,50, 40)
    with pytest.raises(Exception):
        cargo2.is_worth_it()
        