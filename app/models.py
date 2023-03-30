from django.db import models

# Create your models here.
class Table( models.Model ) :
    number = models.IntegerField( primary_key= True)

    def __str__( self ) :
        return str(self.number)
    
class Dish(models.Model ) :
    name = models.CharField( max_length= 50 )
    price = models.FloatField()
    type = models.CharField( max_length= 50 )
    gluten = models.BooleanField( null= False)
    id =models.AutoField(primary_key=True)
    lactose = models.BooleanField( null= False)


    def __str__( self ) :
        return self.name

class Meal(models.Model ) :
    start = models.TimeField()
    end = models.TimeField(blank= True, null= True, default= None)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)

    def __str__( self ) :
        return str(self.table.number)
    
class Order(models.Model):
    request_time = models.TimeField()
    kitchen_start_time = models.TimeField(blank= True, null= True, default= None)
    kitchen_end_time = models.TimeField(blank= True, null= True, default= None)
    delivery_time = models.TimeField(blank= True, null= True, default= None)
    dish_name = models.ForeignKey(Dish, null= True, blank= True, default= None, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, null= True, default= None, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.table.number)