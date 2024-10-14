def compare_list(l1):
    if (len(l1) != 0):
        for i in l1:
            j = i.split("_")
            list2.append(j[0])

        for i in range(len(list2) - 1):
            if (list2[i] == list2[i + 1]):
                print(f"Consecutive occurrence found: {list2[i]} at indices {i} and {i + 1}")
    else:
        print("list is empty")


list1 = ["V1_abcd", "V2_cejn", "V300_dnmewx", "V300_cenjc", "V301_ceiknce"]
list2 = [];
compare_list(list1)
