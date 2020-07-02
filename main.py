from links import read_list_of_links, gen_dict_of_links
from pdfs import gen_pdfs


def main():
    list_of_links = read_list_of_links('links.txt')
    dict_of_links = gen_dict_of_links(list_of_links)
    gen_pdfs(list_of_links, dict_of_links)
    print()
    print("** Finished **")
    print()


if __name__ == '__main__':
    main()
