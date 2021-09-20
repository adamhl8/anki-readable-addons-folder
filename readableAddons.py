import json
import os
import os.path
import sys

from aqt import mw
from anki.utils import isWin

from .config import getReadableAddonsFolder

originalFolder = mw.pm.addonFolder()
readableAddonsFolder = getReadableAddonsFolder()
if not os.path.exists(readableAddonsFolder):
    try:
        os.makedirs(readableAddonsFolder)
    except PermissionError:
        print(
            (
                f"""There is an error with the configuration of the addon "Readable Addons Folder". It is trying to create the folder {readableAddonsFolder}, but you don't have permission to create a folder there.""",
                sys.stderr,
            )
        )

installedAddonNames = set()
for fileName in os.listdir(originalFolder):
    originalAddonDir = os.path.join(originalFolder, fileName)
    if os.path.isdir(originalAddonDir):
        metaFile = os.path.join(originalAddonDir, "meta.json")
        if os.path.exists(metaFile):
            with open(metaFile, "r") as f:
                j = json.load(f)
                if "name" not in j:
                    continue
                name = j["name"]
        else:
            name = fileName
        installedAddonNames.add(name)
        newAddonDir = os.path.join(readableAddonsFolder, name)
        if not os.path.exists(newAddonDir):
            if isWin:
                os.system(r'mklink /J "{}" "{}"'.format(newAddonDir, originalAddonDir))
            else:
                os.symlink(originalAddonDir, newAddonDir)

invalidSymlinks = set(os.listdir(readableAddonsFolder)) - installedAddonNames
for invalidSymlinkName in invalidSymlinks:
    invalidSymlinkPath = os.path.join(readableAddonsFolder, invalidSymlinkName)
    os.remove(invalidSymlinkPath)
