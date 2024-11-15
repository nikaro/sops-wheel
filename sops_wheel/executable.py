import os
import subprocess
import sys


ROOT_DIR = os.path.dirname(__file__)


def _program(name, args):
    bin_dir = ROOT_DIR if os.name == "nt" else os.path.join(ROOT_DIR, "bin")
    return subprocess.call([os.path.join(bin_dir, name)] + args, close_fds=False)


def call_sops(*args):
    suffix = ".exe" if os.name == "nt" else ""
    raise SystemExit(_program("node" + suffix, list(args)))


def sops():
    call_sops(*sys.argv[1:])
