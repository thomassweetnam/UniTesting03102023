import csv
with open('C:\Users\ec221018\Downloads\linear_data.csv') as csv_file:
    csv_read=csv.reader(csv_file, delimiter=',')

print(len(csv_read))