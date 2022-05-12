

from CF.SUBM_D import _01_OPTIONS as CF_OPT


CF_OPT.addAParser()


_args_ = ["-b", "-bonus"]
_KWArgs_ = {
    "dest": "b",
    "help": "swallow 3",
    "nargs": "?",
    "required": False,
    "type": str,
}
CF_OPT.addAnArg(*_args_, **_KWArgs_)


_args_ = ["-a", "-alt"]
_KWArgs_ = {
    "dest": "a",
    "help": "This is the first argument",
    "nargs": "?",
    "required": False,
    "type": str,
}
CF_OPT.addAnArg(*_args_, **_KWArgs_)


CF_OPT.parseKnownIntermixedArgs()


print(f"""
V.CF_OPT.ARGS[0] {CF_OPT.V.ARGS[0]}
  V.CF_OPT.ARGS[0].a {CF_OPT.V.ARGS[0].a}
  V.CF_OPT.ARGS[0].b {CF_OPT.V.ARGS[0].b}

V.CF_OPT.ARGS[1] {CF_OPT.V.ARGS[1]}
""")
