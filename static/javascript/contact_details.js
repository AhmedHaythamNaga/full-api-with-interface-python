document.addEventListener("DOMContentLoaded", function() {
    const toggleEditBtn = document.getElementById("toggleEditBtn");
    const saveBtn = document.getElementById("saveBtn");
    const formElements = document.querySelectorAll("#contactDetails input");

    toggleEditBtn.addEventListener("click", function() {
        const isReadOnly = formElements[0].hasAttribute("readonly");

        formElements.forEach(input => {
            if (isReadOnly) {
                input.removeAttribute("readonly");
            } else {
                input.setAttribute("readonly", true);
            }
        });

        toggleEditBtn.textContent = isReadOnly ? "Disable Editing" : "Enable Editing";
        saveBtn.style.display = isReadOnly ? "inline" : "none";
    });
});
