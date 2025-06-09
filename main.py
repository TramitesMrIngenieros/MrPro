from kivy.config import Config
# Configuración responsive para múltiples dispositivos
from kivy.metrics import dp
from kivy.core.window import Window

# No fijar tamaño específico - será responsive
# Config.set('graphics', 'width', '360')
# Config.set('graphics', 'height', '640')

# Configuraciones para móviles
Config.set('graphics', 'multisamples', '0')  # Mejor rendimiento en móviles
Config.set('graphics', 'resizable', '1')     # Permitir redimensionar
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')  # Soporte touch

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from screens import LoginScreen, RegisterScreen, ProfileScreen, MenuScreen, AdminScreen, SolicitudesScreen, AprobacionScreen, RolesScreen, JerarquiaScreen
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty
import os
from mobile_improvements import initialize_mobile_optimizations

class LoginApp(MDApp):
    def build(self):
        # Configuración de tema responsive
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.material_style = "M3"  # Material Design 3 más moderno
        
        # Configurar ventana responsive
        self.setup_responsive_window()
        
        # Inicializar optimizaciones móviles
        self.mobile_sizes = initialize_mobile_optimizations(self)
        
        # Cargar estilos móviles primero
        Builder.load_file('mobile_styles.kv')
        
        Builder.load_file('loginscreen.kv')
        Builder.load_file('registerscreen.kv')
        Builder.load_file('profilescreen.kv')
        Builder.load_file('adminscreen.kv')
        Builder.load_file('menuscreen.kv')
        Builder.load_file('solicitudes.kv')
        Builder.load_file('aprobacion.kv')
        Builder.load_file('roles.kv')
        Builder.load_file('jerarquia.kv')
        self.sm = ScreenManager()
        self.sm.add_widget(LoginScreen(name='login'))
        self.sm.add_widget(RegisterScreen(name='register'))
        self.sm.add_widget(MenuScreen(name='menu'))
        self.sm.add_widget(ProfileScreen(name='profile'))
        self.sm.add_widget(AdminScreen(name='admin'))
        self.sm.add_widget(SolicitudesScreen(name='solicitudes'))
        self.sm.add_widget(AprobacionScreen(name='aprobacion'))
        self.sm.add_widget(RolesScreen(name='roles'))
        self.sm.add_widget(JerarquiaScreen(name='jerarquia'))
        
        self.setup_auto_reload()
        
        return self.sm

    def setup_responsive_window(self):
        """Configurar ventana responsive para diferentes dispositivos"""
        # Obtener tamaño de pantalla
        width = Window.width
        height = Window.height
        
        # Configurar tamaño mínimo
        Window.minimum_width = dp(320)
        Window.minimum_height = dp(480)
        
        # Si es escritorio, usar tamaño fijo razonable
        if width > 1000:  # Probablemente escritorio
            Window.size = (dp(400), dp(700))
        
        # Centrar ventana en escritorio
        if hasattr(Window, 'center_window'):
            Window.center_window = True

    def on_start(self):
        """Método que se ejecuta al iniciar la app"""
        # Configuraciones adicionales para móviles
        if hasattr(Window, 'softinput_mode'):
            Window.softinput_mode = "below_target"  # Mejor UX con teclado en móvil

    def setup_auto_reload(self):
        self.kv_files = ['mobile_styles.kv', 'loginscreen.kv', 'registerscreen.kv', 'profilescreen.kv', 'adminscreen.kv', 'menuscreen.kv', 'solicitudes.kv', 'aprobacion.kv', 'roles.kv', 'jerarquia.kv']
        self.last_modified = {f: os.path.getmtime(f) for f in self.kv_files}
        
        Clock.schedule_interval(self.check_for_changes, 1.0)

    def check_for_changes(self, dt):
        for kv_file in self.kv_files:
            try:
                current_mtime = os.path.getmtime(kv_file)
                if current_mtime != self.last_modified.get(kv_file):
                    print(f"Cambios detectados en {kv_file}")
                    self.last_modified[kv_file] = current_mtime
                    self.reload_kv_file(kv_file)
            except Exception as e:
                print(f"Error al verificar {kv_file}: {str(e)}")

    def reload_kv_file(self, kv_file):
        try:
            Builder.unload_file(kv_file)
            Builder.load_file(kv_file)
            
            current_screen = self.sm.current
            self.sm.clear_widgets()
            
            # Recargar estilos móviles primero
            Builder.load_file('mobile_styles.kv')
            
            self.sm.add_widget(LoginScreen(name='login'))
            self.sm.add_widget(RegisterScreen(name='register'))
            self.sm.add_widget(MenuScreen(name='menu'))
            self.sm.add_widget(ProfileScreen(name='profile'))
            self.sm.add_widget(AdminScreen(name='admin'))
            self.sm.add_widget(SolicitudesScreen(name='solicitudes'))
            self.sm.add_widget(AprobacionScreen(name='aprobacion'))
            self.sm.add_widget(RolesScreen(name='roles'))
            self.sm.add_widget(JerarquiaScreen(name='jerarquia'))
            
            self.sm.current = current_screen
            
            print(f"Archivo {kv_file} recargado exitosamente")
        except Exception as e:
            print(f"Error al recargar {kv_file}: {str(e)}")

if __name__ == '__main__':
    LoginApp().run()