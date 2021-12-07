import csv

with open("VN30Index_FORMATTED.csv") as fr, open("VN30Index_FORMATTED_R.csv","w",newline="") as fw:
    cr = csv.reader(fr,delimiter=";")
    cw = csv.writer(fw,delimiter=";")
    cw.writerow(next(cr))  # write title as-is
    cw.writerows(reversed(list(cr)))