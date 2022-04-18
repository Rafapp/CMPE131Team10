## <remove all of the example text and notes in < > such as this one>

## Functional Requirements

Login  (Mohammad)
	Seller
	Customer

Logout (Umesh)

Create new account (Rafa)
	Seller
	Customer

View profile/account options (Rafa)
	Delete account

Cart system (Umesh)

Buy item (HP if we decide to add Paypal API) (Mohammad)
	Payment System

Item search database and frontend (Rafa)
	Search bar
	Item database

Add pictures to items(HP) (Alternatively, paypal API integration) (Umesh)

User profiles (Umesh)

Item rating system (Mohammad)

Add items for sale (Mohammad)

Loading screen / splash page (Rafa)


## Non-functional Requirements

Response time for home page under 10 seconds with a 10 mbps network

Search time after input for search, must show all items with pictures under 5 seconds

UI interactive interface (using bootstrap) (HP)

Official support for google chrome


## Use Cases

1. Item search (Mohammad)
Precondition:
	Click on the search bar

Trigger:
	Click on the search button

Primary sequence:
	Click on search bar
	Enter the name of item
	Click the search button

Primary postconditions:
	See a list of available items with that name

Alternate sequence:
	If there are no items with the name, display that there are no items with that name.

Use Case 2:Cart system (Mohammad)

Precondition:
	Be signed in to your account

Trigger:
	Click add to cart/ checkout cart

Primary sequence:
	When there's a desired item click add to cart
	Item then gets sent to cart
	Click view cart 

Primary postconditions:
	See a list of the items in the cart

Alternate sequence:
If there are no items in the cart, display that the cart is empty

