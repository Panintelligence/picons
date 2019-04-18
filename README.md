# ![PIcons Logo](changes/images/picons-logo-small.png) PIcons
This project has the source SVG for the icon fonts used in [Panintelligence](https://panintelligence.com).

# Usage
If you want to experiment, you can just use the url from `githack.com` which serves as an automatic CDN for github-hosted files:
```html
<link href="https://raw.githack.com/Panintelligence/picons/master/dist/css/picons-charts.css" rel="stylesheet">
```
In production, you should do the following:
1. Clone or download this repository
2. Copy `dist/css/picons-charts.css` into your css folder
3. Copy all the fonts inside `dist/fonts` to your fonts folder

If you look inside `picons-charts.css`, it expects the fonts to be one level above and inside `fonts`:
```css
@font-face {
    font-family: 'picons-charts';
    src:  url('../fonts/picons-charts.eot?u53g43');
    src:  url('../fonts/picons-charts.eot?u53g43#iefix') format('embedded-opentype'),
        url('../fonts/picons-charts.ttf?u53g43') format('truetype'),
        url('../fonts/picons-charts.woff?u53g43') format('woff'),
        url('../fonts/picons-charts.svg?u53g43#picons-charts') format('svg');
    font-weight: normal;
    font-style: normal;
}
```

Feel free to change these paths to whatever suits you.

# Developing and contributing

## Editing the fonts
Use any vector-based editor. I like to use [inkscape](https://inkscape.org/), but you can edit the fonts using [fontforge](https://fontforge.github.io/) too.

## Generating fonts
Generating the fonts requires the following:

* [fontforge](https://fontforge.github.io/)
* Python 3

To build all the fonts run:
```bash
./build.sh
```