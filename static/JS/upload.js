SUPPORTED_FILE_EXTENSIONS = [".py"]

function supported(fileName){
    allowed = false
    for( var i = 0; i < SUPPORTED_FILE_EXTENSIONS.length; i++){
        if (fileName.endsWith(SUPPORTED_FILE_EXTENSIONS[i])){
            return true;
        }
    }
    return false;

}

async function upload() {


    const fileInput = document.getElementById("file");
    const files = fileInput.files;
    const loadingIndicator = document.getElementById('loading');
    const responseDiv = document.getElementById('code');
    const fileSelect = document.getElementById('send');



    if (files.length === 0) {
        alert("Please select files before uploading.");
        return;
    }

    loadingIndicator.style.display = 'block';
    responseDiv.style.display = 'none';
    fileSelect.style.display = 'none';

    const formData = new FormData();
    for (const file of files) {
        if(supported(file.name)){
            formData.append("files", file);
        }
    }

    try {
        const response = await fetch("/upload", {
            method: "POST",
            body: formData,
        });

            if (response.ok) {
                const result = await response.json();
                document.getElementById('out').innerHTML = result.message;
                document.getElementById('code').style.display = 'block';
                Prism.highlightAll();
                loadingIndicator.style.display = 'none';
                fileSelect.style.display = 'block';
                fileInput.value = "";
            } else {
                const error = await response.json();
                alert(`Error: ${error.error}`);
                loadingIndicator.style.display = 'none';
                fileSelect.style.display = 'block';
            }
        } catch (error) {
            console.error('Error uploading file:', error);
            alert('Something went wrong. Check the console for details.');
            loadingIndicator.style.display = 'none';
            fileSelect.style.display = 'block';
        }


}