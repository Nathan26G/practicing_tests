from lib.counter import *

def test_Counter_when_adding_positive_num():
  counter = Counter()
  counter.add(1)
  result = counter.report()
  assert result == f"Counted to {1} so far."
  
def test_Counter_when_adding_negative_num():
  counter = Counter()
  counter.add(-1)
  result = counter.report()
  assert result == f"Counted to {-1} so far."

def test_Counter_when_adding_zero():
  counter = Counter()
  counter.add(0)
  result = counter.report()
  assert result == f"Counted to {0} so far."