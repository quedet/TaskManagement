import "../styles/turbo_drive.scss";

import "@hotwired/turbo";

window.document.addEventListener("turbo:load", function () {
    console.log("turbo:load");
});

window.document.addEventListener("turbo:before-cache", function () {
    console.log("turbo:before-cache");
    const form = document.querySelector('form');
    if (form)
        form.reset();
});

window.document.addEventListener("turbo:submit-start", function ({ target }) {
    console.log("Turbo:submit-start");
    console.log(target);
});
