import json

def pretty_print_json_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            input_json = file.read()
            parsed_json = json.loads(input_json)

        formatted_json = json.dumps(parsed_json, indent=2, sort_keys=True)
        return formatted_json

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None

file_path = 'input.json'
formatted_output = pretty_print_json_from_file(file_path)

if formatted_output:
    print("Formatted JSON:")
    print(formatted_output)