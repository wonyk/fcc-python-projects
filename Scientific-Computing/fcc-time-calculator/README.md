## Time Calculator

This project is a time calculator built using Python3. The functionalities are described below.
It has fulfilled all the requirements of the [FCC Scientific Computing with Python Projects - Time Calculator](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator) project.

### About

It has a function named `add_time` that takes in two required parameters and one optional parameter:
* a start time in the 12-hour clock format (ending in AM or PM) 
* a duration time that indicates the number of hours and minutes
* (optional) a starting day of the week, case insensitive

The function adds the duration time to the start time and return the result.

If the result falls on the next day, it should show `(next day)` after the time. If the result will be more than one day later, it should show `(n days later)` after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output will display the day of the week of the result. The day of the week in the output appears after the time and before the number of days later.

Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results.
```py
> add_time("3:00 PM", "3:10")
6:10 PM

> add_time("11:30 AM", "2:32", "Monday")
2:02 PM, Monday

> add_time("11:43 AM", "00:20")
12:03 PM

> add_time("10:10 PM", "3:30")
1:40 AM (next day)

> add_time("11:43 PM", "24:20", "tueSday")
12:03 AM, Thursday (2 days later)

> add_time("6:30 PM", "205:12")
7:42 AM (9 days later)
```

No Python libraries are imported (FCC requirement). I assume that the start times are valid times. The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number. However, a basic check is performed on the optional day argument. Should it have any spelling errors or simply is invalid, it will return `Error: Name of day is not clear.`.

### Development

For development, you can use `main.py` to test your `time_calculator()` function. Click the "run" button and `main.py` will run. This project works only in Python3, preferably Python 3.8+.

### Testing 

The unit tests for this project are in `test_module.py`. We imported the tests from `test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button.

## Acknowledgements

I would like to thank Python.org for their wonderful [official documentation](https://docs.python.org/3/) as well as other sites which offers Python tutorials and syntax assistance. They helped me a lot in completing this without the use of any libraries.
