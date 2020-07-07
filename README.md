# local_news-data_collection

This is a Python web crawler for local news sites.

For each URL listed in `links.txt`, this program generates a PDF of the webpage visited and a list of links found on the webpage, as a TXT file.

(Python3)

```bash
pip3 install bs4
pip3 install requests
python3 main.py
```

Generated PDFs can be found in `/pdfs` and generated TXTs can be found in `/directory_of_links`. Any PDFs and TXTs in these directories will be deleted on successive runs of the Python program.
