async function upload(){
    const fileInput = document.getElementById('file');
    const file = fileInput.files[0]; // Get the selected file

    if (!file) {
        alert("Please select a file before uploading.");
        return;
    }

    // Ensure the file is a .txt file
    if (!file.name.endsWith('.txt')) {
        alert("Only .txt files are allowed!");
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData,
        });

        if (response.ok) {
            const result = await response.json();
            alert(`Success: ${result.message}`);
        } else {
            const error = await response.json();
            alert(`Error: ${error.error}`);
        }
    } catch (error) {
        console.error('Error uploading file:', error);
        alert('Something went wrong. Check the console for details.');
    }
}