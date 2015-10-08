
def stock(ticker):
## function opens csv file for specific stock  ticker
    if ticker == "AAPL":
        stock_table = open("aapl.csv")
    elif ticker == "FB":
        print "in FB"
        stock_table = open("fb.csv")
    elif ticker == "GOOG":
        print "in google"
        stock_table = open("goog.csv")
        #print stock_table
        return stock_table
    elif ticker == "LNKD":
        stock_table = open("lnkd.csv")
    elif ticker == "MSFT":
        stock_table = open("msft.csv")
    else:
        print "Give me right stock ticker"
    return stock_table


fh = stock(ticker) ##insert stock ticker 

c= ## insert number of days 
##str(raw_input('Input # of days'))

def av(c):
## function calculating average opening price based on number of provided days
    file_lines = fh.readlines() [1:]   # file.readlines() returns a list of strings
    second_value_list = []
    total=0
    count = 0
    for line in file_lines:
        splits = line.split(",")# prints 'jw234,Joe,Wilson,Smithtown,NJ,2015585894' 

        second_value = splits[1]
        second_value_list.append(second_value)        # then 'ms15,Mary,Smith,Wilsontown,NY,5185853892'  etc.
        total = total + float(second_value)
        count = count + 1
        if count > c:
            break

    
   
    print float(total/count)
