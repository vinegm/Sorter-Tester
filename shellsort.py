def shellSort(alist):
  sublistcount = len(alist)//2
  while sublistcount > 0:

    for startposition in range(sublistcount):
      gapInsertionSort(alist,startposition,sublistcount)

    sublistcount = sublistcount // 2
    
  return alist

def gapInsertionSort(alist,start,gap):
  for i in range(start+gap,len(alist),gap):

    currentvalue = alist[i]
    position = i

    while position>=gap and alist[position-gap]>currentvalue:
        alist[position]=alist[position-gap]
        position = position-gap

    alist[position]=currentvalue



def shellSort_counting(alist):
  sublistcount = len(alist)//2
  comparisons = 0
  swaps = 0
  while sublistcount > 0:

    for startposition in range(sublistcount):
      comparisons, swaps = gapInsertionSort_counting(alist,startposition,sublistcount)

    sublistcount = sublistcount // 2
  
  return alist, comparisons, swaps


def gapInsertionSort_counting(alist,start,gap):
  comparisons = 0
  swaps = 0
  for i in range(start+gap,len(alist),gap):

    currentvalue = alist[i]
    position = i

    while position>=gap and alist[position-gap]>currentvalue:
      comparisons += 1
      alist[position]=alist[position-gap]
      position = position-gap
      swaps += 1

    alist[position]=currentvalue
    swaps += 1
  
  return comparisons, swaps
