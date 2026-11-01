"""Copy generated files, using independent copy-on-write clones on macOS."""
import shutil
import subprocess
import sys


def copy_asset(source, destination):
    if sys.platform == "darwin":
        result = subprocess.run(
            ["/bin/cp", "-cp", str(source), str(destination)],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
        if result.returncode == 0:
            return str(destination)
    return shutil.copy2(source, destination)
