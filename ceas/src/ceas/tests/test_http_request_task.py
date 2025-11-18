import unittest
from unittest.mock import patch, MagicMock
from ceas.tasks.http_request_task import send_http_request_task

class TestHttpRequestTask(unittest.TestCase):
    
    @patch('ceas.integrations.http.http')
    def test_get_request(self, mock_http):
        # Setup mock
        mock_response = {"status": "success", "data": "test data"}
        mock_http.get.return_value = mock_response
        
        # Call the task with GET method
        result = send_http_request_task(
            endpoint="https://test-api.com/data",
            method="GET"
        )
        
        # Verify the HTTP client was called correctly
        mock_http.get.assert_called_once_with("https://test-api.com/data")
        
        # Verify the result
        self.assertEqual(result, mock_response)
    
    @patch('ceas.integrations.http.http')
    def test_post_request_with_data(self, mock_http):
        # Setup mock
        mock_response = {"status": "created", "id": "123"}
        mock_http.post.return_value = mock_response
        
        # Test data
        test_data = {"name": "Test Item", "value": 42}
        test_headers = {"Authorization": "Bearer token123"}
        
        # Call the task with POST method and data
        result = send_http_request_task(
            endpoint="https://test-api.com/items",
            method="POST",
            data=test_data,
            headers=test_headers
        )
        
        # Verify the HTTP client was called correctly
        mock_http.post.assert_called_once_with(
            "https://test-api.com/items", 
            json=test_data,
            headers=test_headers
        )
        
        # Verify the result
        self.assertEqual(result, mock_response)
    
    @patch('ceas.integrations.http.http')
    def test_unsupported_method(self, mock_http):
        # Call the task with an unsupported method
        result = send_http_request_task(
            endpoint="https://test-api.com/data",
            method="PATCH"  # Unsupported method
        )
        
        # Verify no HTTP methods were called
        mock_http.get.assert_not_called()
        mock_http.post.assert_not_called()
        mock_http.put.assert_not_called()
        mock_http.delete.assert_not_called()
        
        # Verify the result is None for unsupported methods
        self.assertIsNone(result)
    
    @patch('ceas.integrations.http.http')
    def test_exception_handling(self, mock_http):
        # Setup mock to raise an exception
        mock_http.get.side_effect = Exception("Connection error")
        
        # Verify the task raises the exception
        with self.assertRaises(Exception):
            send_http_request_task(
                endpoint="https://test-api.com/data",
                method="GET"
            )

if __name__ == '__main__':
    unittest.main()
