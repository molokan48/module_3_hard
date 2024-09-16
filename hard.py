def calkulate_structure_sum(args):
    result = int(0)
    def calkulate_structure(args):
        nonlocal result
        if isinstance(args,int):
            result = result + int(args)
            return
        if isinstance(args,str):
            result = result + len(args)
            return
        if isinstance(args,list):
            for i in args:
                calkulate_structure(i)
        if isinstance(args,dict):
            for key in args.keys():
                calkulate_structure(key)
            for values in args.values():
                calkulate_structure(values)
        if isinstance(args, tuple):
            for i in args:
                calkulate_structure(i)
        if isinstance(args,set):
            i = list(args)
            calkulate_structure(i)
        return result
    return calkulate_structure(args)


data_structure = [
    [1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])
                ]

result = calkulate_structure_sum(data_structure)
print(result)
