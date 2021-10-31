const dropArea = document.querySelector(".drag-area");
dragText = dropArea.querySelector("h5");
button = dropArea.querySelector("button");
input = dropArea.querySelector("input");

button.onclick = () => {
    input.click();
}
input.addEventListener("change", function () {
    file = this.files[0];
    showFile();
    dropArea.classList.add("act");
});



let file;
//if user drag file over Drop Area
dropArea.addEventListener("dragover", (event) => {
    event.preventDefault();

    console.log("File is over");

    dropArea.classList.add("act");
    dragText.textContent = "Realease To Upload File";

});
//if user leave dragged file on Drop Area
dropArea.addEventListener("dragleave", () => {
    console.log("File is outside of that area ");
    dropArea.classList.remove("act");
    dragText.textContent = "Drag & Drop to Upload Image";

});
dropArea.addEventListener("drop", (event) => {
    event.preventDefault();

    console.log("File is Droped ");
    file = event.dataTransfer.files[0];
    showFile();

});
function showFile() {
    let fileType = file.type;
    // console.log(fileType);
    let validExtension = ["image/jpeg", "image/jpg", "image/png"];
    if (validExtension.includes(fileType)) {
        // console.log("This is Image");
        let fileReader = new FileReader();
        fileReader.onload = () => {
            let fileURL = fileReader.result;

            let imgTag = `<img src="${fileURL}" alt = "">`;
            dropArea.innerHTML = imgTag;
        };
        fileReader.readAsDataURL(file);
    } else {
        alert("Invalid Type");
        dropArea.classList.remove("act");
    }
}
var form = document.getElementById('submit');
form.addEventListener('submit', function (event) {
    event.preventDefault();
    var image = document.getElementById("image");
    console.log(image);
})