from django.db import models

class Foundation(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)                             # Foundation's Name
    address = models.CharField(max_length=255, null=False, blank=False)                          # Foundation's Address
    contact_number = models.CharField(max_length=15, null=False, blank=False)                    # Foundation's ContactNumber
    email = models.EmailField(max_length=255, null=False, blank=False)                           # Foundation's Email    
    logo1 = models.BinaryField(null=True, blank=True)                                            # Foundation's First Logo
    logo2 = models.BinaryField(null=True, blank=True)                                            # Foundation's Second Logo
    #parent_id = models.ForeignKey('self',related_name='parent_id',on_delete=models.CASCADE)      # Foundation's ParentID

    def __str__(self):
        return self.name

