# **Data-Centric Milestone Project 3**

The following section details the culmination of the Data-Centric Development module, which is the third Milestone Project issued by Code Institute for the Full Stack Software Development Diploma Course. The title of my project is **Bukish: The Online Book Reviews and Recommendations Site**.

[**The Deployed Heroku site can be found here**](https://datacentric-milestone-bookrev.herokuapp.com/) 

*For Code Institute testing purposes, I suggest logging into the site as the **Admin**, using the following details*: 
- Username: **admin**   
- Password: **admin99** 

# **Bukish** 

**The Online Book Review and Recommendations Site**


Bukish is a simple, online book reviews forum. The aim of the site is to provide fertile ground for the book loving community to come together to rate and recommend literature. Users join up to engage with others and express their love (or hate!) for books they’ve read. But the site also aides users in discovering new literature, gauging how the community feels about certain books and even directly facilitating an online purchase (via affiliate links to online stores (namely **Amazon**). 

Bukish allows Users to store their personalised content, to delete and update reviews/comments. The aim is to allow for an interactive, fun and personalized user experience.

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

The project is the culmination of the Data-Centric Development Module on the Code Institute Full Stack Software Development Diploma. 

The projects purpose was stated as: 
> "(To) build a full-stack site that allows your users to manage a common dataset about a particular domain".

The value is that Users of the site simply add their own data, with the advantage being, a User can avail of the collective information/data of the site community (including other Users reviews and comments).

Therefore the site owner, who could well be a prodigious User/Member of the community, provides the Users with the site itself, accessing the content within and its functionality. And in return, among other benefits (such as having Administrative Access), the site owner can avail of the acquired collective dataset of the site community. The Users do not have access to the entire dataset as it is stored on a third party cloud database ([MongoDB](https://www.mongodb.com/)). Scalability was another focal point as, with an expanding User base that creates site content at will; it needed to be correctly implemented to facilitate this. Please refer to the Database Schema for more information on the scalable aspect of the site.

The site was built with all of these points in mind, along with the mandatory projects requirements, which were (the following list was taken, and shortened, from the **CI project requirements** section):

* Data handling: Build a MongoDB-backed Flask project...
* Database structure: Put some effort into designing a database structure... 
* User functionality: (CRUD functionality)...
* Use of technologies: Use HTML and custom CSS for the website's front-end....
* Structure: Incorporate a main navigation menu and structured layout...
* Documentation: Write a README.md file...
* Version control: Use Git & GitHub for version control...
* Attribution: Maintain clear separation between code written by you and code from external sources...
* Deployment: Deploy the final version (Heroku)...
* (Secrecy): Make sure to not include any passwords or secret keys in the project repository...

The next section will discuss how I wove these concepts into the UX. 

## **UX**

As specified in the project requirements, the aim of this project is to aid the Users to manage and contribute to a common dataset. So naturally, a massive consideration would be on the User experience and the ease with which Users can navigate the site. 

Bearing this in mind, the goal of this milestone project was to create a web application using **Python**, the **Flask** libraries (a Python web framework) and a (NoSQL) Document-Based Database (in my case; **Mongo DB**) to construct the functioning app, as well as incorporate the main tenets of the *CRUD* operations (Create, Read, Update and Delete). 

**CRUD** refers to [persistence storage](https://en.wikipedia.org/wiki/Persistence_(computer_science)) and encompasses the following 4 main pillars:

**Create**:
- add new, unique data to the database.

**Read**:
- Fetch data from the database.

**Update**:
- change and edit pre-existing database data.

**Delete**:
- completely remove data from database. 


My overarching aim was to create a simple, efficient and sleek User friendly site, using intuitive design, clear and concise text and enticing colours to guide users. The simple layout would facilitate a pleasant experience and hopefully entice Users to add their own reviews and comments, thus participating in building the websites database, as well as the community. The target being **reciprocity**; the more Users, the more comments and reviews, the more the database extends. But with the increasing content, I wanted it also to be scalable, whilst expanding. 

So with these focal points in mind, I tried to adjust the UX of this site for the following User type:


### **User Stories**

A typical/archetypal User would be interested in reading books, book recommendations and writing reviews. They would also be willing members of an online community.


* **As a User**, I would like to browse on site so I can avail of book reviews, comments and links.
* ... I would like to sign up and have my own account, so I can access reviews and comments. 
* ... I would like to add my own personalized reviews and comments. 
* ... I would like to add participate in an online community for a topic that I’m interested in.
* ... I would like to express and share my own views within a likeminded community. 
* ... I would like to update and/or delete my reviews or my comments at any time and also not have any other user update and/or delete my content.
* ... I'm looking for books as gifts and I need inspiration (as well as some links to Amazon so I can buy the book(s) online).

These are just some of the User stories that I considered whilst constructing the site. As a book lover myself I had some personal considerations of what I would like to experience on a similar site, which aided my thought process. 

##### Background Images and Site Colouring: 

For the *index.html*, *login.html* and *signup.html*, I used a book case image (mentioned in the Media section). The aim was to give the User arriving to the Landing page(s) an overt and colourful thematic background image, simply a way to capture the imagination. 

For the *bio.html* and *admin.html* I used my own photo from a library in Lisbon. This was simply a personal choice as I wanted the User/Admin's Bio/Profile section to the feel of an impressive library (a familiar feeling to book lovers).

For the rest of the site, due to the amount and type content (book reviews, pagination page options, book cover images, User comments, add/delete/edit reviews), and after consultation with my Mentor, I decided against using anything other than `background-color: #F0F0F0`, which is a light grey colour. I wanted the functionality and the content of the site to take over. Also as I used the colour `green` for the `navbar` and `footer` and coupling this with the colour  `orange` for the `jumbotron(s)`, I felt that there was more than enough in terms of colouration and style. For the font, I went with [Google Fonts](https://fonts.google.com/) style `Montserrat`, which was simply an aesthetic choice on my part. 


## **Wireframes**


The following section contains the mock-ups/wireframes that I created prior to beginning coding. The aim is to determine a concrete look and style for the site as well as provisionally considering some of its functionality.

I used the site [Figma](https://www.figma.com/) to construct my simple wireframe/mock-ups. It was the first time I used this tool, which was very simple and straight forward.

#### Wireframe 1


![index.html](https://github.com/NeiloErnesto89/Data_Centric_Dev_Milestone_Project3/blob/master/static/images/index_mock.jpg "Index.html Wireframe ")

*Figure 1. Index.html*


**Wireframe 1**: This was my very first mock-ups. On the finished site, I added a background photo that I personally took, of a library I visited in Lisbon for Bio pages and the colourful Book Case image on the Landing Page. The aim was to give the site a professional and crisp look, as well as adding more a thematic features. 


#### Wireframe 2


![mobile view index.html](https://github.com/NeiloErnesto89/Data_Centric_Dev_Milestone_Project3/blob/master/static/images/mobile_mock.jpg  "Mobile view index.html Wireframe ")

*Figure 2. Mobile view index.html*

**Wireframe 2**: Again this was just a very simple visual rendering of my initial concept, now just focusing on the mobile viewport and how everything would be placed for an optimum UX. 


## **Database** 

As mentioned in the mandatory project requirements section, it was necessary to: 
>"Build a MongoDB-backed Flask project for a web application that allows Users to store and manipulate data records"  

It was essential also to create a scalable application, capable efficiently of handling growing numbers of Users and their input on the database. 

With this in mind, I used [MongoDB Atlas](https://www.mongodb.com/cloud/atlas), which is a NoSQL, document-oriented database program.

I used 3 (essential) collections (all interrelated via the `ObjectId`) which were: 

* **Users**: contains the Username and a (Hashed) Password. Both are case-sensitive

* **Books**: containing all the data on the books e.g. name, author, a synopsis, a book cover photo, an amazon link (if possible) and a user rating (stars).

* **Bookscomms**: This collection is a User’s comment (along with Username) about a book review.

There are 2 other collections that are less pertinent to the User/Database interaction but I shall mention them nevertheless. There is a collection on the Mongo DB called '**Comments**' which was used solely for the Admin comments on the Internal Admin Note section. Again they were connected by the `ObjectId`. Also, at the beginning of the project I used another collection called '**Categories**', which was a dropdown list for the Book Review section. However I decided against using this dropdown on the finished product, but instead simply allowing the User to enter the category of their choice manually. It's a consideration for the future. 

**Database Security**:

As mentioned in the project brief, Users cannot access this database and the `MONGO URI` and `SECRET KEY` (which grant the site access to the Database). They are stored on an **env.py** file, which is then directly referred to in the `.gitignore` file (and therefore cannot be accessed from the outside).

Using [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/), which is a WSGI (Web Server Gateway Interface) and it describes how web applications communication with web servers. Using Werkzeug, I was able to hash the User(s) password(s) on the Database and, therefore, store them safely. 

#### Database Schema

As mentioned above, the collections within the Database were interconnected via the `ObjectId`, as represented below (the 3 'essential' collections are shown here):


![Database Schema](https://github.com/NeiloErnesto89/Data_Centric_Dev_Milestone_Project3/blob/master/static/images/database_schema.jpg "Database Schema")


As we can see from above, each Mongo DB collection is connected to the other 2 collections. Meaning the data is interdependent. Each collection contains its own specific data but they are all connected via the `ObjectId`. I ensured to test after each form submission that the correct details were inserted (via the route decorator on the **app.py** file). The relationships can be stated as: Users and Book Reviews, Users and User Comments, Book Reviews and User Comments. 


## **Features**

This section focuses on the pre-existing features present on the site, as well as a look to the future with regards to future improvements. 

### **Existing Features**

**Site Page by Page Breakdown**

*Further details on the site functionality are found on the [**Testing**](#testing) section below*.

In no particular order, here is a synopsis of the pages and their features:

• **Base.html**: This page is the base/layout html page used for Jinja Templates, which is common on all of the HTML pages. Each of the following HTML's use the base.html as their 'base' and are then appropriately adapted but maintain the links e.g. to the CSS stylesheet. The Jinja templating is used here, for example `{% extends "base.html" %}` followed by `{% block content %}` `{% endblock %}`. It's the general page layout, yet Users don't necessarily access this page itself, rather the other pages use it as the building block. 

• **Landing/Home page**:  The first page an existing User or a new site User arrives on. A Modal Pop-Up with a 'famous', randomly selected (from a list on the **app.py**) [quote](https://www.hookedtobooks.com/quotes-about-reading-books/) that greets them. They can close the Modal, but also avail of the information icon (which is used to explain different areas of the site in more detail, if necessary). The person who has arrived on the Landing Page can access the links on the Navbar containing the glasses icon and ‘home’, ‘login’ and ‘signup’ routes. The Jumbotron at the centre of the Landing Page is just a simple explanation of the site with buttons directing to the Login and Sign Up form sections. The Footer simply contains a created by/copyright mention, plus a link to my Github page. This is maintained throughout the site. 

• **Login page**: The same HTML layout persists on all the pages, with regards the Navbar (where only the options change due to User access (e.g. regular User or Admin)) and the Footer, which stays the same. The Login page is a straight forward card displaying a login in form. If a User has already Signed Up and has their details are saved on the Mongo DB, they can then Log In with their Username and Password combo. If they are new to the site, they can avail of the links to the Sign up Page. Any errors will display a flashed error message (e.g. **'Incorrect Password'**). Again, more details on this on the [**Testing**](#testing) section.

• **Sign Up page**: To Sign Up to the site, to avail of a User profile, to observe reviews and comments and create content, a prospective User must Sign Up with their details, which include, a Username, an Email Address (on this site there is currently no 2 factor authentication, so they can add any Email fulfilling the form field requirements, which will be saved on the Database), a Password (which is [Hashed](https://werkzeug.palletsprojects.com/en/1.0.x/utils/) and saved on the Database) plus a *‘Confirm Password’* input. This must match the chosen Password or a Flashed Error Message will appear. Other errors (including a choosing a Username already in existence) will prompt further Error Messages or tell them that the fields inputs are too long or too short. Again, more details on this on the [**Testing**](#testing) section.

• **User Bio/Profile page - (Only Users or Admin can access)**: Once the User has successfully Logged In, their chosen Username is displayed on a Jumbotron, in a *Welcome Message* (e.g. ‘Welcome John’). The Navbar options have changed to give the User access to the site and its functionalities (e.g. add a review or observe all the reviews and comments). Users can also use the buttons to access the main sections of the site.

• **All Reviews page - (Only Users or Admin can access)**:  The All Reviews page displays all the current book reviews that are present on the database. The current, or other, Users have previously added a book review and it is now currently being displayed, along with information such as book title, author, book cover picture and who has added the review (the rest of the information in on the individual book reviews page, the limited amount of information is to entice Users to learn more my click on the individual page.  There is also the paginated display of the book reviews to allow for scalability with increasing amounts content. If Users want to find out more detail on the book and view the User comments associated with a particular book review, they can avail of the **‘view book in more details’** button, which brings Users to Individual book review page. Finally, just above the footer, there is a primary button that Users can click on to add a review themselves (similar to the one found of the User’s Bio Page).

• **Add a Book Review page - (Only Users or Admin can access)**: The page is a straightforward card that displays a form that the User must fill out in order to successfully add their own Book Review. They need to add basic details such as the book’s title, the author, a summary and if possible an image link and an Amazon URL link. If these are incorrect or not available, then a placeholder image takes the place of the book cover and if the Amazon link isn’t provided, the code auto searches the Amazon website, using the associated tags (being the ‘book title’ and ‘author’, but not the other attributes). There is also potential here to monetise the site by becoming an [Amazon Associate]( https://affiliate-program.amazon.com/), which is free affiliate marketing program, which allows site owners to advertise Amazon products on their site (by creating links) and once a customer clicks on the links, and if they purchase a product from Amazon, the site owner can earn a referral fee. This is a future consideration. Each field has an Font Awesome icon attached to it as well as predefined `maxlength` and `minlength` field requirements to guide Users in submitting an appropriate form. Again more on these requirements on the [**Testing**](#testing) section.

• **Individual Book Review page - (Only Users or Admin can access)**: This page consists of a detailed card displaying all the chosen individual book's information (that has been previously added by any site User), such as a (bipartisan) book summary, a link to Amazon (where possible), a book cover picture (where possible), title, author, category, rating (in the form of stars (1-5)) and which User actually added the review. Underneath Users can observe other Users comments but also added their own. This page is probably the most important on the site as it not only gives Users an opportunity to add, edit or delete their own comments on a book but if they current User has actually created the book review itself, they can either delete this review or update/edit it also. This is the essence of the **CRUD based objective**.   

• **Admin Centre - Landing Page - (only for Admins)**: 
- *For CI testing purposes - **Admin** details are as follows (Username: **admin** + Password: **admin99** )*: 
- I added an Admin section so that only the Admin can access this area (if any other User tries to access without admin credentials, they are denied are redirected back the home page with a Pop-Up Modal to explain why). The Admin has full access to the site (so can act like a standard User, adding reviews and leaving, editing and deleting comments). However, the Admin has special access to an Internal Admin Forum. The access to the Internal Admin Forum area is where the Admin can add notes (for example; for future adjustments to the site). It acts like a Post-It Note section. The admin.html is basically acting as the admins landing page/bio. The options are limited but there is a huge amount of future scope. 

•	**Internal Admin Notes Forum - (only for Admins)**: As mentioned above, I also created a section displaying the admins internal comments on any topic (similar to a form), again just to promote a internal community style admin forum (as it's possible there is more than 1 person who has the admin access). The internal admin forum allows the admin to comment on any topic or issue, with a Post-It Sticky Note style feel to the form, either just for the admin to make a personal note for a later date but also for other admins to see (e.g. "need to add a search bar option"). It acts as an area for raising certain onsite topics and making internal constructive criticism. The internal note forum's goal is to aim the admin to build up a repertoire internal 'to-dos' and future topics. 

•	**Admin Internal Notes Form - (only for Admins)**: Originally I planned to utilise this a testing page for the Flask WTF libraries (found on the `forms.py` file) but I had decided to incorporate it with the site as the Admin area. There's room for improvement but I was satisfied with the results and I will be using something similar in the future. It's very straightforward, just a Flask wtf form that the Admin submits their internal notes into, which is then redirected to the **Internal Admin Notes Forum**.

### Further Existing Features

The following 'further existing' section is presented in a loose order of appearances on the app: 

* A Welcome/Random Quote Modal Pop-Up: is a feature that welcomes visitors to the site, displays a random quote (from an assigned list on the app.py file) and offers additional information to client. 

* Edit/Update Users Review Modal Pop-Up: If a User decides to edit their own comment, a Modal Pop-Up  displays a text box, with their old text in it, offering the User the option to craft a new, updated comment, which they can resubmit or, in the event of another change of mind, cancel the editing.

* Logout Modal Pop-Up: Once the user logouts out of their profile, they return to the Landing Page, now logged out of their User session but a Logout Modal Pop-Up prompts the User with information, confirming the log out action but also providing a log back in button if needed. 

* A Navigation bar that, when there is no user logged in, provides links to the home, sign up and login pages. There is a glasses icon that also redirects homeward. Upon a user logging in and being recognised, the Navbar offers different options which are redirecting the known user back to their profile back, the all reviews page or having the option to log out. 

* Buttons: Using Bootstrap, I aimed to have clearly labelled buttons to help users make choices, navigate the site like add, delete, edit, confirm, return, logout, close etc. The Buttons facilitate the CRUD options. 

* Icons and Links: I made use of some Font Awesome icons, such as the info icon to help guide Users. Another example would be the Amazon icon, which Users can click on and can direct them to the Amazon page of the book they have selected (where possible).

* Forms: using a mix of standard HTML forms and Flask-WTF to test out both methods. 

* Pagination: was utilised on the All Reviews section to facilitate site scalability of the site and also on the User Comments Forum


* A Footer: with a link to my Github page and my name/copyright logo.


### **Features Left to Implement**

I found this milestone project to be particularly interesting in terms of the learning curve, because as I moved forward with it, I discovered many new Python libraries and many more different features and functionalities that I could have implemented and utilised. 

In fact, I found it difficult trying to balance learning about new features and trying not to use them all. It was very enjoyable discovering all the possibilities but also, it became an exercise of discipline in terms of using just what was needed. 

Sometimes less is more. However, in the future I plan on adding a lot more functional features to this site. These include:

-	An intuitive search bar to allow for whole site searching. 
-	A more robust sign in/login process, including, for example, reCaptcha functionality.
-	A password and Username reset option.
-	When choosing a Username have a list of available Username (autofills as the User types)
-	Have a Password strength guage.
-	The possibility to delete, edit and update User profile details. 
-	A more expansive User profile in general including dates of signing in, the amount/times/dates of comments, if something was edited, personalised avatars, report comments (among a myriad of other profile options). 
-	Using more of the Flask libraries (lots were tested and not used) including Flask-Login.
-	Like/Dislike buttons for comments and books in the form of Thumbs Up/Down. I could also incorporate a simple counter on this to add the community feel of the site (e.g. 300 likes/24 dislikes).
-	Have the number of stars for the rating symbols displaying (with regard to the rating i.e. 3/5 means 3 separate stars physically appearing). 
-	Allow for more User interaction amongst Users, for example with messaging each other or having a live chat forum/discussion.
-	An autocorrect prompt when comments or reviews are being added.
-	A more efficient method of sorting and breaking up the User comments section such a 'word search' option, dated comments etc.
-	As mentioned in the **Add a Book Review page** section above, the [Amazon Associate]( https://affiliate-program.amazon.com/) program would the next logical and professional step one could make so that the site could potentially be monetised. By simply adding the Amazon affiliate links, providing a simple platform so that the Users can easily click on their chosen affiliate links and potentially purchase the item directly via those links, the site owners could earn a referral fee. So it’s certainly another future term consideration.


## **Technologies Used**

The following technologies were used on this project:

##### **Languages**

- [Python 3.7.5]( https://www.python.org/) - Python is an object-orientated high-level programming language. 


- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - is the renowned programming scripting language and the main libraries are JS. 

- [CSS3](https://developer.mozilla.org/en-US/docs/Archive/CSS3) - is used as the stylesheet language for styling and rendering.

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - is used as the standard Mark-Up  language. 
    
##### Frameworks

- [Flask](https://flask.palletsprojects.com/en/1.1.x/) -  is a micro web framework written in Python. It is used by constructing route decorators for the main functionality of the app. By using the Jinja templating functionality, Flask/Python is rendered on HTML pages. Flask libraries such as Flask-PyMongo (integrating Flask, Python and Mongo DB) were used to build the functionality of the site.

- [Bootstrap 4.3.1](https://getbootstrap.com/docs/4.3/getting-started/introduction/) - is a CSS framework that aids the grid and the layout and also the Modal Pop-Up's in this project

##### Database 

- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) – is a non-SQL, cloud database used to store, manage, update and delete datasets provided in collections.

##### Libraries


-  [JQuery version 3.2.1](https://jquery.com) - JS library to simplify HTML DOM manipulation and used also to initialise JavaScript elements. 
-  [Google Fonts](https://fonts.google.com/) - a library style **Montserrat** was used on this site.
- [Font Awesome 5.7.2](https://use.fontawesome.com/releases/v5.7.2/css/all.css) - used for the icons on the site. 

###### Other Technologies

- To generate the wireframes I used the site [Figma](https://www.figma.com/)
- To generate the Placeholder images I used the site [Placeholder](https://placeholder.com/)


# **Testing**


### **Validation** 

I used a variety of tools provided by specified sites to test my code and the apps functionality:


#### Python
As Python was the main language I used , I tested often and also learned to utilise in-code testing to resolve errors, particularly the pdb module e.g. ‘import pdb;pdb.set_trace()’, which is added above the erroneous code and you can evaluate the error in the terminal (thanks to my mentor Marantha for introducing this to me). 

For my Python code I passed it through the [PEP8online]( http://pep8online.com/). The first time I used the PEP8online I believe between around 90% errors were either `trailing whitespace` , `too many leading '#' for block comment` or `indentation contains tabs`, which I attempted to rectify progressively. The main focus here was always ensuring the code was clean, concise and above all, functioning correctly. 

#### JavaScript

I used [JSHint](https://jshint.com/) to validate the little amount of JavaScript code I used.

There were 3 warnings, which were all **Missing semicolon**, which I left alone as they didn't affect the code. 


#### HTML

For the HTML I passed my code through the [W3C Markup Validation Service](https://validator.w3.org/).

When I passed my HTML pages through this validator, there were some interesting results. I went about rectifying as much as resolved errors and warnings as possible but there were some curious results. For example, the first time I passed my `index.html` into the validation tool, I have **1 warning** and **10 errors**. However, oddly enough some of the errors didn't seem to pick up the Jinja templating and one error in particular for my `{% with messages = get_flashed_messages() %}` section, it said that the error was that **the font element is obsolete**. However, this was inline html code that I utilise as a time saving option (due to the aforementioned time constraints) and its function very much necessary (to test, I changed the size of the font and as expected, the size of the `flashed_messages()` altered). 

But as I discovered shortly after, that the Jinja templating wasn't recognised by this HTML validator, so I just ignored any errors/warnings related to the Jinja templateing.

Despite these anomalies, I generally found it to be a very useful tool and helpful for clarifying and understanding my code better.

#### CSS
For my CSS3 code, I passed it through the [W3C CSS Validation Service - Jigsaw](https://jigsaw.w3.org/css-validator/)

**Congratulations! No Error Found** was the response the validator gave the first time I passed my CSS code in.



### **Tests** 

As I progressed, day to day I mainly used Google Chrome Devtools to test/debug. I also tested the pages and functionality on other browsers Firefox, Safari and Microsoft Edge. I used the Toggle Device Toolbar to evaluate all the different viewports, which really helps the development process. I also enlisted the help of friends to simulate User experience testing on tablets (iPad) and a variety of phones (iPhone 5, iPhone6, Google Pixel 3, Samsung Galaxy). 

###### Referring to Original User Stories

To guide the testing approach, I took the original User Stories into consideration. So I tested to evaluate if I had managed to achieve a semblance of coherence and continuity to the site from the Users perspective. I also referred to the User Stories that I had originally created to help me focus on the site goals; for site responsiveness and functionality. 

On every page I test the navbar (hamburger icon positioning), the buttons (to see if the python code/functionality was operating correctly), if the correct details were registering on the Mongo Database, observing the varying Desktop and Mobile viewports (on different browsers), ensuring that the dropdown menu was the same on the varying screens (among many other checks).

Another huge focus, for example, was evaluating if the error messages were correctly shown to the User. For example, from the following User Stories - attempting to sign up but having a Username that is already taken in the Database. The following sections are a step by step testing guide to evaluate the site functionality from the Users perspective, depending on what the User is attempting to achieve onsite:


1. **New User, yet to have Signed Up, arrives on Landing Page:**

- i. Click on Sign Up Button - redirected correctly to Sign Up Page & Form

- ii. Being wary of the case-sensitive nature of the fields, the prospective User begins to fill in the form, but  using a Username that is already in Database (e.g.'admin). The User proceeds to fill in the form following the prompted regulations.

- iii. The prospective User then submits the form, with a pre-existing Username (unbeknownst to the prospective User) and result is a *Flashed Error Message*, here displayed in Jinja templating: **{form['username']} already exists! Please choose another"**

- iv. The prospective User is redirected back to the refreshed, empty Sign Up page, which is now displaying the aforeformentioned error message above. So then the User adds new Username (not on the Database) but after entering a Password in (following the length requirements), then the prospective Users then enters a *different* password into the **'Confirm Password'** section.

- v. Upon clicking on the form 'Submit' button, the result is a **Flashed Error Message** that is returned, stating correctly that the: **"Passwords Don’t Match!"**. 

- vii. There is also error prompts that occur if the `maxlength` and `minlength` requirements for each field are not met. For example, Passwords need to be `minlength="5"` and a `maxlength="15"`, so the User must enter a Password that is at least 5 characters long (or else they cannot submit their form). These requirements are utilised on all fields of the Sign Up Form with variety of lengths, depending on the fields requirements. 

- vii. Thereafter, I proceed to submit a fully valid Sign Up form (i.e. a new Username, an email address with an @ symbol followed by a part (such as '@hotmail.com') and 2 matching passwords. 

- viii. Upon clicking the Submit button, the new User arrives on the User Bio/Profile page, which displays a 'Welcome  {% username %}' message to confirm they are logged in, as well as new options on the Navbar and new Buttons available on the Jumbotron.

- vi. There is also a Flashed Message depending on if it's a first time Sign Up, which is: **"Congratulations on Successfully Signing Up to Bukish!"**. Or, if it's a pre-exisiting User Logging back in, it simply states *Thanks for Coming Back*.


2. **Returning User or Non-Registered User arrives on Landing Page:**

- i. Clicks on Login Button (on Jumbptron) and is redirected correctly to Login Page & Form:

- ii. The Non-Registered User fills in the Login form with an Incorrect or an Unknown *Username* (with any Password). 

- iii. The User then clicks the Submit button and as none of the data in the fields is registered on the Database, the result will be that the Non-Registered User is correctly redirected to the Sign Up Page, with the following, explanatory Flashed Error Message: **'Oops.. It Looks Like You Have To Sign Up !"**

- iv. Then the Non-Registered site User can Sign Up their details to be stored on the Database and will be granted access to the site. However, if the User has already got a Profile/User Information on the Database (Username, Password etc.) but has simply made an error in the Username field, they can click the link that returns them on Login Page.

- v. If it's simply a case that the User has made a typo error on the Login Username section, they can click back onto the Login Page, the User then proceeds enter the correct Username but then enters the wrong password (for whatever reason), clicking submit afterwards.

- vi. Then, upon submitting the Login form, the result is a correctly displaying the Flashed Error Message stating that the : **"Password Is Incorrect!"**. Clearly telling the site User that they have made an error on the Password.

- vii. Finally, once the User has correctly typed in the correct Username and  correct Password combo. And, then upon resubmiting a fully valid Login form, the User's session is activated and the User is redirected to their Bio/Profile Page, along with the Jinja Template 'Welcome {% username %}' message to confirm that that particular User is logged in.

- Overall, I felt that the Sign Up, Login, and Index/Landing Home Pages demonstrated clear and concise UX in terms of sufficiently prompting and clearly directing all the types of Site Users e.g. the Non-Registered site User(s), Admin(s) and Pre-Existing User(s) (Logged In/Out) to the correct page/form to access the content and explain why other content access is restricted.

3. **As Logged In User/Admin and Non-Signed-Up/Logged to test the clear error messages/prompts:**
- Straightforward testing, once I was either; (1) signed in as User (e.g. John) (2) Not signed in at all (3) Logged in as the Admin, I set about typing into the URL the different routes (e.g. `/all_reviews` (route decorator on the app.py) when not Logged in at all) or (`/admin` when the User was Logged in but not as the Admin) . Underneath is an example of some of the results of testing: 
    
    1. **Pre-Existing or Newly Signed Up User Logged In as a Standard User (e.g. John)**
        - User Logs In as per usual with the predefined Log In Details (case sensitive).
        - Arrives on Bio/Profile page with flash statement (**""**).
        - Then types, for example, `/admin` at the end of the URL and presses enter.
        - As expected, as access to the Admin page is just for the Admin, the User has been redirected back to the Home Landing Page and is met with a flashed message stating **'Restricted Area - Access Denied!'**.   
        - The User can then click on the **Log Back In** button on the Pop Up Modal and, **as the User is still currently logged in on their User session**, the User is automatically redirected back to their Bio Profile page (without having to Sign Back In with their Username and Password). 
        - Once returned to their Bio-Profile Page, the User is greeted with an informative flash message stating either:
            - (1): **"You're Already Logged In"** - This flash message is displayed if they User has selected to click on the 'Login In' button either directly on the on the Modal Pop-Up (with the *restricted* flash message), or, upon closing the Pop-Up Modal, selecting the 'Login' route on the Navbar or the 'Login' button on the Jumbotron. 
            - (2): **"You're Already Signed Up"** - This flash greeting is displayed if the User (who attempts to access a restricted URL e.g. (the `/admin` profile)). They are redirected back to the Landing Home Page (index.html), they must close the modal and either chose the 'Sign Up' route on the Navbar or the 'Sign Up' button on the Landing Jumbotron.
        - This situation is the same if the Pre-Existing User attempts to access the following `/` routes via the Url:
            - `/admin` - the restricted Admin Centre page
            - `/comment_form` - the restricted Admin Internal Notes route decorator Form which utilises the `('GET', 'POST)` methods, which are 2 different [HTTP requests](https://medium.com/@LazaroIbanez/difference-between-the-http-requests-post-and-get-3b4ed40164c1) used to add/update to, and retrieve remote data from, the Database 
            - `/comment_page` - the restricted route decorator which directs the Admin to the Internal Admin Notes Form page
            - `/all_comments` - the restricted Admin Internal Notes Forum page containing all the Admin's previously recorded Internal Notes
    
    2. **Logged In as a Admin (e.g. John)**
        - Using Admin credentials to Log In (Username: **admin** + Password: **admin99** )
        - Arrive on Admin.html (Admin Landing page)
        - Ensuring the different options on the Navbar options are rendering (such as the **Admin** landing page, the **Internal Admin Notes** section as well as the other pages available to all Logged In Users)
        - The Admin has no restrictions, so no flashed messages are displayed (as mentioned above) whilst the Admin is navigating the site. 
        - The testing of the site the redirection options/routes demonstrated this
        
    3. **Non Logged In (e.g. Non-Registered Site User) but on the Home Landing Page**
        - Using no credentials and not Logging In 
        - Arrived on Index.html (Home Landing page)
        - Ensuring the different options on the Navbar options are rendering for specific User (Login Page, Sign Up Page and back to the Home Page)
        - Then typing, for example, either `/admin`, `/bio` or  `/all_reviews` etc., at the end of the URL and pressing enter.
        - As expected, the Site User is met with a message stating **'Restricted Area - Access Denied!'** , with the User redirected back to the Home Landing Page. 
        - As a Non-Logged In, *not in session User*, one may attempt to access the follow routes/pages via the URL, however, all with similar **Restricted Area** flashed message outcomes:
            - `/admin` 
            - `/comment_form` 
            - `/comment_page` 
            - `/all_comments` 
            - `/review_page`
            - `/all_reviews`
            
        - The Non-Logged In site User can then proceed to the Login or Sign Up page and proceed as stated in sections **(1)** and **(2)**. 
        
4(i). **Testing CRUD Functions**:  **Logged In User/Admin Adding a Review - Creating Content**
    
- Attempting to fill in empty book (all fields empty) - as expected, the User prompted to fill out field(s).

- User attempts to fill out some fields but not all (for example, fills Book Title but leaves Author empty) - - as expected, the User prompted to fill out field(s).

- I adjusted the Book_Title's in-field minimum and maximum character length(s) to: `minlength="4"` and `maxlength="50"` and so, if a User doesn't follow these regulations they are prompted to rectify this. 
- I also set the following in-field minimum and maximum character length(s) to:
        - **Book_Author** : `minlength="4"` and `maxlength="35"`
        - **Book_Author** : `minlength="4"` and `maxlength="35"`
        - **Summary** : `minlength="20"` and `maxlength="350"`

- All of which, unless the User follows the minimum and maximum character length requirements, they will be prompted to resolve this and therefore cannot add a review that doesn't follow these requirements.

- The **Book Cover Image Link** and **Amazon Link** fields are specific functions fields that can be filled out (e.g. a link to an image url address and a link to an Amazon book page) which will render on the finished Book Review. However, if left empty, the book cover pic function replaces the empty field with a bookcover placeholder image. And the Amazon function attempts to search the [Amazon](https://www.amazon.co.uk/) website, using the 'book_title' and 'book_author' fields, in an attempt to render a direct and correct link to the book in question.

- The star rating is a dropdown menu giving Users the option to rate the review from either 1-5 stars. It is automatically set at 1 so unless the User adjusts this, the rating will be given at 1 (to imply the lowest rating). All star ratings were tested and functioning. 

- Once all the requirements are met, the User can submit the review. Once they click the submit review form, they are redirected back to the Book Review page and are greeted with a flashed message saying **"Your Review Has Been Added"** 

- The User must go to the last Paginate page to see their most recent review, there they can observe their review card and click **'View book in more detail'** to see the full review and avail of the CRUD options (explained underneath)
    
4(ii). **Testing CRUD Functions**: **Edit and Delete Reviews**

- Once a User has added a review(s) and/or comment(s), the User can avail of the options to **(1) edit (2) delete** the aforementioned review(s) and/or comment(s). Having these options was very important to the site functionality and provides the CRUD tenets. To test these functionalities, I logged in as User and undertook the following steps:
    - I added a Book Review (following the guidelines as stated in the section above) and once I submitted the review, I click the **'View book in more detail'** link underneath the book card on the Book Reviews section and this brings me to the Individual Book Review section. Here is where I can test the CRUD performance.
    
    - If the logged in User has add the Individual Review that they can clicked on, 2 buttons appear at the bottom of the review card, which state **Delete** and **Edit*. These options are only available to the User who actually added the content. This referenced in the route decorator on the app.py file as well as using the Jinja templating e.g. `{% if user._id == book.added_by["_id"] %}`
    
    - Therefore, if the User Id matches the Id of the User who added the Book Review (in the book collection), the option to delete and/or edit the review is available. 
    
    - If the User clicks **Edit**, they are brought to `/adapt_review/<book_id>` page, which is the Add Review card/form but with the current book's (which the User clicked on) details auto-filled in the fields. 
    
    - The User can choose remove, add, update and correct any of the fields they see fit (as long as they follow the max and min length guidelines mentioned previously).
    
    - The User can then **Add updated Review** which adds the Updated view to the Database and the updated version is automatically available of the site. Once they submit the updated review, the User is are greeted with a flashed message saying **"Your Review Has Been Updated"** to confirm the database has received and added the updated file. 
    
    - Other the User can choose to click the **Cancel your update** which stops the editing process and returns the User back to the (all) Book Reviews section to the original, unedited version of the review is still available.
    
4(iii). **Testing CRUD Functions II**: **Edit and Delete Comments**
- To the User Comments section, underneath the individual book review.
    - Within the jumbotron, the User (all Users, not just the ones who have added the book review) has (have) the option to add their own comment. 
    - To add a comment, the User simply has to write what they want in the comment `textarea` and click the submit button. I added the `minlength="3"` and `maxlength="70"` requirements, which I felt were a fair amount for a comment section. If a User goes over or under the length specifications, they will be prompted to rectify this.
    - Once the User clicks submit, the page is refreshed, the User is greeted with a flashed message saying **"Your Comment Has Been Added"**, to confirm their comment has been recorded. 
    - Once the User scrolls down, they can see their comment at the top of the comment list. And underneath the User's added comment, the options **Delete* and **Edit** appear (as buttons).
    - As mentioned above, this is referenced in the route decorator on the app.py file as well as using the Jinja templating e.g. `{% if user.username == incomment.added_by["username"] %}`, so that only the User who has added the comment has the option to either edit and/or delete the comment. All other comments added by all other Users won't have these CRUD option(s). 
    - So, if the Username is the same of the Username of the database, the User can click the **Delete** button to completely remove their comment.
    - Or, they can click the **Edit** button. The edit button opens up a simple in-page Modal Pop-Up. The title on the Modal states (using the Jinja templating) **Edit Your Comment {{username}}** . Underneath is a `textarea` with the original User's comment auto filled as the placeholder text. The User then can edit/update their review (following the length requirements). 
    - Once they are satisfied, they can either click the **Update** button, which will confirm the updating process by prompting the User with a flashed message at the top of the page, stating **Your Comment Has Been Edited!** and now the User's new/updated comment will be visible.
    
4(iv). **Testing CRUD Functions II **: **Admin Area- Create and Delete Notes**
- The Admin can add reviews, update and/or delete their own reviews and/or all other User reviews. Admins also can add, delete and/or edit their own comments and/or all other User comments. 
- However Admin's also have an extra Internal Notes area which is only for the Admin(s) use.
- Here they can simply add notes via a CommentForm using flask-wtf (forms.py- as mentioned above). The Add Internal Notes form is very straightforward and allows the Admin to create internal content.
- For the **Note Header** on the forms.py, I set `Length(max=15)` and for the **Your Comments** I set `Length(min=4), Length(max=50)]`. So the Admin had to abide by these requirements.
- Once the Admin clicks submit, the Internal Note is posted to the **Admin Internal Notes** where the Admin (who is the only User who has access to this area) can **Delete** any notes they see if. 
- I didn't add an **Edit option** due to the shortness of the note. I felt that the Admin would be the only person seeing this so they would simply delete or add another note (for this project, I kept it simple.).
- Overall, the Admins role is indeed that of the administrator. A point of consideration for the Admin is that, obviously, non-valid/inappropriate content can and should be removed to maintain the standard of the site. However discretion is necessary because the Users want to express themselves and not be censored. Also User data is then lost/altered if the Admin deletes or edits them as the Admin is the User who then assumes the `added_by` in the database.

To bring this section to a conclusion, these tests were some (not all) of the tests conducted to observe the site functionality and if the User Stories were respected. The follow section discusses some of the many issues and bugs I encountered on my coding journey.

### Interesting Bugs & Issues:  

- The book cover images sized to `28rem` as it was the size most suited to each screen I tested, but I had some trouble implementing it as it kept returning some funky images. However, if no book cover image was chosen, the Placeholder Image kept returning a much stretched grainy/blurry placeholder. The Placeholder image isn't so clear but due to my own personal project time constraints, I couldn't quite sort it out however it's something I will return to rectify in due course. 

- Another sizing issue I had come with the background image. I resolved it with a cover container on chosen templates and respective sizing on the CSS stylesheet. However, I found that the issue stemmed from AWS Cloud 9's slow CSS preview rendering, making the development process difficult as I would make some tests/previews using Google Chrome Devtools and then implement the adapt CSS on the stylesheet but sometimes the change wouldn't appear for 30/45 minutes (post Git and Heroku push). Sometimes clearing the cache or deleting cookies helped but overall this part of the process was particularly frustrating and it's a consideration for choosing future IDE's.  
 
- Route decorators, Jinja templating and Werkzeug errors were numerous at the beginning, as with any learning curved but I learned (thanks to my mentor Marantha) how to debug inline using the [PDB Python debugger](https://docs.python.org/3/library/pdb.html). I used it particular with the signing/login function. 

- In general, I encountered lots of issues just with getting to grips using Flask and Python in tandem with Mongo DB. One issue that took me a while to sort out was actually to do with Mongo DB registering just the `ObjectId` number but not the `Object Id` itself. For example, when I added a Book Review, underneath the **added by** section, it stated something like `5e43e0c617ae622da15b9d6f`. I finally discovered the issue was simply the renaming of titles of my `if` loops inside my route decorator. 

- There were other similar issues that occured if the indentation was incorrect. I also struggled a bit at the beginning with naming variables for Jinja in my return statements. Sometimes it's the most obvious thing that you can miss when you're looking for a problem. 

- For my `/admin` route decorator, I was having an issue whereby, if I was not signed in and when trying to access this page by typing `/admin` at the end of the URL, it would return a 'key error' page. So after a number of efforts, I tried to insert a `try` and `except` block, which neatly resolved the issue. I found some [documentation on this site](https://docs.python.org/3/tutorial/errors.html) about handling errors and exceptions and so I added them to a few more route decorators to resolve any gaps in the code. 


## **Deployment**


### Github 

#####  *This site is deployed on [Github](https://github.com/NeiloErnesto89/Data_Centric_Dev_Milestone_Project3)

This project was built and tested on the [AWS Cloud 9 IDE.](https://aws.amazon.com/cloud9/) 


This site is hosted using GitHub. My code was directly deployed from the master branch. I added, committed and pushed my updates via the terminal as often as possible. I then deployed the site automatically upon receiving the new commits to the master branch/source. The following commands were used for Github deployment:


- The `$ git init` command was utilised to initialise my local repo. 
- Then then `$ git remote add origin https://github.com/NeiloErnesto89/Data_Centric_Dev_Milestone_Project3.git` command was used to add the new remote repository.  
- Afterward I used the `$ git push -u origin master` command to push my code to the master branch of the Github remote repo.
- Thereafter I used the following commands: `$ git add .` (to add all) or `$ git add 'filename'` (to add just a specific file) and the `$ git commit -m "initial commit"` (followed by any relevant comment with the commit) to add and commit files. 
- Then, I would use the `$ git push -u origin master` command to push my updated code to the remote Github repository.
   


### Heroku

#####  *This site is deployed on [Heroku](https://datacentric-milestone-bookrev.herokuapp.com/)

My project has also been deployed via the master branch and hosted on Heroku. Heroku is a cloud platform that allows for building, developing and operating applications on the cloud [Heroku](https://dashboard.heroku.com/apps) in a range of programming languages. Python was the mainly used for this project.

The following process was undertaken to successfully deploy the project on the Heroku:

- A very straightforward beginning by simply creating my application (named: datacentric-milestone-bookrev) on my Heroku profile. 
- I then had to configure some of the settings. In the *settings* area, I set the `IP: 0.0.0.0` and `PORT: 5000` in the *reveal config vars* section. This is mirrored on my app.py.
- After creating my env.py file (along with the .gitignore file), I added the `MONGO URI` and `SECRET KEY` in to the *reveal config vars* area.
- I installed Heroku via my command line interface, using `sudo snap install --classic heroku` on my AWS C9 terminal. 
- Afterwards, and from there on in, I would simply type `heroku login`, which would redirect me to another tab where I would sign in to Heroku as proceed once more in the terminal.
- The next step was to initialise a git repo and add my Heroku remote repo command: `$ heroku git:remote -a 'datacentric-milestone-bookrev' `. 
- However, as per the requirements, before I can `push` my code to the Heroku app, I need to install 2 important files:
    - A **requirements.txt** file is needed to run the installed dependencies, so to create and commit this file, the following command was used: `$ sudo pip3 freeze --local > requirements.txt` (and also used to update the file if any libraries were added).
    - A **Procfile** is needed to direct the Heroku app to the file that it needs to run. So I used the command `$ echo web: python > Procfile` in the terminal to install the file. This was followed by a simple command in the terminal to run the web process: `$ heroku ps:scale web=1`.
- Finally, to deploy I would use the `$ git push heroku master` to deploy my code on the Heroku app.

After any big changes, advancements on my code, I would push my code to the Heroku app to check if it was functioning. There were some slight issues with the `MONGO URI` and `SECRET KEY` but it was resolved quickly. 


# **Credits**

## **Credits/Content**

- *The Code Institute* documents and modules were a great source of help.
- My mentor Maranatha, who helped to point me in the right direction with some really clear and concise explanations such as for the [pdb](https://docs.python.org/3/library/pdb.html) (for which I used this documentation to further explain its function)
- The Pagination code (plus the explanation) was taken and modified from 'ShaneMuir_Alumni' via a Slack Thread and further from his [cookbook project](https://github.com/ShaneMuir/Cookbook-Recipe-Manager). 
- I read extensively this [Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by Miguel Grinberg. (It's just a shame I discovered it quite late in the day). 
- The `# Book Image/Pic Link Function` and `# Amazon Link Rendering Function` code were both derived, taken and adapted from fellow coding student [JBroks' MS3 project](https://github.com/JBroks/booksy-reviews). Overall, this was excellent project and a great source of inspiration (and something to strive towards) for fellow coding students!
- This unbelievable blog post by [Hackers and Slackers](https://hackersandslackers.com/flask-routes/) was a massive source of clarity and explanation for a huge amount of my code.
- The Werkzeug password hashing function was derived from this very helpful video by [Pretty Printed](https://www.youtube.com/watch?v=jJ4awOToB6k&list=PLgNY7mXdwZG8XgloGmy6PHtLFUA3Qctub&index=93&t=0s)
- Further Pymongo explanations about PyMongo were uncovered via [Tech with Tim](https://www.youtube.com/watch?v=rE_bJl2GAY8&list=PLgNY7mXdwZG8XgloGmy6PHtLFUA3Qctub&index=88&t=331s)
- A lot of [Corey Schafer videos](https://www.youtube.com/user/schafer5) as just general information and explanations on a huge array of topics. 
- Used on many occasions, one example being with a CSRF token on with regards to Flask wtf forms and the Jinja/ templates: [StackOverflow](https://stackoverflow.com/questions/39260241/flask-wtf-csrf-token-missing/39262931). 
- For the *Flask WTF forms* I looked at this [video](https://www.youtube.com/watch?v=8aTnmsDMldY), read this [article](https://hackersandslackers.com/flask-wtforms-forms/) and the [installation guide](https://flask-wtf.readthedocs.io/en/stable/install.html)
- [W3 Schools](https://www.w3schools.com/) as always provided some very good explanations such as with the paginate buttons section

- [Quotes](https://www.hookedtobooks.com/quotes-about-reading-books/) on the Landing Page Modal were taken from this site. Plus one classic [Trump quote](https://bookstr.com/list/top-10-donald-trump-quotes-about-reading-and-writing/)

All book reviews were personally written by me (or by my friends/family for tests) but information and summaries were extracted from [Amazon](https://www.amazon.com/books-used-books-textbooks/b?ie=UTF8&node=283155), [Wikipedia](https://www.wikipedia.org/)
and [Google Books](https://books.google.ie/bkshp?hl=en&tab=pp&authuser=0). I also extracted the book cover images from these sites (mentioned below). 

Further explanations which helped out were:
- For [CRUD](https://en.wikipedia.org/wiki/Persistence_(computer_science))
- For [Scalability](https://www.koombea.com/blog/why-scalability-matters-for-your-app/)
- Using this blog to help explain the [session.clear()](https://www.codepoc.io/blog/asp-net/5138/what-is-the-difference-between-session-abandon-and-session-clear) function

#### **Media**

All the affiliate links are directed to [Amazon](https://www.amazon.com/books-used-books-textbooks/b?ie=UTF8&node=283155), however I have no affiliation to Amazon. The links to the Amazon website was merely a functionality of the site and certainly no User is under any obligation whatsoever to purchase from their site. In fact, I would very much encourage people to go to their local library or book shop instead :) .

- [Book_Case.jpg](https://www.vectorstock.com/royalty-free-vector/library-book-shelf-literature-books-cartoon-vector-21597741) was taken from this site. 

- [Bukish.jpg](https://www.vectorstock.com/royalty-free-vector/open-book-cartoon-symbol-icon-design-beautiful-vector-17379964) was taken from this site. 

- All other images, I own/created:  (1) **libs.jpg** - photo (2) **database_schema.jpg** - screenshots from Mongo DB + Paint (can't beat it!))

- [Figma](https://www.figma.com/) was used to create the Mock-Ups/Wireframes.

I  extracted the 'book cover images' and 'no image placeholder' from these sites: 
- [Amazon](https://www.amazon.com/books-used-books-textbooks/b?ie=UTF8&node=283155), 
- [Wikipedia](https://www.wikipedia.org/)
- [Google Books](https://books.google.ie/bkshp?hl=en&tab=pp&authuser=0). 
- [Placeholder](https://via.placeholder.com/468x60?text=No+Image+Available+on+Bukish)



#### **Acknowledgements**

A huge thank you to my mentor Maranatha Ilesanmi. He is a great guy, who's always calm, concise and just really helped me out a lot.

Thanks to Code Institute Support team (a great bunch), my fellow students/alumni (via Slack), to my family and my girlfriend for everything :)

##### *Disclaimer* 

This is an educational project, built by Neil Smyth for completion of the Data-Centric Development Module for the Code Institute Full Stack Software Development Diploma Course.