import numpy as np
import pandas as pd

from tkinter import *
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


class GUI:
    """
    Show clipped data
    """

    def __init__(self, master) -> None:
        master.title("clip")

        # value
        self.column = [
            "original",
            "clipped",
            "%"
        ]
        self.row = [
            "c",
            "cc",
            "2c",
            "n"
        ]
        self.bins = 50
        self.label_x = r"$value$"
        self.slider_to = 51
        self.slider_values = np.arange(self.slider_to + 1)
        self.values = np.zeros((len(self.row), self.slider_to + 1))
        self.step = None

        # frame
        self.padx_frame_in = 10
        self.pady_frame_in = 10
        self.padx_frame_out = 15
        self.pady_frame_out = 15

        self.frame_input = LabelFrame(master, text="input", padx=self.padx_frame_in, pady=self.pady_frame_in)
        self.frame_input.grid(row=0, column=0, padx=self.padx_frame_out, pady=self.pady_frame_out, sticky=N+W+E+S)

        self.frame_value = LabelFrame(master, text="value", padx=self.padx_frame_in, pady=self.pady_frame_in)
        self.frame_value.grid(row=0, column=1, padx=self.padx_frame_out, pady=self.pady_frame_out, sticky=N+W+E+S)

        self.frame_plot = LabelFrame(master, text="plot", padx=self.padx_frame_in, pady=self.pady_frame_in)
        self.frame_plot.grid(row=1, column=0, columnspan=2, padx=self.padx_frame_out, pady=self.pady_frame_out, sticky=N+W+E+S)

        # widget input
        Label(self.frame_input, text="data:", width=5, anchor="w").grid(row=0, column=0)

        self.label_path_input = Label(self.frame_input, text="", width=13, relief=SUNKEN, anchor="c")
        self.label_path_input.grid(row=0,column=1)

        Button(self.frame_input, text="...", width=5, command=self.func_select_file).grid(row=0, column=2)

        self.slider_value = IntVar()
        self.slider_value.set(self.slider_to)
        self.slider = Scale(self.frame_input, from_=0, to=self.slider_to, orient="horizontal", length=185, command=self.func_slider_changed, variable=self.slider_value)
        self.slider.grid(row=1, column=0, columnspan=3)

        Label(self.frame_input, text="clip:", width=3).grid(row=2, column=0)

        self.clip = Label(self.frame_input, text="...", width=20, anchor="w")
        self.clip.grid(row=2, column=1, columnspan=2)

        # widget table
        self.table = []
        for m, r in enumerate(self.row):
            Label(self.frame_value, text=f"{r}:", width=5, anchor="w").grid(row=m+1, column=0)
            tmp_table_row = []
            for n, c in enumerate(self.column):
                if m == 0:
                    Label(self.frame_value, text=c, width=10, anchor="c").grid(row=0, column=n+1)
                tmp = Label(self.frame_value, text="", width=10, relief=SUNKEN, anchor="e")
                tmp.grid(row=m+1,column=n+1, padx=1)
                tmp_table_row.append(tmp)
            self.table.append(tmp_table_row)

        # widget plot
        self.fig = Figure(figsize=(5, 5), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame_plot)
        self.canvas.draw()
        toolbar = NavigationToolbar2Tk(self.canvas, self.frame_plot)
        toolbar.update()
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    def func_select_file(self) -> None:
        """
        Select csv, calculate values and craate plots
        """
        # get path of csv of data
        path = filedialog.askopenfilename(initialdir="", title="Select File", filetypes=(("all files","*.*"),("csv","*.csv")))

        # derive name from path
        self.label_path_input.config(text=path.split("/")[-1].split(".")[0])

        # get value from csv
        self.data_original = self.func_get_data(path_csv=path)

        # calculate step
        self.step = int(max(abs(self.data_original["a"])) / (self.slider_to - 1) + 1)

        # calc values
        self.func_calc_values()

        # set values of table
        self.func_set_table()

        # clear figure
        self.fig.clf()

        # get plot
        self.func_create_plot(True)

    def func_calc_values(self) -> None:
        """
        Calculate values for every step
        """
        for tmp_slider_value in self.slider_values:
            tmp_clip = tmp_slider_value * self.step
            tmp_res = self.func_calc_something(a=self.data_original["a"], b=self.data_original["b"], clip=[-tmp_clip, tmp_clip])
            for i, v in enumerate(tmp_res.values()):
                self.values[i][tmp_slider_value] = v

    def func_set_table(self, slider_value: int = -1) -> None:
        """
        Set values of table
        """
        for i, (v_original, v) in enumerate(zip(self.values[:, -1], self.values[:, slider_value])):
            tmp_text = f"{v:.3e}"
            if i == len(self.row) - 1:
                tmp_text = str(int(v))
            if slider_value == -1:
                self.table[i][0].config(text=tmp_text)
            self.table[i][1].config(text=tmp_text)
            self.table[i][2].config(text=f"{v / v_original * 100:.3f}")

    def func_get_data(self, path_csv: str) -> dict:
        """
        Get data from csv and return as dictionary
        """
        # read csv
        df = pd.read_csv(path_csv, sep=",", header=0)

        # get value as list
        a = df["a"].values.tolist()
        b = df["b"].values.tolist()

        # return data as dictionary
        return {
            "a": np.array(a),
            "b": np.array(b)
        }

    def func_calc_something(self, a: list, b: list, clip: list) -> dict:
        """
        Calculate something
        """
        # mask to clip
        mask_min = a > clip[0]
        mask_max = a < clip[1]
        mask = mask_min * mask_max
        a = a[mask]
        b = b[mask]

        # calculate results
        c = a + b
        cc = a**2 + b**2
        n = len(a)

        # return results as dictionary
        return {
            "c": sum(c),
            "cc": sum(cc),
            "2c": 2 * sum(c),
            "n": n
        }

    def func_create_plot(self, first: bool = False) -> None:
        """
        Create plot
        """
        # get values to plot
        slider_value, clip = self.func_get_clip()
        x = self.data_original["a"]
        x_slider = self.slider_values * self.step
        m = 1.1
        max_x = max(x_slider) * m
        max_x_clip = max(clip) * m
        color_ax_3_r = "g"

        # mask to clip
        mask_min = x > clip[0]
        mask_max = x < clip[1]
        mask = mask_min * mask_max
        x_clip = x[mask]

        # plot histogram and set figures - first
        if first:
            self.ax_1 = self.fig.add_subplot(3, 1, 1)
            self.ax_2 = self.fig.add_subplot(3, 1, 2)
            self.ax_3_l = self.fig.add_subplot(3, 1, 3)
            self.ax_3_r = self.ax_3_l.twinx()

            self.ax_1.hist(x, bins=self.bins, edgecolor="black", linewidth=1.2, alpha=0.75)
            self.ax_3_l.plot(x_slider, self.values[-1], color="black", label=r"$n$")
            self.ax_3_r.plot(x_slider, self.values[0], color=color_ax_3_r, linestyle="--", label=r"$c$")

            self.ax_1.set_xlabel(self.label_x)
            self.ax_3_l.set_xlabel(r"$clip_{max}$")
            self.ax_1.set_ylabel(r"$n$")
            self.ax_3_l.set_ylabel(r"$n$")
            self.ax_3_r.set_ylabel(r"$c$", color=color_ax_3_r)

            self.ax_1.set_title(f"{r'$n_{all}$'} = {int(self.values[-1][-1])}")

            self.ax_1.ticklabel_format(style="sci", axis="x", scilimits=(0, 0))
            self.ax_3_l.ticklabel_format(style="sci", axis="x", scilimits=(0, 0))
            self.ax_1.ticklabel_format(style="sci", axis="y", scilimits=(0, 0))
            self.ax_3_r.ticklabel_format(style="sci", axis="y", scilimits=(0, 0))
            self.ax_3_l.ticklabel_format(style="sci", axis="y", scilimits=(0, 0))
            self.ax_3_r.tick_params(axis='y', labelcolor=color_ax_3_r)

            self.ax_1.set_xlim([-max_x, max_x])

            lines_l, labels_l = self.ax_3_l.get_legend_handles_labels()
            lines_r, labels_r = self.ax_3_r.get_legend_handles_labels()
            self.ax_3_l.legend(lines_l + lines_r, labels_l + labels_r, loc=4, labelcolor="linecolor")

            self.ax_1.grid()
            self.ax_3_l.grid()

        # plot histogram and set figures - steps
        self.ax_2.cla()

        self.ax_2.hist(x_clip, bins=self.bins, edgecolor="black", linewidth=1.2, alpha=0.75)
        self.ax_2.set_xlabel(self.label_x)

        self.ax_2.set_ylabel(r"$n$")

        self.ax_2.set_title(f"{r'$n_{clipped}$'} = {int(self.values[-1][slider_value])}")

        self.ax_2.ticklabel_format(style="sci", axis="x", scilimits=(0, 0))
        self.ax_2.ticklabel_format(style="sci", axis="y", scilimits=(0, 0))

        self.ax_2.set_xlim([-max_x_clip, max_x_clip])

        self.ax_2.grid()

        self.fig.tight_layout()

        # remove previous clip lines
        while len(self.ax_1.lines) > 0:
            del self.ax_1.lines[-1]
        while len(self.ax_3_l.lines) > 1:
            del self.ax_3_l.lines[-1]

        # create clip lines
        for c in clip:
            self.ax_1.axvline(x=c, color="r", linestyle="-")
            self.ax_2.axvline(x=c, color="r", linestyle="-")
        self.ax_3_l.axvline(x=c, color="r", linestyle="-")

        # draw plots
        self.canvas.draw()

    def func_slider_changed(self, whyisthisneeded) -> None:
        """
        Set vlues of table and update plots
        """
        # Set values of table
        self.func_set_table(self.slider_value.get())

        # update plots
        self.func_create_plot()

    def func_get_clip(self) -> tuple:
        """
        Return value of slider and clip
        """
        # get value of slider
        slider_value = self.slider_value.get()

        # calculate maximum of clip and clip
        v = slider_value * self.step
        clip = [-v, v]

        # set text of clip
        self.clip.configure(text=f"{slider_value} x {self.step} = {v:.3e}")

        # return value of slider and clip
        return slider_value, clip


if __name__ == "__main__":
    # value
    np.random.seed(1)
    n = 10_000
    mu_a = 4500
    sigma_a = 1_500_000
    a = mu_a + sigma_a * np.random.randn(n)
    mu_b = 4500
    sigma_b = 2_500_000
    b = mu_b + sigma_b * np.random.randn(n)
    values_dict = {
        "a": a,
        "b": b
    }
    values_df = pd.DataFrame(values_dict)
    values_df.to_csv(r"GUI_clip_plot_00.csv")

    # plot
    import matplotlib.pyplot as plt
    fig, axs = plt.subplots(2)
    axs[0].hist(a, 50, density=True, edgecolor="black", linewidth=1.2, alpha=0.75)
    axs[1].hist(b, 50, density=True, edgecolor="black", linewidth=1.2, alpha=0.75)
    plt.show()

    # test
    root = Tk()
    gui = GUI(root)
    root.mainloop()
