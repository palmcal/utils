# csvcolumn.py
#
# Usage: python csvcolumn.py [column name] [data file]

import sys
import csv

DEBUG = 1

if __name__ == "__main__":
    # open I/O files
    try:
        column = sys.argv[1]
        ifn = sys.argv[2]
        fin = open(ifn, 'r')
    except Exception, e:
        print e
        if len(sys.argv) > 2:
            print "cannot open '%s'" % (sys.argv[2])
        print "usage: %s column infile" % (sys.argv[0])
        sys.exit(1)

    reader = csv.DictReader(fin)
    #fieldsout = ['specialty']
    fieldsout = [column]
    writer = csv.DictWriter(sys.stdout, fieldsout, restval='', extrasaction='ignore')
    for row in reader:
        writer.writerow(row)
