import csv, codecs


filename = "test.csv"

file = codecs.open(filename, "r", "euc_kr")
reader = csv.reader(file, delimiter=",", quotechar='"')

for cells in reader:
    if len (cells) >=3:
        print(cells[1],cells[2])

#pandas