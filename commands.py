#
# Opens the corresponding unit test of the file being viewed.
#
# Author: Daniel Imhoff
#

import os
import sublime
import sublime_plugin


class CorrespondingunittestOpenCommand(sublime_plugin.WindowCommand):
    def __init__(self, window):
        super().__init__(window)
        self.settings = sublime.load_settings("CorrespondingUnitTest.sublime-settings")
        self.tests_path = self.settings.get("tests_base", "tests/php")

    def run(self, **args):
        project_path = self.window.project_data()['folders'][0]['path']
        file_path = self.window.active_view().file_name()

        if not file_path.startswith(project_path):
            print("file {f} not in project path {p}".format(file_path, project_path))
            return

        file_excluding_project = file_path.replace(project_path + "/", "")
        test_path_one = os.path.join(project_path, self.tests_path, file_excluding_project[:-4] + "Test.php")
        test_path_two = os.path.join(project_path, self.tests_path, file_excluding_project[:-4] + "_Test.php")

        test_path = test_path_one
        if os.path.exists(test_path_two) and not os.path.exists(test_path_one):
            test_path = test_path_two

        test_dir_path = os.path.dirname(test_path)
        if os.path.exists(test_dir_path):
            pass
        else:
            os.makedirs(test_dir_path)
        self.window.open_file(test_path)
