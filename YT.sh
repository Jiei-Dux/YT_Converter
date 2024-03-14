#! /bin/bash

#Distro=$(cat /etc/*release | grep NAME | head -n1 | cut -d '=' -f2 | tr -d \")
Distro=$(cat /etc/*release | grep ID | head -n1 | cut -d '=' -f2 | tr -d \")

if [[ $Distro == "Arch Linux" || $Distro == "EndeavourOS" ]]; then
	if pacman -Qs "yt-dlp" > /dev/null ; then
		printf "%s\nyt-dlp is installed..."
		printf "%s\nproceeding..."
		sleep 1
	else
		printf "%s\nyt-dlp is not installed... \nexiting...\n\n"
		sleep 2
		exit 1
	fi
#if [[ $Distro == "focal" ]]; then
#	if apt
fi

while true
do
	printf '\033\143'
	printf "%s\nChoose:\n 1:SFX\n 2:Music\n Q: Quit\n\n"
	read -p "Choice: " usrInput_Choice
	printf '\033\143'

	case $usrInput_Choice in
		1)
			printf "%sENTER 'B' to go back\n"
			read -p "Link: " usrInput_Link

			if [ "$usrInput_Link" == "b" ] || [ "$usrInput_Link" == "B" ]; then
				continue
			fi

			yt-dlp -P /home/*/Music/SFX -x $usrInput_Link --audio-format mp3
			read -p "Continue? (y/N): " usrInput_Choice

			case $usrInput_Choice in
				y|Y)
					printf "%s\nAight..."
					sleep 1
					;;
				n|N)
					exit 0
					;;
				*)
					exit 0
					;;
			esac
			;;
		2)
			printf "%sENTER 'B' to go back\n"
			read -p "Link: " usrInput_Link

			if [ "$usrInput_Link" == "b" ] || [ "$usrInput_Link" == "B" ]; then
				continue
			fi

			yt-dlp -P /home/*/Music/Library -x $usrInput_Link --audio-format mp3
			read -p "Continue? (y/N): " usrInput_Choice

			case $usrInput_Choice in
				y|Y)
					printf "%s\nAight..."
					sleep 1
					;;
				n|N)
					exit 0
					;;
				*)
					exit 0
					;;
			esac
			;;
		q|Q)
			exit 0
			;;
		*)
			printf "%s\n Bro... Input something...\n"
			exit 1
			;;
	esac
done
