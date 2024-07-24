document.addEventListener("DOMContentLoaded", function() {
    var enableEdit = document.getElementById("m");
    var disableEdit = document.getElementById("b");
    var editableInputs = document.getElementsByClassName("edit");

    enableEdit.addEventListener('change', function() {
        for (var j = 0; j < editableInputs.length; j++) {
            editableInputs[j].removeAttribute("readonly");
        }
    });

    disableEdit.addEventListener('change', function() {
        for (var j = 0; j < editableInputs.length; j++) {
            editableInputs[j].setAttribute("readonly", true);
        }
    });


});
