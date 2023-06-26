import tkinter as tk

def add_message(message):
    subtitle_text.configure(state='normal')
    subtitle_text.insert(tk.END, message + '\n')
    subtitle_text.configure(state='disabled')
    subtitle_text.see(tk.END)

# Create the GUI window
window = tk.Tk()
window.title('Conversation Subtitles')
window.geometry('400x300')

# Create a text widget to display the conversation subtitles
subtitle_text = tk.Text(window, state='disabled')
subtitle_text.pack(fill=tk.BOTH, expand=True)

# Example conversation messages
bot_message = 'Hello, how can I assist you?'
user_message = 'I have a question about the product.'

# Add the messages to the subtitle display
add_message('Bot: ' + bot_message)
add_message('User: ' + user_message)

window.mainloop()