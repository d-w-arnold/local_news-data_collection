import os
import re
import shutil


def gen_command(print_to_pdf_path, link):
    return '"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu ' \
           '--enable-logging --print-to-pdf="{0}" {1}'.format(print_to_pdf_path, link)


def gen_master_pdf(link):
    pdf_filename = str("<" + str(link).replace("://", "_").replace("/", "_") + ">.pdf")
    print_to_pdf_path = os.path.join(os.getcwd(), "pdfs", pdf_filename)
    return os.system(gen_command(print_to_pdf_path, link))


def gen_link_pdf(path_for_lnk_pdfs, link):
    pdf_filename = str("<" + str(link).replace("://", "_").replace("/", "_") + ">.pdf")
    print_to_pdf_path = os.path.join(path_for_lnk_pdfs, pdf_filename)
    return os.system(gen_command(print_to_pdf_path, link))


def del_dir_contents(path_for_lnk_pdfs):
    for filename in os.listdir(path_for_lnk_pdfs):
        file_path = os.path.join(path_for_lnk_pdfs, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
            print("Emptied directory: {}".format(path_for_lnk_pdfs))
        except Exception as e:
            print("Failed to delete: {0} - Reason: {1}".format(file_path, e))


def gen_pdfs(lol, dol):
    for lnk in lol:
        gen_master_pdf(lnk)
        url_domain = re.search('https?://([A-Za-z_0-9.-]+).*', lnk).group(1)
        path_for_lnk_pdfs = os.path.join(os.getcwd(), "pdfs", url_domain)
        if os.path.isdir(path_for_lnk_pdfs):
            # Delete contents of directory
            del_dir_contents(path_for_lnk_pdfs)
        else:
            # Create directory
            os.mkdir(path_for_lnk_pdfs)
            print("Created directory: {}".format(path_for_lnk_pdfs))
        for link in dol[lnk]:
            gen_link_pdf(path_for_lnk_pdfs, link)
