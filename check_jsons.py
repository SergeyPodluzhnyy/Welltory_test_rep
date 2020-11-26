import json
import jsonschema
from jsonschema import validate
import glob

def get_json_from_file(fname):
    with open(fname, 'r') as file:
        schema = json.load(file)
    return schema

def validate_json(json_name, schema_name):
    json_data = get_json_from_file(json_name)
    json_schema = get_json_from_file(schema_name)

    try:
        validate(instance=json_data, schema=json_schema)
    except jsonschema.exceptions.ValidationError as err:
        return False, err

    message = "JSON is valid"
    return True, message

# validate it
json_dir = 'event'
schema_dir = 'schema'
with open("readme.md", "w") as file:
    for json_name in glob.glob(json_dir+'/*.json'):
        json_status = False
        for schema_name in glob.glob(schema_dir+'/*.schema'):
            file.write('JSON file '+ json_name)
            file.write('SCHEMA file '+ schema_name)
            valid_status, msg = validate_json(json_name, schema_name)
            file.write(str(msg))
    file.write('\n')
    file.write('\n')
    file.write('Задание должно составляться таким образом, чтобы исключить \n')
    file.write('всякое двоякое его истолкование, иначе время будет потрачено не на \n')
    file.write('решение задачи, а на решение вопроса - "что считать решением?" !!!! \n')
    file.write('С Уважением, Подлужный Сергей')