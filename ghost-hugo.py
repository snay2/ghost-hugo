import os
import json
from datetime import datetime

def main():
    # Read the Ghost export file
    f = open('GhostData.json', 'r')
    all_posts = json.load(f)['data']['posts']
    f.close()

    for post in all_posts:
        # Create or use a folder for the date
        created = datetime.strptime(post['created_at'], "%Y-%m-%dT%H:%M:%S.000Z")
        if not os.path.exists('./output/%d/%02d/%02d' % (created.year, created.month, created.day)):
            os.makedirs('./output/%d/%02d/%02d' % (created.year, created.month, created.day))

        # Create the Markdown file
        pf = open('./output/%d/%02d/%02d/%s.md' % (created.year, created.month, created.day, post['slug']), 'w')

        # Format the permalink
        post['url'] = '/%d/%02d/%02d/%s' % (created.year, created.month, created.day, post['slug'])

        # Front matter
        pf.write('+++\n')
        pf.write('title = "%s"\n'.encode('utf8') % post['title'].replace('"', '\\"'))
        pf.write('slug = "%s"\n' % post['slug'])
        pf.write('date = "%s"\n' % post['created_at'])
        pf.write('url = "%s"\n' % post['url'])
        if (post['status'] == 'draft'):
            pf.write('draft = true\n')
        pf.write('+++\n\n')

        # Post body
        pf.write(post['markdown'].encode('utf8'))

        # Close the Markdown file
        pf.close()

if __name__=='__main__':
    main()
