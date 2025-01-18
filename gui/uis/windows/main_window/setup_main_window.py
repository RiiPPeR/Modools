# IMPORT PACKAGES AND MODULES
from gui.core.functions import Functions
from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from . functions_main_window import *
import sys
import os

# IMPORT QT CORE
from qt_core import *

# IMPORT SETTINGS
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
from gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
from gui.widgets import *

# LOAD UI MAIN
from .functions_main_window import MainFunctions
from . ui_main import *

# MAIN FUNCTIONS 
from . functions_main_window import *

# PY WINDOW
class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # ADD LEFT MENUS
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon" : "icon_home.svg",
            "btn_id" : "btn_home",
            "btn_text" : "Inicio",
            "btn_tooltip" : "Inicio",
            "show_top" : True,
            "is_active" : True
        },
        {
            "btn_icon" : "person-vcard.svg",
            "btn_id" : "btn_crm",
            "btn_text" : "CRM",
            "btn_tooltip" : "Gestión de clientes",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "cart.svg",
            "btn_id" : "btn_ventas",
            "btn_text" : "Ventas",
            "btn_tooltip" : "Pedidos, facturas, ventas...",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "minecart.svg",
            "btn_id" : "btn_fabricacion",
            "btn_text" : "Fabricación",
            "btn_tooltip" : "Ordenes de producción, materiales...",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "box-seam.svg",
            "btn_id" : "btn_inventario",
            "btn_text" : "Inventario",
            "btn_tooltip" : "Productos, alertas, stock...",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "people.svg",
            "btn_id" : "btn_empleados",
            "btn_text" : "Empleados",
            "btn_tooltip" : "Datos personales, roles...",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "bar-chart-line.svg",
            "btn_id" : "btn_contabilidad",
            "btn_text" : "Contabilidad",
            "btn_tooltip" : "Ingresos, gastos, reportes...",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "wrench.svg",
            "btn_id" : "btn_manteniminento",
            "btn_text" : "Mantenimiento",
            "btn_tooltip" : "Incidencias, instalaciones...",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "calendar3.svg",
            "btn_id" : "btn_proyectos",
            "btn_text" : "Proyectos",
            "btn_tooltip" : "Proyectos, tareas...",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "shop.svg",
            "btn_id" : "btn_compras",
            "btn_text" : "Compras",
            "btn_tooltip" : "Proveedores, ordenes de compra...",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "router.svg",
            "btn_id" : "btn_web",
            "btn_text" : "WEB",
            "btn_tooltip" : "Página web pública",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "tpv.svg",
            "btn_id" : "btn_tpv",
            "btn_text" : "TPV",
            "btn_tooltip" : "Terminal punto de venta",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_info.svg",
            "btn_id" : "btn_menu_2",
            "btn_text" : "Open Info",
            "btn_tooltip" : "Open Info",
            "show_top" : False,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_settings.svg",
            "btn_id" : "btn_settings",
            "btn_text" : "Open Settings",
            "btn_tooltip" : "Open Settings",
            "show_top" : False,
            "is_active" : False
        }
    ]

     # ADD TITLE BAR MENUS
    # ///////////////////////////////////////////////////////////////
    add_title_bar_menus = [
        {
            "btn_icon" : "icon_search.svg",
            "btn_id" : "btn_search",
            "btn_tooltip" : "Buscar",
            "is_active" : False
        },
        {
            "btn_icon" : "icon_signal.svg",
            "btn_id" : "btn_top_settings",
            "btn_tooltip" : "Ayuda",
            "is_active" : False
        }
    ]

    # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
    # Get sender() function when btn is clicked
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])
        
        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # SET SIGNALS
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # ADD Title
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Welcome to PyOneDark")

        # LEFT COLUMN SET SIGNALS
        # ///////////////////////////////////////////////////////////////
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self, self.ui.load_pages.page_1)
        MainFunctions.set_left_column_menu(
            self,
            menu = self.ui.left_column.menus.menu_1,
            title = "Settings Left Column",
            icon_path = Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        # ///////////////////////////////////////////////////////////////
        # EXAMPLE CUSTOM WIDGETS
        # Here are added the custom widgets to pages and columns that
        # were created using Qt Designer.
        # This is just an example and should be deleted when creating
        # your application.
        #
        # OBJECTS FOR LOAD PAGES, LEFT AND RIGHT COLUMNS
        # You can access objects inside Qt Designer projects using
        # the objects below:
        #
        # <OBJECTS>
        # LEFT COLUMN: self.ui.left_column.menus
        # RIGHT COLUMN: self.ui.right_column
        # LOAD PAGES: self.ui.load_pages
        # </OBJECTS>
        # ///////////////////////////////////////////////////////////////

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items
        
        # ADD CUSTOM WIDGETS
        self.btn_1 = PyPushButton(
            text = "Btn 1",
            radius= 8,
            color = self.themes["app_color"]["text_foreground"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["dark_four"],
        )
        self.btn_1.setMinimumHeight(40)
        
        # ADD TO LAYOUT
        self.ui.left_column.menus.btn_1_layout.addWidget(self.btn_1)
        
        # ADD TOGGLE BUTTON
        self.toggle_1 = PyToggle(
            active_color = self.themes["app_color"]["context_color"],
            bg_color = self.themes["app_color"]["dark_one"],
            circle_color = self.themes["app_color"]["icon_color"],
            width = 50,
        )
        
        # ADD TO LAYOUT
        self.ui.left_column.menus.btn_2_layout.addWidget(self.toggle_1, Qt.AlignmentFlag.AlignCenter, Qt.AlignmentFlag.AlignCenter)
        
        # HOME
        # ADD DEFAULT WIDGET
        self.line_edit = QLineEdit()
        self.button = QPushButton("Enviar") 
        
        def print_text():
            print(self.line_edit.text())
            self.line_edit.setText("")
            
        self.button.clicked.connect(print_text)
        
        # ADD TO LAYOUT
        self.ui.load_pages.page_1_layout.addWidget(self.line_edit, Qt.AlignmentFlag.AlignCenter, Qt.AlignmentFlag.AlignCenter)
        self.ui.load_pages.page_1_layout.addWidget(self.button, Qt.AlignmentFlag.AlignCenter, Qt.AlignmentFlag.AlignCenter)
        

        # ///////////////////////////////////////////////////////////////
        # END - EXAMPLE CUSTOM WIDGETS
        # ///////////////////////////////////////////////////////////////

    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)