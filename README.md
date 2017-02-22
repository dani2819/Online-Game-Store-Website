

You can view the deployed project on http://rafay-wsdproject.herokuapp.com/authtest/
Login Credentials for developer:
Username: dani
Password: dani2819
Login Credentials for player:
Username: rafay
Password: dani2819

The project contains following features:
###Developer Module:

- Add the games to inventory
- Edit games
- Remove games
- See list of games on sales 
- See number of sales (sales statistics)


###Player Module

- View the games
- Search games by category
- Purchase the games using Niksula Payment Service api
- Play the game (hosted on the URL given by developer) 
- See game high scores while playing

###Game Service Interaction

Game and service communicate with each other using the message protocol (defined in project description) Player can do the follwing while playing game:
- Load the saved game state 
- Submit Score
- Save the current game state

###User Registration and Login

    Form created by using Django form functionality.
    Login and logout handled using Django Authentication System

###Django Rest Framework

REST API has been create using DJANGO REST framework to see the list of users. (http://rafay-wsdproject.herokuapp.com/api/)

###Responsive Design

For creating responsive design, we use bootstrap all over the project.
