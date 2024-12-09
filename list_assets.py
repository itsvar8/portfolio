import os

_renders = list()
for file in os.listdir(os.path.join(os.getcwd(), "assets", "renders")):
    if os.path.splitext(file)[-1] == "":
        continue
    _renders.append(
        {
            "img": os.path.join("renders", file),
            "thumb": os.path.join("renders", "thumbs", file),
        }
    )

# print(_renders)


_icons = dict()
for root, dirs, files in os.walk(os.path.join(os.getcwd(), "assets", "software_icons"), topdown=False):
    for icon in sorted(files, reverse=True):
        _icons[icon.split(".")[0].capitalize()] = os.path.relpath(os.path.join(root, icon), "assets")

print(_icons)
