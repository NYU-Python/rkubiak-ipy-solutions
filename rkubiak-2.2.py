import csv

f = open('bitly.tsv')

 
 
file_lines = f.readlines() [1:]   # file.readlines() returns a list of strings
cities_list = []

for line in file_lines:
    splits = line.split("\t")
    cities = splits[3]
    cities_list.append(cities)
uniq_cities= set(cities_list)
print uniq_cities
