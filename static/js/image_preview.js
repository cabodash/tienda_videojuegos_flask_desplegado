document.getElementById("fotoPortada").addEventListener('change', function(event) {
    if (event.target.files.length > 0) {
        let src = URL.createObjectURL(event.target.files[0]);
        let preview = document.getElementById("preview-img");
        preview.src = src;
        preview.style.display = "block";
    }
});