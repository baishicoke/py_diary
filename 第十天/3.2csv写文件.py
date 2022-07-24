import csv
with open('test.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(("name","age","from"))
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
    spamwriter.writerows([['Spam'],
                         ['Lovely Spam'],
                         ['Wonderful Spam']])


