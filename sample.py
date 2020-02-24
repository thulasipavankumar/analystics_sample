import pandas as pd
data = pd.read_excel (r'All Orders - Assesment.xlsx')
# Purchase Date	buyer-name	product-name	quantity-shipped	recipient-name

users_products = pd.DataFrame(data, columns= ['buyer-name','product-name'])
users = pd.DataFrame(data, columns= ['buyer-name'])
users_with_count = pd.DataFrame(data, columns= ['buyer-name','product-name','quantity-shipped'])
def get_unique_users(users_products,name_to_match):
    list_of_users = [];
    unique_items = set();
    count = 0;
    for index, row in users_products.iterrows():
    #print(row['buyer-name'],row['product-name'])
        if row['product-name'] ==  name_to_match:
            unique_items.add(row['buyer-name']);
            list_of_users.append(row)
            count+=1;
    return unique_items,count,list_of_users;
#print(users_products)
#print ((users.loc[:,'buyer-name']))
unique_users_A,count_A,all_users_A = get_unique_users(users_with_count,"Product A")
unique_users_B,count_B,all_users_B = get_unique_users(users_with_count,"Product B");
users_A_B = [x for x in unique_users_A if x in unique_users_B]
print(count_A,count_B);
print(len(all_users_A),(all_users_A))
def get_cases_more_than_single_purchase(users_with_count,purchase_count):
    unique_items = set();
    count = 0;
    for index, row in users_with_count.iterrows():
    #print(row['buyer-name'],row['product-name'])
        if row['product-name'] ==  name_to_match:
            unique_items.add(row['buyer-name']);
            count+=1;
    return unique_items,count;



    

