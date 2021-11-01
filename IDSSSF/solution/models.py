from django.db import models



# Create your models here.
class SolutionModel(models.Model):

    def prevent_default():
        return {"prevent": [""]}
    
    def medicine_default():
        return {"medicine": [""]}

    def caution_default():
        return {"caution": [""]}


    disease_name  = models.CharField(max_length=50)
    about = models.CharField(max_length=5000,default=None)
    prevent = models.JSONField(default=prevent_default)
    medicine = models.JSONField(default=medicine_default)
    caution = models.JSONField(default=caution_default)
    medicine_image = models.ImageField(upload_to='solution/',blank = True)

    

    def __str__(self):
        return self.disease_name

   
