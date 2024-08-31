import gradio as gr
import assemblyai as aai
from translate import Translator
import uuid
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from pathlib import Path

def process_input(text_input, audio_file, recorded_audio):
    if text_input:
        return translate_and_generate(text_input)
    elif audio_file:
        transcript = transcribe_audio(audio_file)
    elif recorded_audio:
        transcript = transcribe_audio(recorded_audio)
    else:
        raise gr.Error("Please provide either text input or an audio file.")
    
    if transcript.status == aai.TranscriptStatus.error:
        raise gr.Error(transcript.error)
    
    return translate_and_generate(transcript.text)

def translate_and_generate(text):
    list_translations = translate_text(text)
    generated_audio_paths = []

    for translation in list_translations:
        translated_audio_file_name = text_to_speech(translation)
        path = Path(translated_audio_file_name)
        generated_audio_paths.append(path)

    return tuple(generated_audio_paths) + tuple(list_translations)

def transcribe_audio(audio_file):
    aai.settings.api_key = "551438c8eb2d4eb2927307d8c763408e"
    transcriber = aai.Transcriber()
    return transcriber.transcribe(audio_file)

def translate_text(text: str) -> str:
    languages = ["ru", "tr", "sv", "de", "es", "ja", "hi", "te"]
    list_translations = []

    for lan in languages:
        translator = Translator(from_lang="en", to_lang=lan)
        translation = translator.translate(text)
        list_translations.append(translation)

    return list_translations

def text_to_speech(text: str) -> str:
    client = ElevenLabs(
        api_key="sk_9852342ec7afeaed89f471384e7e8cf019cd2899167704e2",
    )

    response = client.text_to_speech.convert(
        voice_id="nPczCjzI2devNBz1zQrb",
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_multilingual_v2",
        voice_settings=VoiceSettings(
            stability=0.5,
            similarity_boost=0.8,
            style=0.5,
            use_speaker_boost=True,
        ),
    )

    save_file_path = f"{uuid.uuid4()}.mp3"

    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"{save_file_path}: A new audio file was saved successfully!")
    return save_file_path

    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"{save_file_path}: A new audio file was saved successfully!")
    return save_file_path

with gr.Blocks() as demo:
    gr.Markdown("# Translate English to multiple languages (text and voice)")
    
    with gr.Tab("Text Input"):
        text_input = gr.Textbox(label="Enter English text")
        text_submit = gr.Button("Translate Text", variant="primary")

    with gr.Tab("Audio File"):
        audio_file = gr.Audio(label="Upload Audio File", type="filepath")
        file_submit = gr.Button("Translate Audio File", variant="primary")

    with gr.Tab("Record Audio"):
        recorded_audio = gr.Audio(
            label="Record Audio",
            sources=["microphone"],
            type="filepath",
        )
        record_submit = gr.Button("Translate Recorded Audio", variant="primary")

    with gr.Row():
        with gr.Column():
            ru_output = gr.Audio(label="Russian", interactive=False)
            ru_text = gr.Markdown()
        with gr.Column():
            tr_output = gr.Audio(label="Turkish", interactive=False)
            tr_text = gr.Markdown()
        with gr.Column():
            sv_output = gr.Audio(label="Swedish", interactive=False)
            sv_text = gr.Markdown()
        with gr.Column():
            de_output = gr.Audio(label="German", interactive=False)
            de_text = gr.Markdown()

    with gr.Row():
        with gr.Column():
            es_output = gr.Audio(label="Spanish", interactive=False)
            es_text = gr.Markdown()
        with gr.Column():
            jp_output = gr.Audio(label="Japanese", interactive=False)
            jp_text = gr.Markdown()
        with gr.Column():
            hi_output = gr.Audio(label="Hindi", interactive=False)
            hi_text = gr.Markdown()
        with gr.Column():
            te_output = gr.Audio(label="Telugu", interactive=False)
            te_text = gr.Markdown()

    output_components = [
        ru_output, tr_output, sv_output, de_output, es_output, jp_output, hi_output, te_output,
        ru_text, tr_text, sv_text, de_text, es_text, jp_text, hi_text, te_text
    ]

    text_submit.click(fn=process_input, inputs=[text_input, gr.State(None), gr.State(None)], outputs=output_components)
    file_submit.click(fn=process_input, inputs=[gr.State(None), audio_file, gr.State(None)], outputs=output_components)
    record_submit.click(fn=process_input, inputs=[gr.State(None), gr.State(None), recorded_audio], outputs=output_components)
    gr.Markdown("### Developed By Sandeep Gudisa")
if __name__ == "__main__":
    demo.launch()