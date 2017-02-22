You can view the deployed project on http://rafay-wsdproject.herokuapp.com/authtest/

The project contains following features:
-
###Developer Module:
i) Add the games to inventory
ii) Edit games
iii) Remove games
iv) See list of games on sales
v) See number of sales (sales statistics)

###Player Module
i) View the games
ii) Search games by category
iii) Purchase the games using Niksula Payment Service api
iv) Play the game (hosted on the URL given by developer)
v) See game high scores while playing

###Game Service Interaction
Game and service communicate with each other using the message protocol (defined in project description) 
Player can do the follwing while playing game:
i) Load the saved game state
ii) Submit Score
iii) Save the current game state

###User Registration and Login
- Form created by using Django form functionality.
- Login and logout handled using Django Authentication System

###Django Rest Framework
REST API has been create using DJANGO REST framework to see the list of users. (http://rafay-wsdproject.herokuapp.com/api/)

###Responsive Design
For creating responsive design, we use bootstrap all over the project.
