# Movie ratings

## Guidelines

In this assignment, you're tasked with implementing 3 functions:

* `load_movies`
* `mean_rating`
* `best_rated`

Both `mean_rating` and `best_rated` will be using `load_movies`.
They all take 0 arguments and return something.

**NB: this is not an easy exercise, if you feel stuck, take the time to discuss
with your teammate or jump to the next assignment and come back to this
later.**

## 1. `load_movies`
This functions should load the `input/movies.csv` file and returns it as a list
of list where each list of the list is a movie record.

## 2. `mean_rating`
Use your `load_movies` function to load the movies file.  
Then compute the mean rating for the movies and return it.

## 3. `best_rated`
Use your `load_movies` function to load the movies file.  
Then, find the best rated movie and return it.

## General tips

* Don't forget to write docstrings for your functions.
* Module imports are allowed, try to import them at the top of the file, just
  under the module docstring
* Take a look at the file (you can show it using the `cat` command that we've
  seen on day 1), you'll see there is a subteltly in the way we should handle
  the data

