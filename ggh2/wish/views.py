from enum import unique

from django.core.exceptions import ObjectDoesNotExist
from wish.models import *

from django.shortcuts import get_object_or_404, redirect
from goods.models import TimeStampModel
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, TextField
from user.models import User
from goods.models import Goods
