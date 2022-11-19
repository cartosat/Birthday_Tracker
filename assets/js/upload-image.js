const wrapper__img = document.querySelector(".wrapper__img");
const fileName_img = document.querySelector(".file-name__img");
const defaultBtn_img = document.querySelector("#default-btn__img");
const customBtn_img = document.querySelector("#custom-btn__img");
const cancelBtn_img = document.querySelector("#cancel-btn__img i");
const profile_img = document.querySelector("img");
let regExp = /[0-9a-zA-Z\^\&\'\@\{\}\[\]\,\$\=\!\-\#\(\)\.\%\+\~\_ ]+$/;
function defaultBtn_imgActive(){
defaultBtn_img.click();
}
defaultBtn_img.addEventListener("change", function(){
const file_img = this.files[0];
if(file_img){
    const reader = new FileReader();
    reader.onload = function(){
    const result = reader.result;
    profile_img.src = result;
    wrapper__img.classList.add("active");
    }
    cancelBtn_img.addEventListener("click", function(){
    profile_img.src = "";
    wrapper__img.classList.remove("active");
    })
    reader.readAsDataURL(file_img);
}
if(this.value){
    let valueStore = this.value.match(regExp);
    fileName_img.textContent = valueStore;
}
});