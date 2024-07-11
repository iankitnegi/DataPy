# DataPy
Welcome to DATAPy! This repo contains my Python learning from basic to data science, featuring basic programming, logic building, data manipulation, analysis, and visualization. Stay tuned for updates and new content!

### **Learning/Quick-Notes:**  
-     #Use of random module
      import random
      r = random.randint(1, 10)
      print(r)

-     #Use of calendar module
      import calendar
      y = int(input("Enter the year: "))
      m = int(input("Enter the month: "))
      c = calendar.month(y, m)
      print(c)

-     #Use of math module
      import math
      print(math.sqrt(25))

-     #Use of format() funn
      print("{0} is Prime number".format(n))

-     #Binary, Octal, Hexadecimal funn: convert decimal -> binary, octal, hexadecimal
      bin(), oct(), hex()

-     #ASCII: Character -> ASCII number {funn}
      ord()

-     # Data Collection
      data = []
      data.extend([10, 20, 30, 40, 50])

      # Data Cleaning
      if 30 in data:
            data.remove(30)

      # Data Transformation
      data.sort()
      data.reverse()

      # Data Summarization
      total = sum(data)
      max_value = max(data)
      min_value = min(data)

      # Preparing for Visualization
      indexed_data = list(enumerate(data))

      print("Cleaned Data:", data)
      print("Total:", total)
      print("Max Value:", max_value)
      print("Min Value:", min_value)
      print("Indexed Data:", indexed_data)

