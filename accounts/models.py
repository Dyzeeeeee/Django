from django.db import models


class CustomUser(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(
        max_length=255
    )  # Note: Storing plain text passwords is not recommended for production!
    following = models.ManyToManyField(
        "self", symmetrical=False, blank=True, related_name="followers"
    )

    def __str__(self):
        return self.email  # Customize as needed
