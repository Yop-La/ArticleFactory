import shortcodes
import markovify
import random
import glob


# choose a template randomly
paths = glob.glob("../template/*.template")
path = random.choice(paths)

print(path)


# read template
with open(path, 'r') as file:
    html = file.read()


# train model
with open("../corpus.txt") as f:
    text = f.read()

# Build the model.
text = text.strip('\n')
text_model = markovify.Text(text)


# function to generate phrase
def get_phrase(nb_car):
    if nb_car < 30:
        phrase = get_phrase(50)
        words = phrase.split()
        return(words[0] + ' ' + words[1])
    while True:
        phrase = text_model.make_short_sentence(nb_car)
        if phrase is not None:
            return(phrase)



# input scrapped on the web
kws = ["exercice maths terminale s ","exercice maths terminale s nombres complexes","exercice maths terminale s pdf","exercice maths terminale s rattrapage","exercice maths terminale s géométrie dans l'espace","exercice maths terminale s exponentielle type bac","exercice maths terminale s","exercice maths terminale s suites","exercice maths terminale s recurrence","exercice math terminale s algorithme","exercice spé maths terminale s arithmétique","exercice de maths terminale s avec corrigé","exercice spé maths terminale s arithmétique bac","exercices corrigés spé maths terminale s arithmétique","exercices maths terminale s limites de fonctions","exercices maths terminale s limites de suites","exercices annales maths terminale s","exercice maths terminale s bac","correction exercice maths terminale s bordas","exercice maths terminale s type bac","corrigé exercice maths terminale s bordas","exercice spé maths terminale s bac","exercices maths terminale s loi binomiale","exercice spé maths terminale s type bac"]
urls_a = ['url1_a.jpg','url2_a.jpg']
urls_img = ['https://www.courrierinternational.com/sites/ci_master/files/styles/image_original_1280/public/assets/images/github-logo.png?itok=ZpkPiIcm','https://www.courrierinternational.com/sites/ci_master/files/styles/image_original_1280/public/assets/images/github-logo.png?itok=ZpkPiIcm']
urls_iframe = ["https://www.youtube.com/embed/mYurmWCcVkQ","https://www.youtube.com/embed/mYurmWCcVkQ"];

@shortcodes.register('kw_in_phrase')
def kw_in_phrase_handler(context, content, pargs, kwargs):
    begin = get_phrase(29)
    end =  get_phrase(29)
    kw =  random.choice(kws)
    return (begin + ' ' + kw + ' ' + end)



@shortcodes.register('str')
def str_handler(context, content, pargs, kwargs):
    nb_car = int(kwargs['nb_car'])
    phrase = get_phrase(nb_car)
    return (phrase)


@shortcodes.register('one_kw')
def one_kw_handler(context, content, pargs, kwargs):
    kw =  random.choice(kws)
    return (kw)


@shortcodes.register('url_img')
def url_img_handler(context, content, pargs, kwargs):
    url_img =  random.choice(urls_img)
    return (url_img)

@shortcodes.register('url_a')
def url_a_handler(context, content, pargs, kwargs):
    url_a =  random.choice(urls_a)
    return (url_a)

@shortcodes.register('url_iframe')
def url_iframe_handler(context, content, pargs, kwargs):
    url_iframe =  random.choice(urls_iframe)
    return (url_iframe)

final_article = shortcodes.Parser().parse(html)


# write the final article in a file
text_file = open("../final_article/final.html", "w")
text_file.write('<!DOCTYPE html><html lang="fr"><head prefix="og: https://ogp.me/ns#"><meta charset="UTF-8"></head>')
text_file.write(final_article)
text_file.write('</html>')
text_file.close()

