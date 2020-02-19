# **Datacentric Milestone Project 3**

The following section details the project requirements issued by Code Institue for completion of the Milestone 3 Project. The title of my project is **Bukish : The Online Book Review and Recommendation Site**

# **Bukish** 

**The Online Book Review Site**

Bukish is a simple, online book reviews forum. The aim of the site is to provide fertile ground for the book loving community to come together to rate and review literature. Users join up to engage with others and express their love (or hate!) for books they’ve read but also to discover new literature. 

Bukish allows users to store their personalised content, to delete and update reviews/comments and even be linked directly to Amazon to faciliate anonline purchase! The aim is to allow for a interactive, fun and personalized experience.  

Please refer to the **tables to contents** for guidance.

## **Table of Contents**

- [**Bukish**](#bukish)
- [**Project Brief**](#project-brief)
- [**UX**](#ux)
	- [**User Stories**](#user-stories)
- [**Wireframes**](#wireframes)
- [**Database**](#database)
- [**Features**](#features)
	- [Existing features](#existing-features)
	- [Features left to implement](#features-left-to-implement)	        
- [**Technologies used**](#technologies-used)
    - [Languages](#languages)
- [**Testing**](#testing)	
    - [Validation](#validation)
- [**Deployment**](#deployment)
- [**Credits**](#credits)
	- [Content](#content)
	- [Media](#media)
	- [Acknowledgements](#acknowledgements)
	



# **Project Brief**

The project is the culmination of the Data-Centric Development module on the Code Insitute Full Stack Software Development Diploma. 

The projects purpose was stated as: 
> "In this project, you'll build a full-stack site that allows your users to manage a common dataset about a particular domain".

The value being that users of the site simply adds their own data, with the advantage being, a user can avail of the collective information/data of the community. 

Therefore the site owner, who could well be a prodigious user/member of the community, provides the users with the site functionality. And in return, among other benefits, the site owner can avail of the acquired collective dataset.

The site was built with this in mind, along with the mandatory requirements. which were (taken, and shorten, from the CI project requirements section): 

* Data handling: Build a MongoDB-backed Flask project...
* Database structure: Put some effort into designing a database structure ... 
* User functionality: (CRUD functionality)....
* Use of technologies: Use HTML and custom CSS for the website's front-end....
* Structure: Incorporate a main navigation menu and structured layout ...
* Documentation: Write a README.md file ..
* Version control: Use Git & GitHub for version control...
* Attribution: Maintain clear separation between code written by you and code from external sources 
* Deployment: Deploy the final version ( Heroku)...
* Make sure to not include any passwords or secret keys in the project repository....


## **UX**

As specified in the project requirements, the purpose of this project is to “build a full-stack site that allows your users to manage a common dataset about a particular domain”.

Baring this in mind, the goal of this milestone project was to create a web application using Python, the Flask libraries (a Python framework), a NoSQL Document-Based Database (in my case; Mongo DB) to construct the functioning app, as well as incorporate the main tenants of CRUD (Create, Read, Update and Delete). 

CRUD, which refers to [persistence storage](https://en.wikipedia.org/wiki/Persistence_(computer_science))  encompasses 4 main tenants:

Create – add new, unique data to the database
Read – Fetch data from the database
Update – change and edit pre-existing database data
Delete – completely remove data from database. 


My overarching aim was to create a simple, efficient and sleek user friendly site, using intuitive design and enticing colours to guide users. The simple layout would facilitate a pleasant experience and hopefully entice users to add their own reviews and comments, this participating in building the websites databse as well as the community. The target being **reciprocity**; the more users, the more comments and reviews, the more the database extands

So with these focal points in mind, I tried to adjust the UX of this site for the following user type:


### **User Stories**

A typical/archetypal user would be interested in reading books, book recommendations and writing reviews. They would also be willing members of an online community.


•	As a user, I would like to browse on site so I can avail of book reviews, comments and links.
•	As a user, I would like to sign up and have my own account, so I can access reviews and comments. 
•	As a user, I would like to add my own personalized reviews and comments. 
•	As a user, I would like to add participate in an online community for a topic that I’m interested in.
•	As a user, I would like to express and share my own views within a likeminded community. 
•	As a user, I would like to update and/or delete my reviews or my comments at any time and also not have any other user update and/or delete my content.
•	As a user, I'm looking for books as gifts and I need inspiration (as well as some links to Amazon so I can buy the book(s) online).

Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
•	As a user type, I want to perform an action, so that I can achieve a goal.
This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## **Wireframes**

**insert wireframe pngs**


## **Database** 

As mentioned in the mandatory project requirements section, it was neccessary to: 
>"Build a MongoDB-backed Flask project for a web application that allows users to store and manipulate data records"  

It was essential also to create a scalable application, capable efficiently of handling growing numbers of users and their input on the database.

With this in mind, I used [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) which is a NoSQL, document-oriented database program.

I used 3 (essential) collections (all interrelated via the ObjectId) which were: 

* Users: contains the users name and a hashed password

* Books: containing all the data on the books e.g. name, author, a synopsis, a book cover photo, an amazon link (if possible) and a user rating (stars).

* Bookscomms: which was a users comment (along with user name) about a book but not the actual review itself.

#### Database Schema

As mentioned above, the collections within the database were interconnected via the ObjectId, as represented below. 

**insert database schema wireframe**


## **Features**

This section focuses on the pre-existing features present on the site, as well as a look to the future with regards to future improvements. 

### **Existing Features**

In The following features are presented in a loose order of appearances on the app: 

* A Modal pop feature that welcomes visitor, displays a random quote (for assigned list) and offers additional information to client. The modal also supplies different information when a user logouts (including a button to direct users to log back in)

* A Navigation bar that, when there is no user logged in, provides links to the home, sign up and login pages. There is a glasses icon that also redirects homeward. Upon a user logging in and being recognised, the Navbar offers different options which are redirecting the known user back to their profile back, the all reviews page or having the option to log out. 

* Buttons that are facilitating the CRUD options (including adding reviews and comments, editing reviews and comments and deleting reviews and comments.)

* A footer with a link to my Github page and my name/copyright logo.



### **Features Left to Implement**

I found this milestone project to be particularly interesting in terms of the learning curve, because as I moved forward with it, I discovered new python libraries and many different features and functionalities that I could have implemented and utilised. 

In fact, I found it difficult trying to balance learning about new features and trying not to use them all. It was very enjoyable discovering all the possibilities but also, it became an exercise of discipline in terms of using just what was needed. 

Sometimes less is more. However, in the future I plan on adding a lot more functional features to this site. These include:

-	An intuitive search bar 
-	A more robust sign in/login process, including, for example, reCaptcha functionality 
-	A password and username reset option
-	The possiblity to delete, edit and update user profile details. 
-	A more expansive user profile in general including dates of signing in, dates and times of comments, if it was edited, personalised avatars (among other things). 
-	Using more of the flask libraries (lots were tested and not used) including Flask-Login, Flask
-	Like/Dislike buttons for comments and books in the form of Thumbs Up/Down. I could also encorporate a simple counter on this to add the community feel of the site (e.g. 300 likes/24 dislikes)



## **Technologies Used**

The following technologies were used on this project:

##### **Languages**

- [Python]( https://www.python.org/) - Python is an object-orientated high-level programming language. 


- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - is the renowned programming scripting language and the main libraries are JS. 

- [CSS3](https://developer.mozilla.org/en-US/docs/Archive/CSS3) - is used as the stylesheet language for styling and rendering.

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - is used as the standard markup language. 
    
##### Framework

- [Flask](https://flask.palletsprojects.com/en/1.1.x/) is a micro web framework written in Python. It is  used by constructing route decorators for the main functionality of the app. By using the Jinja templating functionality, Flask/Python is rendering on html pages. 


- [Bootstrap 4.3.1](https://getbootstrap.com/docs/4.3/getting-started/introduction/) - is a CSS framework that aids the grid and the layout and also the modal popup in this project

##### Libraries

- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) – is a non-SQL, cloud database used to store, manage, update and delete datasets provided in collections.

##### Libraries


-  [JQuery version 3.3.1](https://jquery.com) - JS library to simplify HTML DOM manipulation and used also to initialise JavaScript elements 



# **Testing**


### **Validation** 

I used a variety of tools provided by specified sites to test my code and the apps functionality:


#### Python
As Python was the main language I used , I tested often and also learned to utilise in-code testing to resolve errors, particularly the  ‘import pdb;pdb.set_trace()’ which is added above the erroneous code and you can evaluate the error in the terminal (thanks to my mentor Marantha for introducing this to me). 
For my Python code I passed it through the [PEP8online]( http://pep8online.com/

#### JavaScript

I used [JSHint](https://jshint.com/) to validate the little amount of JavaScript code I used.

#### HTML
For the HTML I passed my code through the [W3C Markup Validation Service](https://validator.w3.org/).

#### CSS
For my CSS3 code, I passed it through the [W3C CSS Validation Service - Jigsaw](https://jigsaw.w3.org/css-validator/)




### **Tests** 

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.
Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.
For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:
1.	Contact form:
i.	Go to the "Contact Us" page
ii.	Try to submit the empty form and verify that an error message about the required fields appears
iii.	Try to submit the form with an invalid email address and verify that a relevant error message appears
iv.	Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.
You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.
If this section grows too long, you may want to split it off into a separate file and link to it from here.

## **Deployment**

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).
In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
•	Different values for environment variables (Heroku Config Vars)?
•	Different configuration files?
•	Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.



# **Credits**


•	The text for section Y was copied from the Wikipedia article Z

## **Content**

* The Code Insitute 

#### **Media**
•	The photos used in this site were obtained from ...
#### **Acknowledgements**
•	I received inspiration for this project from X