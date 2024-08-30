/**
 * script.js
 * 
 * This script manages the speech recognition process, handles the real-time transcription,
 * sends the transcript to the server for processing, and updates the analysis view with
 * the results. It uses the Web Speech API for speech recognition and fetch API for server
 * communication.
 */

document.addEventListener('DOMContentLoaded', (event) => {
    const startButton = document.getElementById('startRecognition');
    const stopButton = document.getElementById('stopRecognition');
    const transcriptionDiv = document.getElementById('transcription');
    const analysisDiv = document.getElementById('analysis');

    let recognition;
    let fullTranscript = '';
    let isListening = false;
    let analysisHistory = [];

    if ('webkitSpeechRecognition' in window) {
        recognition = new webkitSpeechRecognition();
        recognition.continuous = true;
        recognition.interimResults = true;

        /**
         * Capture the transcription results and update the transcriptionDiv.
         */
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

        /**
         * Handle the end of the recognition process, restarting if necessary.
         */
        recognition.onend = function() {
            console.log('Speech recognition service disconnected');
            if (isListening) {
                console.log('Restarting speech recognition');
                recognition.start();
            }
        };

        /**
         * Handle recognition errors, restarting if necessary.
         */
        recognition.onerror = function(event) {
            console.error('Speech recognition error:', event.error);
            if (event.error === 'no-speech' && isListening) {
                console.log('No speech detected, restarting recognition');
                recognition.stop();
                recognition.start();
            }
        };

        /**
         * Start the speech recognition process when the start button is pressed.
         */
        startButton.onclick = function() {
            fullTranscript = '';
            transcriptionDiv.innerHTML = '';
            recognition.start();
            isListening = true;
            startButton.disabled = true;
            stopButton.disabled = false;
        };

        /**
         * Stop the speech recognition process when the stop button is pressed.
         */
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

    /**
     * Send the current transcript and previous responses to the server for processing.
     */
    function sendTranscriptForProcessing() {
        console.log('Checking for transcript changes...');
        const currentTranscript = transcriptionDiv.innerText;

        console.log('Current transcript:', currentTranscript);
        console.log('Last processed transcript:', lastProcessedTranscript);

        if (currentTranscript !== lastProcessedTranscript) {
            console.log('Transcript changed, processing...');

            // Create a formatted string for previous responses
            const formattedPreviousResponses = analysisHistory.length > 0
                ? "Here are the previous responses that I've already highlighted to the member and call center agent. No need to send information about these items:\n\n" + analysisHistory.join('\n\n')
                : "";

            console.log('Formatted previous responses:', formattedPreviousResponses);

            fetch('/process_transcript', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    transcript: currentTranscript,
                    previousResponses: formattedPreviousResponses
                }),
            })
            .then(response => {
                console.log('Response received:', response);
                return response.json();
            })
            .then(data => {
                console.log('Analysis received:', data.analysis);
                // Add the new analysis to the history
                analysisHistory.push(data.analysis);
                // Update the analysis div with all responses
                updateAnalysisDiv();
            })
            .catch(error => {
                console.error('Error:', error);
            });

            lastProcessedTranscript = currentTranscript;
        } else {
            console.log('No change in transcript');
        }
    }

    /**
     * Update the analysis div with the current analysis history.
     */
    function updateAnalysisDiv() {
        analysisDiv.innerHTML = ''; // Clear existing content

        // Reverse the order of the analysisHistory array
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