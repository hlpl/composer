from   PyQt5.QtCore    import *
from   PyQt5.QtGui     import *
from   PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from hlpl_composer.hlpl_functions import *

import hlpl_composer.images as images
dirx=os.path.dirname(images.__file__)

class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        QBtn = QDialogButtonBox.Ok  # No cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.setWindowTitle("Human Life Programming Language")

        layout = QVBoxLayout()

        title = QLabel("HLPL Composer")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)
        layout.addWidget(title)

        title = QLabel("HLPL Composer is a software composes similar and opposit texts based on synonyms and antonyms.\n  Furthermore, the sofwtare analyses texts templates graphically based on coordinates")
        font = title.font()
        font.setPointSize(14)
        title.setFont(font)
        layout.addWidget(title)
        
        logo = QLabel()
        logo.setPixmap(QPixmap(os.path.join(dirx, 'composer.png')))
        layout.addWidget(logo)

        layout.addWidget(QLabel("Version 1.1.0"))
        layout.addWidget(QLabel("© Copyright 2022 Human Life Programming Language"))

        for i in range(0, layout.count()):
            layout.itemAt(i).setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)


class LicenseDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(LicenseDialog, self).__init__(*args, **kwargs)

        QBtn = QDialogButtonBox.Ok  # No cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.setWindowTitle("Human Life Programming Language")

        layout = QVBoxLayout()

        title = QLabel("MIT License")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)
        layout.addWidget(title)

        title = QLabel("HLPL Composer is licensed under MIT License,\n it is a free open source software.")
        font = title.font()
        font.setPointSize(14)
        title.setFont(font)
        layout.addWidget(title)
        
        logo = QLabel()
        logo.setPixmap(QPixmap(os.path.join(dirx, 'composer.png')))
        layout.addWidget(logo)

        layout.addWidget(QLabel("Version 1.1.0"))
        layout.addWidget(QLabel("© Copyright 2022 Human Life Programming Language"))

        for i in range(0, layout.count()):
            layout.itemAt(i).setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)

















