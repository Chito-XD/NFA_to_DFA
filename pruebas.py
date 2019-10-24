# from itertools import chain

# lst = ['foo.py', 'foo.py','bar.py', 'baz.py', 'qux.py', 'edgar']
# print(len(lst))
# s = set(lst)
# s.add('bar.py')
# print(s)
# print(len(s))
# print('---')
# r = set()
# r.add('edgar')
# r.add('ruben')
# r.add('qux.py')

# combine = set(chain(s,r))
# print(combine)
# print(len(combine))




# # Function which returns subset or r length from n 
# from itertools import combinations 
  
# arr = [1, 2, 3, 4] 
# r = 2

# for i in range(2, len(arr)+1):
#     l = list(combinations(arr, i))
#     print(l)


from itertools import combinations 
  
def rSubset(arr, r): 
  
    # return list of all subsets of length r 
    # to deal with duplicate subsets use  
    # set(list(combinations(arr, r))) 
    return list(combinations(arr, r))
  
# Driver Function 
if __name__ == "__main__": 
    arr = [1, 2, 3, 4] 
    r = 2
    a = rSubset(arr, r)
    print(len(a))
    print(a)
    for element in a: 
        print(element)