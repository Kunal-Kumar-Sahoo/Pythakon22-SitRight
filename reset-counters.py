import csv

file = open('data.csv', 'r')
reader = csv.reader(file, delimiter=',')

st = []
for line in reader:
    line[-1] = '0'
    st.append(line)
file.close()

file_ = open('data.csv', 'w')
writer = csv.writer(file_, delimiter=',')
for line in st:
    writer.writerow(line)
file_.close()