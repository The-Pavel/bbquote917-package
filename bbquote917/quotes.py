# Consume  breaking bad api for quotes
import requests

def get_quote():
  url = "https://wagon-breaking-bad-quotes.herokuapp.com/v1/quotes"
  res = requests.get(url).json()
  return f"{res[0]['quote']} --- by {res[0]['author']}"

if __name__ == "__main__":
  print(get_quote())
