import json


def convert_to_json(output_dict):
    with open("output.json", "w") as outfile:
        val = json.dumps(output_dict)
        outfile.write(val)
    return val