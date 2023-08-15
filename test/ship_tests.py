import pytest
import sys
sys.path.append(r".\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages")
from src.ship import Ship

def test_ship1(): 
    barco1=Ship(50,1)
    assert barco1.is_worth_it()>20 == True
 