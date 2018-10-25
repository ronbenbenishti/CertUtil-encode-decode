import os, sys

def encode(filename, loops):
    num = 1
    original_filename = filename
    for i in range(loops):
        new_filename = '.'.join(filename.split('.')[:-1]) + '.cert' + str(num)
        os.system('certutil -f -encode ' + filename + ' ' + new_filename)
        if filename != original_filename:
            os.system('del ' + filename)
        filename = new_filename
        num += 1

def decode(filename, ext):
    original_filename = filename
    num = 1
    while True:
        new_filename = '.'.join(filename.split('.')[:-1]) + '.tmp' + str(num)
        os.system('certutil -f -decode ' + filename + ' ' + new_filename)
        if filename != original_filename:
            os.system('del ' + filename)
        filename = new_filename
        f = open(filename)
        check = f.readline()
        f.close()
        num += 1
        if 'BEGIN CERTIFICATE' not in check:
            strip_cert = '.'.join(filename.split('.')[:-1])
            final_file = ''.join(strip_cert.split('\\')[-1]) + '.' + ext
            os.system('rename ' + filename + ' ' + final_file)
            break

user_msg = r"""Syntax: python cert.py <MODE> <PATH> <PARAM1>

MODES: -en <path> <loops_count>
       -de <path> <original extension> (optional)

Example: 'python cert.py -en C:\users\Ron\Desktop\nc.exe 20'
         'python cert.py -de C:\users\Ron\Desktop\nc.cert20 exe'
"""

if len(sys.argv) <= 1:
    print user_msg
    x = raw_input("Please choose an option: \n'e' = Encode\n'd' = Decode\n'q' = Quit\n")
    if x == 'e' or x == 'E':
        path = raw_input("Full path: ")
        loops = input('enter loops count: ')
        encode(path,loops)
    elif x == 'd' or x == 'D':
        path = raw_input("Full path: ")
        ext = raw_input("File extension [Enter = exe]: ")
        if ext == '':
            ext = 'exe'
        decode(path, ext)
    elif x == 'q' or x == 'Q':
        print '>> Quitting...'
        quit()
    else:
        print '>> Error: Invalid key'

elif len(sys.argv) > 1:
    if os.path.isfile(sys.argv[2]):
        if sys.argv[1] == '-en':
            path = sys.argv[2]
            try:
                loops = int(sys.argv[3])
                encode(path,loops)
            except Exception as error:
                # print error   # debug level
                print '>> Error: Missing parameter (loops count)'
                print user_msg
        elif sys.argv[1] == '-de':
            path = sys.argv[2]
            try:
                if sys.argv[3]:
                    ext = sys.argv[3]
            except:
                ext = 'exe'
            decode(path, ext)
        else:
            print user_msg
    else:
        print '>> Error: Unknown file'

else:
    pass