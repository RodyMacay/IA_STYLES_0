document.addEventListener("DOMContentLoaded", function() {
    var notificationIcon = document.getElementById("notification-icon");
    var notificationDropdown = document.querySelector(".notification-dropdown");

    notificationIcon.addEventListener("click", function(event) {
        event.stopPropagation();
        notificationDropdown.classList.toggle("active");
    });

    document.addEventListener("click", function() {
        notificationDropdown.classList.remove("active");
    });
});
