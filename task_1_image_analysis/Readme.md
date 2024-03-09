# Image EXIF Data Analysis Web Application

This is a web application built with Flask that allows users to upload images and analyze their Exchangeable Image File Format (EXIF) metadata. The application can detect potential violations based on certain criteria such as image height and speed.

## Features

- **Image Upload**: Users can upload images from their local device.
- **EXIF Analysis**: Extracts and analyzes the EXIF metadata of the uploaded images.
- **Detection Criteria**: Flags images if their height is greater than 60 meters or their speed is higher than 5 meters per second.
- **Dashboard Display**: Displays the analysis results in a dashboard format, including the image, its metadata, and the detection status.
- **Report Generation**: Allows users to download the analysis report in CSV format.

## Methodology

### Backend Development

The backend of the application is developed using Flask, a micro web framework for Python. Flask provides routing, request handling, and other functionalities required for building web applications.

The `app.py` file contains the main Flask application. It defines routes for handling image upload, analysis, and report generation. The backend uses the Pillow library for image processing to extract EXIF metadata from uploaded images.

### Frontend Development

The frontend of the application is built using HTML, CSS. The `index.html` file contains the upload form where users can select an image to upload. Upon submitting the form, the backend processes the uploaded image and displays the analysis results on the `result.html` page.

### Image Processing

The `analyze_image()` function in `app.py` utilizes the Pillow library to extract EXIF metadata from the uploaded images. It then analyzes the metadata to determine if the image meets the detection criteria, i.e., if its height is greater than 60 meters or its speed is higher than 5 meters per second.

### Dashboard Creation

The dashboard for displaying the analysis results is implemented using HTML and Jinja templating. The `result.html` file renders the analysis results, including the image, its metadata, and the detection status. Additionally, a download link is provided to download the analysis report.

### Report Generation

The `download_report()` function in `app.py` generates the analysis report in PDF format using the ReportLab library. It includes the image, its metadata, and the detection status in the report. Users can download the report from the web application.

## Installation

To run the application locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/anchalsingh298358/Dronemaps_tasks.git  
   ``` 
2. Navigate to the project directory:
    ```bash 
    cd image-exif-analysis
    Install the required dependencies:
    pip install -r requirements.txt
    ```
3. Run the Flask application:
    ```bash
    python app.py
    Open a web browser and navigate to http://localhost:5000 to access the application.
    ```
## Dependencies
    Flask
    Pillow
    ReportLab
## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.