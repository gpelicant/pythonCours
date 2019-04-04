# Reading files 

## Guidelines
In this file, you will implement 2 functions:

* `load_data`
* `file_stats`

For both functions, we've provided the file `input/la_classe.txt` so you can
try your implementations.

### `load_data`
This function takes a `filepath` (a path as a string) as argument, open the file and return its
data.
Quite simple, but **Don't forget the docstring.**

### `file_stats`
This function takes a `filepath` as an argument and return some statistics of
the file as a dictionary:

* number of lines for key `num_lines`
* number of words for key `num_words`
* number of characters for key `num_chars`

You'll to initialize an empty `dict`, open the files and keep track of the 3
statistics while reading it.

Again, don't forget to **write a docstring for your function**.

## General tips
`file_stats` is a bit more difficult to implement than `load_data`.
For implementing it, you may be interested to take a look at the `collections` module from the Python's standard library.
