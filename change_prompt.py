import sys
import random
import string
import getopt
import pandas as pd
import spacy
import pyinflect

#This file really needs some cleaning up but maybe I'll do it another time

def changePrompt(argv):
    arg_prefix = ""
    arg_suffix = ""
    arg_help = "arguments:\n{0} -p <prefix> -s <suffix>".format(argv[0]) + "\nIf using special characters, put them in quotation marks."
    
    try:
        opts, args = getopt.getopt(argv[1:], "hp:s:", ["help", "prefix=", "suffix="])
    except:
        print(arg_help)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg_help)  # print the help message
            sys.exit(2)
        elif opt in ("-p", "--prefix"):
            arg_prefix = arg
        elif opt in ("-s", "--suffix"):
            arg_suffix = arg
    #above adapted from https://opensourceoptions.com/blog/how-to-pass-arguments-to-a-python-script-from-the-command-line/

    df = pd.read_csv("./dataset/epic-kitchens/epic-kitchens-100-annotations-master/retrieval_annotations/4P.csv")
    df_s = pd.read_csv("./dataset/epic-kitchens/epic-kitchens-100-annotations-master/retrieval_annotations/4P_s.csv")
    #df = pd.read_csv("./dataset/epic-kitchens/epic-kitchens-100-annotations-master/retrieval_annotations/4P_VBZ.csv")
    #df_s = pd.read_csv("./dataset/epic-kitchens/epic-kitchens-100-annotations-master/retrieval_annotations/4P_VBZ_s.csv")

    #for i in range(0, len(df['narration'])):
        #print(i, flush=True)
    #    df.loc[i, 'narration'] = changeVerbs(df.loc[i, 'narration'])

    df['narration'] = arg_prefix + ' ' + df['narration'] + ' ' + arg_suffix
    #for i in range(0, len(df['narration'])):
    #    df.loc[i, 'narration'] = get_random_string(random.randint(5,10)) + ' ' + get_random_string(random.randint(5,10)) + ' ' + get_random_string(random.randint(5,10))
    df.to_csv("./dataset/epic-kitchens/epic-kitchens-100-annotations-master/retrieval_annotations/EPIC_100_retrieval_test.csv", index=False)

    #for i in range(0, len(df_s['narration'])):
    #    df_s.loc[i, 'narration'] = changeVerbs(df_s.loc[i, 'narration'])

    df_s['narration'] = arg_prefix + ' ' + df_s['narration'] + ' ' + arg_suffix
    #for i in range(0, len(df_s['narration'])):
    #    df_s.loc[i, 'narration'] = get_random_string(random.randint(5,10)) + ' ' + get_random_string(random.randint(5,10)) + ' ' + get_random_string(random.randint(5,10))
    df_s.to_csv("./dataset/epic-kitchens/epic-kitchens-100-annotations-master/retrieval_annotations/EPIC_100_retrieval_test_sentence.csv", index=False)

#from https://pynative.com/python-generate-random-string/
def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    #print("Random string of length", length, "is:", result_str)
    return result_str

def changeVerbs(prompt):

    nlp = spacy.load("en_core_web_trf")

    #text = "drain broccoli"
    doc = nlp(prompt)

    #for i in range(len(doc)):
        #token = doc[i]
        #print(token.tag_)
        #print([(w.text, w.pos_) for w in doc])
        #if token.tag_ in ['VB', 'VBP', 'VBD']:
            #print(token.text, token.lemma_, token.pos_, token.tag_) 
            #prompt = prompt.replace(token.text, token._.inflect("VBZ"))
    #print(prompt)
    token = doc[0]
    prompt = prompt.replace(token.text, token._.inflect("VBZ"))

    return prompt


if __name__ == "__main__":
    changePrompt(sys.argv)