def calkulate_structure_sum(args):
    global summa

    if isinstance(args,int):
        summa = summa + int(args)
        return

    if isinstance(args,str):
        summa = summa + len(args)
        return

    if isinstance(args,list):
        for i in range(len(args)):
            calkulate_structure_sum(args[i])

    if isinstance(args,dict):
        for key in args.keys():
            summa = summa + len(key)
        for values in args.values():
            summa = summa + int(values)

    if isinstance(args, tuple):
        for i in range(len(args)):
            calkulate_structure_sum(args[i])
    if isinstance(args,set):
        args = list(args)
        calkulate_structure_sum(args)
    return summa

data_structure = [
    [1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])
                ]
summa = int(0)
print(calkulate_structure_sum(data_structure))