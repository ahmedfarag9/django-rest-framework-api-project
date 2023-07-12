# Importing necessary modules
from django.db import models
from utils.model_abstracts import Model
from django_extensions.db.models import (
  TimeStampedModel, 
  ActivatorModel,
  TitleDescriptionModel
)

# Defining the Contact model
class Contact(
  TimeStampedModel,  # Inherits from TimeStampedModel to add created_at and updated_at fields
  ActivatorModel,   # Inherits from ActivatorModel to add is_active and activated_at fields
  TitleDescriptionModel,  # Inherits from TitleDescriptionModel to add title and description fields
  Model  # Inherits from Model to add id and uuid fields
  ):

  class Meta:
    verbose_name_plural = "Contacts"  # Sets the plural name for the model in the admin panel

  email = models.EmailField(verbose_name="Email")  # Adds an email field to the model

  def __str__(self):
    return f'{self.title}'  # Returns the title of the Contact instance as a string
