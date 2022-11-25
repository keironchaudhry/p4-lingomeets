# **LingoMeets**

![am-i-responsive](/documents/readme_images/amiresponsive%20image.jpg)

**LingoMeets is a language-learning meet-up website for language-learning enthusiasts with full user and admin functionality.**

This application was built using [GitHub](https://github.com/) and deployed to [Heroku](https://id.heroku.com/login).

<u>Required technologies:</u>

Python (+Django Framework), JavaScript, HTML5 and CSS3.

Deployed version of this project can be found [here](https://lingomeets.herokuapp.com/).


## **Table of content**

* [Project Purpose](#purpose-of-project)
* [UX](#ux)
    * [Project Scope](#project-scope)
    * [Strategy](#strategy)
    * [User Stories](#user-stories)
* [Design](#design)
    * [Website Structure](#website-structure)
    * [Relational Database Diagram](#relational-database-diagram)
    * [Design Diagram](#design-diagram)
    * [Colour Design](#colour-design)
    * [Fonts](#fonts)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Features Left to Implement](#features-left-to-implement)
* [Technologies and libraries used](#technologies-and-libraries-used)
    * [Languages](#languages)
    * [Database Platform and Cloud Storage](#database-platform-and-cloud-storage)
    * [Libraries and other resources](#libraries-and-other-resources)
* [Testing](#testing)
    * [Introduction](#introduction)
    * [Testing User Stories](#testing-user-stories)
    * [Automated Testing](#automated-testing)
    * [Testing Accessibility and Performance](#testing-accessibility-and-performance)
    * [Code Validation](#code-validation)
* [Bugs during development]()
* [Unfixed Bugs]()
* [Development and Deployment](#development-and-deployment)
    * [Local Deployment](#local-deployment)
    * [Deployment to Heroku](#deployment-to-heroku)
* [Credits](#credits)
    * [Code](#code)
    * [Acknowledgments](#acknowledgments)


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

* Website is structured into 8 pages
* All pages extend the same base therefore producing a consistent style across the application
* Pages are the following:

| Page | Description |
| --- | --- |
| **Header** | Navbar header with site logo and collapsable link for media query sizes |
| **Home** | A landing page consisting of a welcome and upcoming meet-up |
| **Past Events** | A list of all previous meet-ups |
| **Meet-Up Detail** | Every meet-up post provides detail on the event with user options |
| **Sign Up** | Where users can create an account |
| **Login** | Where users can login with an account |
| **Logout** | Where users logout of an account |
| **User Profile** | A profile dashboard displaying user information |
| **Profile Settings** | An input page where users can modify their existing information |
| **Footer** | Displays site logo, social media links, timetable, links and contact details |

* **Interactive Design**

    * Collapsable navbar menu for smaller media query screens

    ![responsive-toggle-example](/documents/readme_images/responsive%20collapsable%20toggle.jpg)

    * All buttons, icons and links respond to hovering

    ![responsive-link-example](/documents/readme_images/responsive%20link%20example.jpg)

    * Pop up modals with warnings and messages across site
    
    ![responsive-modal-example](/documents/readme_images/responsive%20modal%20design%20example.jpg)

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

* **Wireframes**
    * Skeleton structure for website was created by hand. 
    * Skeletal design structures exist for imagined landing page and event page, all other pages were created based on these designs once the front-end was comfortably implemented. 
    * Design for landing page can be seen [here](/documents/readme_images/index.jpg).
    * Design for event page can be seen [here](/documents/readme_images/event.jpg).

## **Colour Design**

This colour palette was made using [Color Hunt](https://colorhunt.co/create).

![colour-palette](/documents/readme_images/colour%20palette%20scheme.jpg)

This colour palette has been the basis for colour which has been applied throughout the website in this general order: 

* Navbar color: #07889B (Silver-blue)
* Body : #FDF5E6 ('Oldlace' white)
* Occasional white : #FAFAFA (white)
* Principal font colour : #000000 (black)

## **Fonts**

Font application in this website have been taken from [Google Fonts](https://fonts.google.com/about) and consist principally of the font style **Lora**.


# **Features**

## **Existing features**

Information on existing features can be found on [this page](/documents/features/existing_features.md).

## **Features left to implement**

* Payment system so that users can pay for the meetup cost in advance.
* Ability to connect different profiles so that users can directly "Add friend" or "Connect" with another user.
* Ability to allow different users to privately message each other.
* Complete automated testing to 100%.


# **Technologies and libraries used**

## **Languages**

The languages used are:

* [HTML](https://html.spec.whatwg.org/multipage/)
* [CSS](https://www.w3.org/Style/CSS/Overview.en.html)
* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
* [Python](https://www.python.org/)

## **Database Platform and Cloud Storage**

* [ElephantSQL Postgres](https://www.elephantsql.com/): SQL database service provided by ElephantSQL for data storage.
* [SQLite](https://www.sqlite.org/index.html): SQL database engine used by default as part of Django Framework and used during development.
* [Cloudinary](https://cloudinary.com/home-102622): to store images and static files.
* [Heroku](https://id.heroku.com/login): to deploy and run the application.

## **Libraries and other resources**

This project contains the following resources:

* [Django](https://www.djangoproject.com/): Python-based framework for rapid website development. 
* [Bootstrap](https://getbootstrap.com/): CSS and JavaScript library.
* [Coverage.py](https://coverage.readthedocs.io/en/6.3.2/): used for coverage testing of Python programs. 
* [HTML Markup Validation](https://validator.w3.org/): used to validate HTML code syntax.
* [CSS Validation Service](https://jigsaw.w3.org/css-validator/): used to validate CSS code syntax.
* [PEP8 Validation](http://pep8online.com/): used to validate Python code syntax.
* [Chrome DevTools](https://developer.chrome.com/docs/devtools/): development tool supplied by Google Chrome browser to test responsive design during development.
* [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/): used to access website performance.
* [Quick Database Diagrams](https://www.quickdatabasediagrams.com/): used to create the database model chart.
* [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/index.html): used for user account registration and user authentication.
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/): used for comment and sign-in forms throughout website.
* [Google Fonts](https://fonts.google.com/): used to import font utilised throughout site.
* [Font Awesome](https://fontawesome.com/): used for icons across website.
* [Icons8](https://icons8.com/): used for favicon.
* [GitHub](https://github.com/): used to store, develop and maintain project code.


# **Testing**

## **Introduction**

* Site has been continuously tested throughout development stages using the following features:
    * Python terminal for backend functionalities
    * Google Developer Tools 
    * Manual Testing
    * Automated Testing

## **Testing User Stories**

* Testing user stories can be found [here](/documents/testing/testing_user_stories.md).

## **Automated Testing**

* 18 automated tests have been implemented.
* Automated tests were carried out during the creation of website functions and classes.
* The tool use to measure coverage of code was the Coverage.py tool.
* To check coverage in the HTML format run in the terminal:
    * `coverage run --source=appname manage.py test`
    * `coverage html`
    * Run `python3 -m http.server` (in case there is a server already running, enter `python3 -m http.server 8080`, for example).
    * Live server should be running with a list of HTML options.
    * Pick 'htmlcov/'.

![coverage-report-1](/documents/readme_images/coverage%20part%201.jpg)
![coverage-report-1](/documents/readme_images/coverage%20part%202.jpg)

## **Testing Accessibility and Performance**

* Testing for accessibility and performance is managed using the Lighthouse tool in Chrome extension:

    * For Desktop:

    | Section | Performance | Accessibility | Best Practices | SEO |
    | --- | --- | --- | --- | --- |
    | Home | 99 | 92 | 83 | 90 |
    | Past Events | 93 | 93 | 83 | 90 |
    | Event | 99 | 92 | 83 | 90 |
    | Sign Up | 99 | 92 | 83 | 89 |
    | Login | 99 | 92 | 83 | 89 |
    | User Profile | 99 | 94 | 75 | 90 |
    | User Settings | 99 | 83 | 83 | 89 |

    * For Mobile devices:

    | Section | Performance | Accessibility | Best Practices | SEO |
    | --- | --- | --- | --- | --- |
    | Home | 94 | 92 | 83 | 92 |
    | Past Events | 94 | 93 | 83 | 92 |
    | Event | 92 | 92 | 83 | 92 |
    | Sign Up | 93 | 92 | 83 | 91 |
    | Login | 93 | 92 | 83 | 91 |
    | User Profile | 92 | 94 | 75 | 92 |
    | User Settings | 92 | 83 | 83 | 91 |

## **Code Validation**

* **W3C HTML Code Validator**

    * Each page of the deployed website was run through the [HTML Markup Validation Service](https://validator.w3.org/) and returned no errors.

* **W3C CSS Jigsaw Validator**

    * CSS code was tested with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) via direct input and returned no errors.

    ![css-validator](/documents/readme_images/css%20validator%20.jpg)

* **JSHint validator**

    * No custom JavaScript code has been written for this project, only what is included with Bootstrap4. 

* **Python Validator**

    * All Python files across the application returned no errors.

    ** <u>**NOTE**</u> **

    * At the time of testing (25/11/2022), the [PEP8 Online Service](http://pep8online.com/) has been down.
    * In order to carry out effective validation of standardised Python, the following was done in the GitPod terminal:
        * Run the command `pip3 install pycodestyle`. It may be that this is already installed by default, that being the case, the requirement is met and nothing will happen.
        * Press CTRL+Shift+P (or Cmd+Shift+P on Mac) and type `linter` into the search tab that appears.
        * Click on `Python: Select Linter` from the filtered results.
        * Select `pycodestyle` from the list.
        * PEP8 errors will now be underlined in red and shall also appear in the `PROBLEMS` part of the terminal.


# **Bugs during development** 

To be added during the course of development of project

## **Unfixed bugs**

To be added upon termination of the project


# **Development and deployment**

The development environment used for this project was GitPod. Regular commits and pushes to Github have been employed to be able to track and trace the development process of the website. The Gitpod environment for this particular project was created using a template provided by Code Institute.

For local deployments instructions shall be written below, along with instructions with deployment to Heroku, the hosting service used to deploy this particular website. Heroku was chosen as the hosting service due to its database maintenance capabilities. 

## **Local Deployment**

This repository can be cloned and run locally with the following steps:

1. Login to [GitHub](https://www.github.com).
2. Select repository named: [keironchaudhry/p4-lingomeets](https://github.com/keironchaudhry/p4-lingomeets).
3. Click code toggle button and copy the url (i.e., https://github.com/keironchaudhry/p4-lingomeets.git).
4. In your IDE, open terminal and run the git clone command (i.e., git clone https://github.com/keironchaudhry/p4-lingomeets.git).
5. The repository will now be cloned in your workspace.
6. Create an [env.py file](https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1) (this file should normally be included in .gitignore, therefore it'll not be committed publicly in the root folder of your project) and add in the following code with the relevant key, value pairs, and ensure you enter the correct key values. For example:

`import os`

`os.environ['SECRET_KEY'] = 'ADDED_BY_YOU'`

`os.environ['DATABASE_URL'] = 'ADDED_BY_YOU'`

`os.environ['CLOUDINARY_URL'] = 'ADDED_BY_YOU'`

7. Install the relevant packages as per the requirements.txt file
8. In `settings.py` file, ensure the connection is set to either the Heroku Postgres Database or the local SQLite database
9. Ensure debug is set to true in the `settings.py` file for local development
10. Add localhost/127.0.0.1 to the ALLOWED_HOSTS variable in `settings.py`
11. Run `python3 manage.py showmigrations` to check the status of the migrations
12. Run `python3 manage.py migrate` to migrate the database
13. Run `python3 manage.py createsuperuser` to create a super/admin user
14. Start the application by running `python3 manage.py runserver`

## **Deployment to Heroku**

Deployment to Heroku can be done with the following guideline:

1. Create an account on Heroku
2. Create an app and give it the desired name and select a region
3. <del>Under resources, search for Postgres, and add _Heroku Postgres_ database to the app</del>
    * Due to changes taking place as from the 28/11/2022 with regards to Heroku and their PostgreSQL Add-on, student developers at Code Institute have had to migrate their project database to [ElephantSQL](https://www.elephantsql.com/).
        1. Create an account on ElephantSQL.
        2. Click on 'Create an instance'
        3. Give your plan a Name, select the appropriate Plan and then select a region and data-center closest to your location.
        4. Once details are completed, click 'Create instance'. 
        5. Copy and paste dashboard `DATABASE_URL` and copy and paste into Heroku Config Vars in Settings, and be sure to set your `env.py` in your project IDE to the same URL. 
4. The `DATABASE_URL` needs to be set as an environment variable in both Heroku and in the IDE local environment variables
5. Create a `Procfile` with the following text: `web: gunicorn project_name.wsgi`
6. Make sure you add your environment variables (env.py) to Heroku's Config Vars
7. Ensure `Debug` is set to `False` in the settings.py file
8. Add 'localhost', and 'project_name.herokuapp.com' to the `ALLOWED_HOSTS` variable in `settings.py`
9. Run `python3 manage.py showmigrations` to check the status of the migrations
10. Run `python3 manage.py migrate` to migrate any necessary data to the database
11. Run `python3 manage.py createsuperuser` to create an admin user
12. Connect the app to GitHub, and enable automatic deploys from main (or you can manually deploy).
13. Click 'deploy' to deploy your application to Heroku for the first time


# **Credits**

## **Code**

The following websites proved to be both insightful and helpful during development of this project:

* [Stack Overflow](https://stackoverflow.com/)
* [W3School](https://www.w3schools.com/)
* [GeeksForGeeks](https://www.geeksforgeeks.org/)
* [YouTube](https://www.youtube.com/)

# **Acknowledgments**

For inspiration, guidance and inputs, thank you to:

* Sandeep Aggarwal

    Absolutely fantastic mentor at Code Institute with brilliant insight into Full Stack Software Development and programmatic skills.
    
* Jack Crymble

    Friend and guide, thank you for your knowledge and insight!

* Jody Murray

    Fellow student and colleague, thank you for your input and constant support!