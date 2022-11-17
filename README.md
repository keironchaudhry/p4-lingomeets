# **LingoMeets**

**LingoMeets is a language-learning meet-up website for language-learning enthusiasts with full user and admin functionality.**

This application was built using [GitHub](https://github.com/) and deployed to [Heroku](https://id.heroku.com/login).

<u>Required technologies:</u>

Python (+Django Framework), JavaScript, HTML5 and CSS3.

Deployed version of this project can be found [here]().


## **Table of content**

* [Project Purpose](#purpose-of-project)
* [UX](#ux)
    * [Project Scope](#project-scope)
    * [Strategy](#strategy)
    * [User Stories](#user-stories)
* [Design]()
    * [Website Structure](#website-structure)
    * [Relational Database Diagram](#relational-database-diagram)
    * [Design Diagram](#design-diagram)
    * [Colour Design](#colour-design)
    * [Fonts](#fonts)
* [Features]()
* [Features Left to Implement]()
* [Technologies and libraries used]()
* [Database]()
* [Testing]()
* [Bugs during development]()
* [Unfixed Bugs]()
* [Development and Deployment]()
* [Content]()
* [Credits]()


# **Project Purpose**

LingoMeets is a website application designed specifically for language-learning enthusiasts who wish to join like-minded language enthusiasts on international meet-ups, mainly to practise their abilities and skills with others and also for touristic reasons.

Target audience: language-learning enthusiasts and individuals that want to network with others internationally as part of a wider community.

This is project is the fourth in a series of five milestone projects which are to be completed in order to receive my diploma from Code Institute.


# **UX** 

## **Project Scope**

* **Functionality**

    * To be able to sign-up using an email address and secure password
    * To be able to login and logout of an account
    * To be able to create/view/edit/delete an event as site admin
    * To be able to view past events
    * To be able to view past event information and other user reviews
    * To be able to create/view/edit/delete reviews.
    * To be able to approve reviews as site admin.
    * To be able to create/view/edit/delete user profile information as a user
    * To be able to store and retrieve avatar image
    * To be able to register to/deregister from an event as a user
    * To be able to reset password
    * To be able to change password
    * To handle errors: page 404 'Not Found', page 500 'Internal Server Error' and page 401 'Unauthorised'.

* **Content Requirements**

    * Clear, unambiguous and concise information on how to use the website
    * Event information and details for users
    * Forms where user input is required
    * Engaging headings and content to guide user throughout website
    * Responsive and interactive website that responds to user
    * Images across website to provide visually appealing content

## **Strategy**

Learning languages can be an arduous task, and to be able maintain several languages even more so. It is often hard to find other learners who have the same level and learning requirements as you, and so as part of the inspiration for Lingomeets, this website was created to engage learners who can meet up and network with others in international events for several days for a cost, which covers accomodation and day-trips.

* **Site-owner goal** 

    * To provide a platform for users who are looking to network
    * To provide a platform that allows users to create a profile
    * To create a viable product that can be further developed with additional features

* **User goals**

    * To access a user-friendly application across multiple devices
    * To network with other likeminded users
    * To attend as many meet-up events as possible

## **User Stories**


* As an **admin**, I can **access an admin profile** so that I can **create, edit and delete meet-ups with all relative information for website.**

* As an **admin**, I can **view user reviews of an event** so that I can **approve/disapprove it.**

* As an **admin**, I can **view user profile information** so that I can **modify any particular user detail or delete users.**

* As an **admin**, I can **create a meet-up event** so that I can **create new events for users.**

* As a **first-time site visitor**, I can **view a landing page** so that I can **get information about a website's purpose.**

* As a **first-time site visitor**, I can **sign-up** so that I can **create an account to access user features.**

* As a **first-time site visitor**, I can **find the navigation bar** so that I can **navigate the website.**

* As a **first-time site visitor**, I can **view reviews and ratings of an event by users** so that I can **gain insight into user experience.**

* As a **user**, I can **sign-in and out of an account** so that I can **log-in and out of user account.**

* As a **user**, I can **view past events** so that I can **learn about previous meet-up events.**

* As a **user**, I can **view new events** so that I can **learn about forthcoming meet-up events.**

* As a **user**, I can **view date and location of a meet-up event** so that I can **gain accurate information about an event.**

* As a **user**, I can **register to a meet-up event** so that I can **participate in forthcoming events.**

* As a **user**, I can **create a review of an event** so that I can **review an event.**

* As a **user**, I can **edit my review or delete my review** so that I can **modify and interact with my user content.**

* As a **user**, I can **view confirmation of my action** so that I can **be sure it has processed.**

* As a **user**, I can **view a paginated page of events** so that I can **select a post to view.**

* As a **user**, I can **get to a user profile** so that I can **see my account profile.**

* As a **user**, I can **update my profile information** so that I can **modify user profile dashboard information.**


# **Design**

## **Website Structure**

## **Relational Database Diagram**

* The project uses a relational database (PostgreSQL)

* The following diagram represents the relational database model design for this website. It was made using Quick Database Diagrams:

![relational-database-diagram](/documents/readme_images/model%20database%20diagram%20new.jpg)

**Models**

* **User**
    * The User model contains information about each user that registers an account
    * It is part of the Django allauth library
    * The fields used for this project are: *username*, *email*, *password*

* **Event**
    * The Event model is the principal model
    * Only an admin can create Event objects
    * All users can interact with Event objects
    * The model contains the following fields: *event_id*, *title*, *slug*, *date*, *destination*, *image*, *description*, *price*, *attendees*, *created_on*
    * Contains a method to show if the event has been completed

* **Review**
    * Used to review Event objects by users
    * ForeignKey relationship with both Event and User
    * Contains the following fields: *review_id*, *event*, *user*, *content*, *rating*, *created_at*, *updated_at*, *is_admin_approved*
    * Contains a method to get the range of a user rating, used to create a star-system review as part of the website features.

* **Profile**
    * The Profile model is used to store information regarding any registered user
    * Users can create a profile object upon creating an account
    * Users can modify profile information at any time
    * An admin can also create, modify and delete profile objects
    * ForeignKey relationship with User
    * Contains the following fields: *profile_id*, *user*, *first_name*, *last_name*, *birthday*, *avatar*, *native_language*, *other_language*, *bio*, *created_at*, *updated_at*
    * Contains a method to calculate the age of the user using their birthday date
    * Contains a method to return the user avatar url to display on template

    
## **Design Diagram**

## **Colour Design**

## **Fonts**


# **Features**

To be added


# **Features left to implement**

To be added


# **Technologies and libraries used**

To be added


# **Database**

To be added


# **Testing**

To be added


# **Bugs during development** 

To be added during the course of development of project

## **Unfixed bugs**

To be added upon termination of the project


# **Development and deployment**

To be clarified upon conclusion of the project

Deployed version of project at following URL:


# **Credits**