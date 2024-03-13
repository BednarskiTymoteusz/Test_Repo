

class Transaction():

    def __init__(self, i_price, i_product, i_amount, i_date, i_group, i_color, i_material, i_country):
        self.ProductPrice = i_price
        self.ProductName = i_product
        self.Amount = i_amount
        self.TransactionDate = i_date
        self.Group = i_group
        self.ProductColor = i_color
        self.ProducMaterial = i_material
        self.CountryProducer = i_country