import csv
import os

def build(dir):
    h = open(dir + "/hists.txt")
    if os.path.isfile(dir + "/desc.txt"):
        d = open(dir + "/desc.txt")
    else: d = None
    c = open(dir + "/cov.txt")
    prefix = dir.split("/")[-1]

    with open(dir + '/' + prefix + '.csv', 'wb') as data_file:
        data_writer = csv.writer(data_file, delimiter=',',
                                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
        first_row = []
        first_row.append('name')
        for i in range(1, 8):
            first_row.append(str(i))
        first_row.append('cor')
        first_row.append('date')
        if d:
            first_row.append('label')
        data_writer.writerow(first_row)

        h_lines = h.readlines()

        if d:
            d_lines = d.readlines()
        else:
            d_lines = None
        c_lines = c.readlines()

        for index, line in enumerate(h_lines):
            h_data = line.strip().split(" ")
            sum = 0
            for e in h_data[1:]:
                sum += float(e.strip())
            row = []
            row.append(prefix + "/" + h_data[0])
            for e in h_data[1:]:
                row.append(str(float(e) / sum))
            row.append(c_lines[index].strip().split(" ")[1])
            row.append(str(float(h_data[0][4:6]) / 12.0))
            if d_lines:
                row.append(d_lines[index].strip().split(" ")[1])
            data_writer.writerow(row)
    h.close()
    if d:
        d.close()
    c.close()




