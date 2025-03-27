from django.db import models

class ErrorCalculation(models.Model):
    is_active = models.BooleanField(default=False)
    reference = models.FloatField(default=0)
    measured = models.FloatField(default=0)
    error = models.CharField(max_length=10, blank=True)

    def calculate_error(self):
        if not self.is_active:
            return "---"
        if self.measured == 0:
            return "Referência Inválida"
        error = ((self.measured - self.reference) / self.reference * 100)
        return f"{error:+.2f}%"
