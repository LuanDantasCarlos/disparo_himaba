import os
import logging
from time import sleep
from threading import Thread
from django.apps import AppConfig

log = logging.getLogger(__name__)


class DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'
