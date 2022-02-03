from pathlib import Path

def txt_file_analysis():
    file_path = Path(__file__).parent.absolute()
    file_list_name = ['1.txt', '2.txt', '3.txt']
    list_files = []
    list_txt_files = []
    for file_name in file_list_name:
        with open(str(file_path) + '/' + file_name, 'r', encoding='UTF-8') as txt_file:
            list_txt_files = txt_file.readlines()
        list_files.append([str(len(list_txt_files)), file_name, list_txt_files])
    list_files.sort()
    with open(str(file_path) + '/result.txt', 'w', encoding='UTF-8') as result:
        for file in list_files:
            result.write(file[1] + '\n')
            result.write(file[0] + '\n')
            result.write(''.join(file[2]) + '\n')

txt_file_analysis()