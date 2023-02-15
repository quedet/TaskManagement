import { Controller } from "@hotwired/stimulus";

export default class extends Controller {
    static values = {
        count: { type: Number, default: 0 },
    };

    static targets = ['count'];

    connect () {
        this.countTarget.innerHTML = this.countValue;
    }

    countValueChanged (value, previousValue) {
        console.log(`${previousValue} changed to ${value}`);
    }

    increment () {
        this.countValue++;
        this.countTarget.innerHTML = this.countValue;
    }
}
