import tkinter as tk
from tkinter import filedialog
import pygame

# Initialize pygame mixer for audio playback
pygame.mixer.init()

class AudioPlayer:
    def __init__(self, root):
        self.root = root
        root.title("Simple Audio Player")

        # Create a grid of buttons
        for i in range(3):
            for j in range(3):
                btn_text = f"Button {i*3 + j + 1}"
                btn = tk.Button(root, text=btn_text, command=lambda i=i, j=j: self.play_audio(i, j))
                btn.grid(row=i, column=j)

        # Dictionary to store file paths for each button
        self.audio_files = {}

    def play_audio(self, i, j):
        # Get button index from grid position
        index = i * 3 + j

        # If audio file is not set for this button, prompt user to select file
        if index not in self.audio_files:
            audio_file = filedialog.askopenfilename(title="Select Audio File", filetypes=[("Audio Files", "*.mp3 *.wav")])
            if audio_file:
                self.audio_files[index] = audio_file

        # If audio file is set for this button, play audio
        if index in self.audio_files:
            pygame.mixer.music.load(self.audio_files[index])
            pygame.mixer.music.play()

if __name__ == "__main__":
    root = tk.Tk()
    player = AudioPlayer(root)
    root.mainloop()
