from django.db import models

# competance: machine learning
# technologie:{
#     0:tensorflow,1:pytorche
# }


class Competences(models.Model):
    name = models.fields.CharField(max_length=100)

class Projet(models.Model):
    name = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=200)
    url_depot = models.fields.URLField(null=True,blank=True)
    

class Technologie(models.Model):
    name = models.fields.CharField(max_length=100)
    projet = models.ForeignKey(Projet,null=True,on_delete=models.SET_NULL)

