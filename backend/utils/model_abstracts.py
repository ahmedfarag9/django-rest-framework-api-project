import uuid
from django.db import models


class Model(models.Model):
    """
    Abstract base class for all Django models in this project.
    Provides a UUID primary key field for all models that inherit from it.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    class Meta:
        abstract = True

