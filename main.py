import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

class ScoutingApp(customtkinter.CTk):
	def __init__(self):
		super().__init__()

		# configure vars
		self.x_res = 1100
		self.y_res = 580

		self.game_list = ["Rapid React - 2022", "Energize - 2023"]
		self.game_functions_list = [self.rapid_react, self.energize]

		self.title("4903 Scouting App")
		self.minsize(400, 300)
		self.geometry(f"{self.x_res}x{self.y_res}")

		# configure grid layout (4x4)
		self.grid_columnconfigure((0), weight=1)
		self.grid_columnconfigure((1, 2, 3), weight=2)
		self.grid_rowconfigure((0, 1, 2), weight=1)

		# sidebar
		self.sidebar_frame = customtkinter.CTkFrame(self, corner_radius=0)
		self.sidebar_frame.grid(row=0, column=0, columnspan=1, rowspan=4, sticky="nsew")
		self.sidebar_frame.grid_rowconfigure(4, weight=1)

		self.title_sidebar_frame = customtkinter.CTkLabel(self.sidebar_frame, text="FRC Scouting App", font=customtkinter.CTkFont(size=26, weight="bold"))
		self.title_sidebar_frame.grid(row=0, column=0, padx=20, pady=(20, 10))

		# game select (format: [game name] - [year])
		self.game_select_label = customtkinter.CTkLabel(self.sidebar_frame, text="Select Game", font=customtkinter.CTkFont(size=20, weight="bold"))
		self.game_select_label.grid(row=1, column=0, padx=20, pady=(15, 5), sticky='w')
		self.game_select_menu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=self.game_list, command=self.game_select_event)
		self.game_select_menu.grid(row=2, column=0, padx=20, sticky='w')

		# TODO: Remove after testing
		self.rapid_react()

		
	def game_select_event(self, game: str):
		"""
		Runs on game selection. Updates main frame to selected game.
		"""
		for i in range(len(self.game_list)):
			if self.game_list[i] == game:
				self.game_functions_list[i]()

	# 2022 rapid react functions (probably best to make each year's game its own class)
	def rapid_react(self):
		"""
		Basically just a proof of concept
		"""
		self.auto_high_success = 0
		self.auto_high_fail = 0
		self.auto_low_success = 0
		self.auto_low_fail = 0

		self.teleop_high_success = 0
		self.teleop_high_fail = 0
		self.teleop_low_success = 0
		self.teleop_low_fail = 0

		# main frame
		self.main_frame = customtkinter.CTkFrame(self.master, corner_radius=0)
		self.main_frame.grid(row=0, column=1, columnspan=3, rowspan=4, sticky="nsew", padx=(10, 0))

		# autonomous
		self.autonomous_label = customtkinter.CTkLabel(self.main_frame, text="Autonomous", font=customtkinter.CTkFont(size=20, weight="bold"))
		self.autonomous_label.grid(row=0, column=0, padx=(20, 0), pady=15, sticky='w')

		self.auto_high_suc_down_button = customtkinter.CTkButton(self.main_frame, 
																 width=32, height=32, 
																 corner_radius=8, 
																 text="-", 
																 font=customtkinter.CTkFont(weight="bold"),
																 command=self.rapid_react_auto_high_suc_down())
		self.auto_high_suc_down_button.grid(row=1, column=0, padx=(20, 0), pady=5, sticky='nw')
		self.auto_high_suc_label = customtkinter.CTkLabel(self.main_frame, text=f"{self.auto_high_success}", font=customtkinter.CTkFont(size=20))
		self.auto_high_suc_label.grid(row=1, column=1)
		self.auto_high_suc_up_button = customtkinter.CTkButton(self.main_frame, 
															   width=32, height=32, 
															   corner_radius=8, 
															   text="+", 
															   font=customtkinter.CTkFont(weight="bold"),
															   command=self.rapid_react_auto_high_suc_up())
		self.auto_high_suc_up_button.grid(row=1, column=2, padx=20, pady=5, sticky='nw')
	
	def rapid_react_auto_high_suc_up(self):
		self.auto_high_success += 1
		self.auto_high_suc_label.configure(text = str(self.auto_high_success))
	
	def rapid_react_auto_high_suc_down(self):
		if self.auto_high_success > 0:
			self.auto_high_success -= 1
			self.auto_high_suc_label.configure(text = str(self.auto_high_success))

	# 2023 energize functions (probably best to make each year's game its own class)
	def energize(self):
		pass
		

if __name__ == "__main__" :
	app = ScoutingApp()
	app.mainloop()
