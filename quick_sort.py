def partition(number_list, start_index, end_index):
    middle = start_index + (end_index - start_index) // 2
    pivot = number_list[middle]
    print(' Current pivot value:',pivot)
    print(' Current Starting index:',start_index)
    print(' Current End index:',end_index)

    low = start_index
    high = end_index

    done = False
    while not done:
        print('\n  Current positions:',number_list)
        pivot = number_list[middle]
        print('  Current pivot value:',pivot)

        while number_list[low] < pivot:
            print('   {current_num} is less than {piv}'.format(current_num=number_list[low], piv=pivot))
            low += 1
            print('    New low value:',number_list[low],', Current high value:',number_list[high])

        while pivot < number_list[high]:
            print('   {current_num} is greater than {piv}'.format(current_num=number_list[high], piv=pivot))            
            high -= 1
            print('    New high value:',number_list[high],', Current low value:',number_list[low])

        if low >= high:
            print('  Partitioning Done')
            done = True

        else:
            print(' Finished adjusting low and high, swap time.')
            temp = number_list[low]
            temp2 = number_list[high]
            number_list[low] = temp2
            number_list[high] = temp
            print('   Swapping low:',temp,'and high:',temp2)
            print('    Increasing low and decresing high...')
            low += 1
            high -= 1

    print('  Returning index',high)
    return high

def quick_sort(number_list, start_index, end_index):
    if end_index <= start_index:
        print('Closing out this recursive call')
        return
    
    print('\nPartitioning the list')
    high = partition(number_list, start_index, end_index)

    #sorting left of the pivot
    print('\nSorting left segment with start index',start_index,'and end index',high)
    quick_sort(number_list, start_index, high)
   
    #sorting right of the pivot
    print('\nSorting right segment with start index',high+1,'and end index',end_index)
    quick_sort(number_list, high+1, end_index)

numbers = [12, 2, 33, 44, 1, 0, 11, 77, 76, 90, 3]
print('Unsorted:',numbers)

quick_sort(numbers, 0, len(numbers)-1)
print('\nSorted:',numbers)