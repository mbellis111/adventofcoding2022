
TYPE_FILE = 'file'
TYPE_DIR = 'dir'
TOTAL_SIZE = 70000000
UPDATE_SIZE = 30000000


def main():
    # https://adventofcode.com/2022/day/7
    print("Starting...")

    with open("input.txt", 'r') as infile:
        lines = infile.readlines()

    # create the dir tree structure
    root = create_structure(lines)
    # print(root)

    # populate the sizes for the directories
    used_space = calc_dir_size(root)
    print(used_space)

    # find out space needed
    space_needed = UPDATE_SIZE - (TOTAL_SIZE - used_space)
    print(space_needed)

    # find the smallest directory that is at least space_needed
    smallest_dir = find_smallest_dir(root, space_needed, root)
    print(smallest_dir)
    print(smallest_dir["size"])

    print("Done!")


def find_smallest_dir(root, size_cutoff, curr_smallest):
    if root["size"] >= size_cutoff:
        if root["size"] <= curr_smallest["size"]:
            curr_smallest = root
    for sub_dir in root["dirs"]:
        smallest_sub = find_smallest_dir(sub_dir, size_cutoff, curr_smallest)
        if smallest_sub["size"] <= curr_smallest["size"]:
            curr_smallest = smallest_sub

    return curr_smallest


def calc_dir_size(root):
    # to calculate the size of the dir
    # add up all the file sizes + all the directory sizes
    file_sizes = sum([file["size"] for file in root["files"]])
    for sub_dir in root["dirs"]:
        calc_dir_size(sub_dir)
    dir_sizes = sum([file["size"] for file in root["dirs"]])
    root["size"] = file_sizes + dir_sizes
    return root["size"]


def create_child(name, node_type, size=0):
    return {
        "name": name,
        "type": node_type,
        "parent": None,
        "files": [],
        "dirs": [],
        "size": size
    }


def get_child_dir(parent, dir_name):
    for sub_dir in parent["dirs"]:
        if sub_dir["name"] == dir_name:
            return sub_dir
    return None


def add_child(parent, child):
    child["parent"] = parent
    if child["type"] == TYPE_DIR:
        parent["dirs"].append(child)
    elif child["type"]  == TYPE_FILE:
        parent["files"].append(child)


def create_structure(lines):
    root = create_child("/", TYPE_DIR)
    current_node = root

    for line in lines[1:]:
        line = line.strip()

        # we can ignore any $ ls commands
        if line == "$ ls":
            continue

        # creating children from the ls command
        if not line.startswith("$"):
            left, right = line.split(" ")

            if left == "dir":
                # a directory
                child = create_child(right, TYPE_DIR)
                add_child(current_node, child)
            else:
                # a file
                child = create_child(left, TYPE_FILE, int(left))
                add_child(current_node, child)
        elif line.startswith("$ cd"):
            # cd can only go one level in or up, to keep it easy
            _, _, name = line.split(" ")
            if name == "..":
                current_node = current_node["parent"]
            else:
                current_node = get_child_dir(current_node, name)
    return root


if __name__ == '__main__':
    main()
