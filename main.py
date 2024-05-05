import tkinter as tk
from AthleteManager import ClubUrlGettingSystem


class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("Aplikacja Klubowa")

        # Etykieta "Wprowadź nazwę klubu"
        self.club_name_label = tk.Label(self.root, text="Wprowadź nazwę klubu:")
        self.club_name_label.pack()

        # Pole do wprowadzania nazwy klubu
        self.club_name_entry = tk.Entry(self.root)
        self.club_name_entry.pack()

        # Przycisk "Zatwierdź nazwę klubu"
        self.submit_button = tk.Button(self.root, text="Zatwierdź nazwę klubu", command=self.submit_club_name)
        self.submit_button.pack()

        # Uruchomienie pętli głównej aplikacji
        self.root.mainloop()

    def submit_club_name(self):
        club_name = self.club_name_entry.get()
        self.show_confirmation_window(club_name)

    def show_confirmation_window(self, club_name):
        confirmation_window = tk.Toplevel()
        confirmation_window.geometry("300x300")
        confirmation_window.title("Potwierdzenie")

        # Etykieta z wprowadzoną nazwą klubu
        club_name_label_1 = tk.Label(confirmation_window, text="Wprowadzona nazwa klubu:", font=("Helvetica", 12))
        club_name_label_1.pack()

        # Wyświetlanie nazwy klubu
        club_name_display = tk.Label(confirmation_window, text=club_name, font=("Helvetica", 12, "bold"))
        club_name_display.pack()

        # Przycisk "rozpocznij"
        club_name_button = tk.Button(confirmation_window, text="rozpocznij", font=("Arial", 12),
                                     command=lambda: ClubUrlGettingSystem().GetClubName(club_name))
        club_name_button.pack()


if __name__ == "__main__":
    main = Main()

