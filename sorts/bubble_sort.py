

# Dumb Bubble sort

"""
procedure bubbleSort( A : list of sortable items )
    n = length(A)
    repeat
        newn = 0
        for i = 1 to n-1 inclusive do
            if A[i-1] > A[i] then
                swap(A[i-1], A[i])
                newn = i
            end if
        end for
        n = newn
    until n = 0
end procedure

"""



def buble_sort_basic (unsorted):

    n = len(unsorted)

    while True: #repeat
        # ### interesting []
        ls = 0
        for i in range (1, n):
            if unsorted[i] < unsorted [i-1]:
                temp = unsorted[i-1]
                unsorted [i-1] = unsorted[i]
                unsorted[i] = temp
                ls =i
        n=ls
        print (unsorted)
        if (n==0): #until
            break


    return # we do not return anything we just sort the array








def main():
    random = [5,3,7,6,1,4,9]
    buble_sort_basic (random)
    #print (random)

if __name__ == '__main__':
    main()
