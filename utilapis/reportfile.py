import os
import time


class ReportFile(object):
    report_file_module = '.html'
    key_worsd = 'test_result-'
    cur_time = time.strftime("%Y%m%d%H%M%S", time.localtime())

    default_filename = ''.join((key_worsd, cur_time, report_file_module))
    report_file_abspath = os.path.join(os.getcwd(), default_filename)

    # def __init__(self):

    def set_report_filename(self, name=''):
        if name:
            self.default_filename = ''.join((name, self.default_filename))
        return self.default_filename

    def get_report_abspath(self):
        return self.report_file_abspath

    def report_file_abspath(self, filename=""):
        if filename:
            self.key_worsd = filename
        return self.report_file_abspath


Class_info = ReportFile
print(ReportFile().set_report_filename('Api'))
print(ReportFile().set_report_filename())
print(ReportFile().default_filename)
print(ReportFile().report_file_abspath.__repr__())
print(Class_info().get_report_abspath())
print(ReportFile().report_file_abspath())
