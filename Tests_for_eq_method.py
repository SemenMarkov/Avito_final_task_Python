from cli import Pizza, Margherita, Pepperoni, Hawaiian

new_order1 = Margherita('L')
new_order2 = Margherita('XL')
new_order3 = Pepperoni('L')
new_order4 = Pepperoni('XL')
new_order5 = Hawaiian('L')
new_order6 = Hawaiian('XL')

is_eq1 = (new_order1 == new_order1) # True
is_eq2 = (new_order1 == new_order2) # False

is_eq3 = (new_order3 == new_order3) # True
is_eq4 = (new_order3 == new_order5) # False

is_eq5 = (new_order5 == new_order5) # True
is_eq6 = (new_order5 == new_order1) # False

if __name__ == '__main__':
    print(is_eq1)
    print(is_eq2)
    print(is_eq3)
    print(is_eq4)
    print(is_eq5)
    print(is_eq6)
