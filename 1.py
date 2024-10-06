
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]


odd_index_items = [l1[i] for i in range(1, len(l1), 2)]


even_index_items = [l2[i] for i in range(0, len(l2), 2)]


combined_list = odd_index_items + even_index_items

print(combined_list)
