import Loader
import string
import Text_Preprocess
from nltk.translate.bleu_score import corpus_bleu
from shutil import copyfile
import os


dataset_root_dir = '/home/duc/Documents/Text-and-Content-Based-Image-Retrieval-master/DataSets/'
code_root_dir = '/home/duc/Documents/Text-and-Content-Based-Image-Retrieval-master/'


input_file = open('/home/duc/Documents/Text-and-Content-Based-Image-Retrieval-master/uploads/description.txt', 'r')
predicted_description = input_file.readline()

table = str.maketrans('','',string.punctuation)

desc = predicted_description.split()
desc = [word.lower() for word in desc]
desc = [word.translate(table) for word in desc]
desc = [word for word in desc if len(word)>1]
desc = [word for word in desc if word.isalpha()]
predicted_description =  ' '.join(desc)

testFile = dataset_root_dir + 'Flickr_8k.testImages.txt'
testImagesLabel = Loader.load_set(testFile)
test_descriptions = Loader.load_clean_descriptions(dataset_root_dir + 'descriptions.txt', testImagesLabel)

matchedFiles = set()

for img in testImagesLabel:
    actual, predicted = list(), list()
    yhat = predicted_description.split()
    predicted.append(yhat)
    references = [d.split() for d in test_descriptions[img]]
    actual.append(references) 
    bleu_score_1 = corpus_bleu(actual, predicted, weights=(1, 0, 0, 0))
    bleu_score_2 = corpus_bleu(actual, predicted, weights=(0.5, 0.5, 0, 0))
    bleu_score_3 = corpus_bleu(actual, predicted, weights=(0.33, 0.33, 0.34, 0))
    bleu_score_4 = corpus_bleu(actual, predicted, weights=(0.25, 0.25, 0.25, 0.25))
    bleu_score = ( 4*bleu_score_4 + 3*bleu_score_3 + 2*bleu_score_2 + bleu_score_1 )/10
    #print(bleu_score)
    if bleu_score > 0.2:
        matchedFiles.add(img)
        continue

len(matchedFiles)

path = '/home/duc/Documents/Text-and-Content-Based-Image-Retrieval-master/DataSets/Flicker8k_Dataset/'

matched_img_file = open('/home/duc/Documents/Text-and-Content-Based-Image-Retrieval-master/uploads/matched_images.txt',"w")

folder = '/home/duc/Documents/Text-and-Content-Based-Image-Retrieval-master/uploads/matched-images/'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)

desc_text = Text_Preprocess.load_text(dataset_root_dir + 'Flickr8k.token.txt')
descriptions = Text_Preprocess.load_description(desc_text)

i=0
for img in matchedFiles:
    img_path = path + img + '.jpg'
    i += 1
    matched_img_file.write(descriptions[img][0]+ '\n')
    copyfile(img_path, folder + '/' + format(i,'03d') + '.jpg')
    
matchedFiles    
matched_img_file.close()
