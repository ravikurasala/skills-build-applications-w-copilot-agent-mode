from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Populate users
        users = {}
        for user_data in test_users:
            user = User.objects.create(
                _id=ObjectId(),
                username=user_data['username'],
                email=user_data['email'],
                password=user_data['password']
            )
            users[user_data['username']] = user

        # Populate teams
        for team_data in test_teams:
            team = Team.objects.create(
                _id=ObjectId(),
                name=team_data['name']
            )

        # Populate activities
        for activity_data in test_activities:
            Activity.objects.create(
                _id=ObjectId(),
                user=users[activity_data['username']],
                activity_type=activity_data['activity_type'],
                duration=timedelta(hours=int(activity_data['duration'].split(':')[0]),
                                   minutes=int(activity_data['duration'].split(':')[1]))
            )

        # Populate leaderboard
        for leaderboard_data in test_leaderboard:
            Leaderboard.objects.create(
                _id=ObjectId(),
                user=users[leaderboard_data['username']],
                score=leaderboard_data['score']
            )

        # Populate workouts
        for workout_data in test_workouts:
            Workout.objects.create(
                _id=ObjectId(),
                name=workout_data['name'],
                description=workout_data['description']
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
