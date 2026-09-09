def multiplication_table(num):
    result=0
    for i in range(1,11):
        result=i*num
        print(i,"*",num,"=",result)
    return result