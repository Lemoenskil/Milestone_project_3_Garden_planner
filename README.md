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

- Edit Plant/Crops
page will be a form where you can update the date.  The table will be updated using a checkbox.  and there will be a sudmit button.

- Search result page
This page will sow the result of the search of the name crops or nots.

- Plant Calander
From the Navbar you can navigate here.  A talble will be on this page

- Delete warning page
This page will have a warning before you delete the record and sudmit button

- Register page
Page will have a form and a sudmit button

- login plage
Form with a warning and a sudmit button


##### Font
xxxx

##### Colour Scheme
xxxx

## Features

### Existing Features

- All pages feature a navigation bar at the top, see useful links, or login / logout. 
- Upon viewing the page  the navbar will give you the option to login/or out, go to plant calender, home , register or add plant
- On the landing page maximum of 6 cards will be displayed if you want to browse you can use the page navigation on the bottom.  You can also click on the card that will take you to the plant overview page.
- On the top of the landing page below the navbar you will find a jumbotron with a search bar, which will allow you to search on the name, crop group or notes.
 

- For each vegetable in the list the common name, genus, species and category are shown, and the username of the entry's creator, together with buttons to show a detailed view, and for registered users buttons to edit or delete the vegetable.   The delete option features a modal confirmation dialogue to mitigate the chances of an inadvertant deletion.

- For registered users there is also a well placed "Add Vegetable" link at the top of the list in addition to the one in the navbar.

- As well as information about the site, the "About" page displays live up-to-date statistics about the database and brief details regarding its development.

- The forms to add and edit vegetable entries have sensible defaults for which fields are required and which are not editable, and for exampe allow only alphabetic characters in common names, genera and species.

- When editing or adding a vegetable, the user has the option of uploading a photograph, which will be saved and displayed in the detailed view.

### Features Left to Implement

- Multiple photos for each vegetable.

- More fields, for properties like soil type, recommended acidity (pH value), time to sow (outside / inside), time to plant out, time to harvest, nutrient needs, tips and tricks, together with the ability to sort and filter by these fields.

- A blog page where expert gardeners can share their ideas about organic vegetable growing in West Cork.

- Proper, secure user registration and authorisation.

- Any features subsequently requested if thought to be useful and feasible.

- Augmented and improved content.

- Persistence of user-uploaded images (see the section "Interesting Bugs" below in this README.)

- As the site grows, with more entries, maybe I will create fields for planting time, harvest time, nutrient requirements, soil type etc..   This will depend on what users want and what feels appropriate and useful to me.

- The project is open-source so I am open tto pull requests.


## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

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