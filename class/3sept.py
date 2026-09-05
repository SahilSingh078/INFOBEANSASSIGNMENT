product = [{"name" : "laptop" , "price": 8000},
            {"name" : "mobile" , "price": 6000},
            {"name" : "tablet" ,"price": 4000}]
result = sorted(product, key = lambda x: x["price"])
print(result)