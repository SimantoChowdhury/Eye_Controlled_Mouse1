function login() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  if (username && password) {
    document.querySelector(".login-box").classList.add("hidden");
    document.querySelector(".dashboard").classList.remove("hidden");

    // Call backend to launch Python script
    fetch('/start')
      .then(res => console.log("Python eye control launched"))
      .catch(err => console.error("Error launching:", err));
  } else {
    alert("Please enter username and password.");
  }
}

