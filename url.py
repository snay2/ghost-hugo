import json
from datetime import datetime
import os
import re

def main():
    rootdir = '/home/snay2/blog/content/archive'
    for folder, subs, files in os.walk(rootdir):
        for filename in files:
            lines = []
            slug = fulldate = ''
            print os.path.join(folder, filename)
            with open(os.path.join(folder, filename), 'r') as src:
                lines = src.readlines()
                print lines[2]
                slug = re.search('slug = "(.*)"\n', lines[2]).groups()[0]
                fulldate = re.search('date = "(.*)"\n', lines[3]).groups()[0]
            with open(os.path.join(folder, filename), 'w') as dest:
                created = datetime.strptime(fulldate, "%Y-%m-%dT%H:%M:%S.000Z")
                url = '/%d/%02d/%02d/%s' % (created.year, created.month, created.day, slug)
                dest.writelines(lines[:3])
                dest.write('url = "%s"\n' % url)
                dest.writelines(lines[3:])

if __name__=='__main__':
    main()

