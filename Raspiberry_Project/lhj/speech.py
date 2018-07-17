# -*- coding: utf-8 -*-
#!/usr/bin/env python

<<<<<<< HEAD
# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Cloud Speech API sample application using the streaming API.

NOTE: This module requires the additional dependency `pyaudio`. To install
using pip:

    pip install pyaudio

Example usage:
    python transcribe_streaming_mic.py
"""

# [START import_libraries]
=======
>>>>>>> 9763b6ca0dfaaeca4ec7c60dd525e2ac03c96666
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
import RPi.GPIO as GPIO
from six.moves import queue
<<<<<<< HEAD
# [END import_libraries]
=======
>>>>>>> 9763b6ca0dfaaeca4ec7c60dd525e2ac03c96666

GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

<<<<<<< HEAD
# Audio recording parameters
=======
>>>>>>> 9763b6ca0dfaaeca4ec7c60dd525e2ac03c96666
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms


class MicrophoneStream(object):
    """Opens a recording stream as a generator yielding the audio chunks."""
    def __init__(self, rate, chunk):
        self._rate = rate
        self._chunk = chunk

<<<<<<< HEAD
        # Create a thread-safe buffer of audio data
=======
>>>>>>> 9763b6ca0dfaaeca4ec7c60dd525e2ac03c96666
        self._buff = queue.Queue()
        self.closed = True

    def __enter__(self):
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
<<<<<<< HEAD
            # The API currently only supports 1-channel (mono) audio
            # https://goo.gl/z757pE
            channels=1, rate=self._rate,
            input=True, frames_per_buffer=self._chunk,
            # Run the audio stream asynchronously to fill the buffer object.
            # This is necessary so that the input device's buffer doesn't
            # overflow while the calling thread makes network requests, etc.
=======
            channels=1, rate=self._rate,
            input=True, frames_per_buffer=self._chunk,
>>>>>>> 9763b6ca0dfaaeca4ec7c60dd525e2ac03c96666
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
<<<<<<< HEAD
            # Use a blocking get() to ensure there's at least one chunk of
            # data, and stop iteration if the chunk is None, indicating the
            # end of the audio stream.
=======
>>>>>>> 9763b6ca0dfaaeca4ec7c60dd525e2ac03c96666
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]

<<<<<<< HEAD
            # Now consume whatever other data's still buffered.
=======
>>>>>>> 9763b6ca0dfaaeca4ec7c60dd525e2ac03c96666
            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                except queue.Empty:
                    break

            yield b''.join(data)
<<<<<<< HEAD
# [END audio_stream]

=======
>>>>>>> 9763b6ca0dfaaeca4ec7c60dd525e2ac03c96666

def listen_print_loop(responses):
    """Iterates through server responses and prints them.

    The responses passed is a generator that will block until a response
    is provided by the server.

    Each response may contain multiple results, and each result may contain
    multiple alternatives; for details, see https://goo.gl/tjCPAU.  Here we
    print only the transcription for the top alternative of the top result.

    In this case, responses are provided for interim results as well. If the
    response is an interim one, print a line feed at the end of it, to allow
    the next result to overwrite it, until the response is a final one. For the
    final one, print a newline to preserve the finalized transcription.
    """
    num_chars_printed = 0
    for response in responses:
        if not response.results:
            continue
<<<<<<< HEAD

        # The `results` list is consecutive. For streaming, we only care about
        # the first result being considered, since once it's `is_final`, it
        # moves on to considering the next utterance.
=======
        
>>>>>>> 9763b6ca0dfaaeca4ec7c60dd525e2ac03c96666
        result = response.results[0]
        if not result.alternatives:
            continue

<<<<<<< HEAD
        # Display the transcription of the top alternative.
        transcript = ""
        transcript = result.alternatives[0].transcript

        # Display interim results, but with a carriage return at the end of the
        # line, so subsequent lines will overwrite them.
        #
        # If the previous result was longer than this one, we need to print
        # some extra spaces to overwrite the previous result
=======
        transcript = ""
        transcript = result.alternatives[0].transcript

>>>>>>> 9763b6ca0dfaaeca4ec7c60dd525e2ac03c96666
        overwrite_chars = '' * (num_chars_printed - len(transcript))

        if not result.is_final:
            sys.stdout.write(transcript + overwrite_chars + '\r')
            sys.stdout.flush()

            num_chars_printed = len(transcript)

        else:
            print(transcript + overwrite_chars)
<<<<<<< HEAD
            #print(transcript)
            #print(overwrite_chars)
=======
>>>>>>> 9763b6ca0dfaaeca4ec7c60dd525e2ac03c96666
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
<<<<<<< HEAD
                print("camera")
                
            # Exit recognition if any of the transcribed phrases could be
            # one of our keywords.
=======
                print("카메라 촬영 완료")
            
            elif transcript == "동영상" or transcript == " 동영상":
                camera.video()
                print("동영상 저장")
            
>>>>>>> 9763b6ca0dfaaeca4ec7c60dd525e2ac03c96666
            if re.search(r'\b(exit|quit)\b', transcript, re.I):
                print('Exiting..')
                break

            num_chars_printed = 0

def main():
<<<<<<< HEAD
    # See http://g.co/cloud/speech/docs/languages
    # for a list of supported languages.
=======
>>>>>>> 9763b6ca0dfaaeca4ec7c60dd525e2ac03c96666
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

<<<<<<< HEAD
        # Now, put the transcription responses to use.
=======
>>>>>>> 9763b6ca0dfaaeca4ec7c60dd525e2ac03c96666
        listen_print_loop(responses)


if __name__ == '__main__':
    main()
