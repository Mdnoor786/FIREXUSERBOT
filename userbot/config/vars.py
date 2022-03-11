# Configs imports from here

import os

ENV = bool(os.environ.get("ENV", False))

if not ENV and os.path.exists("exampleconfig.py") or ENV:
    pass

# FIREX
