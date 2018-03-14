import os
import re


regex_dict = {}


def process_lst(lines):
    header = []
    last_index = 0
    for l in lines:
        if l[1] == '#':
            break
        else:
            last_index += 1
            header.append(l)

    blocks = []
    temp_dict = {}
    lst_items = []
    block_found = False
    index = 0
    for line in lines:
        if len(line) < 1 or index < last_index:
            index += 1 
        elif line[0] == '#':
            if line[1] == '#':
                blocks.append(temp_dict)
                block_found = True
                block_name = re.search(regex_dict["block_name"], line).group(1)
                temp_dict = {"block_name": block_name}
            elif block_found:
                block_tags = re.findall(regex_dict["block_tags"], line)
                temp_dict["block_tags"] = [tag[1] for tag in block_tags]
                temp_dict["items"] = []
                block_found = False
            else:
                # add line to last item's "note" key, create if not found
                # if no items in block yet, add to block notes, create if needed
                ...
        else:
            split_line = line
            name = re.search(regex_dict["item_name"], lines[index])
            tags = re.findall(regex_dict["item_tags"], lines[index])
            if name:
                temp_dict["items"].append({"name": name.group(1), "tags": [tag[0] for tag in tags]})


def main():
    data_folder = "./data/pcgen/core_rulebookn"
    files = os.listdir(data_folder)
    lst_files = [x for x in files if os.path.splitext(x)[1] == ".lst"]
    print(lst_files)

    for file in lst_files:
        print(file)
        choice = input("Do you want to open this file?")
        if choice.lower() == 'y':
            with open(os.path.join(data_folder, file)) as f:
                lines = f.readlines()
            temp_dict = process_lst(lines)


if __name__ == '__main__':
    main()
