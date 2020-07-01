from links import get_dict_of_links, read_list_of_links


def main():
    dict_of_links = get_dict_of_links(read_list_of_links('links.txt'))
    print()


if __name__ == '__main__':
    main()
