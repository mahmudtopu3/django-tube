import subprocess
import os
from django.core.management.base import BaseCommand, CommandError

from video.models import Video

class Command(BaseCommand):
    help = 'Optimize Video'

    def handle(self, *args, **kwargs):
        try:
            obj = Video.objects.filter(status='Pending').first()
            if obj:
                obj.status = 'Processing'
                obj.save()
                input_video_path = obj.video.path
                output_directory = os.path.join(os.path.dirname(input_video_path), 'hls_output')
                os.makedirs(output_directory, exist_ok=True)
                output_filename = os.path.splitext(os.path.basename(input_video_path))[0] + '_hls.m3u8'
                output_hls_path = os.path.join(output_directory, output_filename)
               

                # Use ffmpeg to create HLS segments
                cmd = [
                    'ffmpeg',
                    '-i', input_video_path,
                    '-c:v', 'h264',
                    '-c:a', 'aac',
                    '-hls_time', '5',
                    '-hls_list_size', '0',
                    '-hls_segment_filename', os.path.join(output_directory, f'{os.path.splitext(output_filename)[0]}_%03d.ts'),
                    output_hls_path
                ]


                subprocess.run(cmd, check=True)

                # Update the Video object status to 'Processed' or something similar
                obj.hls = output_hls_path 
                obj.status = 'Completed'
                obj.save()

                print(f'HLS segments generated and saved at: {output_hls_path}')
            else:
                print('No video with status "Pending" found.')

        except Exception as e:
            raise CommandError(e)
