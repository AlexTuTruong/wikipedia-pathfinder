var socket = io.connect(location.protocol + '//' + location.hostname + ':' + location.port);
    
    socket.on('connect', function() {
        console.log('Connected to server.')
    })

    socket.on('paths', function (output) {
        document.getElementById('pathOutput').innerText = output;
    });

    socket.on('solutions', function (output) {
        document.getElementById('possiblePaths').innerHTML = output;
    })


document.getElementById('findPath').addEventListener('click', function() {
    
    const formData = {
        startURL: document.getElementById('start_article').value,
        targetURL: document.getElementById('target_article').value
    }

    // Fetch options
    var options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    };

    // Fetch POST request to the Flask endpoint
    fetch('/find-path', options)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            // return response.json();  // Parse response JSON
        })
        .then(data => {
            console.log('Response received:', data);
            // Handle the response data as needed
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
});
