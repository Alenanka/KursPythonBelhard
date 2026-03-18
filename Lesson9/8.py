'''
Дан список содержащий в себе различные типы данных, отфильтровать таким
образом, чтобы 
 - остались только строки.
 - остался только логический тип.
 
'''


start_list = [1, "h",  True, "rgg", False, 42, 55.6,"fff", 0, ""]

strings_only = list(filter(lambda x: isinstance(x, str), start_list))
print("Cтроки:", strings_only)

bools_only = list(filter(lambda x: isinstance(x, bool), start_list))
print("Логические :", bools_only)
