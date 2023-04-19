Post Planner API

The Post Planner API provides a comprehensive back-end interface for storing, creating, and filtering travel-centric content for various locations. The API primarily focuses on two content types: profile pages and post pages.

The profile page enables users to create their unique profiles, select their favorite travel activities, upload a profile picture, and even pen a brief description of themselves.

On the other hand, the post page allows users to post diverse images of their recent trips, add location information, and write a short paragraph to share their travel experiences with others.

# Project plan


# API
The API provides essential resources for managing user accounts, creating and commenting on content, as well as searching and filtering content by location. This allows front-end developers to implement the desired features in their application related to user-generated content and location-based searches

# Project structure
The project's general structure draws inspiration from the DRF-API walkthrough, which adheres to the best practices for implementing APIs in the industry. As a result, the serializer, model, and URL files are structured in a way that reflects the conventional approach to implementing APIs using the Django REST framework.

# List of contents

<li><a herf="#profiles">Profiles</a></li>
<li><a herf="#posts">Posts</a></li>
<li><a herf="#comments">Comments</a></li>
<li><a herf="#search-filter">Search & filter</a></li>
<li><a herf="#"></a></li>
<li><a herf="#"></a></li>
<li><a herf="#"></a></li>




# Profiles

# Posts

# Comments

# Search & filter 

# User stories

 Profile
- As a developer using the post planner API, I want to fetch a list of all the profiles created so that I can display them to the user interface.

- As a developer using the Post Planner API, I want to retrieve data from a user's profile so that I can display it to the user. This includes information such as their profile image, favorite activities, when their profile was created, and a section where they can write a short description about themselves. By accessing this data through the API, I can present a more personalized experience to the user 

- As a developer using the post planner API, I want to approve a users profile before viewing as to protect all user from sensitive user data exposure. 

- As a developer using the post planner API, I want to create two API endpoints for modifying user profile data, one for editing user profiles and another for deleting user profiles. This will provide users with the ability to update or remove their profile information through the API, improving the user experience and making the API more user-friendly.

Travel plan
- As a developer using the post planner API, I want an endpoint to get all travel plans so that I do not have to manually query the database and then add them manually.

- As a developer using the post planner API, I want an endpoint to save a travel plan object to the database so that users and share their content.

- As a developer using the post planner API, I want an endpoint so users can manually edit their travel plan by updating their images or content or loacations, and that the developer dose not need to update the database.

- As a developer using the post planner API, I want an endpoint so users can delete any travel plans manually, so that a developer does not need to update the database.

- As a developer using the post planner API, I want to restrict users from editing or deleting a travel plan that they did not create, ensuring that only the original creators have control over their content.