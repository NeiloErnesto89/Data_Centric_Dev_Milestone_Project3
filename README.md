# **Datacentric Milestone Project 3**

The following section details the data-centric project issued by Code Institute for completion of the milestone 3 project. The title of my project is **Bukish : The Online Book Review and Recommendation Site**

# **Bukish** 

**The Online Book Review Site**

Bukish is a simple, online book reviews forum. The aim of the site is to provide fertile ground for the book loving community to come together to rate and review literature. Users join up to engage with others and express their love (or hate!) for books they’ve read but also to discover new literature. 

Bukish allows users to store their personalised content, to delete and update reviews/comments and even be linked directly to Amazon to  facilitate an online purchase! The aim is to allow for a interactive, fun and personalized user experience.  

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

The value being that users of the site simply add their own data, with the advantage being, a user can avail of the collective information/data of the community. 

Therefore the site owner, who could well be a prodigious user/member of the community, provides the users with the site functionality. And in return, among other benefits, the site owner can avail of the acquired collective dataset.

The site was built with this in mind, along with the mandatory requirements, which were (the following list was taken, and shorten, from the CI project requirements section): 

* Data handling: Build a MongoDB-backed Flask project...
* Database structure: Put some effort into designing a database structure... 
* User functionality: (CRUD functionality)...
* Use of technologies: Use HTML and custom CSS for the website's front-end....
* Structure: Incorporate a main navigation menu and structured layout...
* Documentation: Write a README.md file...
* Version control: Use Git & GitHub for version control...
* Attribution: Maintain clear separation between code written by you and code from external sources...
* Deployment: Deploy the final version (Heroku)...
* Make sure to not include any passwords or secret keys in the project repository...


## **UX**

As specified in the project requirements, the aim of this project is to aid the users to manage and contribute to a common dataset. So naturally, a massive focus would be on the user experience and the ease with which users can navigate the site. 

Baring this in mind, the goal of this milestone project was to create a web application using Python, the Flask libraries (a Python framework), a NoSQL Document-Based Database (in my case; Mongo DB) to construct the functioning app, as well as incorporate the main tenets of the CRUD operations (Create, Read, Update and Delete). 

CRUD, which refers to [persistence storage](https://en.wikipedia.org/wiki/Persistence_(computer_science)) encompasses the following 4 main pillars:

*Create – add new, unique data to the database
*Read – Fetch data from the database
*Update – change and edit pre-existing database data
*Delete – completely remove data from database. 


My overarching aim was to create a simple, efficient and sleek user friendly site, using intuitive design, clear and concise text and enticing colours to guide users. The simple layout would facilitate a pleasant experience and hopefully entice users to add their own reviews and comments, this participating in building the websites database as well as the community. The target being **reciprocity**; the more users, the more comments and reviews, the more the database extends.

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


The following section contains the mockups/wireframes that I created prior to beginning coding. The aim is to determine a concrete look and style for the site as well as provisionally considering some of its functionality.

I used the site [Figma](https://www.figma.com/) to construct my simple wireframe/mockups. It was the first time I used this tool, which was very simple and straight forward.

#### Wireframe 1


![index.html](https://github.com/NeiloErnesto89/Data_Centric_Dev_Milestone_Project3/blob/master/images/index_mock.jpg "Index.html Wireframe ")

*Figure 1. Index.html*


**Wireframe 1**: was my very first mockup. I added a background photo of a library I visited in Lisbon to give it a crip look as well as adding more a thematic features. 


#### Wireframe 2


![mobile view index.html](https://github.com/NeiloErnesto89/Data_Centric_Dev_Milestone_Project3/blob/master/images/mobile_mock.jpg  "Mobile view index.html Wireframe ")

*Figure 2. Mobile view index.html*

**Wireframe 2**: Again was just a very simple visual rendering of my inital concept now just focusing on the mobile viewport and how everything would be placed for an optimum ux. 



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

As mentioned above, the collections within the database were interconnected via the ObjectId, as represented below:


![Database Schema](https://github.com/NeiloErnesto89/Data_Centric_Dev_Milestone_Project3/blob/master/images/database_schema.jpg "Database Schema")


As we can see from above, each Mongo DB collection is connected to the other 2 connects. Meaning the data is interdependant. Each collection contains it's own specific data but they are all connected via the ObjectId. The relationships can be stated as: users and book reviews, users and user comments, book reviews and user comments.


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
-	Have the number of stars for the rating symbols displaying (with regard to the rating i.e. 3/5 means 3 seperate stars physically appearing). 



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

As I progressed day to day I mainly used Google Chrome Devtools to test/debug. I also tested the pages and functionality on Firefox, Safari and Microsoft Edge. I enlisted the help of friends to simulate user experience testing on tablets (ipad) and a variety of phones (iphone 5, iphone6, Google Pixel 3, Samsung Galaxy). 

I refer to the user stories that I had originally created to help me focus on the site goal, mainly for site responsiveness and functionality. On every page I test the navbar (hamburger icon positioning), the buttons (to seen if the python code/functionality was operating correctly), if the correct details were registering on the Mongo Database, observing the varying Desktop and Mobile viewports, ensuring that the dropdown menu was the same on the varying screens (among many other checks).

Another huge focus was evaluting if the error messages were correctly shown to the user. For example, from the following user stories - attempting to sign up. 
1.	Contact form:
i.	Go to the "Contact Us" page
ii.	Try to submit the empty form        




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



**rectified bugs**

- book cover images sized to `28rem` as it was the size most suited to each screen I tested. 
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

All book reviews were personally written by me but information and summaries were extracted from [Amazon](https://www.amazon.com/books-used-books-textbooks/b?ie=UTF8&node=283155), [Wikipedia](https://www.wikipedia.org/)
and [Google Books](https://books.google.ie/bkshp?hl=en&tab=pp&authuser=0). I also extracted the book cover images from these sites. 


#### **Media**
I  extracted the book cover images and no image placeholder from these sites: 
- [Amazon](https://www.amazon.com/books-used-books-textbooks/b?ie=UTF8&node=283155), 
- [Wikipedia](https://www.wikipedia.org/)
- [Google Books](https://books.google.ie/bkshp?hl=en&tab=pp&authuser=0). 
- [Placeholder]("https://via.placeholder.com/468x60?text=No+Image+Available+on+Bukish")

#### **Acknowledgements**

A huge thank you to mentor Maranatha Ilesanmi. A great guy, always calm, concise and helped me out lots.  