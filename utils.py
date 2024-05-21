from functools import partial
import matplotlib.pyplot as plt
import numpy
import pandas

canvas = None
canvas_aux = None


def create_partial_function(handler, **kwargs):
    return partial(handler, **kwargs)


def react_to_keys(years_vector, temperatures_vector,
                  a3, a2, a1, a0,
                  year_min, year_mid, year_max,
                  callback):
    partial_on_key_pressed = create_partial_function(callback,
                                                     years_vector=years_vector,
                                                     temperatures_vector=temperatures_vector,
                                                     a3=a3, a2=a2, a1=a1, a0=a0,
                                                     year_min=year_min, year_mid=year_mid, year_max=year_max)
    canvas.canvas.mpl_connect('key_press_event', partial_on_key_pressed)
    plt.show()


def create_drawing_canvas(x_min, x_max, y_min, y_max, x_label, y_label, fig_label):
    global canvas, canvas_aux
    canvas, canvas_aux = plt.subplots(figsize=(10, 6))
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(fig_label)
    plt.legend()
    plt.ylim(y_min, y_max)
    plt.xlim(x_min, x_max)


def line_plot(x_vector, y_vector, label, color):
    plt.plot(x_vector, y_vector, label=label, color=color)
    canvas.canvas.draw()
    plt.show()


def scatter_plot(x_vector, y_vector, label, color):
    canvas_aux.scatter(x_vector, y_vector, label=label, color=color)
    canvas.canvas.draw()
    plt.show()

def create_vector_with_zeroes(size):
    return numpy.zeros(size)

def create_vector_with_sequence(max):
    return numpy.arange(max)

def read_columm_from_datafile(datafile_path, column_name):
    data_file = pandas.read_csv(datafile_path)
    return data_file[column_name].to_numpy(dtype=float)

def fit_polynomial(x_vector, y_vector):
    [a3, a2, a1, a0] = numpy.polyfit(x_vector, y_vector, 3)
    return [a3, a2, a1, a0]
