

# KENNINGS MANAGER

####  WHAT THIS APP IS:
  - This app is a recommended companion to my Atom Editor reimagined snippets package.
  - It will take your input from a [kennings.cson](./doc/src/02_KenningsCsonFile.md) and make the [initialization](./doc/src/04_AtomEditorLibFiles), [keymap](./doc/srv/03_AtomEditorKeymapsFiles), and [master kennings.cson](./doc/src/05_MasterKenningsCsonFile.md) files.
  - This package does not intend to replace snippets, merely enhance the editor with a different kind of snippets.
  - No attempt is made to follow any style standard other than my own.
  - Because it does not follow any standard, and has hard coded directories matching my usage patterns, this is probably best used as an example or starting point for your own.

  1. Insert selected text into the final string inserted into the editor.
  2. Upper case the selected text before inserting it per grammar.
  3. Markdown/html linkify the selected text before inserting it into the editor per grammar.
  4. Lower case the linkified text before inserting it per grammar.
  5. Add tabs \(%T%\) to the inserted text.
     1. Hard tabs are currently poorly supported.
  6. Add Linux \(%N%\) or Windows \(%CR%\) newline characters.
  7. Add a " \(double quote\) \(%Q%\) to the inserted text.
  8. Insert repeated \(%R%°\<repeated characters\>≈\<number of repeats\>¨\).
  9. Insert pre formatted \(%TF%▷\<filename\>◁\) text from a source file.


##### Characters to use for sections of multi parameter commands.

CHR | NAME                  | DESCRIPTION
----|-----------------------|--------------------------------------------------
°   | degrees symbol        | Start of repeated text template.
≈   | approximate           | End of repeated text, start of number of repeats.
؟   | Reverse Question      | End of number of repeats.
▷   | Right Hollow Triangle | Start of filename to insert.
◁   | Left Hollow Triangle  | End of filename to insert.




###### end of README.md
