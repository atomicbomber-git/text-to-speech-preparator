from preprocessor import preprocess
from tagger import tag
from chunker import chunk
from normalizer import normalize

input_file = open("input.txt")
preprocessed_file = open("preprocessed.txt", "w")
tagged_file = open("tagged.txt", "w")
chunked_file = open("chunked.txt", "w")
normalized_file = open("normalized.txt", "w")

input_text = "\n".join([line for line in input_file])

# Praproses
temp = preprocess(input_text)
preprocessed_file.write(temp)

# Tagging
temp = tag(temp, "http://localhost:7000")
tagged_file.write(temp)

# Chunking
temp = chunk(temp)
chunked_file.write(temp)

# Normalisasi
temp = normalize(temp)
normalized_file.write(temp)


