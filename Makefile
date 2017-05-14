default:
	sudo apt-get update
	sudo apt install -y python3-pip
	pip3 install --upgrade pip
	sudo pip3 install boto3
	sudo apt install -y awscli
	chmod +x minimoto_*
	chmod +x img2video
