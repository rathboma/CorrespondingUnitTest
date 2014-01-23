#
# Opens the corresponding unit test of the file being viewed.
#
# Author: Daniel Imhoff
#

import os, errno
import sublime, sublime_plugin

class CorrespondingunittestOpenCommand(sublime_plugin.WindowCommand):
    def __init__(self, window):
        super().__init__(window)
        self.tests_path = '/tests/php'

    def run(self, **args):
        project_path = self.window.project_data()['folders'][0]['path']
        file_path = self.window.active_view().file_name()
        if file_path.startswith(project_path):
            test_path = project_path + self.tests_path + file_path[len(project_path):-4] + 'Test.php'
            try:
                test_dir_path = os.path.dirname(test_path)
                os.makedirs(test_dir_path)
            except OSError as exc:
                if exc.errno == errno.EEXIST and os.path.isdir(test_dir_path):
                    pass
                else: raise
            self.window.open_file(test_path)
