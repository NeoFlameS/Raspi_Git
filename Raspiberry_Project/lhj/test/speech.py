# -*- coding: utf-8 -*-
#!/usr/bin/env python

from __future__ import division
from __future__ import unicode_literals

import re
import sys
import time
import camera

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import pyaudio
from six.moves import queue

RATE = 16000
CHUNK = int(RATE / 10)  # 100ms
test=0

class MicrophoneStream(object):
    """Opens a recording stream as a generator yielding the audio chunks."""
    def __init__(self, rate, chunk):
        self._rate = rate
        self._chunk = chunk
        self._buff = queue.Queue()
        self.closed = True

    def __enter__(self):
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            channels=1, rate=self._rate,
            input=True, frames_per_buffer=self._chunk,
            stream_callback=self._fill_buffer,
        )
        self.closed = False

        return self

    def __exit__(self, type, value, traceback):
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        # Signal the generator to terminate so that the client's
        # streaming_recognize method will not block the process termination.
        self._buff.put(None)
        self._audio_interface.terminate()

    def _fill_buffer(self, in_data, frame_count, time_info, status_flags):
        """Continuously collect data from the audio stream, into the buffer."""
        self._buff.put(in_data)
        return None, pyaudio.paContinue

    def generator(self):
        while not self.closed:
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]

            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                except queue.Empty:
                    break

            yield b''.join(data)

def listen_print_loop(responses):
    num_chars_printed = 0
    for response in responses:
        if not response.results:
            continue
        
        result = response.results[0]
        if not result.alternatives:
            continue

        transcript = ""
        transcript = result.alternatives[0].transcript

        overwrite_chars = '' * (num_chars_printed - len(transcript))

        if not result.is_final:
            sys.stdout.write(transcript + overwrite_chars + '\r')
            sys.stdout.flush()

            num_chars_printed = len(transcript)

        else:
            print(transcript + overwrite_chars)
            transcript.replace(" ","")
                
            com = "음성인식"
            if transcript == com:
                print("앞으로 갑니다")
                transcript = ""
                
            if transcript == "왼쪽" or transcript == " 왼쪽":
                GPIO.output(12, True)
                print(transcript)
                time.sleep(0.5)
                GPIO.output(12, False)
                transcript = ""
                
            elif transcript == "오른쪽" or transcript == " 오른쪽":
                GPIO.output(18, True)
                print(transcript)
                time.sleep(0.5)
                GPIO.output(18, False)
                transcript = ""
                
            elif transcript == "카메라" or transcript == " 카메라":
                camera.camera()
                print("카메라 촬영 완료")
            
            elif transcript == "동영상" or transcript == " 동영상":
                camera.video()
                print("동영상 저장")
            
            if re.search(r'\b(exit|quit)\b', transcript, re.I):
                print('Exiting..')
                break

            num_chars_printed = 0

def main():
    language_code = 'ko-KR'  # a BCP-47 language tag
    
    i = 0

    client = speech.SpeechClient()
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code=language_code)
    streaming_config = types.StreamingRecognitionConfig(
        config=config,
        interim_results=True)

    with MicrophoneStream(RATE, CHUNK) as stream:
        audio_generator = stream.generator()
        requests = (types.StreamingRecognizeRequest(audio_content=content)
                    for content in audio_generator)

        responses = client.streaming_recognize(streaming_config, requests)

        listen_print_loop(responses)


if __name__ == '__main__':
    main()
