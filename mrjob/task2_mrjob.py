from mrjob.job import MRJob

class AverageRevenuePerCategory(MRJob):

    def mapper(self, _, line):


    def reducer(self, category, values):


if __name__ == '__main__':
    AverageRevenuePerCategory.run()
