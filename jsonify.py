import json
from optparse import OptionParser

# setting up option parser
usage = "usage: %prog -f filename.json -n number_of_records"
parser = OptionParser(usage=usage)
parser.add_option("-f", "--file", action="store", type="string", dest="filename",
                  help="file to store user data as a JSON file")
parser.add_option("-n", "--number", action="store", type="int", dest="num",
                help="denote the number of records you want to enter")

(options, args) = parser.parse_args()

# if filename is not given
if options.filename is None:
    parser.error('Filename not given')

# if number of records is not given
if options.num is None:
    parser.error('Number of records not given')

#function to take user input and produce a json file
def jsonify():
    data = []
    outfile = open(options.filename, "w")

    for i in range(options.num):
        print "Enter information for record %s: \n" % (i+1)
        emp = raw_input("\tEnter employer: ")
        sdate = raw_input("\tEnter date (start-end): ")
        position = raw_input("\tEnter position: ")
        heading = raw_input("\tEnter heading: ")
        numBullets = int(raw_input("\tEnter number of bullets: "))
        bullets = []
        for j in range(numBullets):
            bullets.append(raw_input("\t\tEnter bullet %s: " % (j+1)))

        desc = {"heading":heading, "num":numBullets, "bullets": bullets}
        data.append({"employer":emp, "sdate":sdate, "position":position, "desc": desc})

    json.dump(data, outfile)

if __name__ == "__main__":
    jsonify()
    print "\nDone!\n"
