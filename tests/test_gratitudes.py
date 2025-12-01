from lib.gratitudes import *

def test_gratidute_item_is_added_to_list():
  gratitudes = Gratitudes()
  gratitudes.add('life')
  output = gratitudes.format()
  assert output == 'Be grateful for: life'
  
def test_gratidute_items_are_added_to_list():
  gratitudes = Gratitudes()
  gratitudes.add('life')
  gratitudes.add('family')
  gratitudes.add('friends')
  gratitudes.add('connections')
  output = gratitudes.format()
  assert output == 'Be grateful for: life, family, friends, connections'
  
def test_empty_gratidute_item_is_added_to_list():
  gratitudes = Gratitudes()
  gratitudes.add('')
  output = gratitudes.format()
  assert output == 'Be grateful for: '

def test_empty_gratidute_items_are_added_to_list():
  gratitudes = Gratitudes()
  gratitudes.add('')
  gratitudes.add('')
  gratitudes.add('')
  gratitudes.add('')
  output = gratitudes.format()
  assert output == 'Be grateful for: , , , '