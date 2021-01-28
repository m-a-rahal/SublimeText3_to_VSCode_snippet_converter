import re
from functions import all_sub_files, name_of, show_files


#==================================================================================================
#=== Globals ==================================================================================================
#==================================================================================================

source_folder = 'C:/Users/Mohamed/AppData/Roaming/Sublime Text 3/Packages/User/Snippets/python snippets'
output_file = 'python_snippets.json'
ignored_files = []


def main():
    files = all_sub_files(source_folder)
    with open(output_file, 'w') as res:
        res.write('{\n')
        for f in files:
            snippet = Snippet()
            snippet.extract_data_from_snippet(f)
            # write snippets in a VSCode json file
            
            res.write(snippet.as_json())
        res.write('}\n')


#==================================================================================================
#=== Functions & Classes ==================================================================================================
#==================================================================================================

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

        # remove extras from the body (<![CDATA[...............]]>)
        self.body = self.body[9:-3]
        # normalization:
        # 1. replace all tabs with 4 spaces
        self.body.replace('\t', '    ')
        # trasnform into list of lines
        self.body = self.body.strip().split('\n')
        #print(len(self.body), *self.body,sep='\n')

    def as_json(self):
        lines = []
        lines.append(f'"{self.name}" :'+' {')
        lines.append(f'"prefix" : "{self.trigger}",')
        lines.append(f'"body" : [')
        for l in self.body:
            lines.append('\t'+f'"{l}",')
        lines.append(f'],')
        if self.description is not None:
            lines.append(f'"description" : "{self.description}"')
        lines.append('},\n')

        # at end, add to all lines a leading tab and a newline

        return ''.join(['\t'+line+'\n' for line in lines])

#==================================================================================================
#==================================================================================================

if __name__ == '__main__':
    main()