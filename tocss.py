#!/usr/bin/python

import sys
import fontforge
import ntpath


def generate_header(font_family):
    return "@font-face {\n" + \
        "    font-family: '" + font_family + "';\n" + \
        "    src:  url('../fonts/" + font_family + ".eot?u53g43');\n" + \
        "    src:  url('../fonts/" + font_family + ".eot?u53g43#iefix') format('embedded-opentype'),\n" + \
        "        url('../fonts/" + font_family + ".ttf?u53g43') format('truetype'),\n" + \
        "        url('../fonts/" + font_family + ".woff?u53g43') format('woff'),\n" + \
        "        url('../fonts/" + font_family + ".svg?u53g43#" + font_family + "') format('svg');\n" + \
        "    font-weight: normal;\n" + \
        "    font-style: normal;\n" + \
        "}\n"


def generate_class_globals(font_family):
    return "[class^=\"" + font_family + "-\"], [class*=\" " + font_family + "-\"] {\n" + \
        "    /* use !important to prevent issues with browser extensions that change fonts */\n" + \
        "    font-family: '" + font_family + "' !important;\n" + \
        "    speak: none;\n" + \
        "    font-style: normal;\n" + \
        "    font-weight: normal;\n" + \
        "    font-variant: normal;\n" + \
        "    text-transform: none;\n" + \
        "    line-height: 1;\n" + \
        "    text-align: center;\n" + \
        "    /* Better Font Rendering =========== */\n" + \
        "    -webkit-font-smoothing: antialiased;\n" + \
        "    -moz-osx-font-smoothing: grayscale;\n" + \
        "}\n"

# See https://fontforge.github.io/python.html#Glyph


def generate_class_glyph(font_family, glyph):
    return "." + font_family + "-" + glyph.glyphname + ":before {\n" + \
        "    content: \"\\" + format(glyph.unicode, 'x') + "\";\n" + \
        "}\n"


def generate_css():
    f = fontforge.open(sys.argv[1])
    font_name = ntpath.basename(sys.argv[1]).split('.svg')[0]
    css = generate_header(font_name) +\
        "\n\n" +\
        generate_class_globals(font_name) + "\n"

    for i in f.selection.all():
        if f[i].glyphname != ".notdef":
            css = css + "\n" + generate_class_glyph(font_name, f[i])
    print(css)


generate_css()
