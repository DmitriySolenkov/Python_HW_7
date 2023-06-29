from pathlib import Path
import os


def file_renamer(path, des_name, numbers, orig_ext, des_ext, name_range):
    count = 1
    if numbers > 1:
        for i in range(numbers-1):
            count = int(str(count)+"0")
    p = Path(path)
    for obj in p.iterdir():
        file_name = os.path.basename(obj).split(".")
        if len(file_name) > 1 and file_name[1] == orig_ext:
            goal_name = ""
            name = list(file_name[0])
            for i in range(name_range[0], name_range[1]):
                goal_name += name[i]
            goal_name += des_name+str(count)+"."+des_ext
            count += 1
            obj.rename(goal_name)


file_renamer(".", "Renamed_file", 3, "docx", "txt", (3, 6))
