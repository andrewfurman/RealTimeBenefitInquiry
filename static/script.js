document.addEventListener('DOMContentLoaded', (event) => {
    const startButton = document.getElementById('startRecognition');
    const stopButton = document.getElementById('stopRecognition');
    const transcriptionDiv = document.getElementById('transcription');

    let recognition;
    let fullTranscript = '';
    let isListening = false;

    if ('webkitSpeechRecognition' in window) {
        recognition = new webkitSpeechRecognition();
        recognition.continuous = true;
        recognition.interimResults = true;

        recognition.onresult = function(event) {
            let interimTranscript = '';
            let currentTranscript = '';

            for (let i = event.resultIndex; i < event.results.length; ++i) {
                if (event.results[i].isFinal) {
                    currentTranscript += event.results[i][0].transcript;
                } else {
                    interimTranscript += event.results[i][0].transcript;
                }
            }

            fullTranscript += currentTranscript;

            transcriptionDiv.innerHTML = fullTranscript + 
                '<i style="color: #999;">' + interimTranscript + '</i>';

            transcriptionDiv.scrollTop = transcriptionDiv.scrollHeight;
        };

        recognition.onend = function() {
            console.log('Speech recognition service disconnected');
            if (isListening) {
                console.log('Restarting speech recognition');
                recognition.start();
            }
        };

        recognition.onerror = function(event) {
            console.error('Speech recognition error:', event.error);
            if (event.error === 'no-speech' && isListening) {
                console.log('No speech detected, restarting recognition');
                recognition.stop();
                recognition.start();
            }
        };

        startButton.onclick = function() {
            fullTranscript = '';
            transcriptionDiv.innerHTML = '';
            recognition.start();
            isListening = true;
            startButton.disabled = true;
            stopButton.disabled = false;
        };

        stopButton.onclick = function() {
            recognition.stop();
            isListening = false;
            startButton.disabled = false;
            stopButton.disabled = true;
        };
    } else {
        startButton.style.display = 'none';
        stopButton.style.display = 'none';
        transcriptionDiv.innerHTML = 'Web Speech API is not supported in this browser.';
    }

    let lastProcessedTranscript = '';

    function sendTranscriptForProcessing() {
        console.log('Checking for transcript changes...');
        const analysisTextarea = document.getElementById('analysis');
        const currentTranscript = transcriptionDiv.innerText;

        console.log('Current transcript:', currentTranscript);
        console.log('Last processed transcript:', lastProcessedTranscript);

        if (currentTranscript !== lastProcessedTranscript) {
            console.log('Transcript changed, processing...');
            fetch('/process_transcript', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ transcript: currentTranscript }),
            })
            .then(response => {
                console.log('Response received:', response);
                return response.json();
            })
            .then(data => {
                console.log('Analysis received:', data.analysis);
                analysisTextarea.value = data.analysis;
            })
            .catch(error => {
                console.error('Error:', error);
            });

            lastProcessedTranscript = currentTranscript;
        } else {
            console.log('No change in transcript');
        }
    }

    // Check for changes and process transcript every 5 seconds
    setInterval(sendTranscriptForProcessing, 5000);

    // Immediate call to start the process
    sendTranscriptForProcessing();

    console.log('Script loaded and interval set');

    // Manual trigger for testing
    startButton.addEventListener('click', () => {
        console.log('Manual trigger');
        sendTranscriptForProcessing();
    });
});