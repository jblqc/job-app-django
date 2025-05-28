from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Stock, Order
from .serializers import StockSerializer, OrderSerializer
from django.db.models import F, Sum, DecimalField, ExpressionWrapper
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# Stocks

class StockListCreateView(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class StockRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


# Orders

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer

class OrderRetrieveView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# Portfolio summary - aggregated data
# Custom Pagination without `next` and `previous`
class CustomPagination(PageNumberPagination):
    page_size = 10  # Default items per page
    page_size_query_param = 'items_per_page'
    page_query_param = 'current_page'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            "count": self.page.paginator.count,
            "results": {
                "total_value": self.request.total_value,
                "orders": data
            }
        })


class PortfolioSummaryView(APIView):

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'stock_id',
                openapi.IN_QUERY,
                description="Filter by stock ID (optional)",
                type=openapi.TYPE_INTEGER
            ),
            openapi.Parameter(
                'items_per_page',
                openapi.IN_QUERY,
                description="Number of orders per page (default: 10)",
                type=openapi.TYPE_INTEGER,
                default=10
            ),
            openapi.Parameter(
                'current_page',
                openapi.IN_QUERY,
                description="Current page (default: 1)",
                type=openapi.TYPE_INTEGER,
                default=1
            ),
        ]
    )
    def get(self, request):
        # Get all order/ stock_id get is optional
        stock_id = request.query_params.get('stock_id')
        orders = Order.objects.all().order_by('-created_at')

        if stock_id:
            orders = orders.filter(stock_id=stock_id)

        # Total value = sum of (quantity * price)
        total_value = orders.aggregate(
            total=Sum(
                ExpressionWrapper(F('quantity') * F('price'), output_field=DecimalField())
            )
        )['total'] or 0

        # Paginate results
        paginator = CustomPagination()
        paginated_orders = paginator.paginate_queryset(orders, request, view=self)

        # Attach total_value to request so CustomPagination can access it
        request.total_value = total_value

        return paginator.get_paginated_response(OrderSerializer(paginated_orders, many=True).data)



