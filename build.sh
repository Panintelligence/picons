#!/bin/bash

# ------------------------------------------
SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null 2>&1 && pwd )"
# ------------------------------------------

cd ${DIR}

mkdir -p "${DIR}/dist/"
rm -rf "${DIR}/dist"/*

mkdir -p "${DIR}/dist/fonts"
mkdir -p "${DIR}/dist/css"
mkdir -p "${DIR}/dist/example"

cd "${DIR}/src/svgs"
for filename in *.svg; do
    echo "Converting ${filename}..."
    "${DIR}"/convert.pe "$filename" "eot" > /dev/null 2>&1
    "${DIR}"/convert.pe "$filename" "ttf" > /dev/null 2>&1
    "${DIR}"/convert.pe "$filename" "woff" > /dev/null 2>&1
    "${DIR}"/convert.pe "$filename" "svg" > /dev/null 2>&1
    name=$(echo "$filename" | cut -f 1 -d '.')
    python "${DIR}/tocss.py" "$filename" > "${DIR}/dist/css/${name}.css"
done
python "${DIR}/generate_example.py" "${DIR}/src/svgs"/* > "${DIR}/dist/example/${name}.html"