

from sys import argv as argv
import getopt


try:
  _opts_, _args_ = getopt.getopt(argv[1:], "o:h", ["help", "output"])
except getopt.GetoptError as e:
  print(f"""Error:
Something went wrong:
    {e}
""")


print(f"""
_opts_ {_opts_}
_args_ {_args_}
""")
#
