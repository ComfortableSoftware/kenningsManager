

from CF.SUBM_D import _01_OPTIONS as CF_OPT


CF_OPT.addAParser()


_args_ = ["-a", "-all"]
_KWArgs_ = {
    "dest": "a",
    "help": "Do all [-a '<bool>'] true/fase yes/no",
    "nargs": 1,
    "required": False,
    "type": str,
}
CF_OPT.addAnArg(*_args_, **_KWArgs_)


_args_ = ["-d", "-dir"]
_KWArgs_ = {
    "dest": "d",
    "help": "Root directory to start searching recursively in.",
    "nargs": 1,
    "required": False,
    "type": str,
}
CF_OPT.addAnArg(*_args_, **_KWArgs_)


CF_OPT.parseKnownIntermixedArgs()


print(f"""
V.CF_OPT.ARGS[0] {CF_OPT.V.ARGS[0]}
  V.CF_OPT.ARGS[0].a {CF_OPT.V.ARGS[0].a}
  V.CF_OPT.ARGS[0].d {CF_OPT.V.ARGS[0].d}

V.CF_OPT.ARGS[1] {CF_OPT.V.ARGS[1]}
""")
