from bs4 import BeautifulSoup
import glob


def to_template(article_name):

    soup = BeautifulSoup(open("../articles/" + article_name), 'html.parser')

    # tags = list()
    # for tag in soup.find_all(True):
    #
    #     tags.append(tag.name)
    #
    # print(set(tags))
    # exit()
    #
    #
    # exit()
    #
    # print(soup)
    # exit()


    for tag in soup.find_all():


        # print("tag")
        # print(tag)
        # print("tag")
        # print("childs")


        # special tag
        ## strong done
        ## i done
        ## u done
        ## a done
        ## img done
        ## quote
        ## iframe ?

        contents = list(tag.contents)

        if len(contents) <= 1:
            phrase = tag.string

            if tag.name == "strong" or tag.name == "i" or tag.name == "u":
                tag.string = "[% kw_in_phrase %]"
            elif tag.name == "a":
                tag.string = "[% one_kw %]" #todo
                tag['href'] = "[% url_a %]"
            elif tag.name == "iframe":
                tag['src'] = "[% url_iframe %]"
            elif tag.name == "img":
                tag['alt'] = "[% one_kw %]"
                tag['src'] = "[% url_img %]"
                tag['title'] = "[% one_kw %]"
            elif phrase and len(phrase) > 2:
                tag.string = "[% str nb_car={0} %]".format(len(phrase))
        else:
            for child in contents:
                if child.name == None:

                    phrase = child.string

                    if phrase and len(phrase) > 2:
                        child.replace_with("[% str nb_car={0} %]".format(len(phrase)))







    article_name = article_name.split(".")

    with open("../template/" + article_name[0] + ".template", "w") as file:
        file.write(str(soup))

    #print(soup)





paths = glob.glob("../articles/*.html")

for path in paths:
    path = path.split("/")
    print(path[-1])
    to_template(path[-1])

