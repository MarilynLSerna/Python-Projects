from django.db import models

# Model representing a univeristy campus
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=255, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_id = models.IntegerField(unique=True)

    # Create model manager
    objects = models.Manager()

    # Display the object output values in the form of a string
    def __dir__(self):
        # Returns the input value of the campus name and state
        # field as a tuple to display in the browser instead of the default titles
        display_campus = '{0.campus_name} ({0.state})'
        return display_campus.format(self)

        # Removes added 's' that Django adds to the model name in the browser display
        class Meta:
            verbose_name_plural = "University Campuses"

