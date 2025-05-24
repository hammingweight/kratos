rm -f CDLA-Permissive-2.0.pdf
rm -f kagglecatsanddogs_5340.zip
rm -rf PetImages
rm -f 'readme[1].txt'

wget https://download.microsoft.com/download/3/e/1/3e1c3f21-ecdb-4869-8368-6deba77b919f/kagglecatsanddogs_5340.zip
unzip kagglecatsanddogs_5340.zip
python split_data.py
