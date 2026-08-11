
__counter = 0
 
 
def suml(the_list):
  global __counter
  __counter += 1
  the_sum = 0
  for element in the_list:
   the_sum += element
  return the_sum
 
 
def prodl(the_list):
  global __counter
  __counter += 1
  prod = 1
  for element in the_list:
   prod *= element
  return prod
 
 
if __name__ == "__main__":
  print("I prefer to be a module, but I can do some tests for you.")
  my_list = [i+1 for i in range(5)]
  print(suml(my_list) == 15)
  print(prodl(my_list) == 120)

class LayisLearning:
  def __init__(self, boy, girl):
    self.boy=boy
    self.girl=girl
  def __str__(self):
    return f"{self.boy} really likes {self.girl}"
  def boys(self, num):
    print(f"he has {num} ballon dior")
  def __repr__(self):
    return f"hi {self.boy}, hello {self.girl}"