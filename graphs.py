# Импортируем модули из библиотеки Python
import pylab
import numpy


# Рисуем график этой функции
def func(x):
    return (x ** 3) - 2 * (x ** 2) + 1


# Интервал изменения переменной по оси X
if __name__ == '__main__':
    x_min = 2
    x_max = 2.7

    # Шаг между точками
    h = 0.02

    # Создадаем список координат по оси X
    xlist = numpy.arange(x_min, x_max, h)

    # Вычисляем значение функции в заданных точках
    ylist = [round(func(x), 2) for x in xlist]

    # Рисуем график
    pylab.plot(xlist, ylist, 'b-', label="X" + str(xlist))
    pylab.plot(xlist, ylist, 'b-', label="Y" + str(ylist))

    # Выводим легенду
    legend = pylab.legend()

    # Разрешим перемещать легенду
    legend.set_draggable(True)

    # Выводим окно с нарисованным графиком
    pylab.grid()
    pylab.show()
