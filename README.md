## pysticks

Launch the game with : 

```python 
python main.py 
``` 

## Rules

- The game starts with 15 sticks.
- The two players pick between 1 and 3 sticks in turn. 
- The player that pick the last stick loses. 


## Play against a friend or against a bot

Play against the bot and you start (default case) : 
```python 
python main.py players=bot_last  // or just `python main.py` 
``` 

Play against another person : 
```python 
python main.py players=1v1 
``` 

Play against the bot and let it play first : 
```python 
python main.py players=bot_first
``` 

## Change the game

Edit `./config/game/custom.yaml` to change : 
- the number of sticks
- the maximum number of sticks one can pick.

Then play with : 

```python 
python main.py game=custom
``` 