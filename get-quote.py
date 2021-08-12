def primary():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close() #comment

  print(quotes)

if __name__== "__primary__":
  primary()
# python get-quote.py
