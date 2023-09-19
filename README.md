#  Django Video Encoding and Streaming App

This Django application is designed for video encoding and streaming. It leverages the power of FFmpeg to generate HLS (HTTP Live Streaming) files, calculate video duration, and generate thumbnails. Additionally, it includes a background processing system using Celery to handle video encoding tasks efficiently.


##  Features

-   Video Encoding: Utilizes FFmpeg to encode videos into HLS format, making them compatible with a wide range of devices and browsers.
-   Video Duration Calculation: Automatically calculates the duration of uploaded videos.
-   Thumbnail Generation: Generates thumbnails for videos to provide a preview.
-   Background Processing: Uses Django signals to trigger Celery tasks for seamless and efficient video processing in the background.
-   Extensible: Easily extend the functionality to include more video-related features or customization.

## Installation Process
1. Clone Project from github 
2. Create virtualenv
      ```sh
    $ virtualenv venv
    ```
3. Activate Virtualenv
   ```sh
    $ source venv/Scripts/activate
    ```
4. Add project specific information in .env
5. Make migration
    ```sh
    $ python manage.py makemigrations
    ```
6. Migrate
    ```sh
    $ python manage.py migrate
    ```
7. Create Superuser
    ```sh
    $ python manage.py createsuperuser
    ```
8. Start Server
    ```sh
    $ python manage.py runserver
    ```
9. Install redis on the server and allow redis port 

10. Run Celery for the background tasks
    ```sh
    $ celery -A djtube worker -l info -P threads 
    ```
 ## Contributing

Contributions to the Django Video Encoding and Streaming App are welcome! Feel free to open issues, submit pull requests, or provide feedback.


