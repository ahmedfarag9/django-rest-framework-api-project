from . import models
from rest_framework import serializers
from rest_framework.fields import CharField, EmailField




# Serializer for the Contact model
class ContactSerializer(serializers.ModelSerializer):

  # Map the 'title' field to 'name' and make it required
  name = CharField(source="title", required=True)
  
  # Map the 'description' field to 'message' and make it required
  message = CharField(source="description", required=True)
  
  # Add validation for the 'email' field
  email = EmailField(required=True)
  
  class Meta:
    # Set the model to be serialized
    model = models.Contact
    
    # Define the fields to be serialized
    fields = (
      'name',
      'email',
      'message'    )

