lst = [1, 2, 3, 4, 5, 6, 7, 8]
new_lst = [1, 2, 3, 4, 5, 6, 2, 6, 10]
def modifi_list (lst:list):
    a = []
    for i in lst:
        if i % 2 == 0:
            a.append(i//2)
    lst[:]=a
    pass
modifi_list(new_lst)
print(new_lst)

