from mrjob.job import MRJob

class TotalRevenueAndCountByCategory(MRJob):

    def mapper(self, _, line):
        # Skip the header
        if line.startswith("ProductID"):
            return
        
        # Split the line by commas
        columns = line.split(',')
        item_id = columns[0]  # Changed from product_id
        category_name = columns[1]  # Changed from product_category
        revenue_amount = float(columns[3])  # Changed from revenue_generated
        
        # Emit category_name as key, and (revenue_amount, 1) as the value
        yield category_name, (revenue_amount, 1)

    def reducer(self, category_name, revenue_values):
        # Initialize totals
        total_revenue_amount = 0
        total_product_count = 0
        
        # Sum the revenues and count the products
        for revenue, count in revenue_values:
            total_revenue_amount += revenue
            total_product_count += count

        # Emit the category, total revenue, and total product count
        yield category_name, (total_revenue_amount, total_product_count)


if __name__ == '__main__':  # Corrected condition to use double underscores
    TotalRevenueAndCountByCategory.run()
