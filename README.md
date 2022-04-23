# dotabase3.0
A way to spy on your friends dota games. New and Improved

# Purpose
This is specifically designed to collect match data from a select few players. Regardless of the amount, this data can be used later to create statistics over games or time frames. 

# How it works
This assumed an already working database. Specifically a psql/Elephant sql database was used
```python
postgres://database:password@host/user
port = 5432
```
For connection purposes when using elephantsql

`main.py` is a python program that runs checks against the database to see if the last match played by whatever steam32 user is in said database.
If that steam32 user and that match are not in the database, then the program pings opendota, and collects the match data and inserts it into the database.

# Future improvements
- The ability to quick-shove the last 20 games of a steam32 user into the database
- User ability to add steam32 rather than going into the program itself
- User ability to create the database relations given the parameters of the program
- The ability to use R to analize match data
- A web GUI that allows cleaner view of the data in said database
