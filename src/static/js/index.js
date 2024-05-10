var socket = io.connect(location.protocol + '//' + location.hostname + ':' + location.port);
    
    socket.on('connect', function() {
        console.log('Connected to server.')
    })

    socket.on('paths', function (output) {
        document.getElementById('pathOutput').innerHTML = output;
    });

    socket.on('solutions', function (output) {
        document.getElementById('possiblePaths').innerHTML = output;
    })


document.getElementById('findPath').addEventListener('click', function() {
    
    const formData = {
        startURL: document.getElementById('start_article').value,
        targetURL: document.getElementById('target_article').value
    }

    var options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    };
    fetch('/find-path', options)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
});
