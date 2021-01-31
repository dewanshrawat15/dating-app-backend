# Dating App Backend structure
This repository contains the backend structure for a dating app.

## Getting started

### Creating a virtual environment
- Copy the GitHub repository URL.
- Open ```Git Bash``` and navigate to a place where the repository should be cloned.
- Run ```git clone url``` where ```url``` is the url copied.

### Virtual environment
- Open ```cmd```, navigate to the directory where the repository is cloned.
- Run, ```python -m venv myvenv``` to create a virtual environment.
- To activate the virtual environment:
	- For windows users, run ```myvenv\Scripts\activate```
	- For MacOS/Linux users, run ```source myvenv/bin/activate```
- Run ```pip install -r requirements.txt```

### Setting up
- Run ```cd mysite```
- Run ```python manage.py makemigrations```
- Run ```python manage.py migrate```


### Running the server
- Run ```python manage.py runserver```

## API Endpoints

### Register User API

This API is used to create a new register.

```
{
    "username": $username,
    "first_name": $first_name,
    "last_name": $last_name,
    "email": $email,
    "password": $password
}
```

On a succesful API call, the response returned would be

```
{
    "username": username,
    "first_name": first_name,
    "last_name": last_name,
    "email": email,
    "password": password
}
```

### Auth Token API

Get the authentication token for a user's login. Call this API when logging in a user. It would return an authentication token which can then be used to authorize further API requests.

```
{
    "username": $username,
    "password": $password
}
```

On a succesful API call, the response returned would be

```
{
    "token": $token_value
}
```

### Image Upload API

#### POST request API
Upload the image of a user. The authorization token needs to be set in the header.

```Authorization Token $token```

Attach an image to the ```user_image``` key.

#### GET request API
Get images of a user. The authorization token needs to be set in the header.

```Authorization Token $token```

### Match API

#### POST request API
The authorization token needs to be set in the header.

```Authorization Token $token```

The POST request data should follow this format:

```
{
    "user_one": $username_one,
    "user_two": $username_two,
    "match": true/false
}
```
Where ```user_one``` should be the username of the user who is authenticated, and ```user_two``` is the username of the selected user. The ```match``` parameter should be a true/false value depending upon whether user swiped right/left.

#### GET request API
The authorization token needs to be set in the header.

```Authorization Token $token```

Get profiles that a user can match with to display on the app.
