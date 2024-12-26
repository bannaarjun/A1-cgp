import unittest
from extractor import create_video_from_text

class TestExtractor(unittest.TestCase):
    def test_create_video(self):
        # Test that the video is created from the text
        input_txt = 'test_input.txt'
        output_video = 'test_output.mp4'
        create_video_from_text(input_txt, output_video)
        # Check if the output file exists (this could be expanded with more checks)
        self.assertTrue(os.path.exists(output_video))

if __name__ == '__main__':
    unittest.main()
  
