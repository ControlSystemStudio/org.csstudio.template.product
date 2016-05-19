#!/bin/bash
#
# author : Jeong Han Lee
# email  : jeonghan.lee@gmail.com
#
# This script is only valid for the first time execution.
# If one wants to revert all changes by this script,
# please run bash scripts/checkout.sh
#

set -u

#this_script_name=`basename $0`


echo "What is Your CS-Studio Product Name?";

#
# http://stackoverflow.com/questions/4316730/linux-scripting-hiding-user-input-on-terminal
# 

while IFS= read -r -s -n1 char; do
  [[ -z $char ]] && { printf '\n'; break; } # ENTER pressed; output \n and break.
  if [[ $char == $'\x7f' ]]; then # backspace was pressed
      # Remove last char from output variable.
      [[ -n $searchToReplace ]] && searchToReplace=${searchToReplace%?}
      # Erase '*' to the left.
      printf '\b \b' 
  else
    # Add typed char to output variable.
    searchToReplace+=$char
    # Print '*' in its stead.
    printf ${char}
  fi
done


#echo $searchToReplace
upc_searchToReplace=${searchToReplace^}
#echo $upc_searchToReplace


dir_name=`find  -type d -name '*template*' | head -n1`
file_name=`find  -type f -name '*template*' | head -n1`

new_dir_name=`echo ${dir_name} | sed -e "s/template/${searchToReplace}/g"`
new_file_name=`echo ${file_name} | sed -e "s/template/${searchToReplace}/g"`

mv  $dir_name  $new_dir_name
mv -T $file_name $new_file_name

grep --exclude={*.py,*.md,*.target,*.sh} -rl "template" * | xargs sed -i "s/template/${searchToReplace}/g"
grep --exclude={*.py,*.md,*.target,*.sh} -rl "Template" * | xargs sed -i "s/Template/${upc_searchToReplace}/g"

mvn clean verify

exit
