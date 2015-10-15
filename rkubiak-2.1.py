
import os 
import sys

email=sys.argv[1:]

mydict={'subject':'', 'body':''}
for x in email:
	k, v = x.split('=')
	mydict[k]=v
	


#mydict={'to':'ro','subject':'', 'body':''}

#mydict={'to':'ro','from':'poo','date':'sep','subject':'', 'body':''}

##mydict={'to':'ro','from':'poo','subject':'la', 'body':'pa'}  #correct

mydict_k = mydict.keys()


mydict_k_sorted = sorted(mydict_k)


required_args = set(['to', 'from'])
valid_args = set(['to', 'from', 'subject', 'body'])

req_field = required_args.difference(mydict_k_sorted)
invalid_args=set(mydict_k_sorted).difference(valid_args)
if req_field:
	print 'Please enter required field', req_field

if invalid_args:
	print 'Remove invalid field(s)', invalid_args

if 'body' in mydict:
    del mydict['body']

mydict_sorted_keys = sorted(mydict, key=mydict.get)
for i in mydict_sorted_keys:
    print "{0} = {1}".format(i, mydict[i])
