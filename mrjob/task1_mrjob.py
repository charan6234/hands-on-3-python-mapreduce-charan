from mrjob.job import MRJob

class TotalRevenueByCategory(MRJob):

    def mapper(self, _, line):
        # Skip the header
        if line.startswith("ProductID"):
            return
        
        # Split the line by commas
        columns = line.split(',')
        item_id = columns[0]  # Changed from product_id
        category_name = columns[1]  # Changed from product_category
        revenue_amount = float(columns[3])  # Changed from revenue_generated
        
        # Emit category_name as key, and revenue_amount as the value
        yield category_name, revenue_amount

    def reducer(self, category_name, revenue_values):
        # Initialize total revenue
        total_revenue_amount = 0
        
        # Sum all revenues for the category
        for revenue in revenue_values:
            total_revenue_amount += revenue

        # Emit the category and the total revenue amount
        yield category_name, total_revenue_amount


if __name__ == '__main__':  # Corrected the condition to use double underscores
    TotalRevenueByCategory.run()