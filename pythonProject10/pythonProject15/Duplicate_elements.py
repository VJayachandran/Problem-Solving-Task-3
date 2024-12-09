def Intersectionfunc(myArr1, myArr2, myArr3):
    s1 = set(myArr1)
    s2 = set(myArr2)
    s3 = set(myArr3)

    # Intersection
    set1 = s1.intersection(s2)
    output_set = set1.intersection(s3)

    # Output set to list
    endList = list(output_set)
    print(endList)


# Driver Code
if __name__ == '__main__':
    # Elements of 3 arrays
    myArr1 = [5, 10, 15, 20, 25]
    myArr2 = [2, 5, 6, 7, 10, 15, 18, 20]
    myArr3 = [10, 20, 30, 40, 50, 60]

    # Calling Function
    Intersectionfunc(myArr1, myArr2, myArr3)