from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField("Imagen de perfil", upload_to="profile_pictures/", blank=True,
                                        null=True)
    bio = models.TextField("Biografia", max_length=500, blank=True)
    birth_date = models.DateField("fecha de nacimiento", null=True, blank=True)
    followers = models.ManyToManyField("self", symmetrical=False, related_name="following",
                                       through="Follow")

    
    class Meta:
        verbose_name = "perfil"
        verbose_name_plural = "perfiles"


    def __str__(self):
        return self.username
    


class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, verbose_name="¿Quien esta siguiendo?", on_delete=models.CASCADE,
                                  related_name='follower_set')
    following = models.ForeignKey(UserProfile, verbose_name="¿A quien sigue?",  on_delete=models.CASCADE,
                                   related_name='following_set')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Desde cuando lo sigue")

    class Meta:
        unique_together = ('follower', 'following')

    
    def __init__(self):
        return f"{self.follower.user.username} sigue a {self.following.user.username}"
    
    class Meta:
        verbose_name = "seguidor"
        verbose_name_plural = "seguidores"