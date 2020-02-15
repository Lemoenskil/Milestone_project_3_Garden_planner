 # Garden planner

This web application has been designed and built for the requirements of the "Data Centric Development" project of the Code Institute Full-Stack Software Development course.  It is intended to be a personal planning tool for vegetable and fruit  gardeners in North Brabant, The Netherlands, where I live and have my own vegetable and Fruit garden, and I hope to continue to develop it going forward.

Offering this tool to the local hobby gardeners i hope the get the best input and tips to grow the perfect vegetable.  With the experience and  I hope to get the correct species for plant that if fit for my region and also the best planting methodes for a optimun ylied.

The project can be viewed [https://yvette-garden-planner.herokuapp.com/](https://yvette-garden-planner.herokuapp.com/)

## Specification / Design

Setting up  a database of vegetables that can be grown in North Brabant, which can be changed and new contributions can be made for local vegetable gardeners.

For each vegetable/ Fruit grown, the database will store its common names, crop group (leafy, fuit. root, bulb etc.), information (eg.  soil, feeding potsition ect.), notes, and photographs.   Calander will be availbe that will show time to sow indoors, time to sow outdoors, and time to harvest.

The user can logging to have access to the  all vegetables in the database, with buttons to view, edit or delete them.  Without logging in the user will have the fuctionality to browse or search in the database.    The calender will be showed in ganth chart format which will make it easier for planning porposes. 

Clicking "View" for a vegetable will cause a detailed view to be displayed. with a photograph.   User with accounts  will be able to upload photographs for a new entry, to add to an existing entry or replace an existing image.

User will be allowed to register just by logging in with a username.  Registered users will be automatically approved as editors and as such will have full CRUD permissions.   Unregistered users will not be able to update or delete records.
The vegetables will be stored as documents in a non-relational MongoDB database.   The app will be hosted with Heroku.
 
## UX
 
#### Build Data Centric Website for Garden planning

The Garden Planner website has the following requirements

Their primary target audiences are herb, vegetable and fruit gardeners or prospective gardeners
The website need to include the following 
- Database with plants 
- Ability to add new plant records 
- The ability to change existing records 
- The ability to delete records
- View a single records
- Search for plant records
- View the plant calender
- Browse the website with out signing in 
- Only user signed in can update, create and delete records

I need the following for the website
- logo
- Data Base for the plant records (source of information)
- Picture for the landing page

#### User stories
- As a user, I want to know more about the plants and when to grow them.
- As a user, I'd like to see clean, well presented website that is easy to navigate
- As a user, I'd like to see a variety different plants
- As a user, I’d like for the website to be made so that it will work and adapt to all manner of devices (responsive design) 
- As a user, I want to read on tips and the best way to gow the plant.
- As a user, I want add new plants to the database and have the ability to change or delete it when is have new tips.  
- As a user, I want to have a overview of the plant calender for the plant in my data base
- As a user, I'd like to see some text to explain what is can expect on the website (instructions) 
- As a user, I'd like to see engaging use of colour making the website pleasant to look at and keeping the user interested 
- As a user, I'd want to navigate easly and alway have the ability to return to the home page
- As a user, I want to login to be able to make changes in the database
- As a user, I want to browse through the availbe plant records

### Project Purpose

I am creating a website aimed towards helping current and prospective gardeners getting an overview of plants (vegetable and fruit) that was planted successfully in my region. 
The website will use MongoDB database, flask and CSS to give the data throught to the frontend.    
The infromation that is availbe for the plant will help you to plant it in the right manner which will include infromation on soil, pests, position, harvest and feeding.
When a registered user logon he/she will have the ability to change, add or delete the current records
A not registered user will be able to browse search and view the data on plants.  
Included is an overview of the plant calender where the user can have an quick overview when to plant what.   

### Scope of website
- A Responsive website that is conected with a unstructerd database
- A page to give an overview to browse, search the plants
- A form to change and create a plant records
- A page with a plant calender table
- Logon ability for a user

### Website Structure

### Mockups

In the links below you can see the mock-up’s that I drew using the mock-up tool “Balsamiq”:
![Desk top mockup](/static/images/mockup_garden_planner.jpg)
![Mobile mockup](/static/images/mockup_garden_planner_mobile.jpg)
- 
**Note that the final design has changed from the original design in the mock-ups. The reason why it has changed. I was trying different layouts while I was experimenting and learning the code and sometimes the new designs looked better than the original ones or was just more responsive. *
 
### Design Ideas

- Navbar and Footer
Standart on all the pages there will be a Navbar and footer.  The Navbar will navigate to Home, add Plant, Plant Calander and Registered

- The landing page 
Wil have a maximum of 6 cards displayed with a picture and a plant name. A Jumbothron with a search bar will be shown on top 

- Single plant view
Will have a picture, a plant table and the information on the plant.  A floating button will be availbe when you are loging to change or delete the record.

- Add Plant/Crops
page will be a form where you can create the date.  The table will be updated using a checkbox.  and there will be a sudmit button.

- Edit, Delete and view Plant/Crops
page will be a form where you can update the date (change or delete.  The table will be updated using a checkbox.  button for delete and change with a modal.

- Search result page
This page will sow the result of the search of the name crops or nots.

- Plant Calender
From the Navbar you can navigate here.  A talble will be on this page

- Register page
Page will have a form and a sudmit button

- login plage
Form with a warning and a sudmit button


##### Font
Google fount Roboto is used

##### Colour Scheme
Green Orange and White Scheme with a purple Jumbothron

## Features

### Existing Features

- All pages feature a navigation bar at the top, see useful links, or login / logout. 
- Upon viewing the page  the navbar will give you the option to login/or out, go to plant calender, home , register or add plant
- On the landing page maximum of 6 cards will be displayed if you want to browse you can use the page navigation on the bottom.  You can also click on the card that will take you to the plant overview page.
- On the top of the landing page below the navbar you will find a jumbotron with a search bar, which will allow you to search on the name, crop group or notes.
- On the view page there will be a floading button on which you can either delete or edit the records.  When editing it will redirect you to a form, when deleting it will redirect you to a modal
- From the navigation bar you can be directed to to the add record form
- Both add record and edit record form have a Table with checkbox to select the plant calender.
- The search bar in the Jumbothron will give you the option to search the data base and redirect you to a page with search results
- In the navbar you are redirected to the register page where you can create a user using a form.
- The option to loging is also on the landing page, which will redirect you to a form to loging
- In the responsive view for mobile ther are a side nav bar and the basic sizing
- The creation of an account to edit add and delete records.
- Option on the login screen to register. 

### Features Left to Implement

- Want to make different data object with set fields that you can choose from examle pest type, soil types.
- Want to make it more sosiable add a blog where user can discuss different topics regards to garding
- Proper, secure user registration and authorisation.
- Augmenting the styling and visual effect and improved content.
- I have lose properties like soil, position, pest that i can use later to put into dashbord to make the data more visual
- A option to create your own account select select your plants and get your own calender


## Technologies Used

- Python
- HTML5
- CSS / Bootstrap 4
- CSS / Materialize
- JS / JQuery
- Mongo
- Flask
- Heroku


## Testing

The app has been manually tested extensively throughout the development process, and when bugs have been found they where fixed or a workaround was implemented.

The plant_records page and is tested that they loads the data,the pagenation work, and the links are working correctly.

The registration page are tested, for mismatched passwords, duplicate user names, as well as successful registration that is show when the username is on the navbar.

The login page is tested as all senarios for delete, change and created operations required a logged in user. 

The add_plant page is tested by checking that a plant is entered on sudmit, the page redirects and the new plant is seen on the plant record page.

The plant_records page search functionality  is tested by searching for plant on the  page, getting its id number and going to that search_results page.  

The update_plant page is tested by going to a logged in users view_plant and then via the floating button edit to update_plant page and changing some data and committing it. This the redirects the user to teh plant_records page and check that the information has changed on that plant record. 
  
The delete functionality is tested by going via view_plant to delete where you get modal as a warning and deleting it, then checking the redirect has happened and that the plant does not appear on the the plant_records page.

The list plant page is teste by going via the navbar to the page and check that the data has loaded.

The logout functionality was tested via the navbar a loged in user can logout I have test that as then the name was not visable and the option to sign in was on the navbar and the footer.

As the site is built with a responsive design it works for mobiles it has been checked  on iPhones 6 to X, Samsung Galaxys, iPads (mini to pro), Google's Pixel 2 and 3.

It has been tested with  Chrome Dev Tools and on my Android phone. 

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X