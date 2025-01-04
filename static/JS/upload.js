SUPPORTED_FILE_EXTENSIONS = [".txt", ".py"]

function isFileSupported(fileName){
    let allowed = false;
    for(let i = 0; i < SUPPORTED_FILE_EXTENSIONS.length; i++){
        if(fileName.endsWith(SUPPORTED_FILE_EXTENSIONS[i])){
            allowed = true;
            console.log(SUPPORTED_FILE_EXTENSIONS[i], " allowed is true");
        }

    }
    console.log(allowed);
    return allowed;
}

async function upload(){
    const fileInput = document.getElementById('file');
    const file = fileInput.files[0]; // Get the selected file

    if (!file) {
        alert("Please select a file before uploading.");
        return;
    }

    // Ensure the file is an allowed extension file
    if (isFileSupported(file.name)){
        const formData = new FormData();
        formData.append('file', file);


        try {
            const response = await fetch('/upload', {
                method: 'POST',
                body: formData,
            });

            if (response.ok) {
                const result = await response.json();
                document.getElementById('out').innerHTML = result.message;
                document.getElementById('code').style.display = 'block';
                Prism.highlightAll();
            } else {
                const error = await response.json();
                alert(`Error: ${error.error}`);
            }
        } catch (error) {
            console.error('Error uploading file:', error);
            alert('Something went wrong. Check the console for details.');
        }
    } else{
        alert("Only txt and python files are supported.");
    }


}