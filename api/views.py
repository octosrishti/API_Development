from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from django.db.models import Q
from .models import Market
from rest_framework import status
from datetime import datetime
from django.db.models import Count
from django.db.models.functions import ExtractMonth

@api_view(["POST"])
def get_seats_sold_by_department(request:Request) -> Response:
    try:
        data =  request.data
        
        start_date = data.get("start_date", None)
        end_date = data.get("end_date", None)
        department = data.get("department", None)
        minimum_time = datetime.min.time()
        
        if start_date is None or end_date is None or department is None:
            raise ValueError("Missing required parameters")
        
        start_date = datetime.strptime(start_date, "%y-%m-%d %H:%M:%S")
        end_date = datetime.strptime(end_date, "%y-%m-%d %H:%M:%S")
        
        seats_sold = Market.objects.filter(
            Q(datetime_field__date__gte=start_date) &
            Q(datetime_field__date__lte=end_date) &
            Q(department=department)
        ).aaggregate(sum("seats"))
        
        return Response(seats_sold, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["POST"])
def get_n_most_total_item(request:Request) -> Response:
    try:
        data = request.data
        
        start_date = data.get("start_date", None)
        end_date = data.get("end_date", None)
        item_by = data.get("item_by", None)
        n_most = data.get("n_most", None)
        
        minimum_time = datetime.min.time()
        
        if start_date is None or end_date is None or item_by is None or n_most is None:
            raise ValueError("Missing required parameters")
        
        start_date = datetime.strptime(start_date, "%y-%m-%d %H:%M:%S")
        end_date = datetime.strptime(end_date, "%y-%m-%d %H:%M:%S")
            
            
        if item_by.lower() == "quantity":
            order_by = "seats"
        elif item_by.lower() == "prices":
            order_by = "amount"
        else :
            raise ValueError("Item to be ordered by is not present in db")
            
        market = Market.objects.filter(
            Q(datetime_field__date__gte=start_date) &
            Q(datetime_field__date__lte=end_date) 
        ).order_by(order_by)
        
        if n_most > len(market):
            raise Exception("Item does not exist")
        
        return Response({"item":market[n_most-1]}, status=status.HTTP_200_OK)
        
        
    except Exception as e:
        return Response({"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["POST"])
def get_percentage_sold_items_by_department(request:Request) -> Response:
    try:
        data = request.data
        
        start_date = data.get("start_date", None)
        end_date = data.get("end_date", None)
        
        if start_date is None or end_date is None:
            raise ValueError("Missing required parameters")
        
        start_date = datetime.strptime(start_date, "%y-%m-%d %H:%M:%S")
        end_date = datetime.strptime(end_date, "%y-%m-%d %H:%M:%S")
        
        market = Market.objects.filter(
            Q(datetime_field__date__gte=start_date) &
            Q(datetime_field__date__lte=end_date) 
        )
        
        total_items = market.count()
        
        total_sold = market.aaggregate(sum("seats"))
        
        departments = {}
        
        for item in market:
            if item.department in departments:
                departments[item.department] += item.seats
            else:
                departments[item.department] = item.seats
                
        for department in departments:
            departments[department] = (departments[department]*100)/total_sold
            
        return Response(departments, status=status.HTTP_200_OK)
        
        
    except Exception as e:
        return Response({"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["POST"])
def get_monthly_sales(request:Request) -> Response:
    try:
        data = request.data
        
        product = data.get("product", None)
        year = data.get("year", None)
        
        if product is None or year is None:
            raise ValueError("Missing required parameters")
        
        sold_items_per_month =  Market.objects.filter(
            software=product,
            sold_date__year=year
        ).annotate(
            month=ExtractMonth('sold_date')
        ).values('month').annotate(
            total_sold=Count('id')
        ).order_by('month')
        
        return Response(sold_items_per_month, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)