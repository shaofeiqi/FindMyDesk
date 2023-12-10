let selectedSeatId = null;

function selectSeat(seatElement, seatLabel) {
  // Clear any previously selected seat
  const previouslySelectedSeat = document.querySelector('.seat.selected');
  if (previouslySelectedSeat) {
    previouslySelectedSeat.classList.remove('selected');
  }

  // If the seat is not reserved, mark it as selected
  if (!seatElement.classList.contains('reserved')) {
    seatElement.classList.add('selected');
    // Show the reserve button
    selectedSeatId = seatLabel
    const reserveButton = document.getElementById('reserveButton');
    reserveButton.style.display = 'block'; // Make the button visible
    reserveButton.disabled = false; // Enable the button
  }
}


document.getElementById('reserveButton').addEventListener('click', function() {
  
  let libraryName = document.getElementById('container').getAttribute('data-library-name');
  let floorName = document.getElementById('container').getAttribute('data-floor-name');
  window.location.href = `/select-timeslot/${libraryName}/${floorName}/${selectedSeatId}`;
});


// // JavaScript to make seats draggable and update positions
// document.addEventListener('DOMContentLoaded', function() {
//   var seats = document.querySelectorAll('.seat');

//   seats.forEach(function(seat) {
//     seat.addEventListener('dragstart', function(e) {
//       e.dataTransfer.setData('text/plain', e.target.id);
//     });
//   });

//   var container = document.querySelector('.map-container');
//   container.addEventListener('dragover', function(e) {
//     e.preventDefault(); // Necessary for the drop event to fire
//   });

//   container.addEventListener('drop', function(e) {
//     e.preventDefault();
//     var data = e.dataTransfer.getData('text/plain');
//     var seat = document.getElementById(data);

//     // Calculate new positions as a percentage of the container size
//     var newTop = ((e.clientY - container.offsetTop) / container.offsetHeight) * 100;
//     var newLeft = ((e.clientX - container.offsetLeft) / container.offsetWidth) * 100;

//     // Set the seat's new position
//     seat.style.top = newTop + '%';
//     seat.style.left = newLeft + '%';

//     // Save the new positions to your database using an AJAX call
//     // Example using fetch:
//     fetch('/update-seat-position', {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json',
//       },
//       body: JSON.stringify({
//         id: seat.dataset.id,
//         top: newTop,
//         left: newLeft
//       }),
//     })
//     .then(response => response.json())
//     .then(data => {
//       console.log('Success:', data);
//     })
//     .catch((error) => {
//       console.error('Error:', error);
//     });
//   });
// });
