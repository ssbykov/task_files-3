from pathlib import Path

def txt_file_analysis():
    file_path = Path(__file__).parent.absolute()
    if list(file_path.glob('result.txt')):
        Path(str(file_path) + '/result.txt').unlink()
    text_files = file_path.glob('*.txt')
    common_txt_file_list = []
    txt_file_list = []
    for txt_file_path in text_files:
        with open(txt_file_path, 'r', encoding='UTF-8') as txt_file:
            txt_file_list = txt_file.readlines()
        common_txt_file_list.append([str(len(txt_file_list)), txt_file_path.name, txt_file_list])
    common_txt_file_list.sort()
    with open(str(file_path) + '/result.txt', 'w', encoding='UTF-8') as result:
        for file in common_txt_file_list:
            result.write(file[1] + '\n')
            result.write(file[0] + '\n')
            result.write(''.join(file[2]) + '\n')

txt_file_analysis()