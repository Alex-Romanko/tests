from working_with_gshits2 import insert_data


form_dict = {
    "abc": ['ab', 'bc', 'cd'],
    "def": ['de', 'ef', 'fg'],
    "acb": ['ab', 'ab', 'bc']
}

print(form_dict)

for i, v in form_dict.items():
    print(i)
    print(v)


samples_from_protocol = sorted(form_dict.keys())
print(samples_from_protocol)


sample_data = form_dict.get("abc")

print('===> sample_data:', sample_data)

for sample_name in samples_from_protocol:
    transitional_data_storrage = []
    transitional_data_storrage.append(sample_name)
    sample_data = form_dict.get(sample_name)
    transitional_data_storrage.extend(sample_data)
    insert_data = ''
    for number, value in enumerate(transitional_data_storrage):
        if number <= len(transitional_data_storrage)-2:
            insert_data = insert_data + value + ', '
        else:
            insert_data = insert_data + value
    print(insert_data)
