document.addEventListener("DOMContentLoaded", function() {
    const returnBtn = document.getElementById("returnToContacts");
    var nameInput = document.getElementById("full_name");
    var phoneInput = document.getElementById("phone_number");
    returnBtn.addEventListener("click", function() {
        window.location.href = "/contacts";
        if(nameInput.value != "" && phoneInput.value != "" ) {
        alert("contact added successfully");}
    });
});