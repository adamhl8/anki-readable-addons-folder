import os.path

from aqt import mw


def getReadableAddonsFolder():
    userOption = mw.addonManager.getConfig(__name__)
    parentFolder = userOption.get("parentFolder")
    folderName = userOption.get("folderName")
    if not parentFolder:
        mw.pm.addonFolder()  # ensure that base is set.
        parentFolder = mw.pm.base
    if not folderName:
        folderName = "readableAddons"
    return os.path.join(parentFolder, folderName)
