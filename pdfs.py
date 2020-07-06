import os
import re
import subprocess
from manage_dir import prepare_dir
from urllib.parse import urljoin, urlparse


def gen_command(print_to_pdf_path, link):
    return '"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu ' \
           '--enable-logging --print-to-pdf="{0}" {1}'.format(print_to_pdf_path, link)


def gen_master_pdf(link):
    pdf_filename = str("<" + str(link).replace("://", "_").replace("/", "_") + ">.pdf")
    print_to_pdf_path = os.path.join(os.getcwd(), "pdfs", pdf_filename)
    completed_process = subprocess.run(gen_command(print_to_pdf_path, link), shell=True, check=True)
    print("** Generated PDF: {} **".format(print_to_pdf_path))
    return completed_process


def gen_link_pdf(path_for_lnk_pdfs, link):
    pdf_filename = str("<" + str(urljoin(link, urlparse(link).path)).replace("://", "_").replace("/", "_") + ">.pdf")
    print_to_pdf_path = os.path.join(path_for_lnk_pdfs, pdf_filename)
    completed_process = subprocess.run(gen_command(print_to_pdf_path, link), shell=True, check=True)
    print("** Generated PDF: {} **".format(print_to_pdf_path))
    return completed_process


# TODO: Solve HTTP 403 errors for both gen_pdfs() and gen_only_home_pdfs()
def gen_pdfs(lol, dol, output_dir_name):
    print("** Generating PDFs using list of URLs and dictionary of URLs **")
    prepare_dir(output_dir_name)
    for lnk in lol:
        print("** Generating PDFs for: {} **".format(lnk))
        gen_master_pdf(lnk)
        url_domain = re.search('https?://([A-Za-z_0-9.-]+).*', lnk).group(1)
        path_for_lnk_pdfs = os.path.join(os.getcwd(), "pdfs", "<" + url_domain + ">")
        if not (os.path.isdir(path_for_lnk_pdfs)):
            os.mkdir(path_for_lnk_pdfs)
            print("** Created directory: {} **".format(path_for_lnk_pdfs))
        for link in dol[lnk]:
            # TODO: Check if PDF already exists, if so give a name extension to the newest PDF being saved
            gen_link_pdf(path_for_lnk_pdfs, link)
    print()


def gen_only_home_pdfs(lol, output_dir_name):
    print("** Generating home PDFs using list of URLs **")
    prepare_dir(output_dir_name)
    for lnk in lol:
        print("** Generating PDF for: {} **".format(lnk))
        gen_master_pdf(lnk)
    print()
