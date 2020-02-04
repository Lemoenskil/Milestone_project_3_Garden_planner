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

xxxxx

#### User stories

xxxx

### Project Purpose

xxxxx

### Scope of website

xxxxx

### Website Structure

### Mockups

In the links below you can see the mock-up’s that I drew using the mock-up tool “Balsamiq”:
![Desk top mockup](/static/images/mockup_garden_planner.jpg)
![Mobile mockup](/static/images/mockup_garden_planner_mobile.jpg)
- 
**Note that the final design has changed from the original design in the mock-ups. The reason why it has changed. I was trying different layouts while I was experimenting and learning the code and sometimes the new designs looked better than the original ones or was just more responsive. *
 
### Design Ideas
xxx

##### Font
xxxx

##### Colour Scheme
xxxx

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

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