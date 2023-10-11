# Python Basics
# -------------
##Section 11: Modules & Packages
### Modules
#### import <module_name>
# pricing.py

def get_net_price(price, tax_rate, discount = 0):
    return price * (1 + tax_rate) * (1 - discount)

def get_tax(price, tax_rate = 0):
    return price * tax_rate

#### syntax: import module_name
import pricing

#### syntax: module_name.function_name()
#### main.py
import pricing

net_price = pricing.get_net_price(
    price = 100,
    tax_rate = .01
)

#### Output: 101.0

#### import <module_name> as new_name
import pricing as selling_price

net_price = selling_price.get_net_price(
    price = 100,
    tax_rate = .01
)

#### from <module_name> import <name>
#### syntax: from module_name import fn1, fn2
from pricing import get_net_price

net_price = get_net_price(price = 100, tax_rate = .01)
print(net_price)

#### from <module_name> import <name> as <new_name>: rename the imported objects
#### syntax: from <module_name> import <name> as <new_name>
from pricing import get_net_price as calculate_net_price

net_price = calculate_net_price(
    price = 100,
    tax_rate = .1,
    discount = .05
)

#### from <module_name> import *: import all object from a module
#### from module_name import *
def get_tax(price):
    return price * .1

from pricing import *
from product import *

tax = get_tax(100)
print(tax)


### Module Search Path
#### Intro
#### syntax:
####    import sys
####
####    for path in sys.path:
####       print(path)
import sys
sys.path.append('d:\\modules\\')
import recruitment
recruitment.hire()
# Hire a new employee...


### __name__ variable
#### What's Python __name__?
if __name__ == '__main__':
    main()

#### Python __name__ variable example
def calculate_tax(price, tax):
    return price * tax


def print_billing_doc():
    tax_rate = 0.1
    products = [{'name': 'Book',  'price': 30},
                {'name': 'Pen', 'price': 5}]

    # print billing header
    print(f'Name\tPrice\tTax')

    # print the billing item
    for product in products:
        tax = calculate_tax(product['price'], tax_rate)
        print(f"{product['name']}\t{product['price']}\t{tax}")


print(__name__)

import billing;

python app.py        # displays __name__ variable: billing

python billing.py    # displays __main__

if __name__ == '__main__':
    print_billing_doc()

# Output:
# Name    Price   Tax
# Book    30      3.0
# Pen     5       0.5


### Packages
##### Importing Packages
##### Syntax: import package.module
##### To access package: package.module.function

import sale.order
import sales.delivery
import sales.billing

sale.order.create_sales_order()
sales.delivery.create_delivery()
sales.billing.create_billing()

##### More concise: import <module> import <function>
from sales.order import create_sales_order
from sales.delivery import create_delivery
from sales.billing import create_billing

create_sales_order()
create_delivery()
create_billing()

##### It is possible to rename when importing:
# main.py
from sales.order import create_sales_order as create_order
from sales.delivery import create_delivery as start_delivery
from sales.billing import create_billing as issue_billing


create_order()
start_delivery()
issue_billing()

# Initializing a Package
# When importing a package, pything executes package in __init__.py as so:
# __init__.py

# default sales tax rate
TAX_RATE = 0.07

# From the main.py file, you can access the TAX_RATE from the sales package as so:
# main.py
from sales import TAX_RATE

print(TAX_RATE)

# It also allows you to automatically import modules from the package:
# __init__.py

# import the order module automatically
from sales.order import create_sales_order

# default sales tax rate
TAX_RATE = 0.07


# When importing the sales package from main.py file, the create_sales_order function will be automatically available:
# main.py
import sales

sales.order.create_sales_order()


# From <package> imprt *
# When used, python will look for the __init__.py file. If it exists, it'll load all modules specified in a specail list called __all__
# __init__.py

__all__ = [
    'order',
    'delivery'
]


# The following will show in main.py:
# main.py
from sales import *


order.create_sales_order()
delivery.create_delivery()

# cannot access the billing modu

# Subpackages
# Subpackages help with organization. Everything about packages is also relevant to subpackages:
# main.py
from sales.order import create_sales_order

create_sales_order()