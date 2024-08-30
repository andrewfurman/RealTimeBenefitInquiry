/**
 * process_transcript.js
 * 
 * This script handles updating the analysis view based on the processed transcripts 
 * received from the server. It also manages the UI while the transcript is being 
 * processed, providing feedback to the user.
 */

/**
 * Update the analysis div to display the previous responses in reverse order (newest first).
 * This function clears the existing content and then appends new responses to the analysis div.
 */
function updateAnalysisDiv() {
    const analysisDiv = document.getElementById('analysis');
    analysisDiv.innerHTML = ''; // Clear existing content

    // Display responses in reverse order (newest first)
    previousResponses.slice().reverse().forEach((analysis, index) => {
        const responseDiv = document.createElement('div');
        responseDiv.className = 'response';
        const responseNumber = previousResponses.length - index;
        responseDiv.innerHTML = `<h3>Response ${responseNumber}</h3>${marked.parse(analysis)}`;
        analysisDiv.appendChild(responseDiv);
    });
}

// No longer call updateProcessingIndicator() since it has been removed