from ola import KitchenCalculator
def test_calculator():
    # Do not modify this testing wrapper
    calc = KitchenCalculator()
    return list(calc.calculate_inventory())


print(test_calculator())