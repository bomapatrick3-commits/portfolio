const contactForm = document.getElementById("contactForm");

const nameInput = document.getElementById("name");

const emailInput = document.getElementById("email");

const messageInput = document.getElementById("message");

const nameError = document.getElementById("nameError");

const emailError = document.getElementById("emailError");

const messageError = document.getElementById("messageError");

const successMessage = document.getElementById("successMessage");


        contactForm.addEventListener("submit", function(event) {

            event.preventDefault();


           

            nameError.textContent = "";

            emailError.textContent = "";

            messageError.textContent = "";

            successMessage.textContent = "";


            let valid = true;


            // Check name

            if (nameInput.value.trim() === "") {

                console.log("Name is empty");
                nameError.textContent = "Please enter your name.";

                valid = false;

            }


            // Check email

            if (emailInput.value.trim() === "") {

                console.log("Email is empty");
                emailError.textContent = "Please enter your email address.";

                valid = false;

            }
            else if (!emailInput.validity.valid) {

                console.log("Invalid email:", emailInput.value);
                emailError.textContent = "Please enter a valid email address.";

                valid = false;

            }


            

            if (messageInput.value.trim() === "") {

                console.log("Message is empty");
                messageError.textContent = "Please enter your message.";

                valid = false;

            }
            else if (messageInput.value.trim().length < 10) {

                console.log("Message is too short:", messageInput.value.trim().length);
                messageError.textContent =
                    "Your message should contain at least 10 characters.";

                valid = false;

            }


            

            if (valid) {

                console.log("Form submitted successfully!");
                successMessage.textContent =
                    "Thank you! Your message has been prepared successfully.";

                contactForm.reset();

            }

        });
