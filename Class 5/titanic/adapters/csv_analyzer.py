# A CSVAnalyze class
import csv
import pdb

ENV_NAME = 'PROD'

def tracing():
    if ENV_NAME == 'DEV':
        pdb.set_trace()

class CSVAnalyze:

    data = []

    def __init__(self, csvfilename, delim=",", headers = True):

        self.csvfilename = csvfilename
        self.delim = delim

        try:
            # Try to open the file , exit if the file is not available.
            self.__f = csv.reader( open(self.csvfilename, 'r'), skipinitialspace=True )
            if headers:
                self.columns = self.__f.next()

            # Loading data into a dictionary structure
            self.data = [dict(zip(self.columns, i)) for i in self.__f]
            if not headers:
                self.columns = ["col_{}".format(i) for i in range(len(self.data[0]))]

        except IOError:
            print "File not found or readable."
            raise IOError

        else:
            print "Data loaded successfully..."

    def count(self):
        return len(self.data)

    def head(self,n=5):
        if self.data:
            return self.data[ : min(self.count(),n)]
        else:
            return None

    def tail(self,n=5):
        if self.data:
            return self.data[ : -1 * min(self.count(),n)]
        else:
            return None

    def mean(self,colname):
        #TODO : Implement mean function for a olumn if the column is numeric
        pass

    def __len__(self):
        # TODO: Change the return statement so that it returns the number of records in data
        return 0


    def __getitem__(self, item):
        if isinstance(item,int):
            return self.data[item]
        else:
            return [i[item] for i in self.data]

    def write_to_json(self, filename):
        #TODO: Implement write_to_json function ( Hint: there is  library for json )
        pass


if __name__ == '__main__':
    f = CSVAnalyze('../data/test.csv')
    print f.head(2)