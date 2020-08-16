# !/bin/bash
# author: dead1
# quick script to list bash colour codes
# and allow for quick copy
# inspired by: 
# https://www.unixtutorial.org/how-to-show-colour-numbers-in-unix-terminal/

i = 0
for COLOR in {1..255}; do
	echo -en "\e[38;5;${COLOR}m"
	echo -n "[38;5;${COLOR}m	"
	i=$((i+1))
	if [ $i -gt 4 ]
	then
		echo -e ""
		i=$((0))
	fi
done

echo
