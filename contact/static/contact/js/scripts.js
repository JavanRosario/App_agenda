document.addEventListener("DOMContentLoaded", function () {
  const alert = document.querySelectorAll(".custom-alert");
  alert.forEach((alert) => {
    setTimeout(() => {
      alert.style.opacity = "0";
      setTimeout(() => alert.remove(), 500);
    }, 3000);
  });
});
    