import json
import os
import re


def continuity_check(exons_list: list) -> bool:
    result_list = []
    for each_element in exons_list:
        value_list = re.findall(r'\b\d+\b', each_element)
        try:
            start = int(value_list[0])
            end = int(value_list[1])
        except IndexError:
            print("Missing data!")
            return False

        result_list.extend(list(range(start, end+1)))

    if len(result_list) == max(result_list):
        return True
    else:
        return False


json_file = input("Enter JSON filename: ")
if os.path.isfile(json_file) is False:
    print("File not found!")

else:
    with open(json_file) as handle:
        dict_dump = json.loads(handle.read())

    gene_list = dict_dump.keys()

    for each_gene in gene_list:
        print(f"Gene: {each_gene}")
        result = continuity_check((dict_dump[each_gene]))
        print(result)

