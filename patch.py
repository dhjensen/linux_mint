import yaml

# Content to add in overrides
def add(content, name, items=[]):

  return_content = {name: content}

  for item in items:
    return_content[name].append(item)

  return return_content

def remove(target, remove_items):

  for item in remove_items:
    target.remove(item)

  return target

def create_filename(name):
  filename = 'mint20_override_' + name + '.yaml'
  return filename

def write_yaml_file(filename, output):
  with open(filename, 'w') as file:
    yaml.dump(output, file, explicit_start=True, explicit_end=True, sort_keys=False)

def main():
  # names of sections to work on.
  name_deb = 'deb'
  name_downloads = 'downloads'
  name_files = 'files'
  name_flatpak = 'flatpak'
  name_pip = 'pip'
  name_startup = 'startup'

  # Content to add
  add_deb = [
    'https://github.com/BoostIO/BoostNote.next/releases/download/v0.13.2/boost-note-linux.deb',
    'https://github.com/bitwarden/desktop/releases/download/v1.24.6/Bitwarden-1.24.6-amd64.deb',
    'https://download.teamviewer.com/download/linux/teamviewer_amd64.deb'
  ]
  add_downloads = [
    {'url': 'https://github.com/bitwarden/cli/releases/download/v1.13.3/bw-linux-1.13.3.zip', 'destination': 'bw', 'skip_tree': False}
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

  # Content to remove in overrides
  remove_startup = [
    {'filename': 'dropbox.desktop', 'source': './files/apps/dropbox/dropbox.desktop'},
    {'filename': 'synapse.desktop', 'source': './files/apps/synapse/synapse.desktop'},
    {'filename': 'DockX.desktop', 'source': './files/apps/dockbarx/DockX.desktop'}
  ]

  # Assign content we care about to variables
  with open('mint20.yaml') as file:
    content = yaml.load(file, Loader=yaml.FullLoader)
    deb = content['deb']
    downloads = content['downloads']
    files = content['files']
    flatpak = content['flatpak']
    pip = content['pip']
    startup = content['startup']

  # Remove startup content before creating output.
  remove(startup, remove_startup)

  output_deb = add(deb, name_deb, add_deb)
  output_downloads = add(downloads, name_downloads, add_downloads)
  output_files = add(files, name_files, add_files)
  output_flatpak = add(flatpak, name_flatpak, add_flatpak)
  output_pip = add(pip, name_pip, add_pip)
  output_startup = add(startup, name_startup)

  write_yaml_file(create_filename(name_deb), output_deb)
  write_yaml_file(create_filename(name_downloads), output_downloads)
  write_yaml_file(create_filename(name_files), output_files)
  write_yaml_file(create_filename(name_flatpak), output_flatpak)
  write_yaml_file(create_filename(name_pip), output_pip)
  write_yaml_file(create_filename(name_startup), output_startup)

if __name__ == "__main__":
    # execute only if run as a script
    main()
