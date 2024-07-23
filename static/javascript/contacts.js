


document.addEventListener("DOMContentLoaded", function() {
    var btn = document.getElementById("addContactbtn");
    var trash=document.getElementById("trash");
    btn.addEventListener("click", function() {
        window.location.href = "/contacts/add";
    });
    trash.addEventListener("click", function() {
        alert("contacts removed successfully");
    });
});
