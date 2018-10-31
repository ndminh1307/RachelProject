
#SETUP ON UNIX SYSTEM
#Upgrade system
sudo apt-get update
sudo apt-get upgrade

#Install python 3 env
sudo apt-get install python-dev python3-dev
sudo apt-get install build-essential
sudo apt-get install python3-pip
sudo apt-get install python3-tk
sudo apt-get install python3-pyaudio
sudo apt-get install libasound2-dev

#Install pip3 package
pip3 install numpy
pip3 install matplotlib
pip3 install pandas
pip3 install SpeechRecognition
pip3 install wikipedia
pip3 install gTTS
pip3 install mutagen
pip3 install pyqt5

#Install git
sudo apt-get install git
git config --global user.name "ndminh1307"
git config --global user.email "ndminh1307@gmail.com"

#Install music player
sudo apt-get install sox
sudo apt-get install sox libsox-fmt-all
