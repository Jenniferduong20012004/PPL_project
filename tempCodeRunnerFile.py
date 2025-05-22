import customtkinter as ctk
import random
import os
from controller.getResponseForUser import getResponseForUser
# Set appearance mode and default color theme
ctk.set_appearance_mode("white")
ctk.set_default_color_theme("blue")


class ChatBotApp:
    def __init__(self, root):
        self.getResponse = getResponseForUser()
        self.root = root
        self.root.title("Flu Tracking ChatBot")
        self.root.geometry("500x600")

        # Configure grid layout
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        # Add darker pink border
        self.outer_frame = ctk.CTkFrame(self.root, fg_color="#d36c9e", corner_radius=10)
        self.outer_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.outer_frame.grid_columnconfigure(0, weight=1)
        self.outer_frame.grid_rowconfigure(0, weight=1)

        # Create main frame
        self.main_frame = ctk.CTkFrame(self.outer_frame, fg_color="#ffeef8", corner_radius=10)
        self.main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)

        # Chat display (Textbox)
        self.chat_display = ctk.CTkTextbox(
            self.main_frame,
            height=400,
            wrap="word",
            state="disabled",
            fg_color="#fff5fa",
            text_color="#b03060"  # soft maroon
        )
        self.chat_display.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="nsew")

        # Input frame
        self.input_frame = ctk.CTkFrame(self.main_frame, fg_color="#ffeef8")
        self.input_frame.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        self.input_frame.grid_columnconfigure(0, weight=1)

        # User input entry
        self.user_input = ctk.CTkEntry(
            self.input_frame, placeholder_text="Type your message..."
        )
        self.user_input.grid(row=0, column=0, padx=(0, 5), pady=5, sticky="ew")

        # Send button
        self.send_button = ctk.CTkButton(
            self.input_frame,
            text="Send",
            command=self.send_message,
            fg_color="#fbb1d4", # pastel pink
            hover_color="#f98fc2", # slightly darker pink
            text_color="black"
        )
        self.send_button.grid(row=0, column=1, pady=5)

        # Bind Enter key to send message
        self.user_input.bind("<Return>", lambda event: self.send_message())

        # Predefined responses
        self.responses = {
            "hi": ["Hello!", "Hey there!", "Hi! How can I help you?"],
            "hello": ["Hi!", "Hello! What's up?", "Hey, good to see you!"],
            "how are you": [
                "I'm doing great, thanks!",
                "Just chilling in the digital world!",
                "Awesome, how about you?",
            ],
            "bye": ["Goodbye!", "See you later!", "Take care!"],
            "what is your name": [
                "I'm Flu, your friendly period tracking chatbot!",
                "Call me Flu!",
                "I'm Flu, nice to meet you!",
            ],
            "default": [
                "Hmm, not sure what you mean!",
                "Can you say that again?",
                "Let's talk about something else!",
            ],
        }

        # Initialize chat with a welcome message
        self.add_message(
            "Bot: Welcome to the ChatBot! Type something to start chatting."
        )

    def add_message(self, message):
        """Add a message to the chat display."""
        self.chat_display.configure(state="normal")
        self.chat_display.insert("end", message + "\n")
        self.chat_display.configure(state="disabled")
        self.chat_display.see("end")

    def get_response(self, user_message):
        """Get a response based on user input."""
        user_message = user_message.lower().strip()
        answer = False
        for key in self.responses:
            if key in user_message:
                answer = True
                return random.choice(self.responses[key])
        if (answer== False):
            return self.getResponse.getResponse(user_message)


    def send_message(self):
        """Handle sending a message."""
        user_message = self.user_input.get()
        if user_message.strip():
            # Display user message
            self.add_message(f"You: {user_message}")
            # Get and display bot response
            bot_response = self.get_response(user_message)
            self.add_message(f"Bot: {bot_response}")
            # Clear input
            self.user_input.delete(0, "end")


if __name__ == "__main__":
    root = ctk.CTk()
    app = ChatBotApp(root)
    root.mainloop()
