from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


from accounts.models import userProfile


@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    """Сигнал для создания пользователя"""
    if created:
        userProfile.objects.get_or_create(user=instance)