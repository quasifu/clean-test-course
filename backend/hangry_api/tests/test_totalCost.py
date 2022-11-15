from api.controllers import Total
from django_mock_queries.query import MockSet, MockModel

def test_SimpleCost():
  #Arrange
  order = MockSet()
  order.add(MockModel(quantity=5, item=MockModel(price=1.0)))
  order.add(MockModel(quantity=5, item=MockModel(price=1.0)))
  deliveryFee = 5
  #Act
  cost = Total.calculate(order,deliveryFee)
  #Assert
  assert cost == 16.24


def test_ComplexCost():
  #Arrange
  order = MockSet()
  order.add(MockModel(quantity=2, item=MockModel(price=3.5)))
  order.add(MockModel(quantity=1, item=MockModel(price=4.5)))
  deliveryFee = 5
  #Act
  cost = Total.calculate(order, deliveryFee)
  #Assert
  assert cost == 16.24

def test_Boundaries():
  #Arrange
  order = MockSet()
  order.add(MockModel(quantity=2, item=MockModel(price=-3.5)))
  order.add(MockModel(quantity=1, item=MockModel(price=2)))
  deliveryFee = 5
  #Act
  cost = Total.calculate(order, deliveryFee)
  #Assert
  assert cost == 16.24