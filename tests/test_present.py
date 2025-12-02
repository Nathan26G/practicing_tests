from lib.present import *
import pytest

def test_wrap_when_contents_is_none():
    present = Present()
    present.wrap('somthing')
    output = present.contents
    assert output == 'somthing'
    
def test_unwrap_when_contents_is_not_none():
    present = Present()
    present.wrap('somthing')
    present.unwrap()
    output = present.contents
    assert output == 'somthing'

def test_wrap_when_contents_is_not_none():
    present = Present()
    present.wrap('somthing')
    with pytest.raises(Exception) as error:
        present.wrap('somthing else')
    error_msg = str(error.value)
    assert error_msg == "A contents has already been wrapped."
    
def test_unwrap_when_contents_is_still_none():
  present = Present()
  with pytest.raises(Exception) as error:
      present.unwrap()
  error_msg = str(error.value)
  assert error_msg == "No contents have been wrapped."