from lib.report_length import *

def test_report_length_of_Dougless():
  result = report_length('Dougless')
  assert result == f"This string was {len('Dougless')} characters long."