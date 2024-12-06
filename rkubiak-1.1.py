
keep_while_loop_running = True

while keep_while_loop_running == True:
    print('Enter company name.')
    company = raw_input()
    #check if right company name
    if company in ['aapl','goog','fb','msft','lnkd']:
        #whatever happens here, company is correct
        print('OKay')
        keep_while_loop_running = False
    else:
        #what do we want to do when it is false?
        print('Your name is wrong. Please type correct company')



days = raw_inpu('Insert number of days for average price' [1 up to 251])
stock_table = open(company.lower() +'.csv')
days= int(days)


file_lines = stock_table.readlines() [1:]   # file.readlines() returns a list of strings
second_value_list = []
total=0
count = 0
for line in file_lines:
    splits = line.split(",")
    second_value = float(splits[4])
    second_value_list.append(second_value)  
    count = count + 1
    if count == days:
        break

print(sum(second_value_list)/ len(second_value_list))
