from django.db import models
from django.urls import reverse
from django.utils import timezone


class Family(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Microcontroller(models.Model):
    """Model to represent a Microcontroller."""

    # SKU: Stock Keeping Unit - optional string field to store a unique identifier
    sku = models.CharField(max_length=254, null=True, blank=True)

    # Name of the microcontroller - optional
    name = models.CharField(max_length=100, null=True, blank=True)

    # Category is linked to the Family model via ForeignKey
    category = models.ForeignKey(
        Family,
        on_delete=models.CASCADE,
        related_name="microcontrollers",
        null=True,
        blank=True,
    )

    # Bit width of the microcontroller (typical values for microcontrollers)
    BIT_WIDTH_CHOICES = [
        (8, "8-bit"),
        (16, "16-bit"),
        (32, "32-bit"),
        (64, "64-bit"),
    ]
    bit_width = models.PositiveIntegerField(
        choices=BIT_WIDTH_CHOICES, null=True, blank=True
    )

    # CPU architecture (examples of common architectures for microcontrollers)
    CPU_ARCHITECTURE_CHOICES = [
        ("AVR", "AVR"),
        ("ARM Cortex-M", "ARM Cortex-M"),
        ("ESP32", "ESP32"),
        ("ESP8266", "ESP8266"),
        ("RISC-V", "RISC-V"),
        ("PIC", "PIC"),
        ("8051", "8051"),
        ("MSP430", "MSP430"),
    ]
    cpu_architecture = models.CharField(
        max_length=100, choices=CPU_ARCHITECTURE_CHOICES, null=True, blank=True
    )

    # Maximum operating frequency in MHz - optional field with decimal value
    max_frequency_mhz = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )

    # RAM size in kilobytes (KB)
    RAM_CHOICES = [
        (2, "2 KB"),
        (32, "32 KB"),
        (64, "64 KB"),
        (128, "128 KB"),
        (256, "256 KB"),
        (512, "512 KB"),
        (1024, "1 MB"),
        (2048, "2 MB"),
        (4096, "4 MB"),
    ]
    ram_kb = models.PositiveIntegerField(
        choices=RAM_CHOICES, help_text="RAM capacity in KB", null=True, blank=True
    )

    # Flash memory size in kilobytes (KB)
    FLASH_MEMORY_CHOICES = [
        (32, "32 KB"),
        (64, "64 KB"),
        (128, "128 KB"),
        (256, "256 KB"),
        (512, "512 KB"),
        (1024, "1 MB"),
        (2048, "2 MB"),
        (4096, "4 MB"),
        (8192, "8 MB"),
    ]
    flash_memory_kb = models.PositiveIntegerField(
        choices=FLASH_MEMORY_CHOICES,
        help_text="Flash memory capacity in KB",
        null=True,
        blank=True,
    )

    # Power consumption in milliwatts (mW) - optional decimal field
    power_consumption_mw = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Power consumption in milliwatts",
        null=True,
        blank=True,
    )

    # Package type (common package types for microcontrollers)
    PACKAGE_TYPE_CHOICES = [
        ("DIP", "Dual In-line Package (DIP)"),
        ("QFP", "Quad Flat Package (QFP)"),
        ("BGA", "Ball Grid Array (BGA)"),
        ("TSSOP", "Thin Shrink Small Outline Package (TSSOP)"),
        ("SOIC", "Small Outline IC (SOIC)"),
    ]
    package_type = models.CharField(
        max_length=50, choices=PACKAGE_TYPE_CHOICES, null=True, blank=True
    )

    # Description of the microcontroller
    description = models.TextField(blank=True, null=True)

    # Price in USD (optional decimal field)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    # Rating (optional decimal field for user ratings)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    # URL for an image representing the microcontroller (optional)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    # Image file upload (optional)
    image = models.ImageField(null=True, blank=True)

    def get_absolute_url(self):
        """Returns the absolute URL for the current microcontroller instance.

        The URL is generated using the 'microcontroller_detail' URL pattern,
        which expects 'microcontroller_id' as an argument.

        Parameters:
        self (Microcontroller): The instance of the Microcontroller model.

        Returns:
        str: The absolute URL for the microcontroller detail page.
        """
        return reverse("microcontroller_detail", args=[str(self.id)])

    def __str__(self):
        return self.name
