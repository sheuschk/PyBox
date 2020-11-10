# JP - JackBox in Python
A little game application, to play games similar to Werewolf as a group on personal devices.  
!! The project is not finished. It has no real games and no Front End Design!!

## Installation
Create an venv and install requirements.txt file
* `pip venv -m jp`
* `jp\Scripts\activate`
* go to application directory
* `pip install -r requirements.txt`

Start with command  `flask run`

#### Requirements
It was last tested with python 3.8.4.

## Workflow
1. One Person creates a lobby ```/lobby/create```
2. Every user gets now redirected to ```/lobby/wait```, where a code gets displayed 
3. All users who want to join have to enter the url ```/join```.
 They have to enter the code for the lobby and their name.
4. Everyone waits till the everyone joined and all names are displayed at ```/lobby/wait```
5. Start the game by pressing Start
6. Lobby (`/lobby`): The Lobby displays the general information. Which game is chosen? Who won the last one? and so on.
7. User (`/`): Every User has its personal game space at `/`. This is just on the device they entered the lobby on

With this base multiple games could be programmed and an wrflow for the lobby. For example randomly choose games, or
games can be modified. The principle of an alien in the group of players who gets slightly different questions/ tasks 
in the game and the team has to vote who it is was once the objective.

### Guess Game
The Guess game was the most simple implementation of a possible game. 
It serves as an example of how the workflow between Lobby and the Players should go.
The Lobby generates a number. Every User has to guess and the clostest number wins.

1. Lobby: Start Guess game by pressing "Guess!"
2. User: Gets an alert for the guess game
3. User: Every USer enters a number between 1 and 100 and commits
4. Lobby: After every User entered his number press "Evaluate Guess" to finish the game
4. Lobby: The random number gets displayed and the Player with the closest number gets displayed as the winner

## Architecture:
### Start - Lobby:
- A Web Page, which has a field to create a lobby
- Clicking on this button generates a code
- On this waiting pic is a list for joined Players
- Also a button to start
- Clicking the start button, starts the game

### User - entering:
- A User can enter an IP Address or link to get on the side
- He has to enter a code and a name
- He can press the button (join the game)
- He enters a lobby and gets a waiting sign displayed

- / just join the game with wtforms
- set a cookie and let the game run at /game


### Implementation
- A class Lobby (Singleton)
    - a code
    - users
    - game intern things like time till creation
    
- A User Model
    - Name
    - lobby
    - game things (wins/loss)
    
- Games
    - maybe a factory pattern for different games.
    
 The application is based on Web Socket Communication with the client.
 
### How Games could get served 
 An Observer pattern should recognize changes in the state of the lobby, then trigger a server side event.
 User has states. states == different games or pauses. 
 
## Ideas
- Chose games at the lobby/wait screen and register them afterwards. 
- Usernames just one time
- simple game: push a button as fast as you can

## Tips
- Run flask with threads:   ```flask run --with-threads```