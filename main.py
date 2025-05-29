import customtkinter as ctk

# import tkinter as tk
from datetime import datetime
from controller.getResponseForUser import getResponseForUser

ctk.set_appearance_mode("white")


class LunaApp:
    def __init__(self, root):
        self.getResponse = getResponseForUser()
        self.iniSentence=  self.getResponse.checkPeriodThisMonth()

        self.root = root
        self.root.title("🌸 Luna - Period Tracking Assistant")

        screen_width = self.root.winfo_screenwidth()

        mobile_width = 400
        mobile_height = 650

        margin = 20
        x_position = screen_width - mobile_width - margin
        y_position = margin

        self.root.geometry(f"{mobile_width}x{mobile_height}+{x_position}+{y_position}")

        self.chat_history = []
        self.current_view = "launcher"

        self.create_main_frame()
        self.create_launcher_view()

        self.root.attributes("-topmost", True)

    def create_main_frame(self):
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        self.main_frame = ctk.CTkFrame(
            self.root,
            fg_color="#ffeef8",
            corner_radius=20,
            border_width=2,
            border_color="#d36c9e",
        )
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.main_frame.grid_columnconfigure(0, weight=1)

    def create_launcher_view(self):
        # Clear existing content
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        self.create_launcher_header()
        self.create_features_section()
        self.create_action_buttons()

    def create_launcher_header(self):
        self.header_frame = ctk.CTkFrame(
            self.main_frame, fg_color="#d36c9e", height=180, corner_radius=15
        )
        self.header_frame.grid(row=0, column=0, sticky="ew", padx=5, pady=10)
        self.header_frame.grid_propagate(False)

        # Title
        self.title_label = ctk.CTkLabel(
            self.header_frame,
            text="🌸 Luna",
            font=("Georgia", 36, "bold"),
            text_color="white",
        )
        self.title_label.pack(pady=(20, 5))

        # Subtitle
        self.subtitle_label = ctk.CTkLabel(
            self.header_frame,
            text="Your Personal Period Tracking Assistant",
            font=("Segoe UI", 16),
            text_color="#ffeef8",
            justify="center",
        )
        self.subtitle_label.pack(pady=(0, 8))

        # Description
        self.desc_label = ctk.CTkLabel(
            self.header_frame,
            text="AI-powered chatbot for menstrual cycle,\nsymptoms, and overall health tracking",
            font=("Segoe UI Light", 12),
            text_color="#fff5fa",
            justify="center",
        )
        self.desc_label.pack(pady=(0, 20))

    def create_features_section(self):
        self.features_frame = ctk.CTkFrame(
            self.main_frame, fg_color="#f8e8ff", corner_radius=15
        )
        self.features_frame.grid(row=1, column=0, sticky="ew", padx=5, pady=10)

        # Features title
        self.features_title = ctk.CTkLabel(
            self.features_frame,
            text="✨ Key Features",
            font=("Segoe UI Semibold", 18, "bold"),
            text_color="#8b0045",
        )
        self.features_title.pack(pady=(15, 10))

        features = [
            ("🌙", "Luna Chatbot", "Get conversation with Luna assistant"),
            ("📅", "Cycle Tracking", "Monitor your period cycle patterns"),
            ("🩺", "Symptom Logging", "Track mood, pain, and health symptoms"),
        ]

        for icon, title, desc in features:
            feature_frame = ctk.CTkFrame(
                self.features_frame, fg_color="white", corner_radius=10, height=60
            )
            feature_frame.pack(fill="x", padx=15, pady=5)
            feature_frame.pack_propagate(False)

            icon_label = ctk.CTkLabel(
                feature_frame, text=icon, font=("Segoe UI Emoji", 24)
            )
            icon_label.pack(side="left", padx=(15, 10), pady=15)

            text_frame = ctk.CTkFrame(feature_frame, fg_color="transparent")
            text_frame.pack(side="left", fill="both", expand=True, pady=10)

            title_label = ctk.CTkLabel(
                text_frame,
                text=title,
                font=("Segoe UI Semibold", 13, "bold"),
                text_color="#b03060",
                anchor="w",
            )
            title_label.pack(anchor="w")

            desc_label = ctk.CTkLabel(
                text_frame,
                text=desc,
                font=("Segoe UI", 10),
                text_color="#666666",
                anchor="w",
            )
            desc_label.pack(anchor="w", pady=(2, 0))

        ctk.CTkLabel(self.features_frame, text="", height=10).pack()

    def create_action_buttons(self):
        self.action_frame = ctk.CTkFrame(
            self.main_frame, fg_color="#ffeef8", height=80, corner_radius=0
        )
        self.action_frame.grid(row=2, column=0, sticky="ew", padx=5, pady=10)
        self.action_frame.grid_propagate(False)

        # Button to chat with Luna
        self.start_button = ctk.CTkButton(
            self.action_frame,
            text="🌙 Chat with Luna",
            width=280,
            height=50,
            command=self.start_chat,
            fg_color="#d36c9e",
            hover_color="#c55a8a",
            text_color="white",
            font=("Segoe UI Semibold", 16, "bold"),
            corner_radius=25,
        )
        self.start_button.pack(pady=15)

    def start_chat(self):
        self.current_view = "chat"
        self.create_chat_view()

    def create_chat_view(self):
        # Clear existing content
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Reset grid configuration for chat view
        self.main_frame.grid_rowconfigure(1, weight=1)

        self.create_chat_header()
        self.create_chat_area()
        self.create_input_area()

        # Add welcome message
        self.add_message(
            "Luna",
            "Welcome to your personal period tracking assistant! I'm here to help you monitor your cycle, track symptoms, and answer health questions. How are you feeling today? 💖",
            is_user=False,
        )
        if (self.iniSentence is not None):
            self.add_message(
                "Luna",
                self.iniSentence,
                is_user=False,
            )
        

    def create_chat_header(self):
        self.chat_header_frame = ctk.CTkFrame(
            self.main_frame, fg_color="#d36c9e", height=120, corner_radius=15
        )
        self.chat_header_frame.grid(row=0, column=0, sticky="ew", padx=5, pady=(5, 5))
        self.chat_header_frame.grid_propagate(False)

        # Header content container
        header_content = ctk.CTkFrame(self.chat_header_frame, fg_color="transparent")
        header_content.pack(expand=True, fill="both", padx=20, pady=15)

        # Top container with back button and title
        top_container = ctk.CTkFrame(header_content, fg_color="transparent")
        top_container.pack(fill="x")

        # Back button
        self.back_button = ctk.CTkButton(
            top_container,
            text="← Back",
            width=30,
            height=30,
            command=self.go_back_to_launcher,
            fg_color="#c55a8a",
            hover_color="#b04d7a",
            text_color="white",
            font=("Segoe UI", 10, "bold"),
            corner_radius=15,
        )
        self.back_button.pack(side="left", pady=(5, 0))

        # Title and subtitle container
        title_container = ctk.CTkFrame(top_container, fg_color="transparent")
        title_container.pack(side="left", fill="x", expand=True, padx=(15, 0))

        # Main title
        self.main_title = ctk.CTkLabel(
            title_container,
            text="🌸 Luna",
            font=("Segoe UI", 20, "bold"),
            text_color="white",
            anchor="w",
        )
        self.main_title.pack(anchor="w", pady=(5, 5))

        # Subtitle
        self.subtitle = ctk.CTkLabel(
            title_container,
            text="Your Personal Period Tracking Companion",
            font=("Segoe UI", 12),
            text_color="#ffeef8",
            anchor="w",
        )
        self.subtitle.pack(anchor="w")

    def create_chat_area(self):
        self.chat_container = ctk.CTkFrame(
            self.main_frame, fg_color="#fff5fa", corner_radius=10
        )
        self.chat_container.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        # Scrollable chat
        self.chat_scroll = ctk.CTkScrollableFrame(
            self.chat_container,
            fg_color="transparent",
            scrollbar_button_color="#d36c9e",
            scrollbar_button_hover_color="#c55a8a",
        )
        self.chat_scroll.pack(fill="both", expand=True, padx=10, pady=10)
        self.chat_scroll.grid_columnconfigure(0, weight=1)

    def create_input_area(self):
        self.input_frame = ctk.CTkFrame(
            self.main_frame, fg_color="#f8e8ff", height=140, corner_radius=10
        )
        self.input_frame.grid(row=2, column=0, sticky="ew", padx=5, pady=(5, 10))
        self.input_frame.grid_propagate(False)

        # Input container
        input_container = ctk.CTkFrame(self.input_frame, fg_color="transparent")
        input_container.pack(fill="both", expand=True, padx=15, pady=15)

        # Quick action buttons (top row)
        quick_actions_top = ctk.CTkFrame(input_container, fg_color="transparent")
        quick_actions_top.pack(fill="x", pady=(0, 10))

        # Left side buttons
        left_buttons = ctk.CTkFrame(quick_actions_top, fg_color="transparent")
        left_buttons.pack(side="left")

        self.mood_button = ctk.CTkButton(
            left_buttons,
            text="Mood",
            height=35,
            width=90,
            command=lambda: self.quick_log("mood"),
            fg_color="#ff9ec7",
            hover_color="#ff8bc1",
            text_color="white",
            font=("Segoe UI", 10, "bold"),
            corner_radius=17,
        )
        self.mood_button.pack(side="left", padx=(0, 10))

        self.symptoms_button = ctk.CTkButton(
            left_buttons,
            text="Symptoms",
            height=35,
            width=100,
            command=lambda: self.quick_log("symptoms"),
            fg_color="#d4a5ff",
            hover_color="#c995ff",
            text_color="white",
            font=("Segoe UI", 10, "bold"),
            corner_radius=17,
        )
        self.symptoms_button.pack(side="left")

        # Right side buttons
        right_buttons = ctk.CTkFrame(quick_actions_top, fg_color="transparent")
        right_buttons.pack(side="right")

        self.clear_button = ctk.CTkButton(
            right_buttons,
            text="Clear",
            height=35,
            width=80,
            command=self.clear_chat,
            fg_color="#ff7f7f",
            hover_color="#ff6b6b",
            text_color="white",
            font=("Segoe UI", 10, "bold"),
            corner_radius=17,
        )
        self.clear_button.pack(side="left")

        # Input row (bottom)
        input_row = ctk.CTkFrame(input_container, fg_color="transparent")
        input_row.pack(fill="x", pady=(10, 0))

        # Message input (center)
        self.message_entry = ctk.CTkEntry(
            input_row,
            placeholder_text="Ask about your period and more...",
            height=50,
            fg_color="white",
            text_color="#333333",
            font=("Segoe UI", 11),
            corner_radius=25,
            border_width=1,
            border_color="#e8b4d4",
        )
        self.message_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

        # Send button (right)
        self.send_button = ctk.CTkButton(
            input_row,
            text="Send",
            width=80,
            height=50,
            command=self.send_message,
            fg_color="#d36c9e",
            hover_color="#c55a8a",
            text_color="white",
            font=("Segoe UI", 12, "bold"),
            corner_radius=25,
        )
        self.send_button.pack(side="right")

        # Bind Enter key to send message
        self.message_entry.bind("<Return>", lambda event: self.send_message())

    def go_back_to_launcher(self):
        self.current_view = "launcher"
        self.chat_history.clear()
        # Reset grid configuration
        self.main_frame.grid_rowconfigure(1, weight=0)
        self.create_launcher_view()

    def add_message(self, sender, message, is_user=True):
        # Message container
        msg_container = ctk.CTkFrame(self.chat_scroll, fg_color="transparent")
        msg_container.grid(sticky="ew", pady=3)
        msg_container.grid_columnconfigure(0, weight=1)

        if is_user:
            # User message bubble (right aligned)
            msg_bubble = ctk.CTkFrame(
                msg_container, fg_color="#d36c9e", corner_radius=15
            )
            msg_bubble.grid(row=0, column=0, sticky="e", padx=(50, 5))

            msg_label = ctk.CTkLabel(
                msg_bubble,
                text=message,
                font=("Segoe UI", 11),
                text_color="white",
                justify="left",
                wraplength=220,
            )
            msg_label.pack(padx=12, pady=8)

        else:
            # Luna message bubble (left aligned)
            msg_bubble = ctk.CTkFrame(
                msg_container,
                fg_color="white",
                corner_radius=15,
                border_width=1,
                border_color="#e8b4d4",
            )
            msg_bubble.grid(row=0, column=0, sticky="w", padx=(5, 50))

            msg_label = ctk.CTkLabel(
                msg_bubble,
                text=message,
                font=("Segoe UI", 11),
                text_color="#333333",
                justify="left",
                wraplength=220,
            )
            msg_label.pack(padx=12, pady=8)

        # Auto scroll to bottom
        self.root.after(100, lambda: self.chat_scroll._parent_canvas.yview_moveto(1.0))

        # Save to history
        self.chat_history.append(
            {
                "sender": sender,
                "message": message,
                "timestamp": datetime.now().strftime("%H:%M"),
                "is_user": is_user,
            }
        )

    def quick_log(self, log_type):
        if log_type == "mood":
            self.message_entry.delete(0, "end")
            self.message_entry.insert(0, "How should I track my mood today?")
        elif log_type == "symptoms":
            self.message_entry.delete(0, "end")
            self.message_entry.insert(0, "I want to log my symptoms")
        self.message_entry.focus()

    def clear_chat(self):
        for widget in self.chat_scroll.winfo_children():
            widget.destroy()

        self.chat_history.clear()
        self.add_message(
            "Luna", "Chat cleared! Ready to help you again! 💖", is_user=False
        )

    def get_response(self, user_message):
        """Get response from AI system"""
        response = self.getResponse.getResponse(user_message)
        return response

    def send_message(self):
        """Send message"""
        message_text = self.message_entry.get().strip()

        if not message_text:
            return

        # Add user message
        self.add_message("You", message_text, is_user=True)

        # Clear input
        self.message_entry.delete(0, "end")

        bot_response = self.get_response(message_text)

        print(f"bot_response type: {type(bot_response)}, value: {bot_response}")

        if isinstance(bot_response, dict):
            response_text = bot_response.get("result", "No result available")
            if bot_response.get("type") == "RequireOp":
                if bot_response["result"] is None:
                    response_text = "Please input date"
                elif bot_response["verb"] == "start":
                    start_date = bot_response["result"].start_at
                    if start_date:
                        response_text = (
                            f"Cycle started on {start_date.strftime('%d/%m/%Y')}"
                        )
                    else:
                        response_text = "Cycle start date not available."
                elif bot_response["verb"] == "end":
                    end_date = bot_response["result"].end_at
                    if end_date:
                        response_text = (
                            f"Cycle ended on {end_date.strftime('%d/%m/%Y')}"
                        )
                    else:
                        response_text = "Cycle end date not available."
                elif bot_response["verb"] == "show":
                    result = bot_response.get("result", [])
                    if not result:
                        response_text = "No cycles found."
                    else:
                        formatted_cycles = []
                        for idx, item in enumerate(result, start=1):
                            start = item["start_at"].strftime("%d/%m/%Y")
                            end = item["end_at"].strftime("%d/%m/%Y")
                            formatted_cycles.append(
                                f"{idx}. Cycle {idx} starts at {start} and ends at {end}"
                            )
                        response_text = "Cycles:\n" + "\n".join(formatted_cycles)
            elif bot_response.get("type") == "SpecificPhraseOp":
                response_text = bot_response["result"]
                phrase = bot_response["phrase"]
                if phrase == "ovulation":
                    if (bot_response['result']['second_ovulation_day'] is None):
                        response_text = f"Ovulation date: {bot_response['result']['ovulation_day']}. {bot_response['result']['reminder']}"
                    else:
                        response_text = f"Ovulation date: {bot_response['result']['ovulation_day']}. You are also expected to experiece the second ovulation on {bot_response['result']['second_ovulation_day']}. {bot_response['result']['reminder']}"
                elif phrase == "fertile":
                    response_text = f"Fertile range date: {bot_response['result']['start_at']} to {bot_response['result']['end_at']}. {bot_response['result']['reminder']}"
                elif phrase == "non-fertile":
                    response_text = f"Non-fertile range date: {bot_response['result']['start_at']} to {bot_response['result']['end_at']}. {bot_response['result']['reminder']}"
                elif phrase == "period":
                    if (bot_response['result']['second_start_at'] is None ):
                        response_text = f"Period range date: {bot_response['result']['start_at']} to {bot_response['result']['end_at']}. {bot_response['result']['reminder']}"
                    else:
                        response_text = f"Period range date: {bot_response['result']['start_at']} to {bot_response['result']['end_at']}. You are also expected to experiece the second period from {bot_response['result']['second_start_at']} to {bot_response['result']['second_end_at']}. {bot_response['result']['reminder']}"
            elif bot_response.get("type") == "CycleStatusOp":
                response_text = f"Cycle status on {bot_response['time'].strftime('%d/%m/%Y')}: {bot_response['result']}"
        else:
            response_text = str(bot_response)

        self.root.after(
            800, lambda: self.add_message("Luna", response_text, is_user=False)
        )


if __name__ == "__main__":
    root = ctk.CTk()
    app = LunaApp(root)
    root.mainloop()
