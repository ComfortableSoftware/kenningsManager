

import argparse as AP

_parser_ = AP.ArgumentParser(add_help=True)

_args_ = ["-a", "-alt"]
_KWArgs_ = {
    "dest": "a",
    "help": "This is the first argument",
    "nargs": 2,
    "required": False,
    "type": str,
}
_parser_.add_argument(*_args_, **_KWArgs_)

_args_ = ["-b", "-bonus"]
_KWArgs_ = {
    "dest": "b",
    "help": "swallow 3",
    "nargs": 3,
    "required": False,
    "type": str,
}
_parser_.add_argument(*_args_, **_KWArgs_)


# Parse and print the results
_args_ = _parser_.parse_known_intermixed_args()

print(f"""_args_[0] {_args_[0]}""")
print(f"""_args_[0].a {_args_[0].a}""")
print(f"""_args_[0].b {_args_[0].b}""")

print(f"""_args_[1] {_args_[1]}""")
