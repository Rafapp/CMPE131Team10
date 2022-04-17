## <remove all of the example text and notes in < > such as this one>

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
Incomplete login: Due to inexistent account, or no login user is prompted to log in/create account before purchasing.\n
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
  
  Load error: If the profile could not be correctly loaded, error message is displayed\n
Profile edit error: If information on the profile could not be edited, error message is displayed
