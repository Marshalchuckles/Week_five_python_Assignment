# smartphone_class.py

class Smartphone:
    # Constructor to initialize the object
    def __init__(self, brand, model, battery_level):
        self.brand = brand
        self.model = model
        self.battery_level = battery_level
    
    # Method to make a call
    def make_call(self, number):
        print(f"Calling {number} from {self.model}...")
    
    # Method to charge the battery
    def charge_battery(self):
        self.battery_level = 100
        print(f"{self.model} is now fully charged!")
    
    # Method to display battery status
    def check_battery(self):
        print(f"Battery level of {self.model}: {self.battery_level}%")

# Inheriting Smartphone class to add camera functionality
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_level, camera_quality):
        super().__init__(brand, model, battery_level)
        self.camera_quality = camera_quality
    
    # Overriding the make_call method
    def make_call(self, number):
        super().make_call(number)
        print(f"Taking a selfie before the call with {self.camera_quality} quality camera!")

# Create instances of each class
phone1 = Smartphone("Apple", "iPhone 13", 85)
phone2 = SmartphoneWithCamera("Samsung", "Galaxy S21", 60, "108MP")

# Using the methods
phone1.make_call("0714025935")
phone1.check_battery()
phone1.charge_battery()

phone2.make_call("0725132633")
phone2.check_battery()
