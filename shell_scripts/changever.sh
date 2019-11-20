#1/bin/sh

#PATTERN="template"

if [ $# -ne 2 ]
then
  echo "Error: $0: <from_version> <to_version> missing"
  exit 1
fi

echo "Info: Changing version from $1 to $2 in all template files"
for file in `ls *_template 2>/dev/null`
do
    sed -i 's/'"$1"'/'"$2"'/g' $file
done

