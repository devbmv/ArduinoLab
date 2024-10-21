from django.db import models

# Manufacturer Model
class Manufacturer(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

# Microcontroller Family Model
class MicrocontrollerFamily(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='families', null=True)

    def __str__(self):
        return f"{self.name} ({self.manufacturer.name})"

# Microcontroller Subfamily Model
class MicrocontrollerSubfamily(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    family = models.ForeignKey(MicrocontrollerFamily, on_delete=models.CASCADE, related_name='subfamilies', null=True)

    def __str__(self):
        return f"{self.name} ({self.family.name})"

# Microcontroller Model
class Microcontroller(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(MicrocontrollerSubfamily, on_delete=models.CASCADE, related_name='microcontrollers', null=True)
    bit_width = models.PositiveIntegerField(choices=[(8, '8-bit'), (16, '16-bit'), (32, '32-bit')], null=True, blank=True)
    cpu_architecture = models.CharField(max_length=100, null=True, blank=True)
    max_frequency_mhz = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    ram_kb = models.PositiveIntegerField(help_text='RAM capacity in KB', null=True, blank=True)
    flash_memory_kb = models.PositiveIntegerField(help_text='Flash memory capacity in KB', null=True, blank=True)
    power_consumption_mw = models.DecimalField(max_digits=10, decimal_places=2, help_text='Power consumption in milliwatts', null=True, blank=True)
    package_type = models.CharField(max_length=50, choices=[('DIP', 'DIP'), ('QFP', 'QFP'), ('BGA', 'BGA'), ('TSSOP', 'TSSOP')], null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2,null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.name

# Peripheral Model
class Peripheral(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Microcontroller-Peripheral Association (Many-to-Many Relationship)
class MicrocontrollerPeripheral(models.Model):
    microcontroller = models.ForeignKey(Microcontroller, on_delete=models.CASCADE, null=True)
    peripheral = models.ForeignKey(Peripheral, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1, null=True, blank=True)

    class Meta:
        unique_together = ('microcontroller', 'peripheral')

    def __str__(self):
        return f"{self.microcontroller.name} - {self.peripheral.name}"

# Additional Features for Microcontrollers
class Features(models.Model):
    microcontroller = models.OneToOneField(Microcontroller, on_delete=models.CASCADE, related_name='features', null=True)
    has_eeprom = models.BooleanField(default=False, null=True, blank=True)
    has_adc = models.BooleanField(default=False, null=True, blank=True)
    has_dac = models.BooleanField(default=False, null=True, blank=True)
    pwm_pins = models.PositiveIntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f"Features {self.microcontroller.name}"

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
