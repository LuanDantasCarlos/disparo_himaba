from typing import Optional
from datetime import datetime, timedelta

from openpyxl import Workbook

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from broadcasts.models import Broadcasts


app_name = "broadcasts"

@login_required
def home(request):
    context = {
    }

    return render(request, "broadcasts/broadcast.html", context)
