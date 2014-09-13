# ghost-hugo

This script takes a `GhostData.json` file and converts it to individual
Markdown files for a [Hugo](http://hugo.spf13.com/) site.

My blog doesn't have categories or tags, and pretty much everything else is
vanilla, so this script will only pull over the relevant fields from the Ghost
export file. Feel free to modify it to meet your needs. Also, my site has
historically used WordPress-style permalinks
(`http://myblog.com/YYYY/MM/DD/slug/`), so this script adds a `url` parameter
to each with that permalink.

## Execution

Put your `GhostData.json` file in the same directory as `convert.py` and run
it:

    $ python convert.py

This will create a directory called `output` that you can then move to your
Hugo `content` directory and rename to whatever you want.

