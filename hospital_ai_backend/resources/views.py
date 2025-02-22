# resources/views.py
from rest_framework import viewsets
from .models import Bed, Equipment, Staff, Medicine
from .serializers import BedSerializer, EquipmentSerializer, StaffSerializer, MedicineSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import datetime

class BedViewSet(viewsets.ModelViewSet):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

class ShortagePredictionView(APIView):
    """
    A simple APIView to simulate shortage prediction for hospital beds.
    In a real scenario, you would query historical data from your database.
    """

    def get(self, request, format=None):
        # Simulate 30 days of historical usage data (dummy data)
        dates = pd.date_range(end=datetime.date.today(), periods=30)
        usage = np.random.randint(80, 100, size=30)  # simulated usage numbers
        df = pd.DataFrame({'ds': dates, 'y': usage})
        
        # For regression, convert dates to ordinal numbers
        df['ds_ordinal'] = df['ds'].apply(lambda x: x.toordinal())
        X = df[['ds_ordinal']]
        y = df['y']
        
        # Train a simple linear regression model as a placeholder
        model = LinearRegression()
        model.fit(X, y)
        
        # Predict usage for tomorrow
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        tomorrow_ordinal = np.array([[tomorrow.toordinal()]])
        predicted_usage = model.predict(tomorrow_ordinal)[0]
        
        # For demonstration, assume a threshold usage value (e.g., 95)
        # If predicted usage is above 95, we assume there's a shortage
        threshold = 95
        shortage = max(0, predicted_usage - threshold)
        
        data = {
            'predicted_usage': predicted_usage,
            'shortage': shortage,
            'message': "Shortage predicted" if shortage > 0 else "No shortage predicted"
        }
        return Response(data, status=status.HTTP_200_OK)
