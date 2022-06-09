import tkinter as tk


def init_window():
    def read_file():
        with open("Marvel.txt", "r") as f:
            label1['text'] = f.read()

    def freq():
        content = label1['text']
        print(content)
        wordlist = []

        for word in content.split():
            if word not in wordlist:
                wordlist.append(word)

        for word in wordlist:
            wordlist[wordlist.index(word)] = (word + " = " + str(content.count(word)))

        my_text = ""
        i = 0
        for word in wordlist:
            i = i + 1
            if (i % 2 == 0):
                my_text += word + "\n"
            else:
                my_text += word + "; "
        label1['text'] = my_text

    window = tk.Tk()
    window.title("LAB 10 Program")
    window.geometry("600x360")
    label1 = tk.Label(window, text="Label here", wraplength=500, justify='left')
    label1.grid(column=1, row=0)
    read_button = tk.Button(window, text="Read", command=read_file)
    read_button.grid(column=0, row=0)
    calc_button = tk.Button(window, text="Calculate", command=freq)
    calc_button.grid(column=0, row=1)
    window.mainloop()


if __name__ == '__main__':
    init_window()
