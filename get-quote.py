import random
def POWER():
  #print("Keep it logically awesome.")
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 13
  rnd = random.randint(0,last)
  for idx in range(0,rnd):
    print(quotes[idx],end="")

if __name__== "__main__":
  POWER()
