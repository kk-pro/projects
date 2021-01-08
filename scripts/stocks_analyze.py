import requests, subprocess, os, json, sys


links = []
data = {"totalDebt":[],"interestIncome":[],"totalRevenue":[],"MarketCap":[]}
def get_url(symbol):
    data_type = {'overview':"OVERVIEW",
    'income':"INCOME_STATEMENT",
    'balance':"BALANCE_SHEET",
    }
    print('Checking %s ....'% symbol)
    for v in data_type.values():
        dtype = v
        url = "https://www.alphavantage.co/query?function=" + dtype + "&symbol=" + symbol + "&apikey=XXXXXXXX"
        links.append(url)
            
    

def get_data(symbol):
    get_url(symbol)
    for url in links:
        
        response = requests.request("GET", url)
        results = json.loads(response.text)

        # to check if ticker symbol is wrong or json is empty
        if len(results) == 0:
            print("[+] Erorr: Check ticker symbol please")
            sys.exit()

        else:
            if "INCOME_STATEMENT" in url:
                quarterlyReports = json.loads(response.text)["quarterlyReports"]
                interestIncome = quarterlyReports[0]["netInterestIncome"]
                totalRevenue = quarterlyReports[0]["totalRevenue"]
                
                # filter info for None or zero
                if interestIncome == 'None':
                    print('[+] The are no info about net interest income')
                    sys.exit()
                else:
                    data["interestIncome"]= float(interestIncome)

                if totalRevenue == None:
                    print('[+] There are no info about total revenue')
                    sys.exit()
                else:
                    data["totalRevenue"] = float(totalRevenue)

            elif "BALANCE_SHEET" in url:
                quarterlyReports = json.loads(response.text)["quarterlyReports"]
                print(quarterlyReports)
                longTermDebt = quarterlyReports[0]["longTermDebt"]
                shortTermDebt = quarterlyReports[0]["shortTermDebt"]
                try:
                    totalDebt = int(longTermDebt) + int(shortTermDebt)

                    data["totalDebt"] = float(totalDebt)
                except ValueError:
                    if longTermDebt == 'None':
                        print("[+] There are no info about long term debt")
                        sys.exit()
                    if shortTermDebt == 'None':
                        print('[+] There are no info about short term debt')
                        sys.exit()
            elif "OVERVIEW" in url:
                quarterlyReports = json.loads(response.text)
                print(quarterlyReports)
                MarketCap = quarterlyReports["MarketCapitalization"]

                data["MarketCap"] = float(MarketCap)
    
def check_stock(symbol):
    get_data(symbol)
    #print(data)
    if data['totalRevenue'] == 0:
        if (data['totalDebt'] / data['MarketCap']) * 100 <= 30:
            print("HALAL") 
        else:
            print("HARAM")
    else:
        if (data['totalDebt'] / data['MarketCap']) * 100 <= 30 and (data['interestIncome'] / data['totalRevenue']) * 100 <= 5:
            print("HALAL") 
        else:
            print("HARAM")

check_stock("AAPL")