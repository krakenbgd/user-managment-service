# user-managment-service
This is my implementation of User Managment Service that can be accessed via API endpoints.

## Setup
From the root project location run following command inside the terminal:
```docker-compose up --build```
This command will start the service container along with database containers. <br>
 Use example from ```.env-example``` to populate ```.env``` with correct values. <br>

## Endpoints

### ```GET /liveness```
Check if the API is live and responding.

### Request

```
No request parameters are required.
```
### Response

Returns a JSON object with a "HEALTH" key and value "OK" to indicate that the API is live and responding.

### ```GET /users```
Get a list of all users.

### Request

No request parameters are required.

### Response

Returns a list of all users in the database. Each user object contains the following fields:
```
id (int): unique identifier for the user
first_name (str): first_name of the user
last_name (str): last_name address of the user
age (int): user age
address (str): user address of residence
country (str): user country of residence
```
### ```GET /users/{id}```
Get a specific user by ID.

### Request

id (int): unique identifier for the user to retrieve.
### Response

Returns a JSON object with the user's information, including the fields described in the previous section.

### ```POST /users```
Create a new user.

### Request

Send a JSON object with the following fields:
```
first_name (str): first_name of the user
last_name (str): last_name address of the user
age (int): user age ( optional )
address (str): user address of residence ( optional )
country (str): user country of residence ( optional )
```
### Response

Returns a message with id of newly created user.

### ```PUT /users/{id}```
Update an existing user.

### Request

id (int): unique identifier for the user to update.
Send a JSON object with the following fields:
```
first_name (str): first_name of the user
last_name (str): last_name address of the user
age (int): user age
address (str): user address of residence
country (str): user country of residence
```
### Response

Returns a message indicating whether the update was successful.

### ```DELETE /users/{id}```
Delete a user.

### Request

id (int): unique identifier for the user to delete.
### Response

Returns a message indicating whether the deletion was successful.