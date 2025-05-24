rm -f dogs-vs-cats.zip
rm -f train.zip
rm -f test1.zip
rm -rf cats_vs_dogs
rm -f sampleSubmission.csv
kaggle c download -c dogs-vs-cats
unzip dogs-vs-cats.zip
python split_data.py
