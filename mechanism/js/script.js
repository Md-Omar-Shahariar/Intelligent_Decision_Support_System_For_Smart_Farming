const dropArea = document.querySelector(".drag-area");

let file;
//if user drag file over Drop Area
dropArea.addEventListener("dragover", (event) => {
    event.preventDefault();

    console.log("File is over");

    dropArea.classList.add("act");
});
//if user leave dragged file on Drop Area
dropArea.addEventListener("dragleave", () => {
    console.log("File is outside of that area ");
    dropArea.classList.remove("act");
});
dropArea.addEventListener("drop", (event) => {
    event.preventDefault();

    console.log("File is Droped ");
    file = event.dataTransfer.files[0];
    console.log(file);
    let fileType = file.type;
    console.log(fileType);
    let validExtension = ["image/jpeg", "image/jpg", "image/png"];
    if (validExtension.includes(fileType)) {
        console.log("This is Image");
    } else {
        alert("Invalid Type");
        dropArea.classList.remove("act");
    }

});