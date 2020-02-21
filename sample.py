import pandas as pd
data = pd.read_excel (r'All Orders - Assesment.xlsx')
users_products = pd.DataFrame(data, columns= ['buyer-name','product-name'])
users = pd.DataFrame(data, columns= ['buyer-name'])
def get_unique_users(users_products,name_to_match):
    unique_items = set();
    for index, row in users_products.iterrows():
        if row['product-name'] ==  name_to_match:
            unique_items.add(row['buyer-name'])
    return unique_items;
unique_users_A = get_unique_users(users_products,"Product A")
unique_users_B = get_unique_users(users_products,"Product B");
users_A_B = [x for x in unique_items_A if x in unique_items_B]




    

