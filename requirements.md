## Functional Requirements

1. Login (Mohammad)
2. Logout (Umesh)
3. Signup (Rafael)
4. Profile information page (Rafael)
5. Cart system (Umesh)
6. Item purchase (Mohammad)
7. Item database, and search frontend (Rafael)
8. Item picture (Umesh)
9. User profile (Umesh)
10. Item rating (Mohammad)
11. Item seller (Mohammad)
12. Loading screen/splash page (Rafael)



## Non-functional Requirements

1. Response time for home page under 10 seconds with a 10 mbps network with modern computer (Umesh)
2. Search time after input for search, must show all items with pictures under 5 seconds with 10mbps network, and modern computer (Mohammad)
3. UI interactive interface with animations and effects using bootstrap (HP) (Rafael)
4. Official support for google chrome (Umesh)



## Use Cases

1. Item purchase (Rafael)
- **Pre-condition:**  User has a registered account, and is logged in

- **Trigger:** User clicks the “buy item” button next to the item

- **Primary Sequence:**
  
  1. Purchase page loads
  2. Total to pay, with taxes is displayed
  3. Payment options are displayed (Paypal or credit/debit)
  4. User completes the purchase 
  5. Confirmation message appears on the site


- **Primary Postconditions:** Receipt is sent via email to the user, and viewed

- **Alternate Sequence:**
  Incomplete login: Due to inexistent account, or no login user is prompted to log in/create account before purchasing.

  Incomplete payment: Due to payment error, error message is displayed, and user redirected to the most recently active page.



2. User profile (Rafael)
- **Pre-condition:** User is currently logged in with a complete account

- **Trigger:** Clicking on the user profile

- **Primary Sequence:**
  
  1. User profile information is displayed
  2. If return button is pressed, user is redirected to most recently active page
  3. If any edit button is clicked, new information can be edited and saved

- **Primary Postconditions:** The user was able to see his account information, and update anything required

- **Alternate Sequence:**
  
  Load error: If the profile could not be correctly loaded, error message is displayed
  
  Profile edit error: If information on the profile could not be edited, error message is displayed



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



6.Cart system (Mohammad)

- **Pre-condition:**

Be signed in to your account

- **Trigger:**

Click add to cart/ checkout cart

- **Primary Sequence:**

1.When there's a desired item click add to cart
2.Item then gets sent to cart
3.Click view cart

- **Primary Postconditions:**

See a list of the items in the cart

- **Alternate Sequence:**

If there are no items in the cart, display that the cart is empty