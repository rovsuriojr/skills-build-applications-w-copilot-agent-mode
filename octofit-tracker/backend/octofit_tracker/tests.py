from django.test import TestCase
from .models import Team, Activity, Leaderboard, Workout

class TeamModelTest(TestCase):
    def test_str(self):
        team = Team.objects.create(name='Marvel')
        self.assertEqual(str(team), 'Marvel')

class ActivityModelTest(TestCase):
    def test_str(self):
        activity = Activity.objects.create(user='ironman', type='run', duration=30)
        self.assertEqual(str(activity), 'ironman - run')

class LeaderboardModelTest(TestCase):
    def test_str(self):
        lb = Leaderboard.objects.create(user='ironman', score=100)
        self.assertEqual(str(lb), 'ironman: 100')

class WorkoutModelTest(TestCase):
    def test_str(self):
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        self.assertEqual(str(workout), 'Pushups')
