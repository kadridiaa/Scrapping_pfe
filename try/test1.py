

def product_struct():
    
    return {
        "product_id": "",
        "availability": "",
        "name": "",
        "price": "",
        "familyName": "",
        "subfamilyName": "",
        "sectionName": "",
        "img": "",
    }
    
    
def generate_insert_query(structure, table_name):
   names = list(structure)
   cols = ', '.join(map(query_format, names))  # assumes the keys are valid column names.
   placeholders = ', '.join(['%({})s'.format(name) for name in names])
   query = 'INSERT INTO {} ({}) VALUES ({})'.format(table_name, cols, placeholders)
   return query


print(list(product_struct()))
