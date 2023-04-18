# **Throwback Developments - Introduction**
Throwback Developments is a fully functioning E-Commerce store for retro vehicle parts, utilising Stripe as the payment processor. The site was built in Django using HTML, CSS, Javascript, Python and the Bootstrap libraries, incorporating user authentication and full CRUD functionality for the management of products. For the purposes of this project, the site does not take real card payments and a test card number has been set up:

Card number - 4242 4242 4242 4242 

Expiration date - any future date

CVC - any three-digits

Postcode or zipcode - any five-digits

[Throwback Developments](https://********.herokuapp.com/) - The live site can be viewed here.


## **TABLE OF CONTENTS**

 - [**Business Strategy**](#business-strategy)
    * [Business Model](#business-model)
    * [Web Marketing](#web-marketing)
    * [Search Engine Optimisation](#search-engine-optimisation)
 - [**User Experience (UX)**](#user-experience)
    * [User Stories](#user-stories)
    * [Agile Methodology](#agile-methodology)
    * [The Scope](#the-scope)
 - [**Design**](#design)
    * [Colours](#colours)
    * [Typography](#typography)
    * [Media](#media)
    * [Wireframes](#wireframes)
    * [Database Schema](#database-schema)
 - [**Features**](#features)

<hr>

 ## **BUSINESS STRATEGY**

### **Business Model**

### **Web Marketing**

### **Search Engine Optimisation**

 ## **USER EXPERIENCE (UX)**

### **User Stories**

- #### **Unregistered site user:**

   - As a user, I can quickly understand the sites purpose and navigate through the sites content easily, without any confusion.
   - As a user, I can view a list of featured products on the landing page with clearly visible images, titles and prices.
   - As a user, I can subscribe to a Newsletter with my email address and receive updates and offers.
   - As a user, I can make enquiries via the contact form.
   - As a user, I can click each product to view the product details including price, SKU, category, description, rating and product reviews.
   - As a user, I can organise products in the products list by category, rating in descending order and price in ascending order.
   - As a user, I can easily register for an account which stores my name and address details once completed.

- #### **Regsitered site user:**

   - As a user, I am able to receive a confirmation email once my account has been registered.
   - As a user, I can add products I like to my wishlist and remove products no longer required.
   - As a user, I can easily log in and log out of my account and receive a pop up message alert to notify me of the action.
   - As a user, I can add product reviews and ratings to products I have purchased so that others can see my experience.
   - As a user, I can access my account information to view my order history including the order number, date purchased and products purchased.

- #### **Shopping site user:**

   - As a user, I have access to all of the above features.
   - As a user, I can add products to my basket so I am able to get a total cost of all the parts I am interested in.
   - As a user, I can easily view my order summary including my saved account details and my basket contents before entering my payment details without any confusion.
   - As a user, I am able to view a full order confirmation once a payment has been submitted and receive a message informing me my order confirmation email has been sent.

- #### **Site Admin/Superuser:**

   - I can quickly and easily add new products to the store via the admin tools menu in the navbar.
   - I can edit a products title, description or image via the product listing page and product details page, so that I can effectively maintain the shop.
   - I can remove products from the site via the product listing page or product details page.
   - I can update the products that appear in the featured products section.
   - I can view messages sent through the sites contact form via the admin panel.

### **Agile Methodology**

### **The Scope**

#### **The Site's Main Goals:**

<hr>

## **DESIGN**


### **Colours**


### **Typography**


### **Wireframes**
Wireframes for each page are linked here:

[Home Page](docs/read-me/home-page.png)

[All Products Page](docs/read-me/all-products.png)

[Product Details Page](docs/read-me/product-details.png)

[Shopping Basket Page](docs/read-me/basket.png)

[Order Checkout Page](docs/read-me/checkout-page.png)

[Order Confirmation Page](docs/read-me/order-confirmation.png)

[Account Signup Page](docs/read-me/signup.png)

[Account Login Page](docs/read-me/login.png)

[Contact Page](docs/read-me/contact-page.png)


### **Database Schema**
![Database Schema](docs/read-me/data-schema.png)



## **FEATURES**

<hr>

### **Existing Features**

- #### **Navigation Bar**

   - The navigation bar is located at the top of the page on every page of the site and contains the site Logo on the left hand portion, the search bar in the center and the wishlist, user account and basket menu icons on the right. Below these are the menu icons for the home page, the product categories and the contact us pages. 

   - The navbar is fixed to the top of the screen when users scroll down the page, this allows users to easily navigate through the menu icons to quickly find what they are looking for without the need to scroll back to the top of the page.

   - The basket menu icon updates the basket total when products are added so users are able to see the total cost of the basket content while browsing the site.

   - Drop down menu links were used to further improve the navigation of the product categories, allowing users to define which specific type of product they would like to view.

   - Unregistered users are prompted to register or login when the wishlist or user account icons are selected.

![Desktop navbar](docs/read-me/navbar-sc.png)

- #### **Mobile Navbar**

   - The navbar is fully responsive and on smaller device screens the logo image disappears and the home page, product categories and contact page links are collapsed into a toggler menu. The search bar is reduced to a search icon and sits next to wishlist, user account and basket menu icons.

![Mobile navbar](docs/read-me/mobile-nav-sc.png)

- #### **Footer**

   - Located at the bottom of the each page is the footer which contains 2 sections. The upper section has an email field to allow users to subscribe to the site's newsletter.

   - The lower section contains menu icons for the site's Privacy Policy and Contact page on the left side and links to the Throwback Developments Facebook, Youtube, Instagram and Linkedin social media accounts on the right side.

![Footer](docs/read-me/footer-sc.png)

- #### **Home Page**

   - When user's land on the home page they are presented with a hero image with a link to view all products. The image used for the hero image is a stylish representation of the products that Throwback Developments specialises in, giving the user a clear sense of the site's purpose.

   - 

![Home Page](docs/read-me/home-sc.png)
