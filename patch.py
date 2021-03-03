import yaml

# TODO: Read new content we care about and assign it to variables
with open('mint20.yaml') as file:
  #content = yaml.load(file, Loader=yaml.FullLoader)
  content = yaml.load(file, Loader=yaml.FullLoader)
  #print(content['deb'])

# TODO: Define content to add in script

# TODO: Define content to remove / blacklist

# TODO: Create the new override files