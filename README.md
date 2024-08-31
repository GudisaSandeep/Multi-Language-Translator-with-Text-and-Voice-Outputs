# Multi-Language Translator with Text and Voice Outputs

## Project Overview

This project is a powerful web application that translates English text or audio into multiple languages and provides both text and voice outputs for each translated language. The application is built using Gradio, leveraging AssemblyAI for audio transcription, ElevenLabs for text-to-speech conversion, and the `translate` library for translating text into different languages. It offers a simple and intuitive user interface, making it easy to use for people from different linguistic backgrounds.

## Features

- **Text Input Translation:** Translate English text into multiple languages.
- **Audio File Translation:** Upload an audio file containing English speech, transcribe it, and translate it into multiple languages.
- **Recorded Audio Translation:** Record audio directly in the application, transcribe, and translate it into multiple languages.
- **Multiple Language Support:** Translate English into Russian, Turkish, Swedish, German, Spanish, Japanese, Hindi, and Telugu.
- **Voice Output:** Generate voice output for each translated language using ElevenLabs' text-to-speech service.
- **Intuitive UI:** Built using Gradio, the application offers an easy-to-use interface with tabs for different input methods and organized outputs for translated text and audio.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/GudisaSandeep/Multi-Language-Translator-with-Text-and-Voice-Outputs
   cd Multi-Language-Translator-with-Text-and-Voice-Outputs
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API keys:**

   - **AssemblyAI:** Sign up for an API key at [AssemblyAI](https://www.assemblyai.com/) and replace the placeholder `api_key` in the code with your key.
   - **ElevenLabs:** Sign up for an API key at [ElevenLabs](https://www.elevenlabs.io/) and replace the placeholder `api_key` in the code with your key.

4. **Run the application:**

   ```bash
   python app.py
   ```

5. **Access the application:**

   Open a browser and navigate to `http://127.0.0.1:7860/` to access the application.

## Usage

### Text Input
1. Enter the English text in the text input box.
2. Click the "Translate Text" button.
3. View the translated text and play the generated audio for each language.

### Audio File
1. Upload an audio file containing English speech.
2. Click the "Translate Audio File" button.
3. The application will transcribe the speech, translate it, and provide text and audio outputs.

### Recorded Audio
1. Record audio directly using the microphone.
2. Click the "Translate Recorded Audio" button.
3. The recorded audio will be transcribed, translated, and output as text and audio.

## Project Structure

- **app.py:** Main application script that handles the Gradio interface and integrates all functionalities.
- **requirements.txt:** Lists all Python dependencies needed to run the application.

## Future Improvements

- **Language Expansion:** Add support for more languages.
- **Real-time Translation:** Implement real-time audio translation.
- **User Customization:** Allow users to select specific languages for translation.
- **Improved UI/UX:** Enhance the user interface for a better user experience.

## Credits

- **Gradio:** For the user-friendly interface.
- **AssemblyAI:** For the robust audio transcription service.
- **ElevenLabs:** For the high-quality text-to-speech conversion.
- **translate Library:** For seamless text translation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Developed By

Sandeep Gudisa

---

Feel free to contribute, report issues, or suggest enhancements to improve this project!
