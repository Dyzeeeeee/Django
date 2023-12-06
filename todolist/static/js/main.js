// Get DOM elements
const addTaskLink = document.getElementById("addTaskLink");
const addTaskCard = document.getElementById("addTaskCard");
const cancelTaskButton = document.getElementById("cancelTaskButton");
const addTaskButton = document.getElementById("addTaskButton");
const taskNameInput = document.getElementById("taskNameInput");
const taskDescriptionInput = document.getElementById("taskDescriptionInput");

// Show the card when Add Task link is clicked
addTaskLink.addEventListener("click", function () {
  addTaskLink.style.display = "none";
  addTaskCard.style.display = "block";
});

// Hide the card and show Add Task link when Cancel is clicked
cancelTaskButton.addEventListener("click", function () {
  addTaskLink.style.display = "block";
  addTaskCard.style.display = "none";
});

// Handle Add Task button click
addTaskButton.addEventListener("click", function () {
  // Submit the form
  document.getElementById("addTaskForm").submit();

  // Clear the input fields
  // taskNameInput.value = '';
  // taskDescriptionInput.value = '';

  // Hide the card and show Add Task link
  addTaskLink.style.display = "block";
  addTaskCard.style.display = "none";
});

const toggleBtn = document.getElementById("toggle-sidebar");
const sidebarBtn = document.getElementById("sidebar-btn");
const sidebar = document.getElementById("sidebar");

toggleBtn.addEventListener("click", () => {
  sidebarBtn.style.transform =
    sidebarBtn.style.transform === "translateX(-11%)"
      ? "translateX(0)"
      : "translateX(-11%)";
  sidebar.classList.toggle("sidebar-hidden");
});

new Sortable(document.getElementById("sortable-list"), {
  handle: ".form-check",
  animation: 500,
  onStart: function (evt) {
    // Add any logic you need when sorting starts
  },
  onUpdate: function (evt) {
    // Add any logic you need when sorting updates
    var sortedIds = [];
    var items = evt.from.children;
    for (var i = 0; i < items.length; i++) {
      sortedIds.push(items[i].getAttribute("data-id"));
    }
    console.log(sortedIds);
    // You can send sortedIds to your server using AJAX to update the order in the database
  },
});
