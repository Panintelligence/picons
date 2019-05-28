#!/usr/bin/python

import sys
import fontforge
import ntpath


def generate_header(font_family):
    return "    <link href=\"../css/" + font_family + ".css\" rel=\"stylesheet\">\n" +\
        "    <style>\n" +\
        "        [class^=\"" + font_family + "-\"], [class*=\" " + font_family + "-\"] {\n" +\
        "            font-size:5em;\n" +\
        "        }\n" +\
        "        .container {\n" +\
        "            width:652px;\n" +\
        "            margin:auto;\n" +\
        "        }\n" +\
        "        .glyph-box {\n" +\
        "            display:inline-block;\n" +\
        "            margin:10px;\n" +\
        "            width:140px;\n" +\
        "            text-align: center;\n" +\
        "            color:#777777;\n" +\
        "        }\n" +\
        "        .glyph-box:hover {\n" +\
        "            color:black;\n" +\
        "        }\n" +\
        "        .glyph-name {\n" +\
        "            font-family: 'Monospace';\n" +\
        "        }\n" +\
        "    </style>"


def generate_headers(font_families):
    header_content = ""
    for font_family in font_families:
        header_content += generate_header(font_family["name"]) + "\n"
    return "<head>\n" + header_content + "</head>"


def generate_glyph_box(font_family, glyph, indent):
    # See https://fontforge.github.io/python.html#Glyph
    classname = font_family + "-" + glyph.glyphname
    return indent + "<div class=\"glyph-box\">\n" +\
        indent + "    <div><i class=\"" + classname + "\"></i></div>\n" +\
        indent + "    <div class=\"glyph-name\">" + classname + "</div>\n" +\
        indent + "</div>\n"


def generate_body(font_family, fontfile):
    html = "<div class=\"container\">\n" +\
        "    <h1>"+font_family+"</h1>\n" +\
        "    <div>\n"

    for i in fontfile.selection.all():
        if fontfile[i].glyphname != ".notdef":
            html = html + \
                generate_glyph_box(font_family, fontfile[i], "        ")

    return html + "    </div>\n" +\
        "</div>"


def generate_bodies(font_families):
    body_content = []
    for font_family in font_families:
        body_content.append(generate_body(font_family["name"], font_family["file"]))
    return "<body>\n" + "\n\n<hr/>\n\n".join(body_content) + "</body>"


def fonts(files):
    all_fonts = []
    for font_file in files:
        if ".svg" in font_file:
            f = fontforge.open(font_file)
            all_fonts.append({
                "file": f,
                "name": ntpath.basename(font_file).split('.svg')[0]
            })
    return all_fonts


def generate_html_example():
    all_fonts = fonts(sys.argv)
    html = "<html>\n" + generate_headers(all_fonts) +\
        "\n" +\
        generate_bodies(all_fonts) + "\n</html>"

    print(html)


generate_html_example()
