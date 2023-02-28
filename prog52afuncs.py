
def calcPerim(len, wid):
  return 2 * len * wid

def areaPerim(len, wid):
  area = calcArea(len, wid)
  perim = calcperim(len, wid)
  return area, perim

def main():
  length = int(input("Enter length: "))
  width = int(input("Enter width: "))
  a, p = areaPerim(length, width)
  print(f"Area: {a}\nPerimiter: {p}")

if name == " main ":
  
  



