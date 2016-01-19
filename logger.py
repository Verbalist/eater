__author__ = 'verbalist'
import time
import os

class Log(object):

    debug = False

    def __init__(self, file_name, d_file='d.txt', e_file='e.txt', t_file='t.txt', path='', **kwargs):
        """
        :arg
        d simple log
        e error log
        t time.log
        """
        self.open_file('d_f', d_file, path)
        self.open_file('e_f', e_file, path)
        self.open_file('t_f', t_file, path)
        self.file_name = file_name
        for k, v in kwargs.items():
            setattr(self, k, v)


    def open_file(self, attr_name, file_name, path):
        try:
            setattr(self, attr_name, open(path + file_name, 'a'))
        except FileNotFoundError:
            if path:
                os.mkdir(path)
            else:
                os.mkdir('/'.join(file_name.split('/')[:-1]))
            setattr(self, attr_name, open(path + file_name, 'w'))

    def d(self, *args):
        self.file_log(self.d_f, args)

    def e(self, *args):
        self.file_log(self.e_f, args)

    def t(self, *args):
        self.file_log(self.t_f, args)

    def file_log(self, file_for_log, args):
        if self.debug:
            print(*args)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())), self.file_name + ":",
              *args,
              file=file_for_log)


    def timer_d(self, func):
        def on_call(*args, **kwargs):
            t = time.time()
            f = func(*args, **kwargs)
            if self.debug:
                print('.' + func.__name__, float(time.time() - t))
            self.t(func.__name__, float(time.time() - t))
            return f
        return on_call


if __name__ == '__main__':
    L = Log('logger', 'd.txt', 'e.txt', 't.txt', '/var/www/log/logger/', debug=True)
    t = time.time()
    L.d('its work')
    L.e('its don`t work')
    L.t(time.time() - t)