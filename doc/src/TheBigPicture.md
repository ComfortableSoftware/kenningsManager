

# THE BIG PICTURE

<span>
This is a little more indepth than the README and links to the documentation for each item.
</span>

  - This utility adds one or all [kennings.cson](./02_KenningsCsonFile.md) files in a configured directory to the [MASTER DATABASE](./01_MasterDatabase.md) in the users config directory.

  - ##### SINGLE [KENNINGS.CSON](./02_KenningsCsonFile.md) FILE.
    1. Open a terminal.
    2. Change to the directory where the [kennings.cson](./02_KenningsCsonFile.md) you want to add is.
    3. Run this app `kenningsManager`.
    4. Edit in changes to the [Keymaps Files](./03_AtomEditorKeymapsFiles.md).
    5. Edit in changes to the [Lib Files](./04_AtomEditorLibFiles).
    6. Edit in changes to the master [kennings.cson](./05_MasterKenningsCsonFile.md) file.

  - ##### ALL [KENNINGS.CSON](./02_KenningsCsonFile.md) FILES IN A CONFIGURED DIRECTORY.
    1. Open a terminal.
    2. Run this app `kenningsManager -all`.
    3. Edit in changes to the [Keymaps Files](./03_AtomEditorKeymapsFiles.md).
    4. Edit in changes to the [Lib Files](./04_AtomEditorLibFiles).
    5. Edit in changes to the master [kennings.cson](./05_MasterKenningsCsonFile.md) file.
    6. Edit in changes to individual [kennings.cson](./02_KenningsCsonFile.md) files as needed.

  - ##### ALL [KENNINGS.CSON](./02_KenningsCsonFile.md) FILES IN AN ARBITRARY DIRECTORY TREE.
    1. Open a terminal.
    2. Run this app `kenningsManager -all -dir=<rootOfTree>`.
    3. Edit in changes to the [Keymaps Files](./03_AtomEditorKeymapsFiles.md).
    4. Edit in changes to the [Lib Files](./04_AtomEditorLibFiles).
    5. Edit in changes to the master [kennings.cson](./05_MasterKenningsCsonFile.md) file.
    6. Edit in changes to individual [kennings.cson](./02_KenningsCsonFile.md) files as needed.

###### End of TheBigPicture.md
