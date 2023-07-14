import tkinter as tk
import pyperclip

# Create the window
window = tk.Tk()
window.geometry("600x400")


# Create the input text box
text_box = tk.Text(window, height=10)
text_box.pack()

# Create the button to replace vowels with i's
button_i = tk.Button(window, text="Replace Vowels with i's")
button_i.pack()


# Create the button
button = tk.Button(window, text="Copy Output")
button.pack()

# Create the output text box
output_box = tk.Text(window, height=10)
output_box.pack()


# Define the function that will be called when the button is clicked
def copy_output():
  # Get the text from the output text box
  text = output_box.get("1.0", "end-1c")

  # Copy the text to the clipboard
  pyperclip.copy(text)

# Bind the button to the function
button.config(command=copy_output)

# Define the function that will be called when the button is clicked
def replace_vowels_with_i():
  # Get the text from the input text box
  text = text_box.get("1.0", "end-1c")

  # Replace all vowels with i's
  new_text = ""
  for char in text:
    if char in "aeiouAEIOU":
      new_text += "i"
    else:
      new_text += char

  # Insert the new text into the output text box
  output_box.insert("1.0", new_text)

# Bind the button to the function
button_i.config(command=replace_vowels_with_i)

# Start the main loop
window.mainloop()
