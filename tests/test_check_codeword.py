from lib.check_codeword import *

def test_check_codeword_when_correct():
  result = check_codeword('horse')
  assert result == "Correct! Come in."

def test_check_codeword_when_close_1():
  result = check_codeword('home')
  assert result == "Close, but nope."
  
def test_check_codeword_when_close_2():
  result = check_codeword('hoe')
  assert result == "Close, but nope."
  
def test_check_codeword_when_close_3():
  result = check_codeword('he')
  assert result == "Close, but nope."
  
def test_check_codeword_when_wrong_1():
  result = check_codeword('this is wrong')
  assert result == "WRONG!"
  
def test_check_codeword_when_wrong_2():
  result = check_codeword('h')
  assert result == "WRONG!"
  
# def test_check_codeword_when_empty():
#   result = check_codeword('')
#   assert result == "WRONG!"