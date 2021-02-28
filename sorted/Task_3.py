def create_list_from_file1(file_name, file_name2, file_name3):
    with open(file_name) as fr1, open(file_name2) as fr2, open(file_name3) as fr3:

        lines_list1 = fr1.read().splitlines()
        lines_list1.insert(0, str(len(lines_list1)))
        lines_list1.insert(0, file_name)
        lines_list2 = fr2.read().splitlines()
        lines_list2.insert(0, str(len(lines_list2)))
        lines_list2.insert(0, file_name2)
        lines_list3 = fr3.read().splitlines()
        lines_list3.insert(0, str(len(lines_list3)))
        lines_list3.insert(0, file_name3)
        res_list = [lines_list1, lines_list2, lines_list3]
        res_list.sort(key=len)
    return res_list
create_list_from_file1('1.txt', '2.txt', '3.txt')

def write_file_from_list(file_name):
    list = create_list_from_file1('1.txt', '2.txt', '3.txt')
    with open(file_name, 'w') as f:
        for lines in list:
            for el in lines:
                f.write(f'{el}\n')
    return

write_file_from_list('res.txt')