import math

class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []
    self.cash = 0.00
    self.spending = 0.00

  def __repr__(self):
    # Description has a max length of 23 while amount has a max length of 7
    outputStr = ''
    outputStr += self.name.center(30, '*')
    for item in self.ledger:
      desc = item["description"][:23]
      amt = '{:.2f}'.format(item["amount"])[-7:]
      outputStr += '\n{:<23}{:>7}'.format(desc, amt)
    # Add the total at the end
    outputStr += '\nTotal: {:.2f}'.format(self.cash)
    return outputStr

  def check_funds(self, amount):
    if float(amount) > self.cash:
      return False
    return True

  def deposit(self, amount, *args):
    newDepositObj = {"amount": amount, "description": ""}
    if len(args) == 1:
      newDepositObj["description"] = args[0]
    self.ledger.append(newDepositObj)
    self.cash += float(amount)

  def withdraw(self, amount, *args):
    if not self.check_funds(amount):
      return False
    newWithdrawObj = {"amount": amount * -1, "description": ""}
    if len(args) == 1:
      newWithdrawObj["description"] = args[0]
    self.ledger.append(newWithdrawObj)
    self.cash -= float(amount)
    self.spending += float(amount)
    return True
  
  def get_balance(self):
    return self.cash

  def transfer(self, amount, instance):
    if not self.check_funds(amount):
      return False
    self.withdraw(amount, "Transfer to {}".format(instance.name))
    instance.deposit(amount, "Transfer from {}".format(self.name))
    return True


def create_spend_chart(categories):
  # Calculate the total length required. We use this formula:
  # 5 for the percentage values plus the space
  # (1 + 2) for each category and the spaces to the right respectively
  # For width, we will just calculate the longest category length
  lengRequired = 5 + 3 * len(categories)
  widthRequired = 0
  totalSpending = 0.00
  for category in categories:
    if len(category.name) > widthRequired:
      widthRequired = len(category.name)
    totalSpending += category.spending

  # Calculate the percentage for each category, rounded down to the nearest 10
  percentageList = []
  for category in categories:
    percent = math.floor((category.spending / totalSpending) * 10) * 10
    percentageList.append(percent)
  
  # Showcase the chart now:
  chart = 'Percentage spent by category\n'
  for i in range(100, -1, -10):
    chart += '{i: >3}| '.format(i = i)
    cirleOrSpace = '' 
    for a in range(0, len(categories)):
      # Add 'o' and 2 spaces or 3 spaces
      filled = ''
      if percentageList[a] >= i:
        filled = 'o'
      cirleOrSpace += '{filled: <3}'.format(filled = filled)
    chart +=  cirleOrSpace + '\n'
  chart += '{}{:{fill}>{leng}}'.format(' ' * 4, '', fill = '-', leng = lengRequired - 4)
  # Fill in the category names
  for char in range(widthRequired):
    charOrSpace = ' ' * 5
    for category in categories:
      # Either fill in the char or put a space
      placeholder = ' '
      if char < len(category.name):
        placeholder = category.name[char]
      charOrSpace += '{:<3}'.format(placeholder)
    chart += '\n' + charOrSpace
  return chart