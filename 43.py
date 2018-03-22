# -*- coding: utf-8 -*-

"""

filename: coding_training ex 43
date: 2018-03-22
purpose: website create

input : site name, site author

make index.html file that contains <title> tag and <meta> tag

"""
import os

def main():
    input_site_name = raw_input("Site name: ")
    input_author = raw_input("Author: ")
    input_bool_java = raw_input("Do you want a folder for JavaScript? ")
    input_bool_CSS = raw_input("Do you want a folder for CSS? ")

    if input_bool_java == 'y':
        input_bool_java = True
    else:
        input_bool_java = False

    if input_bool_CSS == 'y':
        input_bool_CSS = True
    else:
        input_bool_CSS = False

    os.mkdir("./" + input_author)
    print "Created ./{}".format(input_author)

    if input_bool_java:
        os.mkdir("./" + input_author + "/js/")
        print "Created ./{}/js/".format(input_author)

    if input_bool_CSS:
        os.mkdir("./" + input_author + "/css/")
        print "Created ./{}/css/".format(input_author)

    with open("./{}/index.html".format(input_author), "w") as f:
        html_content = """
            <!DOCTYPE html>
            <html>

            <head>
             <title>{}</title>
             <meta name="author" content="{}" />
            </head>
            </html>
        """.format(input_site_name, input_author)
        f.write(html_content)
    return


if __name__ == "__main__":
    main()