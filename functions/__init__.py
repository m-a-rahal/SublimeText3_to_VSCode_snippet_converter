import os

def all_sub_files(path):
    inner_files = os.listdir(path)
    onlyfiles = [os.path.join(path, f) for f in inner_files if os.path.isfile(os.path.join(path, f))]
    for directory in [os.path.join(path,f) for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]:
        onlyfiles.extend(all_sub_files(directory))
    return onlyfiles

def name_of(path):
    return path.split('\\')[-1].split('.')[0]


def show_files(files):
    print(*[x[:110] for x in files], sep='\n')
    print(*[name_of(x) for x in files], sep='\n')

def write_footer(file):
    file.write('// SublimeText3 snippets added above ===============================================\n')
    file.write('//==================================================================================\n')

def write_header(file):
    file.write('//==================================================================================\n')
    file.write('// SublimeText3 snippets added above ===============================================\n')