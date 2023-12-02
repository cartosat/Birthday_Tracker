let birthDate = new Date(1998, 05, 01)
let todayDate = new Date()

var endYear = todayDate.getFullYear();
var currentMonth = todayDate.getMonth()+1
var birthMonth = birthDate.getMonth()+1
  
    
if(birthMonth == currentMonth && birthDate.getDate() < todayDate.getDate()){
    endYear = todayDate.getFullYear()+1
}
else if(birthMonth == currentMonth && birthDate.getDate() > todayDate.getDate()){
    endYear = todayDate.getFullYear()
}

else if(birthMonth == currentMonth && birthDate.getDate() == todayDate.getDate()){
    console.log("Its Your birthdayToday")
}

if(birthMonth < currentMonth ){
    
    endYear = todayDate.getFullYear()+1
}

let endDate = new Date(endYear, birthMonth-1, birthDate.getDate(), 00, 00);

let endTime = endDate.getTime();


function countdown() {
      let todayDate = new Date();
      let todayTime = todayDate.getTime();
      let remainingTime = endTime - todayTime;
      let oneMin = 60 * 1000;
      let oneHr = 60 * oneMin;
      let oneDay = 24 * oneHr;

    
    let daysLeft = Math.floor(remainingTime / oneDay);

    console.log(daysLeft)

}
countdown()
