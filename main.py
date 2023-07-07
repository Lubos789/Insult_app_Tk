from tkinter import *
import requests

url = "https://evilinsult.com/generate_insult.php"

window = Tk()
window.minsize(300, 300)
window.resizable(False, False)
window.title("Annoy All")
window.config(background="#042940")


# fce
def insult_me():
    user_language = drop_down_lang.get()
    language_parametrs = {
        "lang": user_language,
        "type": "json"
    }
    response = requests.get(url, language_parametrs)
    response.raise_for_status()
    data = response.json()
    insult_label["text"] = data["insult"]


# Roletka
drop_down_lang = StringVar(window)
drop_down_lang.set("cs")
drop_down_lang_options = OptionMenu(window, drop_down_lang, "en", "es", "fr", "cs")
drop_down_lang_options.config(bg="#9FC131", font=("Arial", 12, "bold"), fg="white")
drop_down_lang_options.pack(pady=10)

# button
insult_button = Button(text="Be Angry", command=insult_me, bg="#9FC131", fg="white", font=("Arial", 12, "bold"))
insult_button.pack(pady=10)

# Label
insult_label = Label(wraplength=200, background="#042940", fg="#D6D58E", font=("Arial", 14, "bold"))
insult_label.pack()

window.mainloop()