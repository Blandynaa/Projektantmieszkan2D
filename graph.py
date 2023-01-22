import sys
import matplotlib

matplotlib.use("Qt5Agg")
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QPoint, QEvent
from PyQt5.QtGui import QMouseEvent
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# Personnal modules
from drag import DraggablePoint
from mebell import DraggableImage


class MyGraph(FigureCanvas):
    """A canvas that updates itself every second with a new plot."""

    def __init__(self, parent, width=18, height=12, dpi=80):
        self.parent = parent
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        self.axes.set_xlim(0, 30)
        self.axes.set_ylim(0, 20)
        self.axes.locator_params(axis='x', nbins=30)
        self.axes.locator_params(axis='y', nbins=20)
        self.axes.grid(True)

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self.list_points = []
        self.list_images = []
        # self.list_points   #= self.parent.list_points
        # print(self.list_points)

        self.show()
        # self.plotFirstPoint()
        # self.plotDraggablePoints()
        # self.plotDraggablePoints2(2, 2)
        # self.add_image()
        # self.list_points.pop(-1)
        # self.updateFigure()
    #
    # def add_image(self):
    #     print("Dodawanie obrazka")
    #     #image_path = 'C:\Users\win10\Desktop\zrzut.jpg'
    #     self.list_images.append(DraggableImage(self))
    #     self.updateFigure()
    #     print("koniec dodawania obrazka")

    def plotFirstPoint(self, size=1):
        """Plot and define the 2 draggable points of the baseline"""
        print("Dodanie początkowego punktu:")
        # del(self.list_points[:])
        self.list_points.append(DraggablePoint(self, 2, 2, size))
        print("Dodano 1. punkt")
        self.updateFigure()
        self.parent.list_points = self.list_points

    def plotDraggablePoints(self, size=1):
        """Plot and define the 2 draggable points of the baseline"""
        print("Rozpoczecie dodawania:")
        # del(self.list_points[:])
        self.list_points.append(DraggablePoint(self, 5, 5, size))
        print("Dodano 1. punkt")
        self.list_points.append(DraggablePoint(self, 10, 10, size))
        print("Dodano 2. punkt")
        # self.list_points.append(DraggablePoint(self, 15, 10, size))
        # print("Dodano 3. punkt")
        # self.list_points.append(DraggablePoint(self, 20, 10, size))
        # print("Dodano 4. punkt")
        # self.list_points.append(DraggablePoint(self, 20, 5, size))
        # self.list_points.append(self.list_points[0])
        # print("Dodano 5. punkt")
        self.updateFigure()
        self.parent.list_points = self.list_points

    def plotDraggablePoints2(self, x, y):
        """Plot and define the 2 draggable points of the baseline"""
        print("Rozpoczecie dodawania:")
        # del(self.list_points[:])
        self.list_points.append(DraggablePoint(self, x, y, 1))
        print("2Dodano 1. punkt")
        # self.list_points.append(DraggablePoint(self, 10, 10, 1))
        # print("2Dodano 2. punkt")
        self.updateFigure()
        self.parent.list_points = self.list_points
        print("Lista parenta po 2 dodaniu punktow:", self.parent.list_points)

    def clearFigure(self):
        """Clear the graph"""

        self.axes.clear()
        self.axes.set_xlim(0, 30)
        self.axes.set_ylim(0, 20)
        self.axes.locator_params(axis='x', nbins=30)
        self.axes.locator_params(axis='y', nbins=20)
        self.axes.grid(True)
        del (self.list_points[:])
        self.updateFigure()

    def updateFigure(self):
        """Update the graph. Necessary, to call after each plot"""

        self.draw()

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        x = event.x()
        y = self.fig.canvas.height() - event.y()
        point = self.axes.transData.inverted().transform((x, y))
        x, y = point[0], point[1]
        size = 1  # Default size of the point
        self.list_points.append(DraggablePoint(self, x, y, size))
        self.list_images.append(DraggableImage(self))
        print("lista obrazkow", self.list_images)

        self.updateFigure()

    # def mouseDoubleClickEvent(self, event: QMouseEvent):
    #     # TODO add the point when clicked
    # x = event.x()
    # y = event.y()
    # x = event.windowPos().x()
    # y = event.windowPos().y()
    # x = event.pos().x()
    # y = event.pos().y()
    # self.
    # print("x y ", x, y)
    # print("Lista punktów myszkax2: ", self.list_points)
    # self.list_points.append(DraggablePoint(self, x, y, 3))
    # print("mouse Dodano 2. punkt")
    # print("Lista punktów myszkax2: ", self.list_points)
    # self.updateFigure()
    # print("Lista punktów myszkax2: ", self.list_points)
    # super().mouseDoubleClickEvent(event)
    # print("Lista punktów myszkax2: ", self.list_points)

# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     ex = MyGraph()
#     sys.exit(app.exec_())
