import os
import argparse

parser = argparse.ArgumentParser(description='Delete large files recursively.')
parser.add_argument('--target-dir', help='The target directory', default='.')
parser.add_argument('--min-size', help='The minimum size of files to be deleted.', type=int, default=1024*1024)
args = parser.parse_args()

for root, dirs, filenames in os.walk(args.target_dir):
    for name in filenames:
        path = os.path.join(root, name)
        if os.access(path, os.R_OK | os.W_OK):
            file_stat = os.stat(path)
            if file_stat.st_size >= args.min_size:
                print 'would you like to delete \'%s\'? (Yes/no)' %path
                answer = raw_input()
                if answer == 'Yes':
                    os.remove(path)
        else:
            print 'Access denied to file \'%s\'.' %path