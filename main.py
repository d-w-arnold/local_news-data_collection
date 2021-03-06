from links import read_list_of_links, gen_dict_of_links
from pdfs import gen_only_home_pdfs


def print_finished():
    print("** Finished **")


def main():
    list_of_links = read_list_of_links('links.txt')
    dict_of_links = gen_dict_of_links(list_of_links, "directory_of_links")
    gen_only_home_pdfs(list_of_links, "pdfs")
    print_finished()


if __name__ == '__main__':
    main()
