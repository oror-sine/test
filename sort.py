import random
import time

def sort_test(func):
    _list = [i for i in range(10)]
    random.shuffle(_list)
    def wrapper(l=_list)->list:
        print("\n",func.__name__)
        # print(l)

        start = time.time()
        result = func(l)
        end = time.time()
        
        # print(result)
        print(end-start)   
        return result
    return wrapper

@sort_test
def selection_sort(_list):
    for i in range(len(_list)):
        min = _list[i]
        tmp = i
        for j in range(i, len(_list)):
            if _list[j]<min:
                min = _list[j]
                tmp = j
        _list[tmp] = _list[i]
        _list[i] = min
    return _list

@sort_test
def bubble_sort(_list):
    for i in range(len(_list)-1):
        for j in range(0,len(_list)-1-i):
            if _list[j]>_list[j+1]:
                tmp = _list[j]
                _list[j] = _list[j+1]
                _list[j+1] = tmp
    return _list

@sort_test
def insertion_sort(_list):
    for end in range(1,len(_list)):
        for j in range(end,0,-1):
            if _list[j]<_list[j-1]:
                _list[j],_list[j-1] = _list[j-1],_list[j]
            else:
                break
    return _list

def quick_sort(_list):
    if len(_list)==0:
        return []
    else:
        pivot = _list[0]
        l,r = [],[]
        for e in _list[1:]:
            l.append(e) if e<pivot else r.append(e)
        return quick_sort(l)+[pivot]+quick_sort(r)

def merge_sort(_list):
    def conquer(left,right):
        l = r = 0
        conquered = []
        while l<len(left) and r<len(right):
            if left[l]<right[r]:
                conquered.append(left[l])
                l+=1
            else:
                conquered.append(right[r])
                r+=1
        conquered += left[l:] + right[r:]
        return conquered

    def merge(devided):
        if len(devided) == 1:
            return devided[0]
        merged = []
        for i in range(len(devided)//2):
            merged.append(conquer(devided[2*i],devided[2*i+1]))
        if len(devided)%2:
            merged[-1]=conquer(merged[-1],devided[-1])
        return merge(merged)

    devided = [[e] for e in _list]
    return merge(devided)

def merge_sort2(_list):
    length = len(_list)
    if length<2:
        return _list

    left, right= merge_sort(_list[:length//2]), merge_sort(_list[length//2:])

    l=r=0
    merged = []
    while l<len(left) and r < len(left):
        if left[l]<right[r]:
            merged.append(left[l])
            l+=1
        else:
            merged.append(right[r])
            r+=1

    merged += left[l:] + right[r:]

    return merged

l = [i for i in range(200000)]
random.shuffle(l)

# selection_sort()
# bubble_sort()
# insertion_sort()
sort_test(quick_sort)(l)
sort_test(merge_sort)(l)
sort_test(merge_sort2)(l)
