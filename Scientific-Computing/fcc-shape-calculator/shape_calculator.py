import math
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __repr__(self):
    return 'Rectangle(width={}, height={})'.format(self.width, self.height)
  
  def set_width(self, width):
    self.width = width
  
  def set_height(self, height):
    self.height = height
  
  def get_area(self):
    return self.width * self.height
  
  def get_perimeter(self):
    parameter = 2 * self.width + 2 * self.height
    return parameter
  
  def get_diagonal(self):
    # Using pythagorus theorum
    diagonal = ((self.width ** 2 + self.height ** 2) ** 0.5)
    return diagonal

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    pictureStr = ''
    for w in range(self.height):
      pictureStr += '{}\n'.format('*' * self.width)
    return pictureStr
  
  def get_amount_inside(self, shape):
    # This method checks if the shape's height is smaller than self's height
    # If yes, it will check for the width and how many of such width can fit in
    # Once this loop completes, it continues to the remaining height until it can no longer fit
    fits = 0
    if self.height < shape.height or self.width < shape.width:
      return fits
    x = shape.height
    while(x <= self.height):
      fits += math.floor(self.width / shape.width)
      x += shape.height
    return fits
      
# Override a few methods
class Square(Rectangle):
  def __init__(self, width):
    self.width = width
    self.height = width

  def __repr__(self):
    return 'Square(side={})'.format(self.width)

  def set_side(self, side):
    self.width = side
    self.height = side

  def set_height(self, height):
    super().set_height(height)
    self.width = height
  
  def set_width(self, width):
    super().set_width(width)
    self.height = width