from django.urls import path
from .views import (
    StockListCreateView, StockRetrieveUpdateDestroyView,
    OrderListCreateView, OrderRetrieveView,
    PortfolioSummaryView,
)

urlpatterns = [
    # Stocks CRUD
    path('stocks/', StockListCreateView.as_view(), name='stock-list-create'),
    path('stocks/<int:pk>/', StockRetrieveUpdateDestroyView.as_view(), name='stock-detail'),

    # Orders CRUD (list + create + retrieve)
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderRetrieveView.as_view(), name='order-detail'),

    # Portfolio summary
    path('portfolio/', PortfolioSummaryView.as_view(), name='portfolio-summary'),
]
