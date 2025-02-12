def quicksort(_list):
    list = _list
    index_pivot = len(list) // 2

    for index, value in enumerate(list):

        ##Verifing left values
        if(list[index_pivot] < value and index_pivot > index):
            aux = list[index]
            del list[index]
            list.append(aux)
            index_pivot -= 1

        ##Verifing right values
        elif(list[index_pivot] > value and index_pivot < index):
            aux = list[index]
            del list[index]
            list.insert(0, aux)
            index_pivot += 1
    
    print(list)

def main():
    quicksort([3, 6, 1, 2, 5, 9, 7, 10, 4])

main()