from gui.uis.windows.main_window.functions_main_window import *
import sys
import os

# IMPORT QT CORE
from qt_core import *

# IMPORT SETTINGS
from gui.core.json_settings import Settings

# IMPORT PY ONE DARK WINDOWS
# MAIN WINDOW
from gui.uis.windows.main_window import *

# IMPORT PY ONE DARK WIDGETS
from gui.widgets import *

# ADJUST QT FONT DPI FOR HIGHT SCALE AN 4K MONITOR
os.environ["QT_FONT_DPI"] = "96"
# IF IS 4K MONITOR ENABLE 'os.environ["QT_SCALE_FACTOR"] = "2"'

# MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.hide_grips = True # Show/Hide resize grips
        SetupMainWindow.setup_gui(self)

        # SHOW MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.show()

    # LEFT MENU BTN IS CLICKED
    # Run function when btn is clicked
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)
        
        # LEFT MENU
        # ///////////////////////////////////////////////////////////////
        btn_dict = {
            "btn_home": self.ui.load_pages.page_1,
            "btn_crm": self.ui.load_pages.page_2,
            "btn_ventas": self.ui.load_pages.page_3,
            "btn_fabricacion": self.ui.load_pages.page_4,
            "btn_inventario": self.ui.load_pages.page_5,
            "btn_empleados": self.ui.load_pages.page_6,
            "btn_contabilidad": self.ui.load_pages.page_7,
            "btn_manteniminento": self.ui.load_pages.page_8,
            "btn_proyectos": self.ui.load_pages.page_9,
            "btn_compras": self.ui.load_pages.page_10
        }
        
        button = btn_dict.get(btn.objectName())
        if button:
            self.ui.left_menu.select_only_one(btn.objectName())
            MainFunctions.set_page(self, button)
            
        # GET TOP SETTINGS
        top_btn_settings = MainFunctions.get_title_bar_btn(self, "btn_top_settings")
            
        # OPEN INFO
        if btn.objectName() == "btn_menu_2" or btn.objectName() == "btn_close_left_column":
            # Disable Selection on title bar
            top_btn_settings.set_active(False)
            
            # Check if left column is not visible
            if not MainFunctions.left_column_is_visible(self):
                # Show/Hide 
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column": # This BTN is defualt btn of left column on TOP
                    # Deselect all tabs
                    self.ui.left_menu.deselect_all_tab()
                    
                    # Show / Hide
                    MainFunctions.toggle_left_column(self)
                    
                # Select tab
                self.ui.left_menu.select_only_one_tab(btn.objectName())
                
            # Change Left Page
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    self.ui.left_column.menus.menu_2,
                    title = "Info tab",
                    icon_path = Functions.set_svg_icon("icon_info.svg")
                )
            
        # OPEN SETTINGS
        if btn.objectName() == "btn_settings" or btn.objectName() == "btn_close_left_column":
            # Disable Selection on title bar
            top_btn_settings.set_active(False)
            
            # Check if left column is not visible
            if not MainFunctions.left_column_is_visible(self):
                # Show/Hide 
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column": # This BTN is defualt btn of left column on TOP
                    # Deselect all tabs
                    self.ui.left_menu.deselect_all_tab()
                    
                    # Show / Hide
                    MainFunctions.toggle_left_column(self)
                    
                # Select tab
                self.ui.left_menu.select_only_one_tab(btn.objectName())
                
            # Change Left Page
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    self.ui.left_column.menus.menu_1,
                    title = "Settings tab",
                    icon_path = Functions.set_svg_icon("icon_settings.svg")
                )
                
        
        
        # TITLE BAR MENU
        # ///////////////////////////////////////////////////////////////
        
        # SETTINGS TITLE BAR
        if btn.objectName() == "btn_top_settings":
            # Toogle Active
            if not MainFunctions.right_column_is_visible(self):
                btn.set_active(True)

                # Show / Hide
                MainFunctions.toggle_right_column(self)
            else:
                btn.set_active(False)

                # Show / Hide
                MainFunctions.toggle_right_column(self)

            # Get Left Menu Settings            
            btn_settings = MainFunctions.get_left_menu_btn(self, "btn_settings")
            btn_settings.set_active_tab(False)        
            
            # Get Left Menu Info            
            btn_info = MainFunctions.get_left_menu_btn(self, "btn_menu_2")
            btn_info.set_active_tab(False)     

        # DEBUG
        print(f"Button {btn.objectName()}, clicked!")

    # LEFT MENU BTN IS RELEASED
    # Run function when btn is released
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # DEBUG
        print(f"Button {btn.objectName()}, released!")

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()


# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()

    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec_())