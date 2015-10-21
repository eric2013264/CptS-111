
def second_highest(thelist):
    second_highest = 0 #set_highest is now 0
    for item in (thelist): #for loop begins, for each item in (thelist)
        if (item > second_highest) and (item != max(thelist)):
            second_highest = item
    return second_highest
 
def product(thelist):
    product = 1
    for x in thelist:
        product = product * x
    return product
 
def multiply_by_scaler(thelist, multiplier):
    products = []
    for item in thelist:
        products.append(item * multiplier)
    return products
 
def multiply_lists(list1, list2):
    products = []
    for idx,item in enumerate(list1):
        products.append(list1[idx]*list2[idx])
    return products
 
 
if __name__ == "__main__":
 
    thelist = [1,10,2,54,32,12,3]
 
    print(second_highest(thelist))
    print(second_highest(thelist[:4]))
 
    print(product(thelist))
    print(product(thelist[2:6]))
 
    print(multiply_by_scaler(thelist, 7))
    print(multiply_by_scaler(thelist, 0.5))
 
    print(multiply_lists(thelist, range(len(thelist))))
    print(multiply_lists(thelist, thelist))
 
        # These can be combined
    print(multiply_by_scaler(thelist, second_highest(thelist)))
    print(multiply_lists(thelist, multiply_by_scaler(thelist, 5)))

#python lab5.py