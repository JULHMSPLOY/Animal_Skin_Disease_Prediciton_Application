import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.uix.modalview import ModalView
from kivy.clock import Clock
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import os
import shutil
from datetime import datetime

# Load the .kv file
Builder.load_file('asd.kv')

class PredictionBar(BoxLayout):
    disease_name = StringProperty('')
    probability = ObjectProperty(0)
    bar_color = ObjectProperty([0, 0, 0, 1])

class MainScreen(BoxLayout):
    selected_image_path = StringProperty('')
    model = None
    classes = ['bacterial', 'fungal', 'healthy', 'hypersensitivity']
    colors = {
        'bacterial': [0.9, 0.3, 0.3, 1],
        'fungal': [0.3, 0.7, 0.3, 1],
        'healthy': [0.3, 0.5, 0.9, 1],
        'hypersensitivity': [0.8, 0.8, 0.2, 1]
    }

    classes_dict = {
        'bacterial': 'Bacterial',
        'fungal': 'Fungal',
        'healthy': 'Healthy',
        'hypersensitivity': 'Hypersensitivity'
    }
    
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.ensure_uploaded_images_folder()
        self.load_model()
    
    def ensure_uploaded_images_folder(self):
        if not os.path.exists('uploaded_images'):
            os.makedirs('uploaded_images')
            
    def load_model(self):
        try:
            model_path = 'C:\\Users\\asus\\OneDrive\\Desktop\\เอกสาร\\241-202\\asdapp\\model2\\model_fit_23-0.84.keras'
            self.model = load_model(model_path)
            print("Model loaded successfully")
        except Exception as e:
            print(f"Failed to load model: {e}")
            self.show_error_popup(f"Failed to load model: {e}")
    
    def show_file_chooser(self):
        content = BoxLayout(orientation='vertical')
        file_chooser = FileChooserIconView(path='.', filters=['*.png', '*.jpg', '*.jpeg'])
        
        buttons = BoxLayout(size_hint_y=None, height=50, spacing=5)
        select_btn = Button(text="Select")
        cancel_btn = Button(text="Cancel")
        
        buttons.add_widget(select_btn)
        buttons.add_widget(cancel_btn)
        content.add_widget(file_chooser)
        content.add_widget(buttons)
        
        popup = Popup(title="Select Image", content=content, size_hint=(0.9, 0.9))
        
        def on_select(instance):
            if file_chooser.selection:
                self.process_selected_file(file_chooser.selection[0])
            popup.dismiss()
        
        select_btn.bind(on_release=on_select)
        cancel_btn.bind(on_release=popup.dismiss)
        popup.open()
    
    def process_selected_file(self, file_path):
        if not file_path or not os.path.exists(file_path):
            self.show_error_popup("Invalid file path or file does not exist.")
            return
        
        timestr = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_ext = os.path.splitext(file_path)[1]
        dest_file = f"uploaded_images/upload_{timestr}{file_ext}"
        
        try:
            shutil.copy2(file_path, dest_file)
            self.selected_image_path = dest_file
            self.ids.preview_image.source = dest_file
            self.ids.predict_button.disabled = False
        except Exception as e:
            self.show_error_popup(f"Failed to copy file: {e}")
    
    def predict(self):
        if not self.selected_image_path:
            self.show_error_popup("Please select an image first")
            return
        
        if not self.model:
            self.show_error_popup("Model not found for prediction")
            return
        
        self.ids.result_label.text = "Analyzing..."
        Clock.schedule_once(self.process_image, 0.1)
    
    def process_image(self, dt):
        try:
            img = load_img(self.selected_image_path, target_size=(224, 224))
            img_array = img_to_array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)
            
            predictions = self.model.predict(img_array)
            predicted_class_idx = np.argmax(predictions[0])
            confidence = float(predictions[0][predicted_class_idx])
            predicted_class = self.classes[predicted_class_idx]
            
            self.ids.result_label.text = f"Prediction: {self.classes_dict.get(predicted_class, predicted_class)} ({confidence * 100:.1f}%)"
            self.update_result_bars(predictions[0])
        except Exception as e:
            self.show_error_popup(f"Image processing error: {e}")
    
    def update_result_bars(self, predictions):
        self.ids.results_grid.clear_widgets()
        for i, cls in enumerate(self.classes):
            prob = float(predictions[i] * 100)
            bar = PredictionBar()
            bar.disease_name = self.classes_dict.get(cls, cls)
            bar.probability = prob
            bar.bar_color = self.colors.get(cls, [0.5, 0.5, 0.5, 1])
            self.ids.results_grid.add_widget(bar)
    
    def show_error_popup(self, message):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text=message))
        button = Button(text="OK", size_hint_y=None, height=40)
        content.add_widget(button)
        popup = Popup(title="Alert", content=content, size_hint=(0.7, 0.3))
        button.bind(on_release=popup.dismiss)
        popup.open()

class AnimalSkinDiseaseApp(App):
    def build(self):
        self.title = 'Animal Skin Disease Prediction App'
        return MainScreen()

if __name__ == '__main__':
    AnimalSkinDiseaseApp().run()

