def print_dict(level, dictionary):
    for field in dictionary:
        if isinstance(dictionary[field], dict):
            print(f'{" "*4*level}{field}:')
            print_dict(level + 1, dictionary[field])
        elif isinstance(dictionary[field], list):
            print(f'{" "*4*level}{field} - lista:')
            field_list = dictionary[field]
            for index, item in enumerate(field_list):
                if len(field_list) > 1:
                    print(f'{" "*4*level}Element listy \'{field}\' nr {index+1}:')
                print_dict(level + 1, item)
        else:
            print(f'{" "*4*level}{field}: {dictionary[field]}')