[![Build Status](https://travis-ci.com/Bumper0417/e-shop-MS-Project-4.svg?branch=master)](https://travis-ci.com/Bumper0417/e-shop-MS-Project-4)

# Happy Cooking Webpage

Milestone Project 4: Full Stack Frameworks with Django - Code Institute

My NBA E-Shop is an Full Stack webpage, which main purpose is to cover the needs of it's users with a variety of NBA apparel. There is a variety of functions that allow the user to register and be able to sign in in the webpage and receive information about each item before they are able to purchase it. Users also have the ability to prossed to payment and by adding their personal information and payment details receive their products in the location of their wish.

## UX

My main purpose when creating the webpage was to ensure that our products are available for all the genders and sizes in order to satisfy the needs of my customers.

### User Stories

- As a user of the webpage i want to be able to register and then log in with my personal data.
- As a user of the webpage i want to be able to specify my search by choosing the specific category i want to receive products from.
- As a user of the webpage I want to be able to view all the products that the owner of the webpage has provided by clicking a button in the navigation bar.
- As a user I want to specify my search criteria and be able to get results for products that fit my style and preferences.
- As a user of the webpage i want to be able to receive information about an item when clicking on it before i decide to buy it.
- As a user of the webpage i want to be able to select the specific size that fit for me before purchasing my product.
- As a user of the webpage i want to be able to be redirected to a payment page where i can add my payment and shipping info and be able to receive the product wherever i want.
- As a user of the webpage i want to be able to receive information about the owners of the webpage and the history behind it.
- As a user I want to access the webpage from all differend types of divices (MObile Phones, Desktops,Laptops, Tablets, etc.).

### Wireframes 

![Mobile-Version](media/wireframes/IMG_4888.jpg)
![Desktop-Version-NBA-Shop](media/wireframes/IMG_4884.jpg)
![Desktop-Version-Home-Page](media/wireframes/IMG_4885.jpg)
![Desktop-Version-Products-Page](media/wireframes/IMG_4886.jpg)
![Desktop-Version-Product-View](media/wireframes/IMG_4887.jpg)

## Features

- Happy Cooking is a webpage that allows the user to have an easy access and by clicking the "Happy Cooking" logo to always redirect to the home page.
- In the home page there are the recipes together with 3 buttons(View, Edit, Delete) where the user can manipulate the recipes.
- In the home page there are also 3 input fields together with a search button to be able to make the user specify the search by suitability(For Vegans or Vegeterians), country(Italy, Greece, Mexico, Thailand) and catecory(Appetisers, Starters, Main Courses, Desserts).
- There is also a navigation bar, created with [Materialise](https://materializecss.com/navbar.html) with 3 sections on the right top corner (Our Recipes, Add your Recipe, Categories):
1. By clicking "Our Recipes" logo it will always redirect you to the home page where all the recipes are stored.
2. By clicking "Add Your Recipe" logo it will redirect you to the page where you can add your recipe.
3. By clicking "Categories" logo it will redirect you to the page where all the categories are stored and there you can add, edit and delete a category.
- The webpage is also using a slide-out side-navigation bar in order to make it more easy to access by mobile phone [Materialise](https://materializecss.com/mobile.html).

## Features Left to be implemented

In the future i would like to add some links to social media and a registration form for new users.

## Technologies Used

### Front-End

- [HTML](https://en.wikipedia.org/wiki/HTML5) Used for storing all my pages.
- [CSS](https://no.wikipedia.org/wiki/Cascading_Style_Sheets) Used for the styling of my webpage.
- [Javascript](https://no.wikipedia.org/wiki/JavaScript) Used for initialising my buttons and some functions for my recipes.
- [Materialise](https://materializecss.com/) Used for styling of the webpage
- [Material-Icons]( https://material.io/resources/icons/?style=baseline) used for styling my input elements.
- [Jquery](https://en.wikipedia.org/wiki/JQuery) Used for manipulating the dom and add the elements to my project.

### Back-End

- [Flask 1.1.1](https://en.wikipedia.org/wiki/Flask_(web_framework)) A library used for the construction of the webpage
- [Python 3.6.8](https://en.wikipedia.org/wiki/Python_(programming_language)) This is the back-end programming language
- [MongoDB Atlas](https://en.wikipedia.org/wiki/MongoDB) To store all the data and collections of my webpage
- [PyMongo 3.8.0](https://api.mongodb.com/python/current/) MongoDB's API to interact with the data.
- [Jinja](https://en.wikipedia.org/wiki/Jinja_(template_engine)) Used for displaying elements from back-end to front0end.
- [Git](https://en.wikipedia.org/wiki/Git) Used for writting commands and inserting new documents in my webpage
- [Github](https://github.com/) Used to store my webpage for the users to have access to that and for my tutors and mentor to help me with my Milestone Project
- [Heroku](https://en.wikipedia.org/wiki/Heroku) Used for the deployment of my project.

## Testing

- For the potencial users of my webpage that want to be able to see the recipes by clicking a button I have created a view button from Materialise and is triggered in my view_recipe.html with jinja. 

**Add Recipe Functionality:**

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on Add recipe button without filling all the forms | Displays Validation to tell the user to enter all the forms | As Expected | Pass |
| Clicking Add Recipe button after filling all the forms | Redirect to the home page and the recipe is added | As expected | Pass |
| Click on View Button to the recipe that you added | All the information of the recipe display fine | As expected | Pass | 

**Edit Recipe Functionality:**

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on Edit recipe button without filling all the forms | Displays Validation to tell the user to enter all the forms | As Expected | Pass |
| Clicking Edit Recipe button after changing some of the forms | Redirect to the home page and the recipe is edited | As expected | Pass |
| Click on View Button to the recipe that you added | All the information of the recipe display fine | As expected | Pass | 

**Delete Recipe Functionality:**

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on Delete recipe button | Removes the recipe and redirects to the home page | As Expected | Pass |

**Categories CRUD Functionality:**

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on Add Category button without filling all the forms | Displays Validation to tell the user to enter all the forms | As Expected | Pass |
| Clicking Add Category button after filling all the forms | Redirect to the categories page and the category is added | As expected | Pass |
| Click on Edit Category button to a category and press the edit button without filling the forms | Displays Validation to tell the user to enter all the forms | As expected | Pass | 
| Clicking Edit Recipe button after changing some of the forms | Redirect to the categories page and the category is edited | As expected | Pass |
| Clicking Delete Category button | Removes the category and redirects to the categories page | As expected | Pass |

**Filter Functionality:**

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on filter button when choosing vegeterian in suitability | Displays all the recipes that fit for vegeterians | As Expected | Pass |
| Clicking on filter button when choosing vegan in suitability | Displays all the recipes that fit for vegans | As Expected | Pass || Click on Edit Category button to a category and press the edit button without filling the forms | Displays Validation to tell the user to enter all the forms | As expected | Pass | 
| Clicking on filter button when choosing Mexico in country | Displays all the recipes that originated form Mexico | As Expected | Pass |
| Clicking on filter button when choosing Thai in country | Displays all the recipes that originated from Thailand | As Expected | Pass |
| Clicking on filter button when choosing Greece in country | Displays all the recipes that originated from Greece | As Expected | Pass |
| Clicking on filter button when choosing Italy in country | Displays all the recipes that originated from Italy | As Expected | Pass |
| Clicking on filter button when choosing a specific Category in category | Displays all the recipes that refer to this specific category | As Expected | Pass |
| Clicking on filter button when applying multiple filters | Displays all the recipes that fit to the category,country of origin and suitability that are selected | As Expected | Pass |

**Styling of the Webpage:**

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Right click on the webpage and press inspect | The webpage displays fine in all types of devices  | As Expected | Pass |

- The Navigation Bar that the webpage is using is tested for all the types of devices and is working properly.

- The site is tested in a variety of devices such as:Iphones(4 to 10),Samsung Galaxy,Ipads and Desktops.In addition it's tested to all the possible browsers:Chrome, Safari, Internet Explorer, FireFox and i assure that it is compatible and responsive.

The biggest problem I faced when creating this website was how to identify and implement the search functionality, which at the end it was a very interesting feature.

## Deployment

My webpage is hosted in Github and deployed directly from the master branch. The whole project can be viewed here:

[Bumper-Milestone-Project-3](https://github.com/Bumper0417/Milestone-project-3-Python)

In addition my project is deployed in Heroku and the live link can be viewed here: 

[Happy-Cooking](https://happy-cooking-project-3.herokuapp.com/)

The website consists of:
1. A static folder with a css folder,which has a style.css file and a wireframes folder with 2 wireframe images. 
2. A templates folder with 9 html pages.
3. An app.py file where all the backend is stored.
4. A procfile for the deployment in Heroku.
5. A requirements.txt file
6. The README.md file of the webpage.

## Credits

### Content
The content in the whole project is written by me.

### Media 

All the wireframes of the webpage are created by me.

### Acknowledgements

I recieved inspiration from sites such as: 
- [W3schools](https://www.w3schools.com/)
- [Stackflow](https://stackoverflow.com/)
- [Youtube](https://www.youtube.com/watch?v=dTN8cBDEG_Q&feature=youtu.be)
- [MongoDB](https://docs.mongodb.com/manual/text-search/#example)
- [Github](https://github.com/Code-Institute-Submissions/COOK-BOOK-4)
- [Recipes](https://www.bbcgoodfood.com/)
