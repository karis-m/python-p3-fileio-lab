def write_file(file_name, file_content):
    with open(file_name, mode='w', encoding='utf-8') as log_file:log_file.write(file_content)

def append_file(file_name, append_content):
    with open(file_name, mode='a', encoding='utf-8') as log_file:log_file.write(append_content)

def read_file(file_name):
    text_file = open(file_name, encoding='utf-8')
    print(f"\n{text_file.read()}")

write_file("lib/log_file.txt","Log 1: 5 bananas added")
append_file("lib/log_file.txt","Log 2: 3 bananas subtracted")
read_file("lib/log_file.txt")