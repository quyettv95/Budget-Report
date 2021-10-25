from django.http.response import HttpResponse
from django.shortcuts import render
from openpyxl import Workbook

# Create your views here.
import pandas as pd
from io import BytesIO

def index(request):

  workbook = Workbook()
  worksheet = workbook.active
  worksheet.title = 'Hello Sample Sheet'

  # Define the titles for columns
  columns = [
    'STT',
    'Segment',
    'Segment Name',
    'Cost center',
    'Cost center name',
    'Item code',
    'Item Name',
    'Month',
    'Amount',
    'User',
  ]
  row_num = 1
