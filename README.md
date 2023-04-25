Post Planner API

The Post Planner API provides a comprehensive back-end interface for storing, creating, and filtering travel-centric content for various locations. The API primarily focuses on two content types: profile pages and post pages.

The profile page enables users to create their unique profiles, select their favorite travel activities, upload a profile picture, and even pen a brief description of themselves.

On the other hand, the post page allows users to post diverse images of their recent trips, add location information, and write a short paragraph to share their travel experiences with others.

# Project goal
The Post Planner API is a Django REST Framework API that powers the Post Planner website. It is designed to help users plan trips abroad by providing them with a unique perspective on various destinations. By browsing through photos and blogs from other travelers, users can gain insights into popular and off-the-beaten-path locations. For adventure enthusiasts, Post Planner offers inspiration to explore and experience new activities like cycling, hiking, and more. With Post Planner, planning a trip has never been easier or more exciting.


# API
The API provides essential resources for managing user accounts, creating and commenting on content, as well as searching and filtering content by location. This allows front-end developers to implement the desired features in their application related to user-generated content and location-based searches

# Project structure
The project's general structure draws inspiration from the DRF-API walkthrough, which adheres to the best practices for implementing APIs in the industry. As a result, the serializer, model, and URL files are structured in a way that reflects the conventional approach to implementing APIs using the Django REST framework.


# List of contents

<li><a herf="#profiles">Profiles</a></li>
<li><a herf="#travel-plan">Travel plan</a></li>
<li><a herf="#search-filter">Search & filter</a></li>
<li><a herf="#"></a></li>
<li><a herf="#"></a></li>
<li><a herf="#"></a></li>


# Data models

The process of designing the database was closely aligned with the development of the API endpoints.  By using this approach, I was able to ensure that each data model was well-suited to support the functionality of the API and the needs of the end-users.


# Profiles
The Profile model allows users to create a personalized profile that is unique to them, using a one-to-one relationship. To create a profile, users must first register and then add the personal details of their choice. The Profile model is only visible to authenticated users through an admin panel. A Boolean field is included with a default value of False to ensure that a user's profile must be approved by the site administrator before it can be viewed. This measure is in place to ensure user and online safety by preventing the creation of malicious profiles.

# Travel plan
The Travel Plan model offers authenticated users the ability to create multiple posts related to their profile, utilizing a one-to-many relationship. This model inherits the Activities list from the Profile model, allowing users to add relevant activities to their travel plans. Additionally, an image field is included, with image size, width, and height regulations in place.

With the Travel Plan model, users can add a title, write a description, specify a location, and upload an image to document their travel experiences for a specific location. Users also have the option to update or delete their posts as needed.

To ensure online safety, users cannot access and edit or delete another individual's post. All posts are subject to regulation through an admin panel and must be approved before the user or other users can view them.


# Search & filter 

# User stories

 Profile
- As a developer using the post planner API, I want to fetch a list of all the profiles created so that I can display them to the user interface.

- As a developer using the Post Planner API, I want to retrieve data from a user's profile so that I can display it to the user. This includes information such as their profile image, favorite activities, when their profile was created, and a section where they can write a short description about themselves. By accessing this data through the API, I can present a more personalized experience to the user 

- As a developer using the post planner API, I want to view and approve a users profile in an admin panel before viewing as to protect all user from sensitive user data exposure. 

- As a developer using the post planner API, I want to create two API endpoints for modifying user profile data, one for editing user profiles and another for deleting user profiles. This will provide users with the ability to update or remove their profile information through the API, improving the user experience and making the API more user-friendly.

Travel plan
- As a developer using the post planner API, I want an endpoint to get all travel plans so that I do not have to manually query the database and then add them manually.

- As a developer using the post planner API, I want an endpoint to save a travel plan object to the database so that users and share their content.

- As a developer using the post planner API, I want an endpoint so users can manually edit their travel plan by updating their images or content or loacations, and that the developer dose not need to update the database.

- As a developer using the post planner API, I want an endpoint so users can delete any travel plans manually, so that a developer does not need to update the database.

- As a developer using the post planner API, I want to restrict users from editing or deleting a travel plan that they did not create, ensuring that only the original creators have control over their content.


