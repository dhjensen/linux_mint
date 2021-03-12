'''
This module create overrides yaml files
'''

import yaml

def add(content, name, items=None):
    '''
    Content to add in overrides
    '''

    return_content = {name: content}

    if items:
        for item in items:
            return_content[name].append(item)

    return return_content

def remove(target, remove_items):
    '''
    Remove unwanted items from the list
    '''
    for item in remove_items:
        target.remove(item)

    return target

def create_filename(name):
    '''
    Creates output filenames
    '''
    filename = 'mint20_override_' + name + '.yaml'
    return filename

def write_yaml_file(filename, output):
    '''
    Write yaml content to disk
    '''
    with open(filename, 'w') as file:
        yaml.dump(output, file, explicit_start=True, explicit_end=True, sort_keys=False)

def main():
    '''
    I'm main :)
    '''
    # names of sections to work on.
    name_deb = 'deb'
    name_downloads = 'downloads'
    name_files = 'files'
    name_flatpak = 'flatpak'
    name_pip = 'pip'
    name_startup = 'startup'

    # Content to add
    # pylint: disable=line-too-long
    add_deb = [
        'https://github.com/BoostIO/BoostNote.next/releases/download/v0.14.1/boost-note-linux.deb',
        'https://github.com/bitwarden/desktop/releases/download/v1.24.6/Bitwarden-1.24.6-amd64.deb',
        'https://download.teamviewer.com/download/linux/teamviewer_amd64.deb'
    ]
    add_downloads = [
        {
            'url': 'https://github.com/bitwarden/cli/releases/download/v1.15.0/bw-linux-1.15.0.zip',
            'destination': 'bw',
            'skip_tree': False
        }
    ]
    add_files = [
        {
        'url': 'https://github.com/ytmdesktop/ytmdesktop/releases/download/v1.12.1/YouTube.Music.Desktop.App-1.12.1.AppImage',
        'destination': 'youtubemusic',
        'desktop_file': './files/apps/youtubemusic/youtubemusic.desktop'
        },
        {
        'url': 'https://developers.yubico.com/yubikey-manager-qt/Releases/yubikey-manager-qt-1.1.5-linux.AppImage',
        'destination': 'yubikeymanager',
        'desktop_file': './files/apps/yubikeymanager/yubikeymanager.desktop'
        }
    ]
    add_flatpak = [
        {'name': 'https://flathub.org/repo/appstream/org.telegram.desktop.flatpakref'},
        {'name': 'https://flathub.org/repo/appstream/org.signal.Signal.flatpakref'},
        {'name': 'https://flathub.org/repo/appstream/us.zoom.Zoom.flatpakref'}
    ]
    add_pip = [
        'pylint'
    ]
    # pylint: enable=line-too-long

    # Content to remove in overrides
    remove_startup = [
        {'filename': 'dropbox.desktop', 'source': './files/apps/dropbox/dropbox.desktop'},
        {'filename': 'synapse.desktop', 'source': './files/apps/synapse/synapse.desktop'},
        {'filename': 'DockX.desktop', 'source': './files/apps/dockbarx/DockX.desktop'}
    ]

    # Assign content we care about to variables
    with open('mint20.yaml') as file:
        content = yaml.load(file, Loader=yaml.FullLoader)

    # Remove startup content before creating output.
    remove(content['startup'], remove_startup)

    write_yaml_file(create_filename(name_deb),
        add(content['deb'], name_deb, add_deb)
    )
    write_yaml_file(create_filename(name_downloads),
        add(content['downloads'], name_downloads, add_downloads)
    )
    write_yaml_file(create_filename(name_files),
        add(content['files'], name_files, add_files)
    )
    write_yaml_file(create_filename(name_flatpak),
        add(content['flatpak'], name_flatpak, add_flatpak)
    )
    write_yaml_file(create_filename(name_pip),
        add(content['pip'], name_pip, add_pip)
    )
    write_yaml_file(create_filename(name_startup),
        add(content['startup'], name_startup)
    )

if __name__ == "__main__":
    # execute only if run as a script
    main()
