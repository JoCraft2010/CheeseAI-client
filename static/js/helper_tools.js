let sliderRegisterOnUpdate = (sliderID, outputID) => {
    var slider = document.getElementById(sliderID);
    var output = document.getElementById(outputID);
    output.innerHTML = slider.value;

    slider.oninput = function() {
        output.innerHTML = this.value;
    }
}
