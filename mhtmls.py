import os
import re
import subprocess
from manage_dir import prepare_dir
from urllib.parse import urljoin, urlparse


def gen_command(print_to_mhtml_path, link):
    return '"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu ' \
           '--enable-logging --save-page-as-mhtml="{0}" {1}'.format(print_to_mhtml_path, link)


def gen_master_mhtml(link, output_dir_name):
    mhtml_filename = str("<" + str(link).replace("://", "_").replace("/", "_") + ">.mhtml")
    print_to_mhtml_path = os.path.join(os.getcwd(), output_dir_name, mhtml_filename)
    completed_process = subprocess.run(gen_command(print_to_mhtml_path, link), shell=True, check=True)
    print("** Generated MTHML: {} **".format(print_to_mhtml_path))
    return completed_process


def gen_link_mhtml(path_for_lnk_mhtml, link):
    mhtml_filename = str("<" + str(urljoin(link, urlparse(link).path)).replace("://", "_").replace("/", "_") + ">.mhtml")
    print_to_mhtml_path = os.path.join(path_for_lnk_mhtml, mhtml_filename)
    completed_process = subprocess.run(gen_command(print_to_mhtml_path, link), shell=True, check=True)
    print("** Generated MHTML: {} **".format(print_to_mhtml_path))
    return completed_process


# TODO: Solve HTTP 403 errors
def gen_mhtmls(lol, dol, output_dir_name):
    print("** Generating MHTMLs using list of URLs and dictionary of URLs **")
    prepare_dir(output_dir_name)
    for lnk in lol:
        print("** Generating MHTMLs for: {} **".format(lnk))
        gen_master_mhtml(lnk, output_dir_name)
        url_domain = re.search('https?://([A-Za-z_0-9.-]+).*', lnk).group(1)
        path_for_lnk_mhtml = os.path.join(os.getcwd(), output_dir_name, "<" + url_domain + ">")
        if not (os.path.isdir(path_for_lnk_mhtml)):
            os.mkdir(path_for_lnk_mhtml)
            print("** Created directory: {} **".format(path_for_lnk_mhtml))
        for link in dol[lnk]:
            # TODO: Check if MHTML already exists, if so give a name extension to the newest MHTML being saved
            gen_link_mhtml(path_for_lnk_mhtml, link)
    print()


def gen_only_home_mhtmls(lol, output_dir_name):
    print("** Generating home MTHMLs using list of URLs **")
    prepare_dir(output_dir_name)
    for lnk in lol:
        print("** Generating MHTML for: {} **".format(lnk))
        gen_master_mhtml(lnk, output_dir_name)
    print()
