// script.js
// Manages speech recognition, real-time transcription, server communication, and analysis updates.
// Uses Web Speech API for speech recognition and fetch API for server communication.

document.addEventListener('DOMContentLoaded', (event) => {
    const startButton = document.getElementById('startRecognition');
    const stopButton = document.getElementById('stopRecognition');
    const transcriptionDiv = document.getElementById('transcription');
    const analysisDiv = document.getElementById('analysis');

    let recognition;
    let fullTranscript = '';
    let isListening = false;
    let analysisHistory = [];
    let lastProcessedTranscript = '';

    if ('webkitSpeechRecognition' in window) {
        recognition = new webkitSpeechRecognition();
        recognition.continuous = true;
        recognition.interimResults = true;

        // Capture the transcription results and update the transcriptionDiv.
        recognition.onresult = (event) => {
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

        // Handle the end of the recognition process, restarting if necessary.
        recognition.onend = () => {
            if (isListening) {
                recognition.start();
            }
        };

        // Handle recognition errors, restarting if necessary.
        recognition.onerror = (event) => {
            if (event.error === 'no-speech' && isListening) {
                recognition.stop();
                recognition.start();
            }
        };

        // Start the speech recognition process when the start button is pressed.
        startButton.onclick = () => {
            fullTranscript = '';
            transcriptionDiv.innerHTML = '';
            recognition.start();
            isListening = true;
            startButton.disabled = true;
            stopButton.disabled = false;
        };

        // Stop the speech recognition process when the stop button is pressed.
        stopButton.onclick = () => {
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

    // Send the current transcript and previous responses to the server for processing.
    function sendTranscriptForProcessing() {
        const currentTranscript = transcriptionDiv.innerText;
        if (currentTranscript !== lastProcessedTranscript) {
            const formattedPreviousResponses = analysisHistory.length > 0
                ? "Here are the previous responses that I've already highlighted to the member and call center agent. No need to send information about these items:\n\n" + analysisHistory.join('\n\n')
                : "";
            fetch('/process_transcript', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    transcript: currentTranscript + formattedPreviousResponses
                }),
            })
            .then(response => response.json())
            .then(data => {
                // Check if the response contains "No Major Update"
                if (!data.analysis.includes("No Major Update")) {
                    analysisHistory.push(data.analysis);
                    updateAnalysisDiv();
                }
            })
            .catch(error => console.error('Error:', error));
            lastProcessedTranscript = currentTranscript;
        }
    }

    // Update the analysis div with the current analysis history.
    function updateAnalysisDiv() {
        analysisDiv.innerHTML = '';
        analysisHistory.slice().reverse().forEach((analysis) => {
            const responseDiv = document.createElement('div');
            responseDiv.className = 'response';
            responseDiv.innerHTML = marked.parse(analysis);
            analysisDiv.appendChild(responseDiv);
        });
    }

    // Check for changes and process transcript every 6 seconds
    setInterval(sendTranscriptForProcessing, 6000);

    // Immediate call to start the process
    sendTranscriptForProcessing();
});