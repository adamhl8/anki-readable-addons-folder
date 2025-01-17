# anki-readable-addons-folder

By default, the Anki addons folder stores each installed addon by its AnkiWeb addon id. This makes it very difficult to tell which folder corresponds with a given addon.

This addon creates a folder next to the original addons folder which contains readable symlinks to each installed addon. These symlinks are named after each addon's actual name, making it easy to navigate to the desired addon folder.

## Usage

The folder and symlinks are created upon starting Anki. If a new addon is installed, the new symlink will be created once Anki is restarted. Old/invalid symlinks are automatically removed.

## Configuration

### `folderName`

- The name of the folder which will contain the readable addon folders.

## Credits

This addon is directly based on Arthur-Milchior's [anki-readable-addon-folders](https://github.com/Arthur-Milchior/anki-readable-addon-folders).

This also incorporates fixes written by [jakublevy](https://github.com/jakublevy): [[Feature] Windows support, remove symlinks of uninstalled add-ons](https://github.com/Arthur-Milchior/anki-readable-addon-folders/pull/4)
