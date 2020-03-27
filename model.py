def get_character(book):
  if book == "bible":
    return "RM"
  elif book == "davinci":
    return "Jhope"
  elif book == "hp":
    return "Suga"
  else:
    return None
  
def get_gif(character):
  if character == "RM":
    return "https://media.giphy.com/media/kC3DZ7PhJHZ38Cjb07/giphy.gif"
  elif character == "Jhope":
    return "https://media.giphy.com/media/1zlDnvnoLbJSnjk1UJ/giphy.gif"
  elif character == "Suga":
    return "https://media.giphy.com/media/h2ZOqa0RyKo7adhaRc/giphy.gif"
  else:
    return None