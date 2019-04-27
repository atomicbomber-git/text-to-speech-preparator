import sys

substitution_map = {
    ',': ' , ',
    '(': ' ( ',
    ')': ' ) ',
    '-': ' - ',
    ':': ' : ',
    '.': ' . ',
}


def preprocess(text):
    # Melakukan konversi karakter sesuai dengan daftar yang telah dibuat diatas
    for key, value in substitution_map.items():
        text = text.replace(key, value)

    return text


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        raise Exception("Anda harus menyertakan input ke program ini.")

    text = " ".join(sys.argv[1:])
    print(preprocess(text))
