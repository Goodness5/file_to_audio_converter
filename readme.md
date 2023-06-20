
# Text-to-Speech Converter App

The Text-to-Speech Converter App is a web application that converts text files (*.txt), Word documents (*.docx), and PDF files (*.pdf) into audio files (*.mp3 or *.wav). It utilizes the gTTS library and Flask framework to provide a user-friendly interface for converting text into speech.

## Prerequisites

Before running the Text-to-Speech Converter App, ensure that you have the following installed on your system:

- Python (version 3.7 or later)
- pip (Python package installer)

## Installation

1. Clone the repository or download the source code.

   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory.

   ```bash
   cd text-to-speech-converter-app
   ```

3. (Optional) Create a virtual environment to isolate the project's dependencies.

   ```bash
   python -m venv env
   ```

4. Activate the virtual environment.

   - For Windows:

     ```bash
     .\env\Scripts\activate
     ```

   - For macOS and Linux:

     ```bash
     source env/bin/activate
     ```

5. Install the required Python dependencies.

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask development server.

   ```bash
   python app.py
   ```

2. Access the app by opening a web browser and visiting `http://localhost:5000`.

3. On the app's homepage, you will see a form to upload a file, select a language, and choose an audio format.

4. Select the file you want to convert by clicking the "Choose File" button and browsing your local file system.

5. Choose the desired language from the provided options.

6. Select the audio format you prefer (MP3 or WAV).

7. Click the "Upload" button to start the conversion process.

8. Once the conversion is complete, you will be redirected to a page where you can either play the generated audio or download it as a file.

9. Enjoy listening to the converted text!

## File Formats

The Text-to-Speech Converter App supports the following file formats:

- **Text Files**: Files with the extension *.txt containing plain text.
- **Word Documents**: Files with the extension *.docx created using Microsoft Word or other compatible word processors.
- **PDF Documents**: Files with the extension *.pdf in the Portable Document Format.

## Language Selection

The app provides a list of available languages for text-to-speech conversion. Choose the desired language from the dropdown menu to generate the audio in that language.

## Audio Format

You can choose between two audio formats:

- **MP3**: Compressed audio format suitable for most purposes.
- **WAV**: Uncompressed audio format that provides higher audio quality but results in larger file sizes.

## Development

If you wish to modify or enhance the Text-to-Speech Converter App, here are some details about the project structure:

- `app.py`: The main Flask application file that handles routing and request handling.
- `templates/`: Contains HTML templates used for rendering the web pages.
- `static/`: Stores static files such as CSS stylesheets and JavaScript files.
- `uploads/`: A directory where uploaded files are stored temporarily.
- `requirements.txt`: Lists the Python dependencies required for the app.

## Contributing

Contributions to the Text-to-Speech Converter App are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.
