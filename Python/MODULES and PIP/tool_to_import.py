import random


def dice_roll(maximum_dice_num):
    return random.randint(1, maximum_dice_num)


def get_file_extension(filename):
    file_types = {"exe": "Microsoft Executable", "dmg": "apple Disk iMaGe ", "pdf": "Portable Document Format"}
    extension = filename[filename.index(".") + 1:]
    filetype = file_types.get(str(extension), "Not a known extension")
    return filetype
