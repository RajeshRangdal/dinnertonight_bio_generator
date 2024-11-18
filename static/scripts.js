document.addEventListener("DOMContentLoaded", function () {
  const bioForm = document.getElementById("bioForm");
  const resultElement = document.getElementById("result");

  bioForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    // Show loading state
    resultElement.textContent = "Generating your perfect bio...🔮";

    // Collect all form data
    const career = document.getElementById("career").value;
    const traits = Array.from(
      document.getElementById("traits").selectedOptions
    ).map((option) => option.value);
    const interests = Array.from(
      document.getElementById("interests").selectedOptions
    ).map((option) => option.value);
    const relationshipGoals =
      document.getElementById("relationship-goals").value;

    try {
      const response = await fetch("/generate_bio", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          career: career,
          traits: traits,
          interests: interests,
          relationshipGoals: relationshipGoals,
        }),
      });

      const data = await response.json();
      if (data.bio) {
        resultElement.textContent = data.bio;
      } else {
        resultElement.textContent =
          "Oops! 😅 " + (data.error || "Failed to generate bio");
      }
    } catch (error) {
      resultElement.textContent = "An error occurred: " + error.message;
      console.error("Error:", error);
    }
  });
});
