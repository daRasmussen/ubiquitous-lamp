const alerts = document.querySelectorAll(".alert")
for(let alert of alerts) {
    alert.classList.add("fadeIn");
    alert.classList.add("fast")
    setTimeout(function() {
        alert.classList.remove("fadeIn");
        alert.classList.add("fadeOut");
        setTimeout(function(){
            alert.remove()
        }, 500)
    }, 1000)
}