def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    for j in range(len(items)-1,0,-1):
        for i in range(j):
            if items[i]>items[i+1]:
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp
    return items

def merge_sort(items):

    '''Return array of items, sorted in ascending order'''
    len_items=len(items)
    if len_items==1:
        return items
    mid_point=int(len_i/2)
    list1=merge_sort(items[:mid_point])
    list2=merge_sort(items[mid_point:])
    return merge(list1,list2)


def merge(list1, list2):
        properlist=[]
        while len(list1)>0 and len(list2)>0:
            if list1[0]<list2[0]:
                properlist.append(list1[0])
                list1.remove(list1[0])
            else:
                properlist.append(list2[0])
                list2.remove(list2[0])
        if len(list1)==0:
             properlist=properlist+list2
        else:
             properlist=properlist+list1
        return properlist

def quick_sort(items):
    if len(items) <= 1:
        return items
    else:
        return quick_sort([x for x in items[1:] if x < items[0]]) + \
               [items[0]] + \
               quick_sort([x for x in items[1:] if x >= items[0]])
