
from django.db.models.signals import  post_save
from django.dispatch import receiver
from .tasks import video_encode
from .models import Video


@receiver(post_save, sender=Video)
def video_signal(sender, instance, created,*args, **kwargs):
     if instance and created:   
        video_encode.delay(3,instance.id)
        print("Task initiated")
     else: 
        # add your logic here
        pass