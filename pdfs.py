import os
import re
import shutil
import subprocess
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


def del_dir_contents(path):
    print("** Deleting files/directories in: {} **".format(path))
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
            print("** Deleted file: {} **".format(file_path))
        except Exception as e:
            print("** Failed to delete ** : {0} - Reason: {1}".format(file_path, e))


def prepare_pdfs_dir():
    pdfs_path = os.path.join(os.getcwd(), "pdfs")
    if os.path.isdir(pdfs_path):
        del_dir_contents(pdfs_path)
    else:
        os.mkdir(pdfs_path)


# TODO: Solve HTTP 403 errors for both gen_pdfs() and gen_only_home_pdfs()
def gen_pdfs(lol, dol):
    print("** Generating PDFs using list of URLs and dictionary of URLs **")
    prepare_pdfs_dir()
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


def gen_only_home_pdfs(lol):
    print("** Generating home PDFs using list of URLs **")
    prepare_pdfs_dir()
    for lnk in lol:
        print("** Generating PDF for: {} **".format(lnk))
        gen_master_pdf(lnk)
