from django.db import models


class SaleProduct(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=200, null=True)
    img = models.ImageField(null=True, upload_to='elements/')
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)

    def get_all(self):
        return [self.name, self.picture, self.description]


img_name = "Users/Desktop/Bild1.png"
s1 = SaleProduct(id=1, name='Sofa', img=img_name, title='SofaBild', description='Ein Sofa')
s1.save()
s2 = SaleProduct(id=2, name='Schrank', img='Bild1.jpeg', title='SchrankBild', description='Ein Schrank')
s2.save()
s3 = SaleProduct(id=3, name='Sofa', img='Bild1.jpeg', title='SofaBild', description='Ein Sofa')
s3.save()
