def primary():
  print("Keep it logically awesome.")
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close() #comment
  print(quotes[0])
  
  if __name__== "__primary__":
  primary()
# python get-quote.py
