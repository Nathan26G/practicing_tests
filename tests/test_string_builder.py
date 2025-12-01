from lib.string_builder import *

def test_StringBuilder_output_valid_string():
  builder = StringBuilder()
  builder.add('test')
  output = builder.output()
  assert output == 'test'
  
def test_StringBuilder_output_empty_string():
  builder = StringBuilder()
  builder.add('')
  output = builder.output()
  assert output == ''

def test_StringBuilder_length_valid_string():
  builder = StringBuilder()
  builder.add('test')
  length = builder.size()
  assert length == len('test')
  
def test_StringBuilder_empty_valid_string():
  builder = StringBuilder()
  builder.add('')
  length = builder.size()
  assert length == len('')