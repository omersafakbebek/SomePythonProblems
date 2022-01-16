def my_permute(green_lst,red_lst):
    if (len(red_lst)+len(green_lst)==0):
        return
    if (len(red_lst)==0):
        print(green_lst)
    for i in range(len(red_lst)):
        green_lst.append(red_lst[i])
        my_permute(green_lst,red_lst[:i]+red_lst[i+1:])
        green_lst.pop()
my_permute([],[1,2,3])