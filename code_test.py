lst = [1,2,3,4,5,6,7,8]

def fun(x):
    if(x%2 == 0):
        return x

l = map(fun,lst)
print(list(l))