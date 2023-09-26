from googletrans import Translator

def translate(text, dest="es"):
    return Translator().translate(text=text, dest=dest).text

