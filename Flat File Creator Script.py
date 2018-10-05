import csv
from pprint import pprint
with open('data.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')

        expandedCsv = [] #temp expansion
        

        

        #read into a list
        data = []
        for row in spamreader:
                data.append(row)
                
                
                #print row [0:7]

        #this little chunk creates a row for each temperature possible
        for row in data:
                #get a header row
                tempLst = data[0][7:12]
                
                #get the temperature truth table
                tTable = row[7:12]

                I = 0
                for truth in tTable:
                        
                        if truth == 'x':
                                rowConc = row[0:7] + [tempLst[I]] + row[12:]
                                expandedCsv.append(rowConc)
                        I =I+1

        #this little chunk creates a row for each finish possible
        header = data[0]
        expandedLstFin = []
        for row in expandedCsv:
                #get a header row
                finLst = header[12:18] #list of finishes
                tTable = row[8:14] #table with the xs in it
                preFix = row[0:8] #the beginning chunk of info
                suffix = row[0-1] #grab qr/sr
                #create the finish matrix
                I = 0
                for truth in tTable:
                        if truth == 'x':
                                #add a new row for each finish
                                rowConc = preFix + [finLst[I]] + [suffix]
                                expandedLstFin.append(rowConc)
                        I = I+1
                                
                


        #this little chunk creates a new row for each approval
        expandedLstApproval = []
        for row in expandedLstFin:
                #get a header row
                approvLst = header[4:7] #list of approvals
                tTable = row[4:7] #table with the xs in it
                preFix = row[0:4] #the beginning chunk of info
                suffix = row[7:] #grab last bit
                #create the finish matrix
                I = 0

                for truth in tTable:
                        if truth == 'x':
                                #add a new row for each finish
                                rowConc = preFix + [approvLst[I]] + suffix
                                expandedLstApproval.append(rowConc)
                        I = I+1

for row in expandedLstApproval:
        print row
        
#write csv out to txt file that can be used in excel
with open('eggs.csv', 'wb') as fd:
        writer = csv.writer(fd, dialect='excel', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerows(expandedLstApproval)



                
