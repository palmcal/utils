# csvshow.py
#
# Print row by row of a csv file with header labels.
# Usage: csv_show infile.csv [firstrow=1] [numrows=1]
#    for all rows: csvshow <infile> 1 <large number>

import sys
import csv

if __name__ == "__main__":
    # open I/O files
    try:
        ifn = sys.argv[1]
        fin = open(ifn, 'r')
    except Exception, e:
        print e
        if len(sys.argv) > 1:
            print "cannot open '%s'" % (sys.argv[1])
        print "usage: %s infile" % (sys.argv[0])
        sys.exit(1)
    firstrow = 1
    if len(sys.argv) > 2:
        firstrow = int(sys.argv[2])
    numrows = 1
    if len(sys.argv) > 3:
        numrows = int(sys.argv[3])

    reader = csv.DictReader(fin)
    try:
        n = 0
        for i in range(1, firstrow):
            row = reader.next()
        for n in range(0, numrows):
            row = reader.next()
            print 'Row #' + str(firstrow + n) + ':'
            for k in row:
                print k[:18].ljust(20), row[k].ljust(20)
            print
    except:
        print str(n) + ' rows printed'
