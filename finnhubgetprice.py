import requests
import time
import json
import sys

# Check this function again
def epoch2time(t):
    # e = int(t[:-3])
    return time.strftime("%d-%m-%Y %H:%M", time.localtime(t)) # might fail

if (len(sys.argv) == 1):
    print("Queries the finnhub.io API and returns the current price (US markets only)")
    print("Argument: SYMBOL")
    exit()

# symbol = "AAPL" # to change this to user input
symbol = sys.argv[1].upper()
# API key redacted
token = "ffffffffffffffffffffffffffffffffffffffff"

print("Getting data for " + symbol)

url = 'https://finnhub.io/api/v1/quote?symbol=' + symbol + '&token=' + token
# Sample output from SPY
# {"c":376.66,"d":-4.74,"dp":-1.2428,"h":383.38,"l":376.42,"o":381.33,"pc":381.4,"t":1672261200}
# What happens for invalid symbol? A: "d" key is null - see below
# {"error":"Market data subscription required for CFD indices."}
# {"c":0,"d":null,"dp":null,"h":0,"l":0,"o":0,"pc":0,"t":0}

response = requests.get(url)
responsetxt = response.text
d = json.loads(responsetxt)

if "error" in d:
    print("Error: " + d["error"])
    exit()

if d["d"] == None:
    print("Error retrieving data")
    exit()

print("")
print("SYMBOL  : " + symbol)
print("PRICE   : " + str(d["c"]))
print("TIME    : " + epoch2time(d["t"]) + " (local time)")
print("")
