SUPPORTED_FILE_EXTENSIONS = [".txt", ".py"]

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

    if (files.length === 0) {
        alert("Please select files before uploading.");
        return;
    }

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
            } else {
                const error = await response.json();
                alert(`Error: ${error.error}`);
            }
        } catch (error) {
            console.error('Error uploading file:', error);
            alert('Something went wrong. Check the console for details.');
        }


}