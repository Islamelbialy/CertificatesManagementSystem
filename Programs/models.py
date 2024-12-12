from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class programe(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    full_path_name = models.CharField(max_length=100,null=False,blank=False)
    desc = models.CharField(max_length=200,null=True,blank=True)
<<<<<<< HEAD
    #parent_id = models.ForeignKey('self',related_name='parent_id',on_delete=models.CASCADE)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        return self.name
=======
    parent_id = models.ForeignKey('self',related_name='child_prog',on_delete=models.CASCADE)
>>>>>>> 4c333a34a5b8f1012ee209b62d00441669c7c53e

class permession(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    desc = models.CharField(max_length=200,null=False,blank=False)

    def __str__(self):
        return self.name
    
<<<<<<< HEAD
#class progUserPermissions(models.Model):
#    user_id = models.ForeignKey(User,'user_id',on_delete=models.CASCADE)
#    permession_id = models.ForeignKey(permession,related_name='permession_id',on_delete=models.CASCADE)
#    program_id = models.ForeignKey(programe,related_name='program_id',on_delete=models.CASCADE)

=======
class progUserPermissions(models.Model):
    user_id = models.ForeignKey(User,related_name='user_programe_permission',on_delete=models.CASCADE)
    permession_id = models.ForeignKey(permession,related_name='permession_user_program',on_delete=models.CASCADE)
    program_id = models.ForeignKey(programe,related_name='program_permission_user',on_delete=models.CASCADE)
>>>>>>> 4c333a34a5b8f1012ee209b62d00441669c7c53e


# class userProgram(models.Model):
#     program_id = models.ForeignKey(programe,related_name='program_id',on_delete=models.CASCADE)
#     user_id = models.ForeignKey(User,'user_id',on_delete=models.CASCADE)

# class ProgPermessions(models.Model):
#     program_id = models.ForeignKey(programe,related_name='program_id',on_delete=models.CASCADE)
#     permession_id = models.ForeignKey(permession,related_name='permession_id',on_delete=models.CASCADE)