 <h1 align = "center">Milestone 3 Project<h1> 

## Data Centric Development by Martin Johnson

Jargon Buster is a website designed and built by Martin Johnson using knowledge
learnt on the Code Institute Full Stack Developers Course Modules 1- 10 which include HTML, CSS, JavaScript
and Python

The purpose of the site is to provide users with explanations for commonly used jargons from the sporting world and understand
what these jargons mean. Site users will also have the option to add, edit and delete jargons that they have heard and used themselves.


![mock ups on various devices.](assets/readme_docs/mockup.png)

[View the live project here.](https://martinjohnson26.github.io/Milestone2-Project/) 

## User Experience (UX)

As a keen sports fan i frequently encountered sayings and jargons that i did not understand the meaning of. This inspired me to create a
website of these phrases for my personal reference and to invite other users to also add to the site in orderr to build up a glossary of
sporting jargons.


 - As a user, I want to be able to find sporting jargons and what they mean
 - As a user, i want to add my sporting jargons and descriptions
 - As a user, I want to edit my sporting jargons and descriptions
 
 - As site owner, I want to build a database of sporting jargons and descriptions
 - As site owner, I want to site users to register with the site and add there own sporting jargons and descriptions
 - As site owner, I want to have full control of the content of the database
 
 ## Wireframes

 Based on user requirements, I used [Balsamiq](https://balsamiq.com/) to create basic site layout templates for desktop,
 tablet and mobile devices. The design consists of 3 sections, a home page, a jargons section, and a 
 sports category section.

 Initial Home page design layouts are displayed below. [Full wireframes can be viewed here](static/readme_docs/wireframes/wireframes.pdf)

 ![Homepage wireframes](static/readme_docs/wireframes/screens.png) 

 The final design is significantly different from the original design.  The sporting category was replaced by an accordion style drop-down 
 which used an alphabetical index rather than individual sports

  ### Strategy

To create a simple and basic site for users to view a glossary of sporting jargons

  ### Scope

To allow users to add , edit and delete their own jargons

 ### Structure

The site is structured to ensure that all elements of the site are easily accessible via a navigation bar. Users are required
to log into the site to get add and edit access to the jargons

 ### Skelton

The initial design layout was created using [Balsamiq](https://balsamiq.com/). The designs are shown above in the
Wireframes section

### Surface

<!-- A team image with an opacity added to enable the text to be more visible is the landing page. -->
    
 ## Design and Website Features

-   ### Initial Design

    A minimalistic simple design was chosen to enable users to focus on their primary reason for visiting the site
    Images were initially chosen as backgrounds but it was later felt that this distracted the user and were subsequently
    removed. 

-   ### Colour scheme

    Shades of grey are the prominent colours for backgrounds on navbars, forms and backgrounds for the pages.
    A black font was initially used but it was felt that this was too harsh against the greys and a dark red
    was easier on the eye. A white text against the grey backgrounds was choosen for the dropdown accordion.
    A light grey background was used to enhance the overall feel to the site.

    * Fonts:#e62851
    * NavBar background:  #b42424
    * Accordion background: #616161
    * Accordion text: #ffffff
    * Body: #eaeae1

-   ### Typography

    Roboto was the chosen font for its clear and easily readable text and strong characters.
    Sans Serif has been selected as the fall back text should the main font fail to import correctly for any reason.

-   ### Site Features

    * Navigation: Permits the user to navigate to all sections of the site in a simply manner and return to the Home page
    from anywhere on the page by selecting the Home menu or by selecting the NavBar brand name.

    * Jargons: Displays an accordion style dropdown of sports sorted alphabetical. When clicked on sporting jargons are
     revealed. Depending on access levels users can edit and delete the jargons. Full details are in the [test log](static/readme_docs/test_log.pdf)

    * Add Jargon: Permits the user to add there own jargons.

    * Profile: Displays the users profile name

    * Social Media: Links to usual social media sites are included in the footer section.

    ### Future Implementations

    * Enhance the profile page to allow the user to provide more details about themselves and their interests.
    * Add a contact form to enable users to contact site owner.
     the stadiums. 

##  Technologies used

* [HTML](https://html.com/) - For the basic site code.
* [CSS](https://www.w3schools.com/css/) - For Styling.
* [Materialize](https://materializecss.com/) - For additional styling, responsiveness and layouts.
* [JQuery](https://jquery.com/) -  For the coding relating to the Materialize form templates used.
* [Python](https://www.python.org/) to run the application
* [GitHub](https://github.com/) -  For version control and committing to GitHub.
* [GitPod](https://www.gitpod.io/) - For the repository to store the pushed code.
* [Flask](https://flask.palletsprojects.com/)To create the framework
* [Jinja](https://jinja.palletsprojects.com/) As the templating language 
* [MongoDB](https://www.mongodb.com/) To host databases
* [Heroku](https://www.heroku.com/) To Host the project
* [FontAwesome](https://fontawesome.com) -  For icon images.
* [Google Fonts](https://fonts.google.com) - For the fonts. 

## Webpage and Code Testing

W3C Markup Validator, W3C CSS Validator, JSHint and PEP8 online Services were used to validate the code used and ensure
there were no syntax errors in the project. Webpages were individually tested to ensure they responded to the code as expected

### User story testing -  All test were manually conducted

 1. As a user, I want to be able to find sporting jargons and what they mean

    Users are presented with a simple navigation bar which directs them to the section containing jargons. This can also
    be accessed via a button on the Home Page
    Users are presented with an alphabetic index for sports where they click on and view jargons.
       
 2. As a user, i want to add my sporting jargons and descriptions

    Users are invited to join the site from the home page or can register via the NavBar. Once registered the user has
    the functionality to add their jargons via a form which has validation controls in place to ensure entries are completed
    correctly before being added to the site

 3.  As a user, I want to edit my sporting jargons and descriptions

     As a registered user, they can edit and/or delete ant jargon that they have created . Edits are performed by an
     edit form has validation controls in place to ensure entries are completed correctly before being updated on 
     the site.

    [Full testing Result](static/readme_docs/test_log.pdf)

## Bugs

There is an issue with the search box on the jargons page . The search is fuctional , however if a searched word
is found within the database, the search result is returned in each of the dropdown sections rather than the 
specific category the word belongs to. A decision was made to leave in the search function to demonstrate that 
the function worked but required further refinements to function as expected. Project submission deadlines
have meant that this has not been completed prior to submission.

## Deployment

### GitHub Pages

<!-- To deploy my site I used GitHub and the following steps:

1. Logged into my GitHub account.
1. Went to my repositories and selected my project.
1. Clicked the Settings icon.
1. Scrolled down the page to the 'GitHub Pages' section
1. I selected 'Master branch' in the dropdown
1. This deployed my project to the URL: https://martinjohnson26.github.io/Milestone2-Project/ -->

### Forking the repository

<!-- 1.  Log in to GitHub and locate the GitHub Repository
1.  At the top of the Repository above the "Settings" Button on the menu, locate the "Fork" Button.
1.  Click the button to create a copy of the original repository in your GitHub account. -->

### Make a local clone
<!-- 
1. Log in to GitHub and locate the GitHub Repository
1. Under the repository name, click "Clone or download".
1. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
1. Open Git Bash
1. Change the current working directory to the location where you want the cloned directory to be made.
1. Type git clone, and then paste the URL you copied in Step 3.
1. Press Enter. Your local clone will be created. -->

## Credits

**Content:** 
<!-- The core HTML, CSS and JS code has been written by myself. Templates taken from [Bootstrapbay](https://bootstrapbay.com/blog/14-days-bootstrap-4/)
were used for the NavBar and fixtures section and modified by myself to meet the needs of the site. The email.JS code was taken from the 
Code Institute Interactive Frontend Development module lessons. The core code for the Google Maps API was taken from following
a YouTube video by [Traversy Media](https://www.youtube.com/watch?v=Zxf1mnP5zcw&t=1445s) and modifying to meet site requirements.
Bootstrap 4 was used to assist with site responsivness and layout -->

**Media**  
 <!-- Icons were sourced from FontAwesome  (https://fontawesome.com)

 Images were sourced from Wikipediae (https://en.wikipedia.org)

 Fonts were sourced from Google Fonts (https://fonts.google.com/) -->

**Acknowledgements**

<!-- https://www.w3schools.com/bootstrap4/ For use of built in class definitions, examples and Try Me Code snippets

Slack community for support and advice during the construction of the site

Code Institute tutors for support and advice during the construction of the site

Code Institute coursework for reference

Traversy Media for YouTube videos related to Google Maps API's

Codecademy for additional tutorials relating to JavaScript

Oluwafemi Medale (CI Mentor) for help, support, advice and positive feedback from the initial inception of the site through to completion
 -->

