document.addEventListener("DOMContentLoaded", function() {
    const returnBtn = document.getElementById("returnToContacts");

    returnBtn.addEventListener("click", function() {
        window.location.href = "/contacts";
        alert("contact added successfully");
    });
});
