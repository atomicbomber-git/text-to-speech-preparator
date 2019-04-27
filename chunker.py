import nltk
import sys

grammar = r"""
		TP : { <WP>+ }
		NP : { <NNP>+ | <FW>+ | <RP>+ }
		KP : { <SC|CC|NEG>+ <IN>* <MD|RB>* | <MD|RB>+ | <IN>+  <SC|CC|NEG>* <MD|RB>* }
		CP : { <CDO|CDP|CDI|CDC>+ | <SYM> }
		
		VP : { <VBI>+ | <VBT>+ }
		NP : { <DT>? <CP|OP|GM|:|;|"|.|,|-|...|NN|PRN|PRP|PRL|NNG|UH>+ <JJ>* <DT>? | <DT>? <JJ> * <DT>? | <DT> }
			
		NP : { <KP> <NP> }
		VP : { <VP> <VP> }
		VP : { <KP> <VP> }
		VP : { <VP> <NP> }
                
        """


def chunk(text):
    for line in text.split("\n"):

        sentence = [nltk.tag.str2tuple(t) for t in line.strip().split()]
        result = nltk.RegexpParser(grammar).parse(sentence)

        text_result = ""
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
                            text_result += ('.' + "\n")
                        else:
                            if item.count('-') != 0:
                                text_result += ('-' + "\n")
                            else:
                                text_result += (str(item) + "\n")
    return text_result


if __name__ == "__main__":
    print(chunk(sys.argv[1]))