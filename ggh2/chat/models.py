from django.db import models
from django.db.models.deletion import CASCADE
from user.models import User 
    
class Room(models.Model):
    name = models.CharField(verbose_name='채팅방 이름', max_length=255)
    def __str__(self):
        return self.name


class RoomMessage(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    message = models.TextField(verbose_name='메세지')
    created = models.DateTimeField(verbose_name='생성 날짜', auto_now_add=True, db_index=True)
    user = models.ForeignKey(User,on_delete=CASCADE,verbose_name="전송자")

    def __str__(self):
        return self.message

    def get_created(self):
        return self.created.strftime('%p %I:%M')