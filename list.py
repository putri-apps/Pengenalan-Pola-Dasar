# mengubah dari 1D menjadi matrik 2D
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
print(list1);

#menggabungkan
list1.extend(list2)
print(list1)

#mengambil nilai
print(list4[2])

#menyisipkan
list1.insert(1, "pear")
print(list1)

#menghapus
list1.remove("cherry")
print(list1)

#mengurutkan
list2.sort()
print(list2)