# **TESTING DOCUMENTATION**

## **TABLE OF CONTENTS**

- [**Manual Testing**](#manual-testing)
    * [User Storys](#user-story-testing)
    * [Lighthouse](#lighthouse)
- [**Validator Testing**](#validator-testing)
    * [HTML](#html)
    * [CSS](#css)
    * [JavaScript](#javascript)
    * [Python](#python)
- [**Bugs and Errors**](#bugs-and-errors)

<hr>

## **MANUAL TESTING**

<br>

### **User Story Testing**

<br>

- #### **User Story:**

        - As a user, I can quickly understand the sites purpose and navigate through the sites content easily, without any confusion. 

    #### **Acceptance Criteria:**
    * The site structure and layout should be clearly understandable and easy to navigate to all users.
    * Unauthenticed users should have restricted access to any pages that require authentication.
    * Unauthenticated users are redirected to registration or log in pages when selected from the navigation menu.

    #### **Actual Results:**
    * User test carried out by peers, friends and family confirmed the site's purpose was clearly understand and easy to navigate.
    * User test carried out by unauthenticated users confirmed pages requiring authentication provided restricted access and were unable to proceed without a registered account.
    * User test carried out by unauthenticated users confirmed log in and registration links redirected to the correct pages on the site.

    #### All Tests: **Passed**

-----

- #### **User Story:**

        - As a user, I can view a list of featured products on the landing page with clearly visible images, titles and prices and redirect users to the product details when clicked. 

    #### **Acceptance Criteria:**
    * The site's Home page should display a list of featured products selected by the site admin.
    * The featured products section of the Home page should display a product image and basic product information to all users.
    * Featured products should redirect all users to the relevant product details when clicked.

    #### **Actual Results:**
    * All users confirmed the Home page displays a selected number of products.
    * All users confirmed each featured product displays a product image and basic product details consisting of product title, price, category, SKU and rating.
    * All users confirmed featured products redirected to the correct product details when clicked.

    #### All Tests: **Passed**

-----

- #### **User Story:**

        - As a user, I can subscribe to a Newsletter with my email address and receive updates and offers. 

    #### **Acceptance Criteria:**
    * The site's footer should be visible at the bottom of every page of the store.
    * The site's footer should contain a Newsletter sign up allowing users to enter an email address. 

    #### **Actual Results:**
    * All users confirmed the footer is present at the bottom of each page of the site.
    * All users confirmed the Newsletter sign up is present in the footer and functions correctly.

    #### All Tests: **Passed**

-----

- #### **User Story:**

        - As a user, I can make enquiries via the contact form. 

    #### **Acceptance Criteria:**
    * The contact form menu links should be clearly visible to all users and redirect to the contact page.
    * The contact form should be well structured and easily understandle.
    * The contact form should allow all users to submit enquiries.
    * A confirmation notification should display to inform users the message has been submitted.
    * Enquiries submitted through the site's contact form should be visible to superusers in the admin panel.

    #### **Actual Results:**
    * All users confirmed the contact page link was easily located and redirected to the correct page.
    * All users confirmed the contact form is well structured, easy to understand and provides adequate information to submit an enquiry.
    * All users confirmed their enquiries were submitted when submit was clicked.
    * All users confirmed a notification pop up message appears to inform them their enquiry was submitted successfully.
    * Superusers confirmed submitted enquiries are visible in the backend admin panel.

    ![Contact Form Success](docs/read-me/screenshots/contact-success.png)

    #### All Tests: **Passed**

-----

- #### **User Story:**

        - As a user, I can click each product on the all products page to view the product details including price, SKU, category, description, rating and product reviews. 

    #### **Acceptance Criteria:**
    * The All Products page should display a list of all the available products to all users.
    * Each product should redirect to the appropriate product details page when clicked.
    * The Product Details page should clearly display the product image and detailed product information.
    * The product review section should be visible below the product information to all users.

    #### **Actual Results:**
    * All users confirmed all products are visible in a clear and readable layout.
    * All users confirmed clicking a product successfully redirected to the appropriate product details page.
    * All users confirmed the product details page displayed a clear image and the product information was clearly displayed and easy to read.
    * All users confirmed the product reviews section was displayed below the product information.

    #### All Tests: **Passed**

-----

- #### **User Story:**

        - As a user, I can organise products in the products list by category, rating in descending order and price in ascending order. 

    #### **Acceptance Criteria:**
    * All site users should be able to filter products by category in ascending order.
    * All site users should be able to filter products by price in ascending order.
    * All site users should be able to filter products by its rating in descending order.

    #### **Actual Results:**
    * All users confirmed filtering products by category displayed products in A-Z category order.
    * All users confirmed filtering products by price displayed products from lowest to highest price.
    * All users confirmed filtering products by product rating displayed product ratings starting from highest to lowest.

    #### All Tests: **Passed**

-----

- #### **User Story:**

        - As a user, I can filter products via the search function at the top of the page. 

    #### **Acceptance Criteria:**
    * The Search function should be visible at the top of every page on the site.
    * The Search function should display search results relevant to the searched term.

    #### **Actual Results:**
    * All users confirmed the search bar is visible at the top of each page on the site.
    * All users confirmed the returned search results displayed the correct products matching the search term.

    #### All Tests: **Passed**

-----

- #### **User Story:**

        - As a user, I can easily register for an account and receive an account registration confirmation email to confirm my account. 

    #### **Acceptance Criteria:**
    * Unauthenticated users should be able to easily navigate to the account registration page.
    * Unauthenticated users can enter their details and register for an authenticated user account.
    * Unauthenticated users receive an account registration confirmation notification and email.

    #### **Actual Results:**
    * Users confirmed the account registration was easy to navigate and redirected to the account registration page when clicked.
    * Users confirmed the account registration process is user friendly.
    * Users confirmed a notification pop up message displayed to confirm their account was register successfully and an email confirmation was received.

    ![Account Registration Email](docs/read-me/screenshots/registration-email.png)

    #### All Tests: **Passed**

-----

- #### **User Story:**

        - As a user, I can easily log in and log out of my account and receive a pop up message alert to notify me of the action. 

    #### **Acceptance Criteria:**
    * Unauthenticated users should be able to navigate to the log in page via the navigation menu.
    * Authenticated users should receive a pop-up notification confirming they have logged in successfully.
    * Authenticated users should receive a pop-up notification confirming they have logged out successfullly.

    #### **Actual Results:**
    * Users confirmed the log in menu link redirects to the account log in page successfully.
    * Users confirmed a pop-up notification message displayed to confirm their log in was successful.
    * Users confirmed a pop-up notification message displayed to confirm their account log out was successful.

    ![Log In Sucess](docs/read-me/screenshots/log-in-success.png)
    ![Log Out Success](docs/read-me/screenshots/log-out-success.png)

    #### All Tests: **Passed**

-----

- #### **User Story:**

        - As a user, I can add products I like to my wishlist and remove products no longer required.

    #### **Acceptance Criteria:**
    * Authenticated users can navigate to their wishlist via the navigation menu.
    * The Wishlist page displays a list of products added by the user.
    * Authenticated users are able to remove products from their wishlist.
    * Authenticated users should receive a pop-up notification message confirming if a product is added or removed from the wishlist.

    #### **Actual Results:**
    * Authenticated users confirmed clicking the Wishlist menu redirected to the Wishlist page. Unauthentiated users confirmed this functionality is restricted without an authenticated account.
    * Authenticated users confirmed the Wishlist page displays products added by the user.
    * Authenticated users confirmed products can be easily removed from the wishlist.
    * Authenticated users confirmed a pop-up notification message displayed when a product is added or removed from the wishlist.

    ![Wishlist Added](docs/read-me/screenshots/wishlist-added.png)
    ![Wishlist Removed](docs/read-me/screenshots/wishlist-removed.png)

    #### All Tests: **Passed**

-----

- #### **User Story:**

        - As a user, I can add product reviews and ratings to products I have purchased so that others can see my experience. 

    #### **Acceptance Criteria:**
    * What should happen

    #### **Actual Results:**
    * Results

    #### All Tests: **Passed**

-----

- #### **User Story:**

        - As a user, I can filter products via the search function at the top of the page. 

    #### **Acceptance Criteria:**
    * What should happen

    #### **Actual Results:**
    * Results

    #### All Tests: **Passed**

-----

<br>

### **LIGHTHOUSE TESTING**

<br>

- #### **Home Page**
Device | Result |
--- | --- |
Desktop | <img src="docs/read-me/lighthouse/dtop-home.png" width="250">
Mobile | <img src="docs/read-me/lighthouse/mob-home.png" width="250">

<br>

---

- #### **Product List Page**
Device | Result |
--- | --- |
Desktop | <img src="docs/read-me/lighthouse/dtop-prod-list.png" width="250">
Mobile | <img src="docs/read-me/lighthouse/mob-prod-list.png" width="250">

<br>

---

- #### **Product Details Page**
Device | Result |
--- | --- |
Desktop | <img src="docs/read-me/lighthouse/dtop-prod-det.png" width="250">
Mobile | <img src="docs/read-me/lighthouse/dtop-prod-det-fix.png" width="250">

<br>

---

- #### **Contact Page**
Device | Result |
--- | --- |
Desktop | <img src="docs/read-me/lighthouse/dtop-contact.png" width="250">
Mobile | <img src="docs/read-me/lighthouse/mob-contact.png" width="250">

<br>

---

- #### **Basket Page**
Device | Result |
--- | --- |
Desktop | <img src="docs/read-me/lighthouse/dtop-basket.png" width="250">
Desktop | <img src="docs/read-me/lighthouse/dtop-basket-fix.png" width="250">
Mobile | <img src="docs/read-me/lighthouse/mob-prod-list.png" width="250">

<br>

---

- #### **Checkout Page**
Device | Result |
--- | --- |
Desktop | <img src="docs/read-me/lighthouse/dtop-checkout.png" width="250">
Mobile | <img src="docs/read-me/lighthouse/mob-checkout.png" width="250">

<br>

---

- #### **Checkout Sucess Page**
Device | Result |
--- | --- |
Desktop | <img src="docs/read-me/lighthouse/dtop-checkout-success.png" width="250">
Mobile | <img src="docs/read-me/lighthouse/mob-checkout-success.png" width="250">

<br>

---

- #### **Add Products Page**
Device | Result |
--- | --- |
Desktop | <img src="docs/read-me/lighthouse/dtop-admin.png" width="250">
Mobile | <img src="docs/read-me/lighthouse/mob-admin.png" width="250">

<br>

---

- #### **My Profile Page**
Device | Result |
--- | --- |
Desktop | <img src="docs/read-me/lighthouse/dtop-profile.png" width="250">
Mobile | <img src="docs/read-me/lighthouse/mob-contact.png" width="250">

<br>

---

- #### **Log in Page**
Device | Result |
--- | --- |
Desktop | <img src="docs/read-me/lighthouse/dtop-login.png" width="250">
Mobile | <img src="docs/read-me/lighthouse/mob-login.png" width="250">

<br>

---

- #### **Register Account Page**
Device | Result |
--- | --- |
Desktop | <img src="docs/read-me/lighthouse/dtop-register.png" width="250">
Mobile | <img src="docs/read-me/lighthouse/mob-register.png" width="250">

<br>

---

- #### **Sign out Page**
Device | Result |
--- | --- |
Desktop | <img src="docs/read-me/lighthouse/dtop-log-out.png" width="250">
Mobile | <img src="docs/read-me/lighthouse/mob-logout.png" width="250">

<hr>

## **VALIDATOR TESTING**

- ### **HTML**

[HTML](https://validator.w3.org/nu/#textarea) HTML validation provided no errors for all 15 HTML files; basket.html, checkout.html, checkout_success.html, contact.html, enquiry_confirm.html, index.html, add_product.html, edit_product.html, product_details.html, wishlist.html, profile.html, footer.html, main-nav.html, mobile-top-header.html and base.html.

File | Result | Evidence | 
--- | --- | --- |
templates/base.html | Pass | [base.html Validation](docs/read-me/testing/w3c-base-html.png)
templates/basket.html | Pass | [basket.html Validation](docs/read-me/testing/w3c-basket-html.png)
templates/checkout.html | Pass | [checkout.html Validation](docs/read-me/testing/w3c-checkout-html.png)
templates/checkout-success.html | Pass | [checkout-success.html Validation](docs/read-me/testing/w3c-checkout-success-html.png)
templates/contact.html | Pass | [contact.html Validation](docs/read-me/testing/w3c-contact-html.png)
templates/enquiry-confirm.html | Pass | [enquiry-confirm.html Validation](docs/read-me/testing/w3c-enquiry-confirm-html.png)
templates/index.html | Pass | [index.html Validation](docs/read-me/testing/w3c-index-html.png)
templates/add-product.html | Pass | [add-product.html Validation](docs/read-me/testing/w3c-add-product-html.png)
templates/edit-product.html | Pass | [edit-product.html Validation](docs/read-me/testing/w3c-edit-product-html.png)
templates/product-details.html | Pass | [product-details.html Validation](docs/read-me/testing/w3c-product-details-html.png)
templates/wishlist.html | Pass | [wishlist.html Validation](docs/read-me/testing/w3c-wishlist-html.png)
templates/profile.html | Pass | [profile.html Validation](docs/read-me/testing/w3c-profile-html.png)
templates/footer.html | Pass | [footer.html Validation](docs/read-me/testing/w3c-footer-html.png)
templates/main-nav.html | Pass | [main-nav.html Validation](docs/read-me/testing/w3c-main-nav-html.png)
templates/mobile-top-header.html | Pass | [mobile-top-header.html Validation](docs/read-me/testing/w3c-mobile-top-header-html.png)

<br>

- ### **CSS**
 
[W3C](https://jigsaw.w3.org/css-validator/#validate_by_input) CSS validation provided no errors for Base, Checkout and Profile CSS files.

File | Result | Evidence | 
--- | --- | --- |
static/css/base.css | Pass | [base.css Validation](docs/read-me/testing/w3c-base-css.png)
static/profiles/css/base.css | Pass | [profile/base.css Validation](docs/read-me/testing/w3c-profile-css.png)
static/checkout/css/checkout.css | Pass | [checkout.css Validation](docs/read-me/testing/w3c-checkout-css.png)

<br>

- ### **JavaScript**

<br>

- ### **Python**

<hr>

## **BUGS AND ERRORS**
