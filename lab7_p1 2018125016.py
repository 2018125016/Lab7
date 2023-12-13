import re

def find_functions_and_calls(file_path):
    func_decl_pattern = r'def\s+(\w+)\('
    func_call_pattern = r'\b(\w+)\('
    func_dict = {}
    line_num = 0
    with open(file_path, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            line_num += 1
            decl_match = re.search(func_decl_pattern, line)
            if decl_match:
                func_name = decl_match.group(1)
                func_dict[func_name] = {'declaration': line_num, 'calls': []}
            call_matches = re.finditer(func_call_pattern, line)
            for call in call_matches:
                func_name = call.group(1)
                if func_name in func_dict and line_num not in func_dict[func_name]['calls'] and line_num != func_dict[func_name]['declaration']:
                    func_dict[func_name]['calls'].append(line_num)
    return func_dict

def format_output(func_dict):
    output = []
    for func_name, details in func_dict.items():
        calls = [call for call in details['calls'] if call != details['declaration']]
        output.append(f"{func_name}: def in {details['declaration']}, calls in {sorted(calls)}")
    return '\n'.join(output)

file_path = 'input_7_1.txt'
functions_info = find_functions_and_calls(file_path)
print(format_output(functions_info))
