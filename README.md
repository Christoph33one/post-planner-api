# Post Planner API

The Post Planner API provides a comprehensive back-end interface for storing, creating, and filtering travel-centric content for various locations. The API primarily focuses on two content types: profile pages and post pages.

The profile page enables users to create their unique profiles, select their favorite travel activities, upload a profile picture, and even pen a brief description of themselves.

On the other hand, the post page allows users to post diverse images of their recent trips, add location information, and write a short paragraph to share their travel experiences with others.

All registered users can search a location, view a travel plan and even comemnt on a travel plan to give updates to the location or any small ideas. 

---

# Project goal
The Post Planner API is a Django REST Framework API that powers the Post Planner website. It is designed to help users plan trips abroad by providing them with a unique perspective on various destinations. By browsing through photos and blogs from other travelers, users can gain insights into popular and off-the-beaten-path locations. For adventure enthusiasts, Post Planner offers inspiration to explore and experience new activities like cycling, hiking, and more. With Post Planner, planning a trip has never been easier or more exciting.

"Capturing the World: Exploring New Places and Moments Through the Lens"

---

# API
The API provides essential resources for managing user accounts, creating and commenting on content, as well as searching and filtering content by location. This allows front-end developers to implement the desired features in their application related to user-generated content and location-based searches

---

# Project structure
The project's general structure draws inspiration from the DRF-API walkthrough, which adheres to the best practices for implementing APIs in the industry. As a result, the serializer, model, and URL files are structured in a way that reflects the conventional approach to implementing APIs using the Django REST framework.


# List of contents
<ul>
<li><a herf="#data-models">Data models</a></li>
<li><a herf="#profiles">Profiles</a></li>
<li><a herf="#travel-plan">Travel plan</a></li>
<li><a herf="#comments">Comments</a></li>
<li><a herf="#search-filter">Search & filter</a><li>
<li><a herf="#user-stories">User stories</a></li>
<li><a herf="testing">Testing</a></li>
<li><a herf="#deployment">Deployment</a></li>
<li><a herf="#"></a></li>
</ul>

---

# Data models
The process of designing the database was closely aligned with the development of the API endpoints.  By using this approach, I was able to ensure that each data model was well-suited to support the functionality of the API and the needs of the end-users.

### Data base structure
![](assets/Screenshot%202023-05-06%20at%2017.46.45.png)


# Profiles
The Profile model allows users to create a personalized profile that is unique to them, using a one-to-one relationship. To create a profile, users must first register and then add the personal details of their choice. The Profile model is only visible to authenticated users through an admin panel. A Boolean field is included with a default value of False to ensure that a user's profile must be approved by the site administrator before it can be viewed. This measure is in place to ensure user and online safety by preventing the creation of malicious profiles.

To further enhance the user experience, an update function has been implemented that lets the users effortlessly update their profile image or content.

---

# Travel plan
The Travel Plan model offers authenticated users the ability to create multiple posts related to their profile, utilizing a one-to-many relationship. This model inherits the Activities list from the Profile model, allowing users to add relevant activities to their travel plans. Additionally, six image fields are included to allow a user the ability to post six images per post, with image size, width, and height regulations in place.

With the Travel Plan model, users can add a title, write a description, specify a location, and upload images to document their travel experiences for a specific location. Users also have the option to update or delete their posts as needed.

To ensure online safety, users cannot access and edit or delete another individual's post. All posts are subject to regulation through an admin panel and must be approved before the user or other users can view them.

To further enhance the user experience with a travel post, an update and delete function has been implemented that lets the users effortlessly update a post or to delete a post when needed.

---
# Comments
With the Comments model, authenticated users can conveniently leave feedback on fellow users' travel plans. This model leverages a one-to-many relationship, connecting comments to the relevant travel plan through a foreign key. It also provides users with a content field to enter their comments, as well as created-at and updated-at timestamps. To ensure online safety, I have included an "approved" boolean field, allowing the site administrator to review and approve comments that adhere to the site's guidelines.

---

# Search & filter 
In order to enhance the user experience and assist with location-based travel planning, I have incorporated a search bar feature. Users are able to easily search for a desired destination and access any relevant travel plans that have been created for that location.

---

# User stories
### Profile
- As a developer using the post planner API, I want to fetch a list of all the profiles created so that I can display them to the user interface.

- As a developer using the Post Planner API, I want to retrieve data from a user's profile so that I can display it to the user. This includes information such as their profile image, favorite activities, when their profile was created, and a section where they can write a short description about themselves. By accessing this data through the API, I can present a more personalized experience to the user 

- As a developer using the post planner API, I want to view and approve a users profile in an admin panel before viewing as to protect all user from sensitive user data exposure. 

- As a developer using the post planner API, I want to create two API endpoints for modifying user profile data, one for editing user profiles and another for deleting user profiles. This will provide users with the ability to update or remove their profile information through the API, improving the user experience and making the API more user-friendly.

--- 

### Travel plan
- As a developer using the post planner API, I want an endpoint to get all travel plans so that I do not have to manually query the database and then add them manually.

- As a developer using the post planner API, I want an endpoint to save a travel plan object to the database so that users and share their content.

- As a developer using the post planner API, I want an endpoint so users can manually edit their travel plan by updating their images or content or loacations, and that the developer dose not need to update the database.

- As a developer using the post planner API, I want an endpoint so users can delete any travel plans manually, so that a developer does not need to update the database.

- As a developer using the post planner API, I want to restrict users from editing or deleting a travel plan that they did not create, ensuring that only the original creators have control over their content.

---

### Comments
- As a developer using the post planner API, I want an endpoint to get all comments added so that I do not have to manually query the database and then add them manually.

-  As a developer using the post planner API, I want a url endpoint to retreieve a comment by users ID.

-  As a developer using the post planner API, I want to be able ot add a comment to a post I do not own.

- As a developer using the post planner API, I want a user to be able to edut and delete a comment they added.

- As a developer using the post planner API, I want only authenticated / logged in users to add comments. This ensures online safety.

- As a developer using the post planner API, I want the site administrator to have control over if the commetn can be added to a post. This also enusures site safety and harmful content being added.

---

# Testing

### Automated tests
I have used Django's API Test Case to perform all automated tests. I have thoroughly tested all three models to ensure that all user and API functions are working as expected. Additionally, I have verified that each URL endpoint corresponds to the correct function.

- A logged-in user can create a post with the correct user ID. Additionally, three fields from the travelplan model were tested within the response, as these fields have an attribute of blank set to false. This return a status.HTTP_201_CREATED

- An unauthorized user attempting to create a post will receive a status.HTTP_403_FORBIDDEN error, indicating that they do not have the necessary permissions. This is also tested as part of the overall verification process.

### Profile

- Test a profile is created with an authenicated user only and can be viewed withe url endpoint of /profiles/ also status.HTTP_200_OK displayed from the api.

- Test a profile can be retieved using a matching user ID WHY IS THIS TEST PASSING ON A 403    ???????????????????????????????

- Test a unauthorised user can not log into a profile they do not own and return a status HTTP_403_FORBIDDEN displayed from the api.

- Test a authenticated user can log into thier profile and a url endpoint of /profiles/1 to give the users ID. Also a status.HTTP_200_OK displayed from the api.

- Test a logged in user can update their with the url endpoint of /profiles/1/ and the api returns a status.HTTP_200_OK

- Test an unauthorised user can not update a profile they do not own and the api returns a status HTTP_403_FORBIDDEN

- Test a user can delete their profile on the request and the api returns a status.HTTP_204_NO_CONTENT after deletion

- Test an unauthorised user can not delete a profile they do not won and the pai returns a status HTTP_403_FORBIDDEN


### Travel plan post detail

- Tested that all traveplans can be viewed as a list in the api /travelplanposts/

- Tested whether a travel plan can be retrieved using the URL /travelplanposts/?owner__profile=3 and the correct user ID. Additionally, verified that the response returns a status.HTTP_200_OK error, indicating that the operation was successful.

- Tested the scenario where an incorrect URL is used to retrieve a post (e.g., /posts/999). As this post count does not exist, the response should return a status.HTTP_404_NOT_FOUND error, indicating that the requested resource could not be found.

- As part of our testing process, I verified that a user is able to update their own posts. To do so, I used the user's ID and a filter method to identify the correct post ID, and updated the post with a new title. I also verified that the response returns a status.HTTP_200_OK error, indicating that the update was successful. This helps ensure that users are able to modify their own posts as needed

- As part of the testing process, I verified that a user is not able to update another user's post. To do so, I added a logged-in user ID to the response of a different post ID, and verified that the expected result is a status.HTTP_403_FORBIDDEN error. This helps ensure that authenticated users cannot edit posts that do not belong to them.

- As part of the testing process, I verified that a user is able to delete their post. To do so I added a filter method to indentify the owner is the onwer of that post with the correct user ID. Once a post had been delete the api is to return a status.HTTP_204_NO_CONTENT. YOU NEED TO WRITE THIS TEST !!!!!!!!! ????????

- As part of the testing process, I wanted a unauthorised user to not be able to delete a post they do not own. To verify the result the api is to return a status.HTTP_403_FORBIDDEN error.  This helps ensure that authenticated users cannot delete posts that do not belong to them. NEED TO WRITE THIS TEST !!!!!!!! ???????????

---

### Comments test

- Tested the all comments can be viewed in a list within the api and using the correct url endpoint of /travelplanposts/ and that the api returns a status of Http_200_OK.

- To ensure the proper functioning of the filtering method, I tested the endpoint URL "/travelplanposts/?owner__profile=3" to retrieve all the travel plans that correspond to the user ID number.

- As part of the testing process, I wanted to test an logged our user can not adda comment. I tested see the api retunr a status.HTTP_403_FORBIDDEN and that no comments are able to post.

- As part of the testing process, I have tested that a logged in user can add a comment with the url endpoint of /comments/?post=3 and view a comment form and post option within the api. Also forthe api to return a status status.HTTP_201_CREATED to confirm the comment is added.

- Tested to see that a incorrect user ID and a unrelated comment do not match. Also for the api to show a status of status.HTTP_404_NOT_FOUND.

- Tested to see if a comment added with certain user can be retreieved with the users ID and for the pai to return a status of status.HTTP_200_OK.

- As part of the testing process, I wanted to test the a logged in uer can not update their comment if not logged in. The api to return a status of status.HTTP_200_OK.

- As part of the testing process, I wanted to see if a test would not allow for a user to update another owners comment. In this case the api should return a status.HTTP_403_FORBIDDEN.

- As part of the testing process, I aimed to test whether a user can delete their comment. Using the endpoint URL "/comment/1/", I retrieved the user's comment and then issued a DELETE request to the API to check whether the response would return a status of status.HTTP_204_NO_CONTENT.

- As part of the testing process, I sought to verify that an unauthorized user cannot delete a comment they don't own. To do so, I used a different username and a non-matching endpoint URL ("/comment/1/"), retrieved a user's comment, and then issued a DELETE request to the API. This was done to check whether the response would return a status of status.HTTP_403_FORBIDDEN.


### Coverage test report
By installing coverage and running a coverage test, I was able to generate a detailed report of all the code that was tested through the automated testing process. The report is presented in an HTML format that enhances its readability and can be used for documentation purposes.

![](assets/coverage%20test%20report%20API.png)

---

### Manual testing

To provide a comprehensive overview of the application's performance, I have personally tested all the functions for storing, viewing, retrieving, updating, and deleting data.

1. To verify the functionality of the profile model and the user profile creation process, I utilized the populated form from the API and provided the necessary information along with a user image. Afterwards, I accessed the user's profile through the URL endpoint '/profiles/1', which returned an array containing all the added data as well as the image link to be viewed.

2. I implemented a new URL endpoint on /profiles/ with the expectation of being able to view a complete list of all profiles in the system through the API, and receive a status code of HTTP_200_OK. When I accessed this endpoint, I was able to successfully retrieve a list of all profiles that had been created, along with their associated data.

3. To ensure that invalid profile IDs cannot be retrieved, I added a URL endpoint to the profiles URL (/profiles/999/). Upon accessing this endpoint, I received the expected HTTP 404 Not Found status code, along with a message indicating that the profile was not found. This confirmed that the functionality was working correctly.

4. I accessed the URL endpoint /travelplanposts/ to retrieve a comprehensive list of all travel plans created. This endpoint allowed me to view an array of data and images stored in the TravelPlan data model. Additionally, the displayed data and time was posted in a well-formatted, easily readable format.


5. I accessed the URL endpoint /travelplanposts/ to retrieve a comprehensive list of all travel plans created. I verified that users who are not registered or logged in are not able to create a travel plan as the API does not show the form to create a travel plan.

6. 
To retrieve an individual travel plan, I utilized the URL endpoint /posts/3. This provided me access to the third travel plan created, including the user ID and all data associated with that plan. I also verified that even an unregistered or logged-out user can view the travel plan. As anticipated, the API returned a status of HTTP_200_OK.







---

# Deployment
Deployment
To deploy Django application follow link instructions
https://github.com/Code-Institute-Org/python-essentials-template
Creating an app in Django - please follow the link below with instructions to create an app

https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf
Repository using GitPod
Navigate to the repository page on GitHub
Click the "GitPod" button in the top right of the repository.
You will now be taken to an open workspace.
Now you can create your files within your work space. Remeber to add (.html) for example when creating an html file, as this lets GitPod know what script and code you will be using.
For documentation and saving your work, which should be done on a regular basis. Use the command:
git add .
git commit -m"YOUR MESSAGE HERE! PLEASE KEEP IT SHORT BUT BRIEF!"
git push ( saves your work with the commit message. Your work will now be pushed to your GitHub repository )
Setting up Django Project and Deploying to Heroku Please follow the cheat sheet links below and in the order provided.

https://docs.google.com/document/d/1P5CWvS5cYalkQOLeQiijpSViDPogtKM7ZGyqK-yehhQ/edit#

Deployment: Heroku app

Click "create a new app" in top right corner
Give your app a name and select the region closest to you. When you’re done, click “Create app” to confirm.
Create a database
Log in to ElephantSQL.com to access your dashboard
Click “Create New Instance”
Set up your plan

Give your plan a Name (this is commonly the name of the project)
Select the Tiny Turtle (Free) plan
You can leave the Tags field blank
Select “Select Region”
Then click “Review”
Return to the ElephantSQL dashboard and click on the database instance name for this project
In the URL section, click the copy icon to copy the database URL
That’s the database created
Process
In your project workspace, create a file called env.py. It’s a good idea to check that this file is included in the .gitignore file too. If you are using the Code Institute provided GitHub template, then the env.py file is already in the .gitignore file.

In your env.py file add the following line of code. import os

Next we need to set some environment variables. os.environ["DATABASE_URL"]=""

As this is a Django application it has a SECRET_KEY os.environ["SECRET_KEY"]="my_super^secret@key"

We don't want to share our secrets either, so this documentation shows you a made up key. Just replace my_super^secret@key with your key

### Make sure you save the file.

Modifying settings.py
Now you have created an env.py file in your file paths add the following: import os import dj_database_url if os.path.isfile('env.py'): import env

A little further down, remove the insecure secret key provided by Django and replace with: SECRET_KEY = os.environ.get('SECRET_KEY')

Now that is taken care of, we need to hook up your database. We are going to use the dj_database_url import Comment out the original DATABASES variable and add the code below, as shown.

DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL")) }

The code that has been commented out connects your Django application to the created db.sqlite3 database within your repo.

With those changes in place, make sure to save your file. Your application will now connect to your remote database hosted on ElephantSQL

Run the command - python manage.py migrate



