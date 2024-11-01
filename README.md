# Arduino Lab - E-Commerce Project

## Welcome to Arduino Lab

Arduino Lab is an online shop concept dedicated to Arduino enthusiasts, hobbyists, and makers looking for a variety of Arduino-compatible microcontrollers and accessories. This project showcases a fully functional e-commerce platform built with Django, featuring product listings, cart functionality, user accounts, and secure checkout with simulated payment processing.

This project is the final portfolio submission for the Code Institute Diploma in Fullstack Software Development and serves as a demonstration of full-stack development skills in e-commerce application design.

> **Disclaimer**: This project is intended exclusively for educational purposes and should not be used for real commercial transactions or any unauthorized business or other purposes. The author assumes no responsibility for misuse or adaptation for commercial objectives.

You can explore the live project here: [Arduino Lab](https://arduino-lab-project-ab20ce1e1a15.herokuapp.com/)

## Table of Contents

- [Project Overview](#project-overview)
  - [Agile Workflow](#agile-workflow)
- [User Experience](#user-experience)
  - [Strategy](#strategy)
    - [Primary Goals](#primary-goals)
    - [Business Model](#business-model)
    - [Marketing](#marketing)
    - [Search Engine Optimisation](#search-engine-optimisation)
  - [Structure](#structure)
    - [Pages](#pages)
    - [Pages provided by Django](#pages-provided-by-django)
    - [Technical Design](#technical-design)
      - [Code Structure](#code-structure)
      - [Database](#database)
      - [Data Models](#data-models)
      - [Schema of models](#schema-of-models)
  - [Scope - Epics and User Stories](#scope-epics-and-user-stories)
  - [Project Setup](#project-setup)
    - [Epic 1: Django Project Initialization](#django-project-initialization)
    - [Epic 2:Install Required Packages](#install-required-packages)
    - [Epic 3:Setup Admin Panel for Store Management](#setup-admin-panel-for-store-management)
    - [Epic 4:User Authentication Setup](#user-authentication-setup)
    - [Epic 5:E-commerce App Creation](#e-commerce-app-creation)
    - [Epic 6:Database Configuration](#database-configuration)
    - [Epic 7:Static and Media Files Configuration](#static-and-media-files-configuration)

  - [Project Implementation](#project-implementation)
    - [Epic 1:Product Search and Browsing](#product-search-and-browsing)
    - [Epic 2:Detailed Product Information](#detailed-product-information)
    - [Epic 3:Shopping Cart](#shopping-cart)
    - [Epic 4:Account Creation](#account-creation)
    - [Epic 5:Secure Payment](#secure-payment)
    - [Epic 6:Order Confirmation](#order-confirmation)
    - [Epic 7:Product Filtering](#product-filtering)
    - [Epic 8:Product Reviews](#product-reviews)
    - [Epic 9:Create a Comprehensive README File](#create-a-comprehensive-readme-file)
    - [Epic 10:Deployment to Heroku](#deployment-to-heroku)

  - [Skeleton](#skeleton)
    - [Wireframes](#wireframes)
  - [Surface](#surface)
    - [Colors](#colors)
    - [Design Choices](#design-choices)
    - [Typography](#typography)
- [Existing Features](#existing-features)
  - [Feature 1: The Navbar](#feature-1-the-navbar)
  - [Feature 2: The Home Page](#feature-2-the-home-page)
  - [Feature 3: The Footer](#feature-3-the-footer)
  - [Feature 4: The Products List](#feature-4-the-products-list)
  - [Feature 5: The Product Detail Page](#feature-5-the-product-detail-page)
  - [Feature 6: The Cart](#feature-6-the-cart)
  - [Feature 7: The Checkout Page](#feature-7-the-checkout-page)
  - [Feature 8: The Order Successful Page](#feature-8-the-order-successful-page)
  - [Feature 9: The Sign Up/In/Out Pages](#feature-9-the-sign-up-in-out-pages)
  - [Feature 10: My Arduino Lab](#feature-10-my-arduino-lab)
  - [Feature 11: The Wishlist](#feature-11-the-wishlist)
  - [Feature 12: The Contact Page](#feature-12-the-contact-page)
  - [Feature 13: The Admin Features](#feature-13-the-admin-features)
  - [Feature 14: The Django Admin](#feature-14-the-django-admin)
- [Features Yet to Implement](#features-yet-to-implement)
- [Technologies Used](#technologies-used)
  - [Languages](#languages)
  - [Frameworks, Libraries and Other Resources](#frameworks-libraries-and-other-resources)
- [Testing](#testing)
- [Other Services](#other-services)
  - [Stripe](#stripe)
- [Deployment](#deployment)
  - [Forking the GitHub Repository](#forking-the-github-repository)
  - [Making a Local Clone](#making-a-local-clone)
  - [Heroku](#heroku)
  - [AWS S3](#aws-s3)
- [Performance](#performance)
- [Validation](#validation)
- [Accessibility](#accessibility)
- [Bugs](#bugs)
- [Credits](#credits)
  - [Copyrights](#copyrights)
    - [Media](#media)
    - [Content](#content)
  - [Coding Tips and Tricks](#coding-tips-and-tricks)
  - [Acknowledgments](#acknowledgments)

---

## Project Overview

**Arduino Lab** is an online store designed to meet the needs of hobbyists, students, and professionals working with Arduino and other electronics projects. The platform provides a wide range of microcontrollers like: Arduino , ESP32, RPi,STM32 and other, making it a one-stop shop for DIY electronics enthusiasts. 

The project is built with the **Django** web framework, combining a robust backend with dynamic and user-friendly frontend features. This online shop is structured to be highly modular and scalable, supporting future enhancements like additional product categories, user accounts, and more extensive e-commerce functionalities.

### Key Features

- **Product Catalog**: A categorized, searchable list of products, each with detailed descriptions, specifications, and pricing.
- **User Registration and Account Management**: Users can register, log in, and manage their accounts, including viewing order history and updating profile information.
- **Shopping Cart and Checkout**: A secure, streamlined shopping experience with cart management and integrated payment options.
- **Admin Dashboard**: Site administrators can manage products, orders, and user accounts, with full access to the backend database via the Django admin interface and site interface.

### Technologies Used

- **Django**: As the primary web framework, Django enables rapid development, scalability, and maintainability.
- **Bootstrap 4**: For responsive and modern design, ensuring the shop is accessible and attractive on any device.
- **PostgreSQL**: A robust relational database for storing user, product, and order information.
- **Stripe API**: Integrated for secure payment processing, supporting a smooth checkout process.
- **AWS S3**: For storing and serving media files efficiently.

### Agile Development

## Agile Workflow

For this project, an agile approach was used to manage tasks effectively and ensure a smooth development process. The workflow was structured using GitHub Projects to track and visualize progress. The following boards represent the project's tasks, organized in columns for **Todo**, **In Progress**, and **Done** stages.

### Project Setup Board

This board includes initial setup tasks required to build the foundation of the application. The completed tasks for project setup are:

- Django Project Initialization
- Install Required Packages
- Setup Admin Panel for Store Management
- User Authentication Setup
- E-commerce App Creation
- Database Configuration
- Static and Media Files Configuration

![Project Setup Board](media/documentations/agile2.PNG)

### Project Development Board

This board tracked the primary development tasks for the e-commerce functionalities of **Arduino Lab**. Key tasks included:

- Product Search and Browsing
- Detailed Product Information
- Shopping Cart
- Account Creation
- Secure Payment
- Order Confirmation
- Product Filtering
- Product Reviews
- Create a Comprehensive README File
- Deployment to Heroku

![Project Development Board](media/documentations/agile1.PNG)

This agile structure facilitated organized development, allowed monitoring of project progress, and provided visibility into tasks yet to be completed or those in the pipeline. This approach enabled incremental development, delivering features in manageable portions, and adjusting priorities as needed.

### User Experience

#### Strategy

##### Primary Goals
- **Arduino Lab**
Welcome to Arduino Lab – Unleash Your Creativity with Our Latest Microcontroller Collection! Dive into the world of innovation and discover powerful microcontrollers designed for your next project.
Arduino Lab  aims to be a specialized online store dedicated to selling microcontrollers, specifically tailored for electronics enthusiasts and professional developers. The platform focuses exclusively on offering a wide range of microcontrollers, including popular models such as ESP, STM, AVR, and more.
- The primary goal is to provide users with a seamless shopping experience for microcontrollers, offering advanced search and filtering options based on specifications and categories, along with secure payment processing.

## Strategy

### Primary Goals
1. **Product Availability**: Offer a wide range of microcontrollers and related components, catering to both beginner and advanced makers.
2. **User Engagement**: Encourage customers to explore, learn, and experiment with various microcontroller platforms.
3. **Customer Satisfaction**: Provide a seamless shopping experience, quick support, and informative resources to assist users with their projects.
4. **Sales Growth**: Increase sales through effective marketing, special offers, and loyalty programs.

### Business Model
Arduino Lab is an e-commerce platform focused on selling microcontrollers, development boards, and accessories. The primary products include items from categories such as **AVR**, **ARM**, **ESP**, **Raspberry Pi**, **MSP430**, and **8051**. Key elements of the business model include:

- **Revenue Model**: Product sales with a focus on bundle offers, cross-selling, and upselling.
- **Free Delivery**: For orders over $50, incentivizing higher purchase values.
- **Educational Resources**: Provide learning materials and tutorials to support customers' projects and drive engagement.

### Marketing
1. **Target Audience**:
   - Electronics hobbyists, students, and professionals working on embedded systems and IoT projects.
2. **Promotional Offers**:
   - Highlight special deals and seasonal discounts to attract and retain customers.
3. **Content Marketing**:
   - Publish articles, project ideas, and tutorials to inspire customers and position Arduino Lab as a resourceful learning hub.
4. **Email Marketing**:
   - Use email campaigns to inform customers of new arrivals, special offers, and educational content.
    ![Subscription option ](media\documentations\subscribe.PNG) 

### Search Engine Optimization
- **SEO Strategy**: To increase visibility, Arduino Lab will implement SEO practices, including keyword optimization for terms related to microcontrollers, technical specifications, and DIY electronics. The website will be structured with descriptive meta tags, optimized product descriptions, and relevant keywords to improve search rankings and reach a broader audience in the electronics and developer communities.
Arduino Lab is aimed at becoming a trusted source for Arduino and electronics supplies, combining a clean design with efficient backend operations to deliver an enjoyable shopping experience.
1. **Keyword Strategy**:
   - Use keywords relevant to microcontroller brands, electronics projects, tutorials, and related accessories.
2. **On-Page SEO**:
   - Optimize page titles, meta descriptions, and headings for better visibility in search engine results.
3. **Product Descriptions**:
   - Include detailed, keyword-rich descriptions of products to improve ranking and inform potential buyers. 
    ![SEO ](media\documentations\meta_tags.PNG) 
4. **Content SEO**:
   - Regularly publish informative articles, tutorials, and guides to drive organic traffic.
   
5. **Social Media Marketing**
   - **Facebook Page**: Engage with our audience by sharing educational content, project ideas, and promotions. We will also create interactive posts such as polls, live Q&A sessions, and giveaways to increase engagement.
         ![Footer with social media ](media\documentations\social_account.PNG) 
            ![Facebook page ](media\documentations\FACEBOOK_PAGE.PNG) 

6. **Email Marketing**
   - Build a subscriber list by offering valuable content like project tutorials and special discounts.
   - Run regular email campaigns with promotions, new product launches, and exclusive offers to engage our customer base and encourage repeat purchases.
   ![Subscription option ](media\documentations\subscription1.PNG) 
7. **Collaborations & Partnerships**
   - Partner with educational institutions, makerspaces, and electronics hobbyist communities to promote our products as tools for learning and innovation.
   - Collaborate with influencers in the electronics and maker communities to review our products and create project videos.
      ![Colaboration and Partnerships ](media\documentations\Colaboration.PNG) 
## Structure

### Pages

1. **Home Page**: Welcomes users to Arduino Lab, showcases the latest microcontroller collection, and includes a prominent call-to-action button ("Shop Now") for easy navigation.
![Main page](media\mainPage.PNG)
2. **Product Categories**:
   - **All Items**: Lists all products available in the store. ![All items](media\all_items.PNG)
   - **AVR, ARM, ESP, Raspberry Pi, MSP430, 8051**: Individual pages dedicated to each microcontroller type. ![Microcontrollers](media\microcontrollers.PNG)
   - **Special Offers**: Highlights any active promotions or discounts.
3. **Search**: A search bar at the top allows users to find specific products quickly. ![Search bar](media\search_bar.PNG)
4. **Cart & Checkout**: Provides a seamless shopping and payment process. ![Cart and Checkout](media\shop_bag.PNG)
5. **Account Management**:
   - **My Account**: User login, profile management, and order history.

### Pages Provided by Django

1. **Login/Logout**: Allows users to sign in or out of their accounts.  ![Login page ](media\sign_in.PNG) ![Logout page ](media\sign_out.PNG) 
2. **User Registration**: Page for new users to create accounts. ![Registration page ](media\register.PNG)
3. **Password Reset**: Helps users recover their accounts if they forget their passwords.
4. **Admin Panel**: Django's default admin panel for managing products, orders, and users. ![Store setting page ](media\store_settings.PNG)

## Technical Design

### Code Structure

The **Arduino Lab** project is organized following Django's standard MVC (Model-View-Controller) structure, allowing for a clear separation of responsibilities. This structure helps with scalability, maintainability, and collaboration across different parts of the project.

#### Code Structure

The codebase for **Arduino Lab** is divided into modular Django apps, following Django’s best practices to separate functionality across the different areas of the project.

- **Home** - Provides the basic functionality for the homepage, displaying the welcome message, featured products, and navigation options.
  
- **Products** - Manages all functionality related to the products, including listing, filtering by category, and product details. This app supports various microcontrollers like ESP, STM, AVR, ARM, and Raspberry Pi.

- **Cart** - Implements shopping cart functionality, allowing users to add products, update quantities, and view their cart before proceeding to checkout.

- **Checkout** - Handles the checkout process, including order summary, payment processing, and order confirmation.

- **Profiles** - Manages user profiles, order history, and personal details for logged-in users. This feature is branded as "My Arduino Lab."

- **User Account** - Allows users to manage their accounts, including account deletion and authentication functionalities provided by Django allauth.

**Other Directories and Files**

- **static/** - Contains CSS, JavaScript, and other static assets used across the project.
  
- **media/** - Stores images for the development environment. In production, images are hosted separately on a cloud storage provider.

- **arduino_lab/** - Main Django project folder containing project settings, URLs, and configuration files for the entire project.

- **templates/** - Contains the base HTML templates, as well as templates specifically designed for Django allauth authentication (login, signup, etc.).

- **manage.py** - The primary Django command-line utility for executing administrative tasks, such as running the server, database migrations, and other commands.

- **README.md** - This file provides documentation for the project, including setup instructions, features, and usage information.

- **custom_storages.py** - Manages storage configurations for media and static files on a cloud provider, such as AWS S3, in the production environment.

- **Procfile** - Defines commands for deploying the app to Heroku, specifying how to start the web server.

- **requirements.txt** - Lists all dependencies and libraries required for the project, allowing for easy installation with `pip`.

- **robots.txt** and **sitemap.xml** - Configured for search engine optimization to help search engines index the site efficiently.

Environment variables such as API keys and database credentials are securely managed in the backend for both the development environment and the Heroku App settings. This ensures that sensitive information is protected and only accessible by authorized systems.


### Database

This project uses a PostgreSQL database hosted by Code Institute, designed to support full-featured e-commerce functionality. The database configuration provided by Code Institute simplifies the setup, allowing me to focus on developing and implementing features rather than database infrastructure.



#### Data Models

1. **Category**
   - Represents different categories of microcontrollers (e.g., AVR, ESP, ARM).
   - **Fields**:
     - `name`: The name of the category.
     - `description`: A brief description of the category.
     - `slug`: A URL-friendly identifier for the category.

2. **Product**
   - Represents an individual microcontroller or accessory available in the shop.
   - **Fields**:
     - `name`: The name of the product.
     - `description`: A detailed description of the product.
     - `price`: The price of the product.
     - `category`: A foreign key linking to the `Category` model.
     - `stock`: Number of units available.
     - `image`: Image of the product for display in the store.
     - `created_at`: Date when the product was added to the inventory.
     - `updated_at`: Date when the product details were last updated.

3. **User Profile**
   - Stores additional user information linked to Django’s default `User` model.
   - **Fields**:
     - `user`: One-to-one relationship with Django’s `User` model.
     - `address`: User’s primary address.
     - `city`: User’s city.
     - `postal_code`: Postal code for the user’s address.
     - `phone_number`: Contact number for the user.

4. **Cart**
   - Represents a shopping cart for a user session, storing items before checkout.
   - **Fields**:
     - `user`: A foreign key linking to the `User` model (optional, can also support guest checkout).
     - `created_at`: Date and time when the cart was created.
     - `updated_at`: Date and time when the cart was last updated.

5. **CartItem**
   - Represents individual items within a cart, linked to both `Cart` and `Product`.
   - **Fields**:
     - `cart`: A foreign key linking to the `Cart` model.
     - `product`: A foreign key linking to the `Product` model.
     - `quantity`: Number of units of the product in the cart.
     - `price`: Price of the item at the time of adding to the cart (for snapshotting).

6. **Order**
   - Represents a finalized purchase made by the user.
   - **Fields**:
     - `user`: A foreign key linking to the `User` model.
     - `total_price`: Total amount for the order, calculated from `OrderItem` entries.
     - `status`: Status of the order (e.g., pending, processing, completed).
     - `created_at`: Date and time when the order was placed.
     - `updated_at`: Date and time when the order status was last updated.

7. **OrderItem**
   - Represents individual items in an order, linked to both `Order` and `Product`.
   - **Fields**:
     - `order`: A foreign key linking to the `Order` model.
     - `product`: A foreign key linking to the `Product` model.
     - `quantity`: Number of units of the product in the order.
     - `price`: Price of the item at the time of purchase.

8. **Payment**
   - Manages payment information for an order, storing details from the payment gateway.
   - **Fields**:
     - `order`: A foreign key linking to the `Order` model.
     - `amount`: Total amount paid.
     - `status`: Status of the payment (e.g., successful, failed).
     - `payment_date`: Date and time of payment.

#### Schema of Models

The schema for the **Arduino Lab** project is designed to follow best practices for e-commerce applications:

- **User Profile** ↔ **User** (1-to-1)
- **Category** ↔ **Product** (1-to-Many)
- **Product** ↔ **CartItem** (Many-to-Many through Cart, with quantity tracking)
- **Cart** ↔ **User** (1-to-1 or Many-to-1, supports guest sessions)
- **Order** ↔ **User** (Many-to-1)
- **OrderItem** ↔ **Order** (Many-to-1)
- **Payment** ↔ **Order** (1-to-1)

This relational setup allows flexible operations for managing products, tracking user carts, processing orders, and handling payments. It is tailored to suit the functionality required for a microcontroller-focused e-commerce platform.


!!!!!!!!!!!!!!!!### Schema of Models


User
├── id (Primary Key)
├── username
├── email
├── password
└── date_joined

Category
├── id (Primary Key)
├── name
└── description

Product
├── id (Primary Key)
├── name
├── description
├── price
├── stock
├── category (Foreign Key to Category)
└── created_at

Order
├── id (Primary Key)
├── user (Foreign Key to User)
├── order_date
├── status
└── total_price



##  Scope - Epics and User Stories 
  ### Agile Workflow

To organize and manage the development process of the **Arduino Lab** project, I created two Agile boards, each representing a set of user stories that focus on distinct aspects of the project. This method enabled an efficient workflow, allowing me to structure the project setup and feature implementation in a systematic and visual manner.

#### Project Setup Board

The first board is dedicated to the setup phase of the project, covering foundational configurations and initial setup tasks. This board is a collection of tasks that establish the project environment, necessary installations, and settings, forming the groundwork for further development.

**Completed Tasks:**

- #### Epic 1:  Django Project Initialization:
  As a developer, I want to initialize a new Django project so that I can build the e-commerce platform.

- #### Epic 2: Install Required Packages:
  As a developer, I want to install essential packages like Django REST framework, Pillow, and PostgreSQL support so that I can develop key features of the e-commerce site.
- #### Epic 3: Setup Admin Panel for Store Management:
  As a developer, I want to configure the Django admin panel to manage products, categories, and orders so that the store owner can manage the shop from the backend.
- #### Epic 4: User Authentication Setup:
  As a developer, I want to set up user authentication (registration, login, logout) so that customers can create and manage accounts on the site.
- #### Epic 5: E-commerce App Creation:
  As a developer, I want to create a Django app for handling the store’s products, categories, and orders so that the e-commerce functionalities are organized.
- #### Epic 6: Database Configuration:
  As a developer, I want to configure a PostgreSQL database for the project so that data can be stored securely.
- #### Epic 7: Static and Media Files Configuration:
  As a developer, I want to configure static and media file settings so that product images and other media can be uploaded and displayed.

Each task in this board represents a key step in preparing the environment, ensuring the project is ready for feature implementation and deployment.

#### Feature Implementation Board

The second board focuses on the core features and functionalities required for **Arduino Lab**. This board represents the essential components that enhance the user experience and meet the requirements of a functional e-commerce platform for microcontrollers. It encompasses various user stories, from basic shopping cart functionality to product reviews, enabling a streamlined development process. 

**Task Statuses:**
  
- **Completed**:
  -  #### Epic 1:Product Search and Browsing:
    As a user, I want to browse and search for products like microcontrollers (ESP, AVR, STM32, Raspberry Pi) so I can find what I need easily.
  -  #### Epic 2:Detailed Product Information:
    As a user, I want to see detailed product information for each electronic component so that I can make informed purchasing decisions.
  -  #### Epic 3:Shopping Cart:
    As a user, I want to add multiple products to my shopping cart so that I can purchase them in a single transaction.
  -  #### Epic 4:Account Creation:
    As a user, I want to be able to create an account so that I can save my shipping details and access my order history.
  -  #### Epic 5:Secure Payment:
    As a user, I want to securely pay for my order using common payment methods like credit card or PayPal.
  -  #### Epic 6:Order Confirmation:
    As a user, I want to receive a confirmation of my order after purchase so I can be sure the transaction was successful.
  -  #### Epic 7:Product Filtering:
    As a user, I want to filter products by category (e.g., microcontrollers, sensors, hobby kits) so that I can narrow down my search results.
  -  #### Epic 8:Product Reviews:
    As a user, I want to be able to leave a review on the products I’ve purchased to share my feedback with other users.
  -  #### Epic 9:Create a Comprehensive README File:
    As a developer, I want to create a detailed README file so that other developers can understand how to set up and contribute to the project.
  -  #### Epic 10:Deployment to Heroku:
    As a developer, I want to deploy the Django project to Heroku so that the e-commerce site is accessible online.

This board represents a progressive approach to adding value to the project by implementing features that improve usability and support a comprehensive shopping experience for users. Using labels like **Must Be**, **Should Be**, and **Could Be** in the Agile workflow allowed me to maintain focus on core project requirements while also planning for additional functionalities that improve the user experience. By organizing tasks in this way, I ensured that critical setup and feature tasks were completed systematically and prioritized appropriately, supporting a clear and effective development path for **Arduino Lab**.

This Agile workflow allowed me to manage tasks efficiently, keeping track of progress and completing each step in an organized manner. Each user story reflects a specific component or functionality critical to the overall success of the **Arduino Lab** project. By dividing the work into these two boards, I maintained clarity between the setup tasks and feature development, ensuring that the project goals were achieved systematically.

### Skeleton

#### Wireframes

![Wireframe of Product Detail on Desktop](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/wireframes/images/product_detail_desktop.png)

Wireframe images were made for all pages except for the ones rarely used by the site, for example password change and email confirmation.

All wireframes can be viewed [here](https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/docs/wireframes/WIREFRAMES.md)


#### Colors

The color scheme for **Arduino Lab** has been carefully chosen to create a clean, professional, and technology-oriented aesthetic. Here are the primary colors used across the site:

- **Primary Blue (#0096D6)**: Used for headers, buttons, and links, this shade of blue reflects trustworthiness and aligns well with the tech-focused theme of Arduino and microcontrollers.
- **Dark Blue (#003366)**: Employed for backgrounds and darker text areas to add depth and contrast, especially in sections like banners or hero sections.
- **White (#FFFFFF)**: Used for the primary background and text color, maintaining a clean and readable design.
- **Black (#000000)**: For text in specific areas, especially for critical calls-to-action like "Shop Now," ensuring readability and focus.

These colors provide a modern and high-tech feel, encouraging users to explore and interact with the site.

#### Design Choices

The design of **Arduino Lab** is structured to provide users with a seamless and intuitive shopping experience. Here are some of the main design elements:

- **Minimalistic and Clean Layout**: The design avoids unnecessary clutter, allowing users to focus on the primary content and products offered. This clean layout makes it easy for customers to find the information they need without distraction.
- **Large, Engaging Hero Section**: The hero section immediately greets users with a bold welcome message and a clear call-to-action button ("Shop Now"), inviting users to explore the product catalog.
- **Responsive Design**: The layout is optimized for different screen sizes, ensuring a consistent experience across devices, whether on a desktop, tablet, or mobile.
- **Highlighted Offers and Categories**: Key information like free delivery promotions and major product categories are prominently displayed, guiding users effortlessly through the site.

These design choices aim to balance aesthetics with functionality, creating a site that is both visually appealing and easy to navigate.

#### Typography

The typography chosen for **Arduino Lab** is straightforward and professional, aligning with the clean and tech-focused brand image.

- **Primary Font**: A sans-serif font like *Roboto* or *Open Sans* has been used for its clarity and readability, particularly on digital screens. This typeface contributes to a modern and tech-savvy look.
- **Font Sizes**:
  - **Headers**: Larger font sizes are used for headers, such as the main welcome text, to draw attention and create a visual hierarchy.
  - **Body Text**: Regular-sized fonts are used for descriptions, product details, and other information-heavy sections to ensure easy readability.
  - **Buttons and Links**: Bold and slightly larger fonts are used for calls-to-action like "Shop Now" to emphasize clickable elements.

This typography enhances the overall readability of the site, ensuring that information is accessible and visually balanced.

## Existing Features

### Feature 1: The Navbar
- **Purpose**: Provides users with easy access to all parts of the website.
- **Features**:
  - **Categories Links**: Includes quick links to product categories such as AVR, ARM, ESP, Raspberry Pi, MSP430, and more, making it easy for users to find the specific type of microcontroller they're looking for.
 ![Microcontrollers](media\microcontrollers.PNG)
  - **Search Bar**: Positioned at the top of the page, enabling users to quickly search for products by keywords.![Search bar](media\search_bar.PNG)
  - **Account and Cart Icons**: Accessible icons for user account management and shopping cart overview. The cart icon displays the current item count, helping users keep track of their purchases as they browse.
  ![Account and Cart Icons](media\my_account.PNG)

 This is how Navigation bar looks on mobile device: 
- **Mobile navigation bar**  ![Mobile navigation bar](media\documentations\MOBILE_NAVBAR.PNG)

### Feature 2: The Home Page
- **Purpose**: Acts as the main entry point for the site, showcasing featured content and promotions.
- **Features**:
  - **Hero Banner**: A visually engaging banner that welcomes users to Arduino Lab, with a message encouraging creativity with the latest microcontrollers.
  ![Hero banner](media\documentations\hero_banner.PNG)
  - **Shop Now Button**: A call-to-action button in the hero banner that directs users to the product listings, inviting them to start browsing immediately.
  ![Shop now button](media\documentations\Shopnow_button.PNG)
  - **Promotional Banner**: Highlights promotions such as "Free delivery on orders over $50," to encourage larger purchases.
  ![Promotional banner](media\documentations\promotional_banner.PNG)
  - **Social Media and Newsletter Section**: A section at the top that allows users to subscribe to the newsletter for exclusive deals.
  ![Social Media and Newsletter Section](media\documentations\media_and_newsletter.PNG)
  
   This is how Home Page looks on mobile device: 
- **Mobile Home Page**  ![Mobile Home Page](media\documentations\mobile_homepage.PNG)

### Feature 3: The Footer
- **Purpose**: Provides additional navigational links and engagement options at the bottom of page.
- **Features**:
  - **Social Media Link**: Links to Arduino Lab’s Facebook page, offering users a way to stay connected and informed about updates.
   ![Social Media and Newsletter Section](media\footer.PNG)
  - **Newsletter Signup**: An email signup form where users can subscribe to monthly updates, receiving exclusive offers and product news.
  ![ Newsletter Section](media\documentations\subscribe.PNG)

  This is how Footer looks on mobile device: 
- **Mobile Footer**  ![Mobile footer](media\documentations\mobile_footer.PNG)