import os

#==================================================================================================
#=== Globals ==================================================================================================
#==================================================================================================

source_folder = 'C:/Users/Mohamed/AppData/Roaming/Sublime Text 3/Packages/User/Snippets/python snippets'

def main():
    files = all_sub_files(source_folder)
    # print(*[x[:110] for x in files], sep='\n')
    # print(*[name_of(x) for x in files], sep='\n')

    



#==================================================================================================
#=== Functions ==================================================================================================
#==================================================================================================

def all_sub_files(path):
    inner_files = os.listdir(path)
    onlyfiles = [os.path.join(path, f) for f in inner_files if os.path.isfile(os.path.join(path, f))]
    for directory in [os.path.join(path,f) for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]:
        onlyfiles.extend(all_sub_files(directory))
    return onlyfiles

def name_of(path):
    return path.split('\\')[-1].split('.')[0]
#==================================================================================================
#==================================================================================================

if __name__ == '__main__':
    main()