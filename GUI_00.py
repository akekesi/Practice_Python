from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext

from varname import nameof
from GUI_00_function import func_test


class GUI:
    """GUI with inputs, buttons and text box"""

    def __init__(self, master) -> None:
        master.title("Test")

        # value
        self.value_1 = "a.bc"
        self.value_2 = "1.23"
        self.path_1 = r"C:\Users\kekesati\OneDrive\Py_json\00_automated_simulation\02_python\GUI_00_file.txt"

        # frame
        self.padx_frame_in = 10 
        self.pady_frame_in = 10
        self.padx_frame_out = 15
        self.pady_frame_out = 15
        self.padx =0
        self.pady =0
        self.width_row_0 = 8
        self.width_row_1 = 11
        self.width_button_1 = 3
        self.width_button_2 = 10
        self.width_button_3 = 20

        self.frame_input = LabelFrame(master, text="Input",padx=self.padx_frame_in, pady=self.pady_frame_in)
        self.frame_input.grid(row=0, column=0, padx=self.padx_frame_out, pady=self.pady_frame_out, sticky=N+W+E+S)

        self.frame_button = LabelFrame(master, text="Button",padx=self.padx_frame_in, pady=self.pady_frame_in)
        self.frame_button.grid(row=0, column=1, padx=self.padx_frame_out, pady=self.pady_frame_out, sticky=N+W+E+S)

        self.frame_preview = LabelFrame(master, text="Preview",padx=self.padx_frame_in, pady=self.pady_frame_in)
        self.frame_preview.grid(row=1, column=0, columnspan=2, padx=self.padx_frame_out, pady=self.pady_frame_out, sticky=N+W+E+S)

        self.text_box = scrolledtext.ScrolledText(self.frame_preview, wrap=WORD, state=DISABLED, width=35, height=5)
        self.text_box.grid(row=0, column=0, sticky=W+E)

        # widget
        Label(self.frame_input, text="value_1:", width=self.width_row_0, anchor="w").grid(row=0, column=0, padx=self.padx)
        Label(self.frame_input, text="value_2:", width=self.width_row_0, anchor="w").grid(row=1, column=0, padx=self.padx)
        Label(self.frame_input, text="path_1:", width=self.width_row_0, anchor="w").grid(row=2, column=0, padx=self.padx)

        self.entry_value_1 = Entry(self.frame_input, width=self.width_row_1+2, justify="center")
        self.entry_value_1.grid(row=0,column=1)
        self.entry_value_1.insert(0, self.value_1)

        self.entry_value_2 = Entry(self.frame_input, width=self.width_row_1+2, justify="center")
        self.entry_value_2.grid(row=1,column=1)
        self.entry_value_2.insert(0, self.value_2)

        self.label_path_1 = Label(self.frame_input, text=self.path_1, width=self.width_row_1, relief=SUNKEN, anchor="e")
        self.label_path_1.grid(row=2,column=1, padx=self.padx)

        Button(self.frame_input, text="...", width=self.width_button_1, command=lambda: self.func_path_file(self.label_path_1, self_variable=nameof(self.path_1))).grid(row=2, column=2, padx=self.padx)
        Button(self.frame_button, text="Run", width=self.width_row_0, command=lambda: self.func_run(func_test)).grid(row=1, column=0)
        Button(self.frame_button, text="Clear", width=self.width_row_0, command=self.func_clear).grid(row=2, column=0)
        Button(self.frame_button, text="Close", width=self.width_row_0, command=quit).grid(row=3, column=0)

    def func_path_file(self, label: Label, self_variable: str = "", name: str = "Select File") -> None:
        """
        Select path of file and set label and self variable
        Args:
            label:          label to set
            self_variable:  self variable to set
            name:           name of select window
        Retrun:
            None
        """
        path = filedialog.askopenfilename(initialdir="", title=name, filetypes=(("all files","*.*"),("text","*.txt")))
        label.config(text=path)
        if self_variable:
            setattr(self, self_variable, path)
    
    def func_run(self, func) -> None:
        """
        Run funciton
        Args:
            func:   function to run
        Returns:
            None
        """
        # get value
        self.value_1 = self.entry_value_1.get()
        self.value_2 = self.entry_value_2.get()
        self.path_1 = self.label_path_1.cget("text")

        # run function
        self.func_show(f"start {func.__name__}")
        res = func(self.value_1, float(self.value_2), self.path_1)
        self.func_show(f"result {res}")
        self.func_show(f"end {func.__name__}")

    def func_show(self, text) -> None:
        """
        Show text in text box
        Args:
            text: string to show
        Returns:
            None
        """
        self.text_box.config(state=NORMAL)
        self.text_box.insert(INSERT, f"--> {text}\n")
        self.text_box.config(state=DISABLED)

    def func_clear(self) -> None:
        """
        Clear values and widgets
        Args:

        Returns:
            None
        """
        # clear value
        self.value_1 = ""
        self.value_2 = ""
        self.path_1 = ""

        # clear widget
        self.entry_value_1.delete(0, 'end')
        self.entry_value_2.delete(0, 'end')
        self.entry_value_1.insert(0, self.value_1)
        self.entry_value_2.insert(0, self.value_2)
        self.label_path_1.config(text=self.path_1)
        self.text_box.config(state=NORMAL)
        self.text_box.delete('0.0', END)
        self.text_box.config(state=DISABLED)


if __name__ == "__main__":
    root = Tk()
    gui_00 = GUI(root)
    root.mainloop()
