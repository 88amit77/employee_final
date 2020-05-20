from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
import requests


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'

