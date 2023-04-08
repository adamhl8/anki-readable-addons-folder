import json
from pathlib import Path

from aqt import mw

if mw is None:
    message = "mw is None"
    raise RuntimeError(message)

config = mw.addonManager.getConfig(__name__)
if config is None:
    message = "config is None"
    raise RuntimeError(message)

anki_addons_path = Path(mw.pm.addonFolder())
folder_name = config.get("folderName") or "Readable Addons"
readable_addons_path = (anki_addons_path.parent / folder_name).resolve()
readable_addons_path.mkdir(exist_ok=True)

installed_addons: set[str] = set()
for addon_dir in anki_addons_path.iterdir():
    if not addon_dir.is_dir():
        continue

    addon_name = addon_dir.name
    meta_json = addon_dir / "meta.json"
    if meta_json.is_file():
        with meta_json.open() as f:
            j = json.load(f)
            if "name" not in j:
                continue
            addon_name: str = j["name"]

    installed_addons.add(addon_name)
    readable_addon_dir = readable_addons_path / addon_name
    if not readable_addon_dir.exists():
        readable_addon_dir.symlink_to(addon_dir, target_is_directory=True)

addon_symlinks: set[str] = set()
for addon_symlink in readable_addons_path.iterdir():
    addon_symlinks.add(addon_symlink.name)
invalid_symlinks = addon_symlinks - installed_addons
for invalid_symlink in invalid_symlinks:
    (readable_addons_path / invalid_symlink).unlink()
