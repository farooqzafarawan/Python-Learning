""" Class and its usage for 'ls -laR' created files 
    os.path (Common pathname manipulations)-like function interfaces are made as similar to standard as possible
"""
import re
import string


class lslaRfile:
    """Virtual directory, created by 'ls -laR>filename' 
    Takes such file and operates on it"""
    # line types:
    PATH, TOTAL, FILE, EMPTY, ERROR, EOF = 1, 2, 3, 4, 0, -1
    ERR_MAX = 10

    def __init__(self, file):
        self.repath = re.compile(":$")
        self.retotal = re.compile("total (\d+)")
        self.refile = re.compile(
            "(.{10})\s+(\d+)\s+(\S)+\s+(\S+)\s+(\d+) (\S+)\s+(\d+)\s+(\d\d):(\d\d) (\S.*)")
        self.refile2 = re.compile(
            "(.{10})\s+(\d+)\s+(\S)+\s+(\S+)\s+(\d+) (\S+)\s+(\d+)\s+(\d\d\d\d) (\S.*)")
        self.read(file)

    def read(self, filename):
        """read in ls-laR files, and create apropraiate data structure 
        filename - ls -laR file name"""
        self.f = open(filename, "rb")
        self.h = {}
        self.lines_cnt = 0
        err_cnt = 0
        err_lst = []
        path = ''
        total = 0
        files = []
        self.root_dir = None
        while True:
            linetype, info = self.readline()
            if linetype == lslaRfile.EOF:
                if path != '':
                    self.h[path] = files
                    path = ''
                    files = []
                break
            if linetype == lslaRfile.ERROR:
                err_cnt += 1
                if err_cnt <= lslaRfile.ERR_MAX:
                    err_lst.append(info)
                else:
                    break
            # populate tree (replaced with hash as prototype)
            if linetype == lslaRfile.PATH:
                path = info
                if not self.root_dir:
                    self.root_dir = info
            elif linetype == lslaRfile.TOTAL:
                total = info
            elif linetype == lslaRfile.FILE:
                files.append(info)
            elif linetype == lslaRfile.EMPTY:
                assert(path != '')
                self.h[path] = files
                # total - eto summa v Kb files.size
                path = ''
                files = []

            if self.lines_cnt % 10000 == 0:
                print(" %d-th line..." % self.lines_cnt)
        print("lslaRfile.read(): %s: %d lines found, %d errors." %
              (filename, self.lines_cnt, err_cnt))
        if len(err_lst) > 0:
            for l in err_lst:
                print("'%s'" % l)
        self.f.close()

    def remove_endline(self, lineN):
        if lineN[-2:] == '\r\n':
            lineN = lineN[:-2]
        elif lineN[-1] == '\n':
            lineN = lineN[:-1]
        return lineN

    def readline(self):
        """return (line_type, info)"""
        lineN = self.f.readline()
        if '' == lineN:
            return (lslaRfile.EOF, [])
        line = self.remove_endline(lineN)
        self.lines_cnt += 1

        if line == '':
            return (lslaRfile.EMPTY, None)
        m = self.retotal.match(line)
        if m:
            return (lslaRfile.TOTAL, int(m.group(1)))
        if line[-1] == ':':
            if line[:2] == './':
                line = line[2:]
            return (lslaRfile.PATH, line[:-1])
        m = self.refile.match(line)
        if m:
            return (lslaRfile.FILE, m.groups())
        m = self.refile2.match(line)
        if m:
            return (lslaRfile.FILE, m.groups())
        return (lslaRfile.ERROR, line)

    def dirsum(self, dir, opts):
        """dir - directory path in disk
        opts - options for printing size
        return string size of dir"""
        pass

    def ls(self, opts, dir):
        """list dir directory using opt options
        return string"""
        # for e in self.h:
        #	print "hash_key= ",e
        files = self.lso(dir)
        for f in files:
            assert(f[0], self.stat(dir, f[-1]))
            print(f[-1], " ", f[0])  # name, attrib

    def lso(self, dir):
        "list objects in dir directory"
        # simplify directory:
        if type(dir) != type(""):
            print(" method lso() Error: dir=", dir)
        if dir[:2] == './':
            dir = dir[2:]

        if not self.h.has_key(dir):
            print("key(dir) %s is not found in hash_table:\n" % dir)
            print("h=\n")
            for k in self.h:
                print(k)
            print("\n/h\n")
            # raise Exception, "No key '%s'" % dir
        # --if dir=='.': print "  lso' dir=", dir,"\n", self.h[dir]
        return self.h[dir]

    def stat(self, dir, name):
        "return string like 'drwxrwx--x' for dir:file"
        ls = self.lso(dir)
        for f in ls:
            if f[-1] == name:
                return f[0]
        return 'erro-r-r--'

    def is_dir2(self, dir, file):
        return self.stat(dir, file)[0] == 'd'

    def is_dir(self, path):
        if path == '.':
            return True
        dir, file = self.split(path)
        return self.is_dir2(dir, file)

    def join_path(self, dir, name):
        return dir+self.get_separator()+name

    def get_separator(self):
        "to read from file"
        return '/'

    def split(self, path):
        # print " --%s==\n" %(path)
        if path == '.':
            return ".", ""
        i = string.rfind(path, self.get_separator())
        if i == -1:
            return "", path
        dir = path[0:i]
        file = path[i+1:]
        return dir, file


"Testing functions"


def browse(lar):
    """keyboard-browse lar file
    lar - lslaR_file object"""
    lar.ls('.', {})
    # x=sys.stdin.read(1)


def test1():
    f = lslaRfile('zZash.txt')
    f.ls({}, '.')
    f.ls({}, 'z_lracucich_gluxner/hfelib_dll')
    # print "-"


def test2():
    file = 'ctdisk_laR.txt'
    f = lslaRfile(file)
    f.ls({}, '.')
    # test operations
    # browse(f)


def main():
    pass
    test1()
    # test2()


if __name__ == '__main__':
    main()
