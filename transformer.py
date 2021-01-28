import re
from functions import all_sub_files, name_of

#==================================================================================================
#=== Globals ==================================================================================================
#==================================================================================================

source_folder = 'C:/Users/Mohamed/AppData/Roaming/Sublime Text 3/Packages/User/Snippets/python snippets'

def main():
    files = all_sub_files(source_folder)
    # print(*[x[:110] for x in files], sep='\n')
    # print(*[name_of(x) for x in files], sep='\n')
    with open(files[0], 'r') as f:
        snippet = Snippet().extract_data_from_snippet(f.read())


#==================================================================================================
#=== Functions & Classes ==================================================================================================
#==================================================================================================

class Snippet():
    def __init__(self, name = '', body = '', descripion = '', trigger = '', scope = 'source.python'):
        self.name = name
        self.body = body
        self.descripion = descripion
        self.trigger = trigger

    def extract_data_from_snippet(self, snippet_text):
        '''takes SublimeText3 snippet text and extracts data from it'''
        pattern = r'''<snippet>\n<content>((?:.|\n)+?)</content>\n<tabTrigger>(.+?)</tabTrigger>\n<scope>(.+?)</scope>\n(?:<description>(.*?)</description>)?\n</snippet>'''
        res = re.search(pattern, snippet_text)
        if res:
            print(res.group(0))
            print(00000)
        else:
            print(11111)




        

#==================================================================================================
#==================================================================================================

if __name__ == '__main__':
    main()