import sublime, sublime_plugin

class AddPythonDocstringsCommand(sublime_plugin.TextCommand):

    DEF_KEYWORD = 'def'
    DEF_PATTERN = '%s\s+' % DEF_KEYWORD

    def _find_function_region(self, start):
        return self.view.find(self.DEF_PATTERN, start)

    def insert_docstrings(self, edit):
        start = 0
        region = self._find_function_region(start)
        while region:
            line = self.view.line(region)
            line_str = self.view.substr(line)
            indent = '\n\t%s' % line_str[0:line_str.find(self.DEF_KEYWORD)]
            line_tokens = line_str.split()
            if line_tokens[0] == self.DEF_KEYWORD:
                function_name = line_tokens[1][0:line_tokens[1].find('(')].strip()
                docstring = '%s""" TODO: write documentation for %s.%s"""' % (indent, function_name, indent * 2)
                self.view.insert(edit, line.end(), docstring)
            start = region.end()
            region = self._find_function_region(start)

    def run(self, edit):
        self.insert_docstrings(edit)