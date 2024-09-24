from mrjob.job import MRJob

class TotalSalesPerCategory(MRJob):

    def mapper(self, _, line):
        # write mapper code here


    def reducer(self, category, values):
        # write reducer code here


if __name__ == '__main__':
    TotalSalesPerCategory.run()
