import urllib.request

DEFAULT_URL = "https://www.sap.com/belgique/index.html"

def read_replace_save(url):
    fp = urllib.request.urlopen(url)
    my_bytes = fp.read()
    my_str = my_bytes.decode("utf8")
    fp.close()
    new_str = my_str.replace("SAP", "Odoo")
    with open("odoo.html", "w") as html_file:
        html_file.write(new_str)

read_replace_save(DEFAULT_URL)
