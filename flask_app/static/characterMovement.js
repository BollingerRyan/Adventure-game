// Get the character image element
const characterImage = document.getElementById('character-image');

// Add an event listener to the document
document.addEventListener('keydown', (event) => {
  // Get the current position of the character image
    const x = parseInt(characterImage.style.left);
    const y = parseInt(characterImage.style.top);

  // Define the distance to move the character for each arrow key pressed
    const distance = 32;

  // Move the character image based on the arrow key pressed
    if (event.key === "ArrowRight") {
    characterImage.style.left = `${x + distance}px`; // Move character right
    } else if (event.key === "ArrowLeft") {
    characterImage.style.left = `${x - distance}px`; // Move character left
    } else if (event.key === "ArrowUp") {
    characterImage.style.top = `${y - distance}px`; // Move character up
    } else if (event.key === "ArrowDown") {
    characterImage.style.top = `${y + distance}px`; // Move character down
    }
});