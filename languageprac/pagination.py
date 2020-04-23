from rest_framework.pagination import PageNumberPagination


class DashboardPageNumberPagination(PageNumberPagination):
    page_size = 5


class ListPageNumberPagination(PageNumberPagination):
    page_size = 20

