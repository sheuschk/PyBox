# JP - JackBox in Python
A little game application, to play games similar to Werewolf on smartphones.

## Functionalities:
### Start - Lobby:
- A Web Page, which has a field to create a lobby
- Clicking on this button generates a code
- On this waiting pic is a list for joined Players
- Also a button to start
- Clicking the start button, starts the game

### User - entering:
- A User can enter an IP ADresse or link to get on the side
- He has to enter a code and a name
- He can press the button (join the game)
- He enters a lobby and gets a waiting sign displayed

- / just join the game with wtforms
- set a cookie and let the game run at /game
- after beeing  

## Work Packages:
- Create Lobby
- Create User Model

- Create a frontend


## Architecture
- A class Lobby (Singleton)
    - a code
    - users
    - game intern things like time till creation
    
- A User Model
    - Name
    - lobby
    - game things (wins/loss)
    
- Games
    - maybe a factory for different games or so.
    
 
## How Games get served
 Observer pattern to recognize changes, then trigger a server side event.
 User has states. states == different games or pauses. 
 
## Ideas
- Chose games at the lobby/wait screen and register them afterwards. 
- Username just one time
-spiel: so oft wie möglich drücken in 10 Sekunden

## Tips
- Run flask with threads:   ```flask run --with-threads```