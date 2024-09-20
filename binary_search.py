def binary_search(list, item):
    start=0
    end=len(list)-1
    
    while  end >= start :
        
        middle = (start + end)//2
        number = list[middle]
        
        if number == item:
            print("item found")
            return number
        
        if number > item:
            end = middle - 1 
        
        if number < item:
            start = middle + 1
    
    
    return None



list = [1, 3, 5, 8, 12, 15, 16, 19, 25, 28, 50, 52, 54, 62]

print(binary_search(list, 12))
