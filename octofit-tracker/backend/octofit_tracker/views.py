from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from .models import User, Team, Activity, Leaderboard, Workout
import logging

logger = logging.getLogger(__name__)

@api_view(['GET'])
def api_root(request, format=None):
    base_url = request.build_absolute_uri('/')[:-1].replace('http://localhost:8000', 'https://miniature-parakeet-5vr54x94x66f7pqg-8000.app.github.dev')
    logger.info(f"Base URL: {base_url}")
    return Response({
        'users': base_url + '/api/users/?format=api',
        'teams': base_url + '/api/teams/?format=api',
        'activities': base_url + '/api/activities/?format=api',
        'leaderboard': base_url + '/api/leaderboard/?format=api',
        'workouts': base_url + '/api/workouts/?format=api'
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
