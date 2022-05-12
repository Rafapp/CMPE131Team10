## Functional Requirements

1. Login (Rafael)
2. Logout (Rafael)
3. Signup (Rafael)
4. Responsive home page (Rafael)
5. Profile information page: Log out, Return home, Delete account (Rafael)
6. Add items to cart, view cart (Mohammad)
7. Search items on item database (Mohammad)
8. Display item information and picture upon search (Mohammad)
9. Post product in item database (Mohammad)
10. Loading screen/splash page (Umesh)
11. Rate a purchased item in cart (Umesh)
12. Register as seller on seller registration page (Umesh)

## Non-functional Requirements

1. Response time for home page under 10 seconds with a 10 mbps network with modern computer (Umesh)
2. Search time after input for search, must show all items with pictures under 5 seconds with 10mbps network, and modern computer (Mohammad)
3. UI interactive interface with animations and effects using bootstrap (HP) (Rafael)
4. Official support for google chrome (Umesh)

## Use Cases

1. Login (Rafael)
- **Pre-condition:** Splash page has loaded, home page has completely loaded and user is active in the page

- **Trigger:** User clicks the "Log in" button in the navbar at the top of the page

- **Primary Sequence:**
  
  1. The log-in button is clicked
  2. A request for the login page is sent to the server
  3. The request is received by the user's computer
  4. The webpage loads completely
  5. The user enters his e-mail using his keyboard and typing inside the e-mail text box
  6. The user enters his password using his keyboard and typing inside the e-mail text box
  7. The log in button is pressed
  8. The information is processed by the server, and the account information matches
  9. The user is returned to the home page and his account is considered as signed in


- **Primary Postconditions:** The user's account is considered as signed in, which enables other services of the platform like creating products, and changing account settings

- **Alternate Sequence:**
  Inexistent account / wrong information: There is no match in the sign up database to the provided information, then:
  1. Log-in error message is flashed
  2. User types in correct information
  3. Primary sequence is completed

2. Profile information page (Rafael)
- **Pre-condition:** User is currently logged in with a complete account

- **Trigger:** User clicks the "Account information" button in the navbar

- **Primary Sequence:**
  1. The account information button is clicked
  2. A request for the account information page is sent to the server
  3. The request is received by the user's computer
  4. The webpage loads completely

  If Return home button is pressed:
  1. A request for the home page is sent to the server
  2. The request is received by the user's computer
  3. The home page is completely loaded

  If Log out button is pressed:
  1. The log-in status is disabled on the system, which disables other services of the platform like creating products, and changing account settings
  2. A request for the home page is sent to the server
  3. The request is received by the user's computer
  4. The home page is completely loaded

  If Delete account button is pressed:
  1. The currently signed in account information is queried on the database
  2. The database entry is deleted from the user database
  3. The log-in status is disabled on the system, which disables other services of the platform like creating products, and changing account settings
  4. A request for the home page is sent to the server
  5. The request is received by the user's computer
  6. The home page is completely loaded
  7. "Your account was successfully deleted" message is flashed in the page

- **Primary Postconditions:** 
  Option A: The user was able to return home, and the webpage is loaded successfully
  Option B: The user was succesful in logging out, and must sign in to activate account features
  Option C: The account is deleted from the database for eternity

- **Alternate Sequence:**
  If the user isn't logged in:
  1. User is redirected to the home page
  2. "Log in to access account information" message is flashed



3. Add item for sale (Umesh)
- **Pre-condition:** User has to be logged in as a seller. Buyers accounts will not see this option.

- **Trigger:** A click on the “Add Item” button located under “options” on the top-right corner of the page. 

- **Primary Sequence:**
  
  1. Systems prompts the seller to enter details regarding the item. Seller has to give:
	a. Name
	b. Description of item
	c. Quantity
	d. Cost per item
	e. Photo (optional)
  2. Seller enters all the required information.
  3. System stores a new record of the added items.
  4. System checks if the seller is fruad. (If seller rating is less than 2 out of 5, seller is a fruad)
  5. If the seller is not fruad, system puts these items on display for the buyers (on buyer's page). 
  6. Seller logs out of the system.

- **Primary Postconditions:** A record of sellers' additions was created. The items were also added on the buyer page so that people can start buying these items. 

- **Alternate Sequence:**
  
  Wrong account error: If the user is not logged in from his seller account, ask him to log in through his seller account because buyers can't sell items.
  
  Fruad Seller error: If the seller is a fruad, systems gives directions on how they can improve their rating to avoid being considered fruad.



4. Item rating (Umesh)
- **Pre-condition:** User has to be logged in as a customer. Sellers can't review their own items. Item has to already bought by the user within last 30 days.

- **Trigger:** A click on the “Rate Me" button next to the item's name located in user's buying history. 

- **Primary Sequence:**
  
  1. System prompts the user to give a star rating from 0 to 5.
  2. System asks the user to fill an optional text box stating the reason why they liked/disliked the item.
  3. After the user submits this text box, the user is redirected to the home page.
  4. This review can now be viewed under item's "reviews" section.
  5. The ratings the item and seller get updated on the system and also on the "buy" page.
  6. User logs out of the system.

- **Primary Postconditions:** The ratings of the item and seller get updated according to the review.

- **Alternate Sequence:**
  
  Wrong account error: If the user is not logged in from his buyer account, ask him to log in through his buyer account because sellers can't rate items.

  Time Period to Rate Expired: If the item got delivered to the user more than 30 days ago, the user can no longer rate the item. Display a useful message if the user tries to rate an item that he bought more than 30 days ago.  

5. Item search (Mohammad)
- **Pre-condition:**

Click on the search bar

- **Trigger:**

Click on the search button 

- **Primary Sequence:**

   1. Click on search bar
   2. Enter the name of item 
   3. Click the search button

- **Primary Postconditions:**

Display a list of available items with that name 

- **Alternate Sequence:** 

  If there are no items with the name, display that there are no items with that name.



6. Cart system (Mohammad)

- **Pre-condition:**

Be signed in to your account

- **Trigger:**

Click add to cart/ checkout cart

- **Primary Sequence:**
 main

1.When there's a desired item click add to cart
2.Item then gets sent to cart
3.Click view cart

- **Primary Postconditions:**

See a list of the items in the cart

- **Alternate Sequence:**
If there are no items in the cart, display that the cart is empty 