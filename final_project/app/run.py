import Tkinter as tk
import tkFileDialog
from model import model
import pandas as pd
from learning import simple_learn
from learning import parser as p
from PIL import ImageTk, Image


class Sandwich(tk.Frame):

    # init frames
    def __init__(self, master):
        self.files = []
        self.clf = None
        self.clf1 = None
        self.clf2 = None
        self.clf3 = None
        self.clf4 = None
        self.pred_images = []
        tk.Frame.__init__(self, master, padx=10, pady=10)
        master.title("Images")
        master.minsize(width=250, height=400)
        self.pack()
        self.groups = tk.Text(root, height=6, width=50)
        tk.Button(master, text="Add models", command=self.add_models).pack()
        self.groups.pack()
        tk.Button(master, text="Learn", command=self.learn).pack()
        self.T = tk.Text(root, height=8, width=50)
        self.T.pack()
        tk.Button(master, text="Predict", command=self.predict).pack()
        self.P = tk.Listbox(master)
        self.P.pack()
        self.panel = tk.Label(root)
        self.panel.pack(side="right")
        tk.Button(master, text="Image", command=self.image).pack()

    # add prebuilt models
    def add_models(self):
        files = tkFileDialog.askopenfiles()
        self.files.append(files)
        for f in files:
            self.groups.insert(tk.END, f.name.split("/")[-1] + "\n")

    # train classifier
    def learn(self):
        def log(str):
            self.T.insert(tk.END, str+'\n')
        data = pd.concat([pd.read_csv(f.name) for row in self.files for f in row], ignore_index=True)
        self.clf = simple_learn.learn(data, p_func=log)

    # predict labels of test directory without labels
    def predict(self):
        dir = tkFileDialog.askdirectory(parent=self)
        model.build(dir)
        data = pd.read_csv(dir + "/" + dir.split("/")[-1] + ".csv")
        features = data.copy()
        features.drop(['name'], axis=1, inplace=True)
        y_pred = self.clf.predict(features)
        named = p.with_names(data)
        for index, v in enumerate(y_pred):
            name = named.icol(0).values[index].split('/')[1]
            self.pred_images.append(dir + '/' + name)
            s = named.icol(0).values[index] + ',' + str(v)
            self.P.insert(tk.END, s)

    # show image of labeled test file from selected directory
    def image(self):
        selection = self.P.curselection()
        path = self.pred_images[selection[0]]
        img = Image.open(path)
        width, height = img.size
        scale = 2
        while width > 250 and height > 250:
            width = width / scale
            height = height / scale
            scale *= 2
        img = img.resize((width, height), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.panel.configure(image=img)
        self.panel.image = img

root = tk.Tk()
app = Sandwich(root)
app.mainloop()