    def add_message(self, sender, message, is_user=True):
        # Message container
        msg_container = ctk.CTkFrame(self.chat_scroll, fg_color="transparent")
        msg_container.grid(sticky="ew", pady=3)
        msg_container.grid_columnconfigure(0, weight=1)
        
        if is_user:
            # User message bubble (right aligned)
            msg_bubble = ctk.CTkFrame(
                msg_container,
                fg_color="#d36c9e",
                corner_radius=15
            )
            msg_bubble.grid(row=0, column=0, sticky="e", padx=(50, 5))
            
            msg_label = ctk.CTkLabel(
                msg_bubble,
                text=message,
                font=("Segoe UI", 11),
                text_color="white",
                justify="left",
                wraplength=220
            )
            msg_label.pack(padx=12, pady=8)
            
        else:
            # Luna message bubble (left aligned)
            msg_bubble = ctk.CTkFrame(
                msg_container,
                fg_color="white",
                corner_radius=15,
                border_width=1,
                border_color="#e8b4d4"
            )
            msg_bubble.grid(row=0, column=0, sticky="w", padx=(5, 50))
            
            msg_label = ctk.CTkLabel(
                msg_bubble,
                text=message,
                font=("Segoe UI", 11),
                text_color="#333333",
                justify="left",
                wraplength=220
            )
            msg_label.pack(padx=12, pady=8)
        
        # Auto scroll to bottom
        self.root.after(100, lambda: self.chat_scroll._parent_canvas.yview_moveto(1.0))
        
        # Save to history
        self.chat_history.append({
            "sender": sender,
            "message": message,
            "timestamp": datetime.now().strftime("%H:%M"),
            "is_user": is_user
        })