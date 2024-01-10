# Bane Of Wargs Map Editor

```bash
lolo@fedora ~ $ python map.yaml
████████████████████████████████████████████████████████████████████▀███████
█▄─▄─▀██▀▄─██▄─▀█▄─▄█▄─▄▄─███─▄▄─█▄─▄▄─███▄─█▀▀▀█─▄██▀▄─██▄─▄▄▀█─▄▄▄▄█─▄▄▄▄█
██─▄─▀██─▀─███─█▄▀─███─▄█▀███─██─██─▄██████─█─█─█─███─▀─███─▄─▄█─██▄─█▄▄▄▄─█
▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▀▀▄▄▄▄▀▄▄▄▀▀▀▀▀▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
Please enter the path to your yaml file: map.ya_
```

This repository is a work environment for developing [Bane Of Wargs](https://github.com/Dungeons-of-Kathallion/Bane-Of-Wargs) 'map.yaml's files.
It uses a python script to parse a [Libre Office Calc](https://www.libreoffice.org/discover/calc/) .ods file into a yaml file.

## How-To

```python
pip install -r requirements.txt
# next edit the .ods file how you want
python map.py
```

Check the [`docs/MAP_ODS.MD`](https://github.com/Dungeons-of-Kathallion/Bane-Of-Wargs-Map-Editor/blob/master/docs/MAP_ODS.md) documentation to know everything about how to edit that map.ods file.

## Python Module Requirements
The script has minimal module requirements, only two module is required by now for running the map.py script.
[PyYaml](https://pypi.org/project/PyYAML/), [pyexcel_ods](https://pypi.org/project/pyexcel-ods/).

---

_If you have ran the `pip install -r requirements.txt` command, you won't have to install all of theses modules since you already did._

## Contributing
All conributions like PR, issues that can go from bug reporting or feature request are all welcome!\n Just check the [CONTRIBUTING](https://github.com/Dungeons-of-Kathallion/Bane-Of-Wargs-Map-Editor/blob/master/.github/CONTRIBUTING.md) guidelines.

## Licensing
Bane Of Wargs Map Editor is a free, open source script. The source code and every file you will find on this repository is avaible under the GPL v3 license. All its work and artwork is all public domain. Feel free to fork, or copy the game source to make your own version of the engine.
