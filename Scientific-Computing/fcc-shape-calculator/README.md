## Shape Calculator

This project is a basic shape parsing and display library which runs on Python3. 
It has fulfilled all the requirements of [FCC Scientific Computing with Python Projects - Polygon Area Calculator](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/polygon-area-calculator) project.

### Assignment

In this project I have used object oriented programming (oop) to create a Rectangle class and a Square class. The Square class is a subclass of Rectangle and inherit methods and attributes.

#### Rectangle class
When a Rectangle object is created, it is initialized with `width` and `height` attributes. The class also contain the following methods:
* `set_width(width)`
* `set_height(height)`
* `get_area`: Returns area (`width * height`)
* `get_perimeter`: Returns perimeter (`2 * width + 2 * height`)
* `get_diagonal`: Returns diagonal (`(width ** 2 + height ** 2) ** .5`)
* `get_picture`: Returns a string that represents the shape using lines of "\*". The number of lines are equal to the height and the number of "\*" in each line is equal to the width. There is a new line (`\n`) at the end of each line. If the width or height is larger than 50, it will return the string: "Too big for picture.".
* `get_amount_inside(shape)`: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.

Additionally, if an instance of a Rectangle is represented as a string, it looks like: `Rectangle(width=5, height=10)`

#### Square class
The Square class is a subclass of Rectangle, made using inheritance. When a Square object is created, a single side length is passed in. The `__init__` method stores the side length in both the `width` and `height` attributes from the Rectangle class.

The Square class is able to access the Rectangle class methods but does also contain an additional `set_side` method. If an instance of a Square is represented as a string, it will look like: `Square(side=9)`

Additionally, the `set_width` and `set_height` methods on the Square class will set both the width and height, which differs from the Rectangle class.

#### Usage example
```py
rect = shape_calculator.Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
```
That code should return:
```
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
```

The unit tests for this project are in `test_module.py`.

### Development

For development, you can use `main.py` to test your `shape_calculator()` function. Click the "run" button and `main.py` will run.

### Testing 

We imported the tests from `test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button.

## Acknowledgements

I would like to thank [Python.org](https://docs.python.org/3/index.html) as usual for their official Python 3.8 guide. It, as well as multiple other online tutorial, has benefitted me a lot in the development for this project. 

This project has only been tested thoroughly on Python 3.8+.
