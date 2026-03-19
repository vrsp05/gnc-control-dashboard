from django.test import TestCase, Client
from django.urls import reverse
from .models import SetPointLog

class FormValidationTests(TestCase):
    def setUp(self):
        # The Client acts as our "Robot Operator"
        self.client = Client()
        self.url = reverse('dashboard')

    def test_valid_input_within_bounds(self):
        """Test Case 1 & 2: Boundary values 0 and 500 should pass."""
        for val in [0.0, 250.0, 500.0]:
            response = self.client.post(self.url, {'threshold': val})
            # Check that the form submitted successfully (302 redirect or 200 success)
            self.assertEqual(response.status_code, 200)
            # Verify it saved to the database
            self.assertTrue(SetPointLog.objects.filter(value=val).exists())

    def test_invalid_negative_input(self):
        """Test Case 3: Negative values should be rejected by the form."""
        response = self.client.post(self.url, {'threshold': -1.0})
        
        # The page should re-render (status 200) but with an error message
        self.assertEqual(response.status_code, 200)
        # Check if the error message is present in the HTML response
        self.assertContains(response, "Ensure this value is greater than or equal to 0.0.")
        # Verify NOTHING was saved to the database
        self.assertEqual(SetPointLog.objects.count(), 0)

    def test_invalid_high_input(self):
        """Test Case 4: Values above 500 should be rejected."""
        response = self.client.post(self.url, {'threshold': 501.0})
        
        self.assertContains(response, "Ensure this value is less than or equal to 500.0.")
        self.assertEqual(SetPointLog.objects.count(), 0)

    def test_invalid_data_type(self):
        """Test Case 5: Text input should be rejected."""
        response = self.client.post(self.url, {'threshold': 'abc'})
        
        self.assertContains(response, "Enter a number.")
        self.assertEqual(SetPointLog.objects.count(), 0)

class HistorianConsistencyTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('dashboard')

    def test_chronological_ordering(self):
        """Test Case 5: Ensure the newest logs appear first (LIFO)."""
        # Create three logs with specific values
        SetPointLog.objects.create(value=10.0, status_message="Log 1")
        SetPointLog.objects.create(value=20.0, status_message="Log 2")
        SetPointLog.objects.create(value=30.0, status_message="Log 3")

        response = self.client.get(self.url)
        # Check if the values appear in the HTML in reverse order (30, then 20, then 10)
        content = response.content.decode()
        pos30 = content.find("30.0 cm")
        pos20 = content.find("20.0 cm")
        pos10 = content.find("10.0 cm")

        # In a 'Latest First' system, 30.0 should appear before 20.0 in the HTML string
        self.assertTrue(pos30 < pos20 < pos10)

    def test_ui_display_limit(self):
        """Test Case 6: Verify the UI only shows the last 5 entries."""
        # Create 10 logs
        for i in range(10):
            SetPointLog.objects.create(value=float(i), status_message="Filling Historian")

        response = self.client.get(self.url)
        # Check the 'history' variable passed to the template context
        history_in_context = response.context['history']
        
        # The database has 10, but the UI context should only have 5
        self.assertEqual(len(history_in_context), 5)
        # The first one in the list should be the very last one we created (9.0)
        self.assertEqual(history_in_context[0].value, 9.0)

class UITestCases(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('dashboard')

    def test_warning_state_ui_change(self):
        """Test Case 7: High threshold should trigger 'WARNING' in HTML."""
        # Submit a value that triggers the warning (anything > 400)
        response = self.client.post(self.url, {'threshold': 450.0})
        
        # 1. Check if the text "WARNING" appears in the status
        self.assertContains(response, "WARNING: High Threshold Set")
        
        # 2. Check if the 'warning' CSS class is applied to the span
        self.assertContains(response, 'class="warning"')

    def test_normal_state_ui(self):
        """Verify that a normal value does NOT show the warning."""
        response = self.client.post(self.url, {'threshold': 100.0})
        
        self.assertNotContains(response, "WARNING")
        self.assertNotContains(response, 'class="warning"')