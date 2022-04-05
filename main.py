import json
import pandas as pd
import os


def as_dict(out_data):
    return json.dumps(out_data.to_dict(orient='records'), indent=4)


def as_array(out_data):
    return json.dumps(list(cleaned_data.iloc[:, 0]), indent=4)


if __name__ == '__main__':
    file_name = input("Enter Input filename (default: 'values.csv')") or "values.csv"
    output_name = input("Enter Output filename (default: 'output.json')") or "output.json"
    output_type = input("What type of file would you like? dict, list").lower() or "list"
    data = pd.read_csv(os.path.join('input', file_name))
    cleaned_data = data.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    output_string = None

    if output_type == 'dict':
        output_string = as_dict(cleaned_data)
    else:
        output_string = as_array(cleaned_data)

    with open(os.path.join('output', output_name), 'w+') as file:
        file.writelines(output_string)