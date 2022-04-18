## Functional Requirements

 1. Login
 2. Logout
 3. Signup
 4. Profile information page
 5. Cart system
 6. Item purchase
 7. Item database, and search frontend
 8. Item picture
 9. User profile
 10. Item rating
 11. Item seller
 12. Loading screen/splash page

## Non-functional Requirements

 1. Response time for home page under 10 seconds with a 10 mbps network with modern computer
 2. Search time after input for search, must show all items with pictures under 5 seconds with 10mbps network, and modern computer
 3. UI interactive interface with animations and effects using bootstrap (HP)
 4. Official support for google chrome


## Use Cases

 5. Item search
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


 6.Cart system

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
