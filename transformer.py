import re
from functions import all_sub_files, name_of, show_files, write_footer, write_header


#==================================================================================================
#=== Globals ==================================================================================================
#==================================================================================================

source_folders = [
    'C:/Users/Mohamed/AppData/Roaming/Sublime Text 3/Packages/User/Snippets/python snippets',
    #'C:/Users/Mohamed/AppData/Roaming/Sublime Text 3/Packages/Python/Snippets'
]
output_file = 'python_snippets.json'
success = []
ignored_files = []


def main():
    files = []
    for path in source_folders:
        files += (all_sub_files(path))
    with open(output_file, 'w') as res:
        write_header(res)
        for f in files:
            snippet = Snippet()
            if snippet.extract_data_from_snippet(f):
                # write snippets in a VSCode json file
                res.write(snippet.as_json())
                success.append(name_of(f))
            
        write_footer(res)

    # success rate
    print('\n\n'+'-'*100+f'\nsuccessfully trasnformed {len(success)} files ({int(1000*len(success) / (len(success)+len(ignored_files)))/10}%)\n')
    print('trasnformed files:', *success, sep = '\n- ')


#==================================================================================================
#=== Functions & Classes ==================================================================================================
#==================================================================================================

class Snippet():
    def __init__(self, name = '', body = '', description = '', trigger = '', scope = 'source.python'):
        self.name = name
        self.body = body
        self.description = description
        self.trigger = trigger

    def extract_data_from_snippet(self, snippet):
        with open(snippet, 'r') as f:
            snippet_text = f.read()
        self.name = name_of(snippet)
        '''takes SublimeText3 snippet text and extracts data from it'''
        pattern = r'''<snippet>
\s*<content>((?:.|\n)+?)</content>
\s*<tabTrigger>(.+?)</tabTrigger>
\s*<scope>(.+?)</scope>
(?:\s*<description>(.*?)</description>\n)?</snippet>'''
        res = re.search(pattern, snippet_text)
        if not res:
            print(f"can't match file '{self.name}', skipped")
            ignored_files.append(snippet)
            return False
        

        # assign each one to it's value
        desc = res.group(4)

        self.body = res.group(1)
        self.trigger = res.group(2)
        self.scope = res.group(3)
        self.description = desc if desc is not None and len(desc.strip()) > 0 else None 

        # remove extras from the body (<![CDATA[...............]]>)
        self.body = self.body[9:-3]
        
        # normalization:
        # 1. replace all tabs with 4 spaces
        self.body = self.body.replace('\t', '    ')
        # 2. replace " with \"
        self.body = self.body.replace('"', '\\"')

        # trasnform into list of lines
        self.body = self.body.strip().split('\n')
        #print(len(self.body), *self.body,sep='\n')
        return True

    def as_json(self):
        lines = []
        lines.append(f'"{self.name}" :'+' {')
        lines.append(f'\t"prefix" : "{self.trigger}",')
        lines.append(f'\t"body" : [')
        for l in self.body:
            lines.append('\t\t'+f'"{l}",')
        lines.append(f'\t],')
        if self.description is not None:
            lines.append(f'\t"description" : "{self.description}"')
        lines.append('},\n\n')

        # at end, add to all lines a leading tab and a newline

        return '\n'.join(lines)

#==================================================================================================
#==================================================================================================

if __name__ == '__main__':
    main()