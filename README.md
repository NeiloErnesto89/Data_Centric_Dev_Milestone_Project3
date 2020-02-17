# Datacentric Milestone Project 3

Online Book Review and Recommendation Forum - 'Bukish:The Online Book Review Site'

## Project Brief 

Data driven application using technolgies 


# Bukish – The Online Book Review Site

Bukish is a simple, online book reviews forum. The aim of the site is to provide fertile ground for the book loving community to come together to read, rate and review literature. Users join up to engage with others and express their love (or hate!) for books they’ve read and to discover new literature. 

Bukish allows users to store their personalised content, to delete and update reviews and comments they’ve made to allow for a personalized experience. 

It was essential also to create a scalable application, capable efficiently of handling growing numbers of users and their input. 

Essentially, this part is your sales pitch.

## UX

As specified in the project requirements, the purpose of this project is to “build a full-stack site that allows your users to manage a common dataset about a particular domain”.

The goal of this milestone project was to create a web application using Python, the Flask libraries (a Python framework), a NoSQL Document-Based Database (in my case; Mongo DB) to construct the functioning app as well as incorporate the main tenants of CRUD (Create, Read, Update and Delete). 

My aim was to create a simple, efficient and sleek user friendly site, using intuitive design and enticing colours to guide user. 

So with these focal points in mind, I tried to adjust the UX of this site for the following user type:


### User Stories

Typical, archetypal user would be interested in reading and writing reviews. They would also be willing members of an online community.

•	As a user, I would like to sign up so I can access reviews and comments. 
•	As a user, I would like to add my own personalized reviews and comments. 
•	As a user, I would like to add participate in an online community for a topic that I’m interested in. 
•	As a user, I would like to express and share my own views within a likeminded community. 
•	As a user, I would like to update and/or delete my reviews or my comments at any time and also not have any other user update and/or delete my content.

Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
•	As a user type, I want to perform an action, so that I can achieve a goal.
This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.


## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.

## Existing Features

In The following features are presented in a loose order of appearances on the app: 

•	A Modal pop feature that welcomes visitor, displays a random quote (for assigned list) and offers additional information to client. The modal also supplies different information when a user logouts (including a button to direct users to log back in)

•	A Navigation bar that, when there is no user logged in, provides links to the home, sign up and login pages. There is a glasses icon that also redirects homeward. Upon a user logging in and being recognised, the Navbar offers different options which are redirecting the known user back to their profile back, the all reviews page or having the option to log out. 


For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.
In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

## Features Left to Implement

I found this milestone project to be particularly interesting in terms of the learning curve because as I moved forward with it, I discovered new python libraries and many different features that I could have implemented and utilised. In fact, I found it difficult trying to balance learning about new features and trying not to use them all. It was very enjoyable discovering all the possibilities but also, it became an exercise of discipline in terms of using just what was needed. Sometimes less is more. However, in the future I plan on adding a lot more functional features to this site. These include:
-	An intuitive search bar 
-	A more robust sign in/login process including reCaptcha functionality 
-	A more expansive profile including dates of signing in, comments, avatars for the users etc. 
-	Using more of the flask libraries (lots were tested and not used) including Flask-Login, Flask  


## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.
•	JQuery
o	The project uses JQuery to simplify DOM manipulation.

## Testing

## Validation 
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

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).
In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
•	Different values for environment variables (Heroku Config Vars)?
•	Different configuration files?
•	Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.



# Credits


•	The text for section Y was copied from the Wikipedia article Z

## Content

* The Code Insitute 

Media
•	The photos used in this site were obtained from ...
Acknowledgements
•	I received inspiration for this project from X