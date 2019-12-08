import nltk
import sys

grammar = r"""

        G1 : { <NN> <IN> <CDP> }
        G2 : { <NN> <VBT> <IN> }

        KP : { <SC|RP|UH>+ }
        VP : { <VBI|VBT|MD>+ <NN|RB>*}
        NP : { <WP|PRP|PRN>+ }

        G3 : { <IN> <NN>* <VP>+ }
        G4 : { <KP>+ <NP|VP|KP|G3|NN|PRL>+ }
        G5 : { <NP|CC|RB|NEG|MD>+ <VP|G1|NP|G3|CDI|DT|PRL>+ }
        G6 : { <VP> <G3> }
        
                
        """


def chunk(text):
    for line in text.split("\n"):

        # Mentag setiap kata yang ada dari kalimat input yg dibersihkan dari spasi di sisi kiri dan kanan terlebih dahulu
        sentence = [nltk.tag.str2tuple(t) for t in line.strip().split()]
        
        # Melakukan parsing terhadap kalimat
        result = nltk.RegexpParser(grammar).parse(sentence)

        text_result = ""
        # Memproses satu per satu hasil parsing; Jika hasil berupa tanda baca, maka tanda baca tersebut akan ditambahkan ke output beserta dengan tanda akhir baris ('\n'). Jika hasil bukan merupakan tanda baca maka hasil langsung ditambahkan ke ke output beserta dangan tanda akhir baris ('\n')
        for i, item in enumerate(result):
            if item.count(',') != 0:
                text_result += (',' + "\n")
            else:
                if item.count('?') != 0:
                    text_result += ('?' + "\n")
                else:
                    if item.count('!') != 0:
                        text_result += ('!' + "\n")
                    else:
                        if item.count('.') != 0:
                            text_result += ('.' + "\n\n")
                        else:
                            text_result += (str(item) + "\n")
    return text_result


if __name__ == "__main__":
    print(chunk(sys.argv[1]))