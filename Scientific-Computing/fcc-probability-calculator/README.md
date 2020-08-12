## Probability Calculator

This project utilises out of the box thinking to calculate probabilities. It does not use mathematical forumlas (expected) but utilises experiment approach to obtain the result by performing it a large number of times.

It has fulfilled all the requirements of [FCC Scientific Computing with Python Projects - Probability Calculator](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator) project.

### Assignment

Suppose there is a hat containing 5 blue balls, 4 red balls, and 2 green balls. What is the probability that a random draw of 4 balls will contain at least 1 red ball and 2 green balls? While it would be possible to calculate the probability using advanced mathematics, an easier way is to write a program to perform a large number of experiments to estimate an approximate probability.

For this project, it has a program to determine the approximate probability of drawing certain balls randomly from a hat. 

The `hat` class will take a variable number of arguments that specify the number of balls of each color that are in the hat. For example, a class object could be created in any of these ways:
```
hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
```

A hat will always be created with at least one ball. The arguments passed into the hat object upon creation are converted to a `contents` instance variable. `contents` is a list of strings containing one item for each ball in the hat. Each item in the list is a color name representing a single ball of that color. For example, if your hat is `{"red": 2, "blue": 1}`, `contents` should be `["red", "red", "blue"]`.

The `Hat` class also have a `draw` method that accepts an argument indicating the number of balls to draw from the hat. This method should remove balls at random from `contents` and return those balls as a list of strings. The balls will go back into the hat during the draw, similar to an urn experiment without replacement. If the number of balls to draw exceeds the available quantity, return all the balls.

There is also an `experiment` function in `prob_calculator.py` (not inside the `Hat` class). This function accepts the following arguments:
* `hat`: A hat object containing balls that should be copied inside the function.
* `expected_balls`: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, set `expected_balls` to `{"blue":2, "red":1}`.
* `num_balls_drawn`: The number of balls to draw out of the hat in each experiment.
* `num_experiments`: The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)

The `experiment` function will return the probability calculated. 

For example, let's say that you want to determine the probability of getting at least 2 red balls and 1 green ball when you draw 5 balls from from a hat containing 6 black, 4 red, and 3 green. To do this, we perform `N` experiments, count how many times `M` we get at least 2 red balls and 1 green ball, and estimate the probability as `M/N`. Each experiment consists of starting with a hat containing the specified balls, drawing a number of balls, and checking if we got the balls we were attempting to draw.

Here is how you would call the `experiment` function based on the example above with 2000 experiments:

```
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, 
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
```

Since this is based on random draws, the probability will be slightly different each time the code is run.

### Development

For development, you can use `main.py` to test your code. Click the "run" button and `main.py` will run.
There are 2 different methods of using the `random` library to pick the colored balls from the hat - Both are documented in the code and the more verbose one is used mainly because the steps seemed to reflect the instructions in README more closely.

### Testing 

The unit tests for this project are in `test_module.py`. We imported the tests from `test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button.

## Acknowledgements

I would like to thank the various python tutorials out there which aided my learning throughout the 5 projects. Special mention to [Python.org's Random library docs](https://docs.python.org/3/library/random.html) and GeeksForGeeks for their tutorials in shallow copying lists.

This project has been tested running on Python 3.8+.
