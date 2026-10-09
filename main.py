from pathlib import Path

from railgo.parser.entry import *

Path("./export").mkdir(parents=True, exist_ok=True)
resetWorks()
launchMainPipe()
