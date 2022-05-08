

#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of CF.setup.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


from setuptools import find_packages
from setuptools import setup


setup(
  author="GaelicGrime",
  author_email="will.angus.blaylock@gmail.com",
  license="GPLv3",
  name="kenningsManager",
  url="https://github.com/ComfortableSoftware/kenningsManager",
  version="0.2.0",
  summary="""
Processes all of the 'kennings.cson' files in my personal code repositories into keymaps, an initialization stub, and refactored/sorted/prettified source files where the originals were found.
""",
  package_dir={
      "kenningsManager": "kenningsManager"
  },
  package_data={
      "kenningsManager": [
          "../doc/*",
      ]
  },
  packages=["kenningsManager"],
  install_requires=[
      "CF",
  ],
  extras_require={
  },
  scripts=[
      "scripts/kenningsManager",
  ],
)
