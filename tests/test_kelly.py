"""
Unit tests for Kelly AI Chatbot
"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import after path modification
try:
    from app import KellyAIChatbot
except ImportError:
    # Fallback for different import scenarios
    import importlib.util
    spec = importlib.util.spec_from_file_location("app", "../app.py")
    app = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(app)
    KellyAIChatbot = app.KellyAIChatbot


class TestKellyAIChatbot(unittest.TestCase):
    """Test cases for Kelly AI Chatbot"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.kelly = KellyAIChatbot()
    
    def test_chatbot_initialization(self):
        """Test that chatbot initializes correctly"""
        self.assertEqual(self.kelly.name, "Kelly")
        self.assertIsInstance(self.kelly, KellyAIChatbot)
    
    def test_topic_identification_emotions(self):
        """Test emotion topic detection"""
        question = "Can AI understand human emotions?"
        topic = self.kelly._identify_topic(question.lower())
        self.assertEqual(topic, "emotions")
    
    def test_topic_identification_jobs(self):
        """Test job automation topic detection"""
        question = "Will AI replace all jobs?"
        topic = self.kelly._identify_topic(question.lower())
        self.assertEqual(topic, "jobs")
    
    def test_topic_identification_creativity(self):
        """Test creativity topic detection"""
        question = "Is AI truly creative?"
        topic = self.kelly._identify_topic(question.lower())
        self.assertEqual(topic, "creativity")
    
    def test_topic_identification_consciousness(self):
        """Test consciousness topic detection"""
        question = "Can machines become conscious?"
        topic = self.kelly._identify_topic(question.lower())
        self.assertEqual(topic, "consciousness")
    
    def test_topic_identification_bias(self):
        """Test bias topic detection"""
        question = "How do we address AI bias?"
        topic = self.kelly._identify_topic(question.lower())
        self.assertEqual(topic, "bias")
    
    def test_topic_identification_safety(self):
        """Test safety topic detection"""
        question = "What are the risks of AI?"
        topic = self.kelly._identify_topic(question.lower())
        self.assertEqual(topic, "safety")
    
    def test_topic_identification_intelligence(self):
        """Test intelligence topic detection"""
        question = "How intelligent is AI really?"
        topic = self.kelly._identify_topic(question.lower())
        self.assertEqual(topic, "intelligence")
    
    def test_topic_identification_future(self):
        """Test future prediction topic detection"""
        question = "What will AI look like in the future?"
        topic = self.kelly._identify_topic(question.lower())
        self.assertEqual(topic, "future")
    
    def test_topic_identification_learning(self):
        """Test learning topic detection"""
        question = "How does machine learning work?"
        topic = self.kelly._identify_topic(question.lower())
        self.assertEqual(topic, "learning")
    
    def test_topic_identification_limits(self):
        """Test limitations topic detection"""
        question = "What are the limitations of AI?"
        topic = self.kelly._identify_topic(question.lower())
        self.assertEqual(topic, "limits")
    
    def test_topic_identification_general(self):
        """Test general topic fallback"""
        question = "Tell me about AI"
        topic = self.kelly._identify_topic(question.lower())
        self.assertEqual(topic, "general")
    
    def test_generate_response_returns_string(self):
        """Test that generate_response returns a string"""
        question = "Can AI understand emotions?"
        response = self.kelly.generate_response(question)
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)
    
    def test_response_contains_practical_guidance(self):
        """Test that responses contain practical advice"""
        question = "Can AI feel emotions?"
        response = self.kelly.generate_response(question)
        # Check for common practical advice patterns
        has_guidance = any(marker in response for marker in [
            "Practical", "Evidence", "Best practice", 
            "Research", "Deploy", "Use", "Test"
        ])
        self.assertTrue(has_guidance, "Response should contain practical guidance")
    
    def test_response_is_poetic(self):
        """Test that responses follow poetic structure"""
        question = "Will robots take our jobs?"
        response = self.kelly.generate_response(question)
        # Check for multiple stanzas (indicated by double newlines)
        lines = response.split('\n')
        self.assertGreater(len(lines), 4, "Response should have multiple lines")
    
    def test_response_length_appropriate(self):
        """Test that responses are of reasonable length"""
        question = "What is AI?"
        response = self.kelly.generate_response(question)
        word_count = len(response.split())
        self.assertGreater(word_count, 50, "Response should be substantial")
        self.assertLess(word_count, 500, "Response shouldn't be too long")
    
    def test_multiple_questions(self):
        """Test handling multiple questions"""
        questions = [
            "Can AI be creative?",
            "Will AI replace jobs?",
            "Is AI conscious?"
        ]
        
        for question in questions:
            response = self.kelly.generate_response(question)
            self.assertIsInstance(response, str)
            self.assertGreater(len(response), 0)
    
    def test_case_insensitivity(self):
        """Test that topic detection is case-insensitive"""
        q1 = "CAN AI UNDERSTAND EMOTIONS?"
        q2 = "can ai understand emotions?"
        
        topic1 = self.kelly._identify_topic(q1.lower())
        topic2 = self.kelly._identify_topic(q2.lower())
        
        self.assertEqual(topic1, topic2)
    
    def test_poem_methods_exist(self):
        """Test that all poem methods are defined"""
        poem_methods = [
            '_poem_emotions',
            '_poem_jobs',
            '_poem_creativity',
            '_poem_consciousness',
            '_poem_bias',
            '_poem_safety',
            '_poem_intelligence',
            '_poem_future',
            '_poem_learning',
            '_poem_limits',
            '_poem_general'
        ]
        
        for method_name in poem_methods:
            self.assertTrue(
                hasattr(self.kelly, method_name),
                f"Method {method_name} should exist"
            )
            method = getattr(self.kelly, method_name)
            self.assertTrue(callable(method), f"{method_name} should be callable")
    
    def test_all_poems_return_strings(self):
        """Test that all poem methods return strings"""
        poem_methods = [
            self.kelly._poem_emotions,
            self.kelly._poem_jobs,
            self.kelly._poem_creativity,
            self.kelly._poem_consciousness,
            self.kelly._poem_bias,
            self.kelly._poem_safety,
            self.kelly._poem_intelligence,
            self.kelly._poem_future,
            self.kelly._poem_learning,
            self.kelly._poem_limits,
            self.kelly._poem_general
        ]
        
        for poem_method in poem_methods:
            result = poem_method()
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)


class TestKellyResponseQuality(unittest.TestCase):
    """Test the quality and characteristics of Kelly's responses"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.kelly = KellyAIChatbot()
    
    def test_skeptical_tone(self):
        """Test that responses contain skeptical language"""
        question = "AI will solve all our problems, right?"
        response = self.kelly.generate_response(question)
        
        skeptical_words = [
            "question", "doubt", "skeptic", "careful", "caution",
            "perhaps", "but", "yet", "however", "limit"
        ]
        
        response_lower = response.lower()
        has_skepticism = any(word in response_lower for word in skeptical_words)
        self.assertTrue(has_skepticism, "Response should express skepticism")
    
    def test_analytical_content(self):
        """Test that responses contain analytical thinking"""
        question = "Is AI intelligent?"
        response = self.kelly.generate_response(question)
        
        analytical_words = [
            "evidence", "test", "analyze", "examine", "study",
            "research", "measure", "evaluate", "assess"
        ]
        
        response_lower = response.lower()
        has_analysis = any(word in response_lower for word in analytical_words)
        self.assertTrue(has_analysis, "Response should be analytical")
    
    def test_professional_tone(self):
        """Test that responses maintain professional tone"""
        question = "Tell me about AI"
        response = self.kelly.generate_response(question)
        
        # Check there are no casual/slang words
        casual_words = ["gonna", "wanna", "kinda", "sorta", "yeah"]
        response_lower = response.lower()
        
        has_casual = any(word in response_lower for word in casual_words)
        self.assertFalse(has_casual, "Response should be professional")


def run_tests():
    """Run all tests"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test cases
    suite.addTests(loader.loadTestsFromTestCase(TestKellyAIChatbot))
    suite.addTests(loader.loadTestsFromTestCase(TestKellyResponseQuality))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return exit code
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    exit_code = run_tests()
