document.addEventListener("DOMContentLoaded", function () {
  const alerts = document.querySelectorAll(".custom-alert");
  alerts.forEach((alert) => {
    setTimeout(() => {
      alert.style.opacity = "0";
      setTimeout(() => alert.remove(), 500);
    }, 3000);
  });
  
  const html_ = document.querySelector(".data p");
  if (html_) {
    const data = new Date();
    html_.innerHTML = data.toLocaleDateString("pt-BR", {
      dateStyle: "full",
    });
  }
});
