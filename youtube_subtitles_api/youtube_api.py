from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

# Replace with the YouTube video ID
video_id = '8BsAa_94dao'

try:

    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    formatter = TextFormatter()
    formatted_transcript = formatter.format_transcript(transcript)

    print("Transcript:")
    print(formatted_transcript)

    with open(f'{video_id}_transcript.txt', 'w', encoding='utf-8') as file:
        file.write(formatted_transcript)

except Exception as e:
    print(f"An error occurred: {e}")

