
import tkinter as tk
from tkinter import simpledialog, messagebox
import random
from quiz_questions import questions

# Shuffle and divide into levels
random.shuffle(questions)
levels = [questions[i:i + 10] for i in range(0, 100, 10)]  # 10 levels, 10 questions each

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz Challenge")
        self.root.geometry("700x500")
        self.root.config(bg="#f0f4f7")
        self.init_game()

    def init_game(self):
        self.username = simpledialog.askstring("Welcome", "Enter your name to begin:")
        if not self.username:
            self.username = "Player"

        self.level = 0
        self.score = 0
        self.correct_in_level = 0
        self.q_index = 0

        self.title_label = tk.Label(self.root, text=f"Welcome, {self.username}!", font=("Helvetica", 16, "bold"), bg="#f0f4f7")
        self.title_label.pack(pady=10)

        self.level_label = tk.Label(self.root, text=f"Level {self.level + 1}", font=("Helvetica", 14), bg="#f0f4f7", fg="#333")
        self.level_label.pack()

        self.question_label = tk.Label(self.root, text="", wraplength=600, font=("Helvetica", 13), bg="#f0f4f7", justify="left")
        self.question_label.pack(pady=20)

        self.buttons = {}
        for opt in ["A", "B", "C", "D"]:
            self.buttons[opt] = tk.Button(self.root, text="", width=40, font=("Helvetica", 12), bg="#ffffff",
                                          command=lambda o=opt: self.check_answer(o))
            self.buttons[opt].pack(pady=5)

        self.status_label = tk.Label(self.root, text="", font=("Helvetica", 12), bg="#f0f4f7")
        self.status_label.pack(pady=10)

        self.load_question()

    def load_question(self):
        if self.q_index < 10:
            q = levels[self.level][self.q_index]
            self.question_label.config(text=f"Q{self.q_index + 1}. {q['question']}")
            for key, val in q['options'].items():
                self.buttons[key].config(text=f"{key}. {val}", state="normal")
            self.status_label.config(text=f"Correct in this level: {self.correct_in_level}/10")
        else:
            self.end_level()

    def check_answer(self, selected):
        q = levels[self.level][self.q_index]
        if selected == q['answer']:
            self.score += 1
            self.correct_in_level += 1
        self.q_index += 1
        self.load_question()

    def end_level(self):
        if self.correct_in_level >= 5:
            messagebox.showinfo("Level Passed", f"✅ Great! You passed Level {self.level + 1}.\n"
                                                f"Correct Answers: {self.correct_in_level}/10")
            self.level += 1
            if self.level >= len(levels):
                self.end_game()
            else:
                self.q_index = 0
                self.correct_in_level = 0
                self.level_label.config(text=f"Level {self.level + 1}")
                self.load_question()
        else:
            retry = messagebox.askyesno("Level Failed", f"❌ You did not pass Level {self.level + 1}.\n"
                                                        f"You needed 5 correct answers.\nRetry this level?")
            if retry:
                self.q_index = 0
                self.correct_in_level = 0
                self.load_question()
            else:
                self.end_game()

    def end_game(self):
        result = messagebox.askyesno("Quiz Complete", f"🎉 {self.username}, your final score is {self.score}/100.\n"
                                                      "Do you want to play again?")
        if result:
            for widget in self.root.winfo_children():
                widget.destroy()
            random.shuffle(questions)
            global levels
            levels = [questions[i:i + 10] for i in range(0, 100, 10)]
            self.init_game()
        else:
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = QuizGame(root)
    root.mainloop()
