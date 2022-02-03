from pathlib import Path

def txt_file_analysis():
    file_path = Path(__file__).parent.absolute()
    if list(file_path.glob('result.txt')):
        Path(str(file_path) + '/result.txt').unlink()
    text_files = file_path.glob('*.txt')
    list_files = []
    list_txt_files = []
    for txt_file_path in text_files:
        with open(txt_file_path, 'r', encoding='UTF-8') as txt_file:
            list_txt_files = txt_file.readlines()
        list_files.append([str(len(list_txt_files)), txt_file_path.name, list_txt_files])
    list_files.sort()
    with open(str(file_path) + '/result.txt', 'w', encoding='UTF-8') as result:
        for file in list_files:
            result.write(file[1] + '\n')
            result.write(file[0] + '\n')
            result.write(''.join(file[2]) + '\n')

txt_file_analysis()