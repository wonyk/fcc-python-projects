import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for color, num in kwargs.items():
      for i in range(num):
        self.contents.append(color)
    self.copy = self.contents[:]

  def draw(self, num):
    self.contents = self.copy[:]
    if num >= len(self.contents):
      return self.contents
    # I can loop and remove the elements by random or use the method below. I am unsure what is the "correct" method I am supposed to use.
    # Thus, I use this method since it resembles the instructions in README more.
    chosenBalls = []
    for i in range(num):
      color = random.choice(self.contents)
      chosenBalls.append(color)
      self.contents.remove(color)

    # A one-liner which might not be what FCC wants.
    # chosenBalls = random.sample(self.contents, num)
    # for color in chosenBalls:
    #   self.contents.remove(color)

    return chosenBalls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  matchedTally = 0
  for i in range(num_experiments):
    actual = {}
    result = hat.draw(num_balls_drawn)
    for color in result:
      if color in actual:
        actual[color] += 1
      else:
        actual[color] = 1
    # Check that for every colour in expected, there is a match in actual and if there is, it will check if the actual
    # meet the requirement by having more than or equal to expected before incrementing the matchedTally
    if all(key in actual and actual[key] >= expected_balls[key] for key in expected_balls):
      matchedTally += 1
  return (matchedTally / num_experiments)