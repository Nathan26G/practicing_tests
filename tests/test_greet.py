from lib.greet import *

def test_greet_when_Doug():
  greeting = greet('Doug')
  assert greeting == "Hello, Doug!"
  
def test_greet_when_Bob():
  greeting = greet('Bob')
  assert greeting == "Hello, Bob!"
  
def test_greet_when_David():
  greeting = greet('David')
  assert greeting == "Hello, David!"
  
def test_greet_when_Nathan():
  greeting = greet('Nathan')
  assert greeting == "Hello, Nathan!"