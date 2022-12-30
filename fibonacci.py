#fibonacci

def fav(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fav(n-1)+fav(n-2)

print(fav(5))