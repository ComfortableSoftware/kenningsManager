

# KENNINGS MANAGER

##### FLY BY LEVEL GET STARTED GUIDE.
  - This app is the needed support utility for my [ATOM EDITOR](https://atom.io/) macro snippet mashup package "Kennings" which older members of my family used in place of the concept most Americans think of as snippets, little pieces of knowledge that make life easier in some way.
    - I have tried to use generic Linux directory names like `~` instead of `/home/user`
  - I have zero idea how to make this app usable on a modern Windows system, and I can probably work with you if you have an idea how to get around on your system.
  - This app is personalized to the absolute, probably much more useful if you fork it and change it to meet your needs than as it comes.
  - I make heavy use of my CF Python package
    - Especially my os wrapper and my SQLite wrapper.
  - Ken, kent, kenning, etc. are used heavily in some parts of Scotland as knowledge about, additions to understanding of, perception, etc.
    - Kennings are little scraps of information, snippets.
  - ##### BASIC INSTRUCTIONS
    1. Write your `kennings.cson`
       1. First location sourced `~/.atom/packages/kennings/kennings.cson`
       2. Second in the project's `.atom` directory.
       3. In the directory the file you are editing is in.
      - This process is additive and replacing only, if you set strings in `~/.atom/packages/kennings/kennings.cson` and don't change them later in the process, they stay.
      - All of the keyboard shortcuts need to be defined in advance and the files from this app melded into the appropriate source files in `~/.atom/packages/kennings/*`, this can not be done on the fly see [The Big Picture](#the-big-picture)
      - You can change strings to insert on the fly.
    2. Run this app in the directory the file resides in.
    3. Copy `~/.atom/packages/kennings/keymaps/\_\_PROJECT_NAME\_\_.cson` to the project directory and or edit it into the mail `kennings.cson` file.
      - I keep links in `~/.atom/packages/kennings/keymaps` and move the actual files to the .atom
    4. Edit `~/.atom/packages/kennings/keymaps/kennings.cson` to include the latest output of this package.
    5. Edit `~/.atom/packages/kennings/lib/kennings.coffee` replacing the current `initialize` section with the one from the output of this app in `~/.atom/packages/kennings/lib/init.coffee`
    6. Enjoy.


##### HOW TO CONSTRUCT THE STRINGS TO INSERT.
  -

# THE BIG PICTURE
  - Goes here.



###### end of README.md
