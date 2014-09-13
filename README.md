# ghost-hugo

This script takes a `GhostData.json` file and converts it to individual
Markdown files for a [Hugo](http://hugo.spf13.com/) site.

My blog doesn't have categories or tags, and pretty much everything else is
vanilla, so this script will only pull over the relevant fields from the Ghost
export file. Also, my blog historically used WordPress-style permalinks
(`http://myblog.com/YYYY/MM/DD/slug/`), so this script adds a `url` parameter
to each post with that permalink.

## Execution

Put your `GhostData.json` file in the same directory as `ghost-hugo.py` and run
it:

    $ python ghost-hugo.py

This will create a directory called `output` that you can then move to your
Hugo `content` directory and rename to whatever you want.

## url.py

I've also included a script I used after the initial Ghost import. I had
forgotten the permalink and needed to add it to each file already generated.
This script provides a template if you need to perform a similar operation on
your own files.

