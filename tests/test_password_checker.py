from lib.password_checker import *
import pytest

def test_valid_password_len_is_true():
  password = PasswordChecker()
  output = password.check('12345678')
  assert output == True
  

def test_invalid_len_error_is_correct():
  password = PasswordChecker()
  with pytest.raises(Exception) as error:
    password.check('banana')
  error_msg = str(error.value)
  assert error_msg == "Invalid password, must be 8+ characters."
  