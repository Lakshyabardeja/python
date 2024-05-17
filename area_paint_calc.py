
import math

def paint_calc(height, width, cover):
  num_of_cans = (height * width) / coverage
  roundof_cans = math.ceil(num_of_cans)
  print(f"you will need {roundof_cans} cans of paint")
  
test_h = int(input()) 
test_w = int(input()) 
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

