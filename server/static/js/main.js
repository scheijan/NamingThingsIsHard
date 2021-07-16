function onSliderChange(mode, amount){
    console.log(mode, amount)
    const inputElement = document.getElementsByName(mode+"Amount")[0]
    RPGUI.set_value(inputElement, amount)
}

function onInputChange(mode, amount){
    console.log(mode, amount)
    const sliderElement = document.getElementsByName(mode + "AmountRange")[0]
    RPGUI.set_value(sliderElement, amount)
}