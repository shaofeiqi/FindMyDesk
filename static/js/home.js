// // Update this function to calculate the remaining time
// function checkTime() {
//   // Get the current time and end time from the DOM
//   const endTime = document.getElementById('endTime').innerText;
//   const currentTime = new Date();

//   // Parse the end time and compare it with the current time
//   // Show the extend offer if there's 15 minutes left
//   // This is a placeholder, you'll need to parse the times and calculate the difference
//   if (/* condition for 15 minutes left */) {
//     document.getElementById('extendOffer').classList.remove('hidden');
//     // Show the phone notification
//     if (Notification.permission === "granted") {
//       new Notification("FindMyDesk: 15 More Minutes", {
//         body: "Would you like to extend your reservation?"
//       });
//     }
//   }
// }

// // Check every minute
// setInterval(checkTime, 60000);

// // Request permission for Notifications on page load
// document.addEventListener('DOMContentLoaded', function () {
//   if (Notification.permission !== "granted")
//     Notification.requestPermission();
// });

// // Event listeners for the buttons
// document.getElementById('leaveNowBtn').addEventListener('click', function() {
//   // Implement leave action
// });

// document.getElementById('friendsBtn').addEventListener('click', function() {
//   // Implement friends action
// });

// document.getElementById('yesBtn').addEventListener('click', function() {
//   // Implement yes action for extending time
// });

// document.getElementById('noBtn').addEventListener('click', function() {
//   // Implement no action for not extending time
// });

const endTime = {{end_time}}
let timerInterval;

const timeDisplay = document.getElementById('time');
const timerCircle = document.querySelector('#timer-svg circle');
const circumference = 2 * Math.PI * timerCircle.r.baseVal.value;

timerCircle.style.strokeDasharray = `${circumference} ${circumference}`;
timerCircle.style.strokeDashoffset = `${circumference}`;

function updateTimer() {
  const now = new Date().getTime();
  let remainingTime = endTime - now;

  // If the countdown is over, clear the interval
  if (remainingTime <= 0) {
    clearInterval(timerInterval);
    timeDisplay.textContent = '00:00';
    timerCircle.style.strokeDashoffset = circumference;
    // You might want to add some additional code here to handle what happens when the timer reaches zero.
    return;
  }

  // Calculate remaining time
  const minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);

  // Update the timer display
  timeDisplay.textContent = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;

  // Update the stroke offset
  const offset = circumference - (endTime - now) / (endTime - startTime) * circumference;
  timerCircle.style.strokeDashoffset = offset;
}

// Start the timer
timerInterval = setInterval(updateTimer, 1000);

