from functools import partial
import matplotlib.pyplot as plt
import numpy
import pandas

canvas = None
canvas_aux = None
x_max_global = 0

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

def set_graph(x_label, y_label, x_min, x_max, y_min, y_max):
    global x_max_global, x_min_global
    x_max_global = x_max
    x_min_global = x_min
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xlim(x_min,x_max)
    plt.ylim(y_min,y_max)
    
def view_curve(x_vector, y_vector, color):
    plt.plot(x_vector, y_vector, color=color)

def view_polynomial(a3, a2, a1, a0, color):
    x_vector = create_vector_with_sequence(max=x_max_global)
    y_vector = create_vector_with_zeroes(size=x_max_global)
    for x in x_vector:
        y_vector[x] = a0 + a1 * x + a2 * x ** 2 + a3 * x ** 3
    plt.plot(x_vector, y_vector, color=color)


def view_scatter(x_vector, y_vector, color):
    plt.scatter(x_vector, y_vector, color=color)

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
