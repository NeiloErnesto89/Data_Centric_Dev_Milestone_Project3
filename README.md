# **Data-Centric Milestone Project 3**

The following section details the data-centric development, which is the third milestone project issued by Code Institute. The title of my project is **Bukish : The Online Book Reviews and Recommendations Site**

# **Bukish** 

**The Online Book Review and Recommendations Site**

Bukish is a simple, online book reviews forum. The aim of the site is to provide fertile ground for the book loving community to come together to rate and recommend literature. Users join up to engage with others and express their love (or hate!) for books they’ve read. But also aides users in discovering new literature, gauging how the community feels about certain books and even directly facilitating an online purchase (via links to online stores - namely  **Amazon**). 

Bukish allows users to store their personalised content, to delete and update reviews/comments. The aim is to allow for an interactive, fun and personalized user experience.

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

The project is the culmination of the Data-Centric Development module on the Code Institute Full Stack Software Development Diploma. 

The projects purpose was stated as: 
> "(To) build a full-stack site that allows your users to manage a common dataset about a particular domain".

The value is that users of the site simply add their own data, with the advantage being, a user can avail of the collective information/data of the community.

Therefore the site owner, who could well be a prodigious user/member of the community, provides the users with the site and its functionality. And in return, among other benefits, the site owner can avail of the acquired collective dataset. Scalability was another focal point as, with an expanding user based which creates site content at will; it needed to be correctly implemented to facilitate this. Refer to the Database Schema for more information on the scalable aspect of the site.

The site was built with all of these points this in mind, along with the mandatory requirements, which were (the following list was taken, and shortened, from the CI project requirements section):

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

As specified in the project requirements, the aim of this project is to aid the users to manage and contribute to a common dataset. So naturally, a massive consideration would be on the user experience and the ease with which users can navigate the site. 

Bearing this in mind, the goal of this milestone project was to create a web application using **Python**, the **Flask** libraries (a Python framework) and a (NoSQL) Document-Based Database (in my case; **Mongo DB**) to construct the functioning app, as well as incorporate the main tenets of the *CRUD* operations (Create, Read, Update and Delete). 

**CRUD** refers to [persistence storage](https://en.wikipedia.org/wiki/Persistence_(computer_science)), encompasses the following 4 main pillars:

**Create**:
- add new, unique data to the database.

**Read**:
- Fetch data from the database.

**Update**:
- change and edit pre-existing database data.

**Delete**:
- completely remove data from database. 


My overarching aim was to create a simple, efficient and sleek user friendly site, using intuitive design, clear and concise text and enticing colours to guide users. The simple layout would facilitate a pleasant experience and hopefully entice users to add their own reviews and comments, thus participating in building the websites database, as well as the community. The target being **reciprocity**; the more users, the more comments and reviews, the more the database extends.  But with the increasing content, I wanted it also to be scalable whilst expanding. 

So with these focal points in mind, I tried to adjust the UX of this site for the following user type:


### **User Stories**

A typical/archetypal user would be interested in reading books, book recommendations and writing reviews. They would also be willing members of an online community.


* **As a user**, I would like to browse on site so I can avail of book reviews, comments and links.
* ... I would like to sign up and have my own account, so I can access reviews and comments. 
* ... I would like to add my own personalized reviews and comments. 
* ... I would like to add participate in an online community for a topic that I’m interested in.
* ... I would like to express and share my own views within a likeminded community. 
* ... I would like to update and/or delete my reviews or my comments at any time and also not have any other user update and/or delete my content.
* ... I'm looking for books as gifts and I need inspiration (as well as some links to Amazon so I can buy the book(s) online).

These are just some of the user stories that I considered whilst constructing the site. As a book lover myself I had some personal considerations of what I would like to experience on a similar site, which aided my thought process. 


## **Wireframes**


The following section contains the mock-ups/wireframes that I created prior to beginning coding. The aim is to determine a concrete look and style for the site as well as provisionally considering some of its functionality.

I used the site [Figma](https://www.figma.com/) to construct my simple wireframe/mock-ups. It was the first time I used this tool, which was very simple and straight forward.

#### Wireframe 1


![index.html](https://github.com/NeiloErnesto89/Data_Centric_Dev_Milestone_Project3/blob/master/images/index_mock.jpg "Index.html Wireframe ")

*Figure 1. Index.html*


**Wireframe 1**: This was my very first mock-ups. On the finished site, I added a background photo that I personally took, of a library I visited in Lisbon. The aim was to give the site a professional and crisp look, as well as adding more a thematic features. 


#### Wireframe 2


![mobile view index.html](https://github.com/NeiloErnesto89/Data_Centric_Dev_Milestone_Project3/blob/master/images/mobile_mock.jpg  "Mobile view index.html Wireframe ")

*Figure 2. Mobile view index.html*

**Wireframe 2**: Again this was just a very simple visual rendering of my initial  concept, now just focusing on the mobile viewport and how everything would be placed for an optimum ux. 


## **Database** 

As mentioned in the mandatory project requirements section, it was necessary to: 
>"Build a MongoDB-backed Flask project for a web application that allows users to store and manipulate data records"  

It was essential also to create a scalable application, capable efficiently of handling growing numbers of users and their input on the database. 

With this in mind, I used [MongoDB Atlas](https://www.mongodb.com/cloud/atlas), which is a NoSQL, document-oriented database program.

I used 3 (essential) collections (all interrelated via the `ObjectId`) which were: 

* Users: contains the Username and a (Hashed) Password. Both are case-sensitive

* Books: containing all the data on the books e.g. name, author, a synopsis, a book cover photo, an amazon link (if possible) and a user rating (stars).

* Bookscomms: This collection is a User’s comment (along with Username) about a book review.

#### Database Schema

As mentioned above, the collections within the database were interconnected via the `ObjectId`, as represented below:


![Database Schema](https://github.com/NeiloErnesto89/Data_Centric_Dev_Milestone_Project3/blob/master/images/database_schema.jpg "Database Schema")


As we can see from above, each Mongo DB collection is connected to the other 2 connects. Meaning the data is interdependent. Each collection contains its own specific data but they are all connected via the `ObjectId`. I ensured to test after each form/input that the correct details were inserted (via the route decorator on the app.py file). The relationships can be stated as: users and book reviews, users and user comments, book reviews and user comments.  


## **Features**

This section focuses on the pre-existing features present on the site, as well as a look to the future with regards to future improvements. 

### **Existing Features**

**Site Page by Page Breakdown**

In no particular order, here is a synopsis of the pages and their features:

•	**Landing/Home page**:  The first page an existing user or a new site user arrives on. A Modal popup with a famous, randomly selected (from a list) quote that greets them. They can close the model but also observe the information icon which explains different parts of the site in more detail if necessary. The person who has entered the landing page can access the links on the Navbar containing the glasses icon and ‘home’, ‘login’ and ‘signup’ links. The Jumbotron at the centre of the landing page is just a simple explanation of the site with buttons directing to the login and sign up sections. 

•	**Login page**: a straight forward card displaying a login in form. If user has already signed up and has their details saved on the Mongo DB. They can log in with their username and password combo. If they are new to the site, they can avail of the links to the sign up page. Any errors will display a flashed error message (e.g. incorrect password).

•	**Sign Up page**: To sign up to the site, to avail of a user profile, to observe reviews and comments and create content, a prospective user must sign up with their details, which include, a username, an email address (on this site there is no 2 factor authentication so they can add any email, which will be saved on the Database), a password (which is hashed and saved on the Database) plus a ‘confirm password’ input. This must match the chosen password or an error message will appear. Other errors (including a choosing a username already in existence) will prompt an error message. 

•	**User Bio/Profile page**: Once the user has successfully logged in, their chosen username is displayed on a Jumbotron, in a welcome message (e.g. ‘Welcome John’). The Navbar options have changed given the user access to the site (e.g. add a review or observe all the reviews and comments). Users can also use the buttons to access the main sections of the site.

•	**All Reviews page**: A page that displays all the current book reviews that are present on the database. The current, or other, Users have previously added a book review and it is now currently being displayed, along with information such as book title, book cover picture and who has actually added the review.  There is also the paginated display of the book reviews to allow for scalability with increasing amounts content. If Users want to find out more detail on the book and view the User comments associated with a particular book review, they can avail of the ‘view book in more details’ button, which brings Users to Individual book review page. Finally, just above the footer, there is a primary button that Users can click on to add a review themselves (similar to the one found of the User’s Bio Page).

•	**Add a Book Review page**: The page is a straightforward card that displays a form that the User must fill out in order to successfully add their own book review. They need to add basic details such as the book’s title, the author, a summary and if possible an image link and an Amazon URL link. If these are incorrect or not available, then a placeholder image takes the place of the book cover and if the Amazon link isn’t provided, the code auto searches the Amazon website, using the associated tags (being the ‘book title’ and ‘author’, but not the other attributes). There is also potential here to monetise the site by becoming an [Amazon Associate]( https://affiliate-program.amazon.com/) , which is free affiliate marketing program, which allows site owners to advertise Amazon products on their site (by creating links) and once a customer clicks on the links, and if they purchase a product from Amazon, the site owner can earn a referral fee. 

•	**Individual Book Review page**: This page consists of a detailed card displaying all the chosen individual books information (that has been previously added), such as a summary, a link to Amazon (where possible), a book cover picture (where possible), title, author, category, rating (in the form of stars (1-5)) and which User actually added the review. Underneath uses can observe other users comments but also added their own. This page is probably the most important on the site as it not only gives Users an opportunity to add, edit or delete their own comments on a book but if they current User has actually created the book review itself, they can either delete this review or update/edit it also. This is the essence of the CRUD based objective.   

•	**Admin Landing Page**: (For CI testing purposes - Admin details are as follows (Username: **admin** + Password: **admin99** ) 
    - I added an Admin section that only the Admin can access this area (so if any other User tries to access without admin credentials, they are denied are redirected back the home page with a Pop-Up Modal to explain why). The Admin has full access to the site (so can act like a standard User, adding reviews and leaving.editing and deleting comments). However, the Admin has special access to an Internal Admin Forum . The access to the Internal Admin Forum an area where the Admin can add notes (for example; for future adjustments to the site). It acts like a Post-It Note section. The admin.html is basically acting as the admins landing page/bio. The options are limited but there is a huge amount of future scope. 

•	**Internal Admin Notes Forum**: As mentioned above, I also created a section displaying the admins internal comments on any topic (similar to a form), again just to promote a internal community style admin forum (as it's possible there is more than 1 person who has the admin access). The internal admin forum allows the admin to comment on any topic or issue, with a Post-It Sticky Note style feel to the form, either just for the admin to make a personal note for a later date but also for other admins to see (e.g. "need to add a search bar option"). It acts as an area for raising certain onsite topics and making internal constructive criticism. The internal note forum's goal is to aim the admin to build up a repertoire internal 'to-dos' and future topics. 

•	**Admin Internal Notes Form**: Orginally I planned to utilise this a testing page for the Flask WTF libraries (found on the `forms.py` file) but I had decided to incorporate it with the site as the Admin area. There's room for improvement but I was satisfied with the results and I will be using something similar in the future. It's very straightforward, just a Flask wtf form that the Admin submits their internal notes into, which is then redirected to the **Internal Admin Notes Forum**.

### Further Existing Features

The following 'further existing' section is presented in a loose order of appearances on the app: 

* A Welcome/Random Quote Modal Pop-Up: is a feature that welcomes visitors to the site, displays a random quote (from an assigned list) and offers additional information to client. 

* Edit/Update Users Review Modal Pop-Up: If a User decides to edit their own comment, a Modal Pop-Up  displays a text box, with their old text in it, offering the User the option to craft a new, updated comment, which they can resubmit or, in the event of another change of mind, cancel the editing.

* Logout Modal Pop-Up: Once the user logouts out of their profile, they return to the Landing Page, now logged out of their User session but a Logout Modal Pop-Up prompts the User with information, confirming the log out action but also providing a log back in button if needed. 

* A Navigation bar that, when there is no user logged in, provides links to the home, sign up and login pages. There is a glasses icon that also redirects homeward. Upon a user logging in and being recognised, the Navbar offers different options which are redirecting the known user back to their profile back, the all reviews page or having the option to log out. 

* Buttons: Using Bootstrap, I aimed to have clearly labelled buttons to help users make choices, navigate the site like add, delete, edit, confirm, return, logout, close etc. The Buttons facilitate the CRUD options. 

* Icons and Links: I made use of some Font Awesome icons, such as the info icon to help guide Users. Another example would be the Amazon icon, which Users can click on and can direct them to the Amazon page of the book they have selected (where possible).

* Forms: using a mix of standard HTML forms and Flask-WTF to test out both methods. 

* Pagination: was utilised on the All Reviews section to facilitate site scalability of the site and also on the User Comments Forum


* A footer with a link to my Github page and my name/copyright logo.


### **Features Left to Implement**

I found this milestone project to be particularly interesting in terms of the learning curve, because as I moved forward with it, I discovered new python libraries and many different features and functionalities that I could have implemented and utilised. 

In fact, I found it difficult trying to balance learning about new features and trying not to use them all. It was very enjoyable discovering all the possibilities but also, it became an exercise of discipline in terms of using just what was needed. 

Sometimes less is more. However, in the future I plan on adding a lot more functional features to this site. These include:

-	An intuitive search bar to allow for whole site searching. 
-	A more robust sign in/login process, including, for example, reCaptcha functionality.
-	A password and username reset option.
-	The possiblity to delete, edit and up date user profile details. 
-	A more expansive user profile in general including dates of signing in, dates and the amount/times/dates of comments, if it was edited, personalised avatars (among a myriad of other things). 
-	Using more of the Flask libraries (lots were tested and not used) including Flask-Login.
-	Like/Dislike buttons for comments and books in the form of Thumbs Up/Down. I could also encorporate a simple counter on this to add the community feel of the site (e.g. 300 likes/24 dislikes).
-	Have the number of stars for the rating symbols displaying (with regard to the rating i.e. 3/5 means 3 seperate stars physically appearing). 
-	Allow for more user interaction amongst Users, for example with messaging each other or having a live chat forum. 
-	As mentioned in the **Add a Book Review page ** section above, the [Amazon Associate]( https://affiliate-program.amazon.com/) program would the next logical and professional step one could make so that the site could potentially be monetised. By simply adding the Amazon affiliate links, providing a simple platform so that the Users can easily click on their chosen affiliate links and potentially purchase the item directly via those links,  the siteowners could earn a referral fee. So it’s certainly another longer term consideration.


## **Technologies Used**

The following technologies were used on this project:

##### **Languages**

- [Python 3.7.5]( https://www.python.org/) - Python is an object-orientated high-level programming language. 


- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - is the renowned programming scripting language and the main libraries are JS. 

- [CSS3](https://developer.mozilla.org/en-US/docs/Archive/CSS3) - is used as the stylesheet language for styling and rendering.

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - is used as the standard markup language. 
    
##### Frameworks

- [Flask](https://flask.palletsprojects.com/en/1.1.x/) is a micro web framework written in Python. It is  used by constructing route decorators for the main functionality of the app. By using the Jinja templating functionality, Flask/Python is rendering on html pages. Flask libraries such as Flask-PyMongo were used to build the functionality of the site.

- [Bootstrap 4.3.1](https://getbootstrap.com/docs/4.3/getting-started/introduction/) - is a CSS framework that aids the grid and the layout and also the modal popup in this project

##### Database 

- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) – is a non-SQL, cloud database used to store, manage, update and delete datasets provided in collections.

##### Libraries


-  [JQuery version 3.2.1](https://jquery.com) - JS library to simplify HTML DOM manipulation and used also to initialise JavaScript elements. 
-  [Google Fonts](https://fonts.google.com/) library style **Montserrat** was used on this site.

###### Other Technologies

To generate the wireframes I used the site [Figma](https://www.figma.com/)
To generate the Placeholder images I used the site [Placeholder](https://placeholder.com/)


# **Testing**


### **Validation** 

I used a variety of tools provided by specified sites to test my code and the apps functionality:


#### Python
As Python was the main language I used , I tested often and also learned to utilise in-code testing to resolve errors, particularly the  ‘import pdb;pdb.set_trace()’ which is added above the erroneous code and you can evaluate the error in the terminal (thanks to my mentor Marantha for introducing this to me). 

For my Python code I passed it through the [PEP8online]( http://pep8online.com/). The first time I used the [PEP8online]( http://pep8online.com/) I believe between around 90% errors were either `trailing whitespace` , `	too many leading '#' for block comment` or `indentation contains tabs`, which I attempted to recify progressively. The main focus here was always ensuring the code was clean, concise and functioning. 

#### JavaScript

I used [JSHint](https://jshint.com/) to validate the little amount of JavaScript code I used.

There were 3 warnings, which were all **Missing semicolon**


#### HTML

For the HTML I passed my code through the [W3C Markup Validation Service](https://validator.w3.org/).

When I passed my HTML pages through this validator, there were some interesting results. I went about rectifying as much as resolved errors and warnings as possible but there were some curious results. For example, the first time I passed my `index.html` into the validation tool, I have **1 warning** and **10 errors**. However, oddly enough some of the errors didn't seem to pick up the Jinja templating and one error in particular for my `{% with messages = get_flashed_messages() %}` section, it said that the error was that **the font element is obsolete**. However, this was inline html code that I utilise as a time saving option (due to the aforementioned time constraints) and its function very much necessary (to test, I changed the size of the font and as expected, the size of the `flashed_messages()` altered). 

Despite these anomalies, I generally found it to be a very useful tool and helpful for clarifying and understanding my code better.

#### CSS
For my CSS3 code, I passed it through the [W3C CSS Validation Service - Jigsaw](https://jigsaw.w3.org/css-validator/)

**Congratulations! No Error Found** was the response the validator gave the first time I passed my CSS code in.



### **Tests** 

As I progressed day to day I mainly used Google Chrome Devtools to test/debug. I also tested the pages and functionality on Firefox, Safari and Microsoft Edge. I enlisted the help of friends to simulate user experience testing on tablets (ipad) and a variety of phones (iphone 5, iphone6, Google Pixel 3, Samsung Galaxy). 

###### Referring to Orginal User Stories

To guide the testing approach, I took the orginal User Stories into consideration. So I tested to evaluate if I had managed to achieve a semblance of coherence and continuity to the site from from the Users perspective. I also referred to the User Stories that I had originally created to help me focus on the site goals; for site responsiveness and functionality. 

On every page I test the navbar (hamburger icon positioning), the buttons (to seen if the python code/functionality was operating correctly), if the correct details were registering on the Mongo Database, observing the varying Desktop and Mobile viewports (on different browsers), ensuring that the dropdown menu was the same on the varying screens (among many other checks).

Another huge focus was evaluting if the error messages were correctly shown to the User. For example, from the following User Stories - attempting to sign up but having a Username that is already taken in the Database. The following sections are a step by step testing guide to evaluate the site functionality from the Users perspective, depending on what the User is attempting to achieve onsite:


1.	**New User arrives on Landing Page:**
i.	Click on Sign Up Button - redirected correctly to Sign Up Page & Form:
ii.	Fill in form with Username I know is already in Database.
iii. Submit form and result is Error Message : {form['username']} already exists!"
iv. Submits new form, with new Username but after entering a password in, then the prospective Users enters a different password into the 'Confirm Password' section.
v. Then upon clicking on submit form and the result is an Error Message that is returned, stating correctly that the: "Passwords dont match!"
vi. Thereafter, I proceed to submit a fully valid Sign Up form ( i.e. a new Username, an email address with an @ followed by a part (such as '@hotmail.com') and 2 matching passwords. 
vii. Upon clicking the Submit button, the new User arrives on the User Bio/Profile page, which displays a Weclome {% username %} message to confirm they are logged in, as well as new options on the Navbar and new Buttons available on the Jumbotron.


2.	**Returning User arrives on Landing Page:**
i.	Clicks on Login Button - redirected correctly to Login Page & Form:
ii.	The User fills in the form with an incorrect or unknown Username with any chosen password
iii. Enters the submit button and the prospective User is correctly redirected to the Sign Up Page, with the following, explanatory Error Message: 'Oops . . It looks like you gotta sign up !""
iv. If the User has already got a Profile but has simply made an error, they can click the link that returns them on Login Page.
v. The User then proceeds enter the correct Username but then enters the wrong password, clicking submit afterwards.
vi. Then, upon submitting the Login form, the result is a correctly displaying the Error Message : "Password Is Incorrect!".
vii. Finally, once the User has correctly typed in the right Username and Password combo. And then resubmit a fully valid Login form, the User returns to their Bio/Profile Page, with the Weclome {% username %} message to confirm they are logged in.

3.	**Logged User, from Bio/Profile Page Wants to Add a Book Review:**
i.	Clicks on Add Review - redirected correctly to Add a Review Page & Form:
ii.	The User fills in the form, all of the maxlength form functions are implemented preventing the User from going overboard and keeping the content succint: 
    - **Book Title**: has maxlength of of 50 characters
    - **Author**: has maxlength of of 35 characters
    - **Category**: has maxlength of of 35 characters
    - **Summary**: has maxlength of of 350 characters 
iii. Then the User can either add an Book Cover Image link,  leave this section blank or type anything into the textarea, with the result being:
    - If the image address is correct, the book cover image will display above the review in the correct size:
    - Anything else will illict the Placeholder image to take the place of the Book Cover Image
iv. If the User has already got a Profile but has simply made an error, they can click the link that returns them on Login Page.
v. The User then proceeds enter the correct Username but then enters the wrong password, clicking submit afterwards.
vi. Then, upon submitting the Login form, the result is a correctly displaying the Error Message : "Password Is Incorrect!".
vii. Finally, once the User has correctly typed in the right Username and Password combo. And then resubmit a fully valid Login form, the User returns to their Bio/Profile Page, with the Weclome {% username %} message to confirm they are logged in.

3.	**As Logged In User/Admin and Non-Signed-Up/Logged to test the clear error messages/prompts:**
i. straightforward testing, once I was either; (1) signed in as User (e.g. John) (2) Not signed in at all (3) Logged in as the Admin, I set about typing into the URL the different routes (e.g. `/all_reviews` (route decorator on the app.py) when not Logged in at all) or (`/admin` when the User was Logged in but not as the Admin) .Underneath is an example of some of the results of testing. 
    
    1. **Logged In as a standard User (e.g. John)**
        - Logs In as per usual with predefined Log In Details.
        - Arrives on Bio/Profile page.
        - Then types `/admin` at the end of the URL and presses enter.
        - As expected, I am met with a message stating 'Restricted Area - Access Denied!' and I have been redirected back to the Home Landing Page. 
        - The User can then proceed to Log Back in and attempt to access other routes. 
    
    2. **Logged In as a Admin (e.g. John)**
        - Using Admin credentials to Log In (Username: **admin** + Password: **admin99** )
        - Arrive on Admin.html (admin landing page)
        - Ensuring the different options on the Navbar options are rendering (such as the Admin landing page, the Internal Admin Notes section as well as the other pages available to all Logged In Users)
        - The Admin has no restrictions so no error messages redirect the Admin back to the Landing Page with a Modal Pop-Up Error message)
        
    3. **Not Logged in but on the Home Landing Page**
        - Using no credentials and not Logging In 
        - Arrive on Index.html (home landing page)
        - Ensuring the different options on the Navbar options are rendering (Login Page, Sign Up Page and back to the Home Page)
        - Then typeing either `/admin` or `/all_reviews` at the end of the URL and presses enter.
        - As expected, I am met with a message stating 'Restricted Area - Access Denied!' and I have been redirected back to the Home Landing Page. 
        - The Non Logged In site User can then proceed to the Login or Sign Up page. 


These were some (not all) of the tests conducted to observe the site functionality and if the User Stories could persist. The follow section discusses some of the many issues and bugs I encountered on my coding journey.

### Interesting Bugs & Issues:  

- The book cover images sized to `28rem` as it was the size most suited to each screen I tested, but I had some trouble implementing it as it kept returning some funky images. However, if no book cover image was chosen, the Placeholder Image kept returning a much stretched grainy/blurry placeholder. The Placeholder image isn't so clear but I due to time constraints it's something I will return to rectify. 

- Another sizing issue I had come with the background image. I resolved it with a cover container on chosen templates and respective sizing on the CSS stylesheet. However, I found that the issue stemmed from AWS Cloud 9's slow CSS preview rendering, making the development process difficult as I would make some tests/previews using Google Chrome Devtools and then implement the adapt CSS on the stylesheet but sometimes the change wouldn't appear for 30/45 minutes (post Git and Heroku push). Sometimes clearing the cache or deleting cookies helped but overall this part of the process was particularly frustrating and it's a consideration for choosing future IDE's.  
 
- Route decorators, jinja templating and werkzeug errors were numerous at the beginning, as with any learning curved but I learned (thanks to my mentor Marantha) how to debug inline using the [PDB Python debugger](https://docs.python.org/3/library/pdb.html). I used it particular with the signing/login fuction. 


## **Deployment**


### Github 

#####  *This site is deployed on [Github](https://github.com/NeiloErnesto89/Data_Centric_Dev_Milestone_Project3)

This project was built and tested on the [AWS Cloud 9 IDE.](https://aws.amazon.com/cloud9/) 


This site is hosted using GitHub. My code was directly deployed from the master branch. I added, committed and pushed my updates via the terminal as often as possible. I then deployed the site automatically upon receiving the new commits to the master branch/source. The following commands were used for Github deployment:


- The `$ git init` command was utilised to initialise my local repo. 
- Then then `$ git remote add origin https://github.com/NeiloErnesto89/Data_Centric_Dev_Milestone_Project3.git` command was used to add the new remote repository.  
- Afterward I used the `git push -u origin master` command to push my code to the master branch of the Github remote repo.
- Thereafter I used the follwoing commands: `$ git add .` (to add all) or `$ git add 'filename'` (to add just a specific file) and the `$ git commit -m "initial commit"` (followed by any relevant comment with the commit) to add and commit files. 
- Then, I would use the `$ git push -u origin master` command to push my updated code to the remote Github repository.
   


### Heroku

#####  *This site is deployed on [Heroku](https://datacentric-milestone-bookrev.herokuapp.com/)

My project has also been deployed via the master branch and hosted on Heroku. Heroku is a cloud platform that allows for building, developing and operating applications on the cloud [Heroku](https://dashboard.heroku.com/apps) in a range of programming languages. Python was the mainly used for this project.

The following process was undertaken to succesfully deploy the project on the Heroku:

- A very straightforward beginning by simply creating my application (named: datacentric-milestone-bookrev) on my Heroku profile. 
- I then had to configure some of the settings. In the *settings* area, I set the `IP: 0.0.0.0` and `PORT: 5000` in the *reveal config vars* section. This is mirrored on my app.py.
- After creating my env.py file (along with the .gitignore file), I added the `MONGO URI` and `SECRET KEY` in to the *reveal config vars* area.
- I installed Heroku via my command line interface, using `sudo snap install --classic heroku` on my AWS C9 terminal. 
- Afterwards, and from there on in, I would simply type `heroku login`, which would redirect me to another tab where I would sign in to heroku as proceed once more in the terminal.
- The next step was to initialise a git repo and add my Heroku remote repo command: `$ heroku git:remote -a 'datacentric-milestone-bookrev' `. 
- However, as per the requirements, before I can `push` my code to the Heroku app, I need to install 2 important files:
    - A **requirements.txt** file is needed to run the installed dependencies, so to create and commit this file, the following command was used: `$ sudo pip3 freeze --local > requirements.txt` (and also used to update the file if any libraries were added).
    - A **Procfile** is needed to direct the Heroku app to the file that it needs to run. So I used the command `$ echo web: python > Procfile` in the terminal to install the file. This was followed by a simple command in the terminal to run the web process: `$ heroku ps:scale web=1`.
- Finally, to deploy I would use the `$ git push heroku master` to deploy my code on the Heroku app.

After any big changes, advancements on my code, I would push my code to the Heroku app to check if it was functioning. There were some slight issues with the `MONGO URI` and `SECRET KEY` but it was resolved quickly. 


# **Credits**

## **Credits/Content**

- *The Code Insitute* documents and modules were a great source of help. 
- The Pagination code (plus the explanation) was taken and modifed from 'ShaneMuir_Alumni' via a Slack Thread and further from his [cookbook project](https://github.com/ShaneMuir/Cookbook-Recipe-Manager). 
- I read extensively this [Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by Miguel Grinberg. (It's just a shame I discovered it quite late in the day). 
- The `# Book Image/Pic Link Function` and `# Amazon Link Rendering Function` code were both derived, taken and adapted from fellow coding student [JBroks' MS3 project](https://github.com/JBroks/booksy-reviews). Overall, this was excellent project and a great source of inspiration (and something to strive towards) for fellow coding students!
- This unbelievable blog post by [Hackers and Slackers](https://hackersandslackers.com/flask-routes/) was a massive source of clarity and explanation for a huge amount of my code.
- The Werkzeug password hashing function was derived from this very helpful video by [Pretty Printed](https://www.youtube.com/watch?v=jJ4awOToB6k&list=PLgNY7mXdwZG8XgloGmy6PHtLFUA3Qctub&index=93&t=0s)
- Further Pymongo explanations about PyMongo were uncovered via [Tech with Tim](https://www.youtube.com/watch?v=rE_bJl2GAY8&list=PLgNY7mXdwZG8XgloGmy6PHtLFUA3Qctub&index=88&t=331s)
- A lot of [Corey Schafer videos](https://www.youtube.com/user/schafer5) as just general information and explanations on a huge array of topics. 
- Used on many occasions, one example being with a CSRF token on with regards to Flask wtf forms and the Jinja/ templates: [StackOverflow](https://stackoverflow.com/questions/39260241/flask-wtf-csrf-token-missing/39262931). 
- For the wtf forms I looked at this [video](https://www.youtube.com/watch?v=8aTnmsDMldY), read this [article](https://hackersandslackers.com/flask-wtforms-forms/) and the [installation guide](https://flask-wtf.readthedocs.io/en/stable/install.html)
- [W3 Schools](https://www.w3schools.com/) as always provided some very good explanations such as with the paginate buttons section

All book reviews were personally written by me (or by my friends/family for tests) but information and summaries were extracted from [Amazon](https://www.amazon.com/books-used-books-textbooks/b?ie=UTF8&node=283155), [Wikipedia](https://www.wikipedia.org/)
and [Google Books](https://books.google.ie/bkshp?hl=en&tab=pp&authuser=0). I also extracted the book cover images from these sites (mentioned below). 

Further explanations which helped out were:
- [CRUD](https://en.wikipedia.org/wiki/Persistence_(computer_science)
- [Scalability](https://www.koombea.com/blog/why-scalability-matters-for-your-app/)
- Using this blog to help explain the  [session.clear()](https://www.codepoc.io/blog/asp-net/5138/what-is-the-difference-between-session-abandon-and-session-clear) function

#### **Media**

All the links are to [Amazon](https://www.amazon.com/books-used-books-textbooks/b?ie=UTF8&node=283155), however I have no affliation to Amazon,. The links to the Amazon website was merely a functionality of the site and no user is under any obligation whatsoever to purchase from their site. In fact, I would very much encourage people to go to their local library or book shop instead :) .

- [Book Case Image](https://www.vectorstock.com/royalty-free-vector/library-book-shelf-literature-books-cartoon-vector-21597741) was taken from this site. 

- I own/created all other images (1) **libs.jpg** - photo (2) **database_schema.jpg* - screenshots from Mongo DB + Paint (can't beat it!))


[Figma](https://www.figma.com/) was used to create the Mock-Ups/Wireframes.

I  extracted the book cover images and no image placeholder from these sites: 
- [Amazon](https://www.amazon.com/books-used-books-textbooks/b?ie=UTF8&node=283155), 
- [Wikipedia](https://www.wikipedia.org/)
- [Google Books](https://books.google.ie/bkshp?hl=en&tab=pp&authuser=0). 
- [Placeholder]("https://via.placeholder.com/468x60?text=No+Image+Available+on+Bukish")



#### **Acknowledgements**

A huge thank you to mentor Maranatha Ilesanmi. A great guy, always calm, concise and helped me out lots.

Thanks to Code Insitute Support team (a great bunch), my fellow students/alumni (via Slack), to my family and my girlfriend for everything :)