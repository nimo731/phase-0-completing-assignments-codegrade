// Morning: 5:00 AM to 11:59 AM (hours >=5 && hours < 12).

// Afternoon: 12:00 AM to 5:59 PM (hours >= 12 && hours < 18).

// Evening: 6:00 PM to 8:59 PM  (hours >= 18 && hours < 21 ).

// Night: 8:00 PM to 4:59 AM(else case).

const hours = 24;

if (hours >=5 && hours < 12) {
    console.log("morning") 
}else if (hours >= 12 && hours < 18) {
    console.log("afternoon")
}else if (hours >= 18 && hours < 21) {
    console.log ("evening")
}else (
    console.log ("night")
)