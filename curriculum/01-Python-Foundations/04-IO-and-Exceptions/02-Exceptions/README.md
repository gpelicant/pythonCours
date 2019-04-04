# Exceptions

In this assignment, you'll use `Exceptions` to build stronger programs.

## 1. `load_data`
Previously, you defined a `load_data` function. This time, you will write one
that can log if the file isn't found.

### `load_data`
This function takes a `filepath` (a path as a string) as argument, open the file and return its data if the file exists, otherwise it should print out
```
"Logging: file does not exist...")
```

**Open `src/data.py` and implement the function.**  
As usual, don't forget the docstring 😉


### `Counter`
As you might have guessed from this past week, we might have to count things
quite a little bit during the next 9 weeks.

Open the `src/counter.py` file and implement the class `Counter`.  
This class should:

* Take no initialization arguments
* Use a `dict` for tracking value counts
* Implement a `count` method which takes 2 arguments:
  * key: the thing we want to count
  * amount (default to 1): by how much you want to increment/decrement

**You need to use exceptions handling, at least `try` and `except`. Bonus point
if you manage to use `else` or `finally`.
