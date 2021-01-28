import re
from functions import all_sub_files, name_of


#==================================================================================================
#=== Globals ==================================================================================================
#==================================================================================================

source_folder = 'C:/Users/Mohamed/AppData/Roaming/Sublime Text 3/Packages/User/Snippets/python snippets'
output_file = 'results.py'
ignored_files = []

#==================================================================================================
#=== Functions & Classes ==================================================================================================
#==================================================================================================

def main():
    files = all_sub_files(source_folder)
    for f in files:
        snippet = Snippet().extract_data_from_snippet(f)





class Snippet():
    def __init__(self, name = '', body = '', descripion = '', trigger = '', scope = 'source.python'):
        self.name = name
        self.body = body
        self.descripion = descripion
        self.trigger = trigger

    def extract_data_from_snippet(self, snippet):
        with open(snippet, 'r') as f:
            snippet_text = f.read()
        self.name = name_of(snippet)
        '''takes SublimeText3 snippet text and extracts data from it'''
        pattern = r'''<snippet>\n<content>((?:.|\n)+?)</content>\n<tabTrigger>(.+?)</tabTrigger>\n<scope>(.+?)</scope>\n(?:<description>(.*?)</description>\n)?</snippet>'''
        res = re.search(pattern, snippet_text)
        if not res:
            print(f"can't match file '{self.name}', skipped")
            ignored_files.append(snippet)
            return

        # assign each one to it's value
        self.body = res.group(1)
        self.trigger = res.group(2)
        self.scope = res.group(3)
        self.description = res.group(4) if res.group(4) is not None and len(res.group(4)) > 0 else None





def show_files(files):
    print(*[x[:110] for x in files], sep='\n')
    print(*[name_of(x) for x in files], sep='\n')
    
        

#==================================================================================================
#==================================================================================================

if __name__ == '__main__':
    main()