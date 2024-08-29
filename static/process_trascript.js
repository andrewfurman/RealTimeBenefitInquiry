let lastProcessedTranscript = '';
let isProcessing = false;

function updateProcessingIndicator() {
    const processingIndicator = document.getElementById('processingIndicator');
    processingIndicator.textContent = isProcessing ? 'Processing...' : 'Analysis will appear here during the conversation';
}

function sendTranscriptForProcessing() {
    console.log('Checking for transcript changes...');
    const transcriptionDiv = document.getElementById('transcription');
    const analysisTextarea = document.getElementById('analysis');
    const currentTranscript = transcriptionDiv.innerText;

    console.log('Current transcript:', currentTranscript);
    console.log('Last processed transcript:', lastProcessedTranscript);

    if (currentTranscript !== lastProcessedTranscript) {
        console.log('Transcript changed, processing...');
        isProcessing = true;
        updateProcessingIndicator();
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
            isProcessing = false;
            updateProcessingIndicator();
        })
        .catch(error => {
            console.error('Error:', error);
            isProcessing = false;
            updateProcessingIndicator();
        });

        lastProcessedTranscript = currentTranscript;
    } else {
        console.log('No change in transcript');
    }
}

// Check for changes and process transcript every 7 seconds
setInterval(sendTranscriptForProcessing, 7000);

// Immediate call to start the process
sendTranscriptForProcessing();

console.log('Script loaded and interval set');

// Add this at the end of the file
document.getElementById('startRecognition').addEventListener('click', () => {
    console.log('Manual trigger');
    sendTranscriptForProcessing();
});

// Ensure the processing indicator is visible immediately
updateProcessingIndicator();