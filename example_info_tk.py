from tkinter import *

root = Tk()
root.title("example_profile")
root.geometry("700x1000")

label = Label(anchor = N, text="Таланян Артур", font=("verdana", 30))
label_bio = Label(anchor = W, text="Биография:", font=("verdana", 20))
label_bio_info = Label(anchor = W, text="Студент 2-го курса в МАИ, Инноватика, М3О-236БВ-24", font=("verdana", 14))
label_skills = Label(anchor = W, text="Умения:", font=("verdana", 20))
label_skills_info = Label(anchor = W, text="Базовый Python, SQL", font=("verdana", 14))
label_exp = Label(anchor = W, text="Опыт:", font=("verdana", 20))
label_exp_info = Label(anchor = W, text="Отсутствует", font=("verdana", 14))
#label.pack(side=BOTTOM, padx=10, pady=10) 
  
label.place(x=200, y=635)
label_bio.place(x=10, y=700)
label_bio_info.place(x=10, y=740)
label_skills.place(x=10, y=800)
label_skills_info.place(x=10, y=840)
label_exp.place(x=10, y=900)
label_exp_info.place(x=10, y=940)

canvas = Canvas(bg="white", width=513, height=534)
canvas.pack(anchor=N)
#canvas.place

profile_image = PhotoImage(file="profile.png")
 
canvas.create_image(1, 1, anchor=NW, image=profile_image)


root.mainloop()