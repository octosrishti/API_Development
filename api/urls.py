from django.urls import path, include
from .views import get_monthly_sales, get_n_most_total_item, get_percentage_sold_items_by_department, get_seats_sold_by_department

urlpatterns = [
    path('total_items', get_seats_sold_by_department),
    path('nth_most_total_item', get_n_most_total_item),
    path('percentage_of_department_wise_sold_items',get_percentage_sold_items_by_department),
    path('monthly_sales', get_monthly_sales)
]
