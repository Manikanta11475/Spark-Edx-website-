// ============================================================================
// GOOGLE FORMS INTEGRATION CONFIGURATION
// ============================================================================

const GOOGLE_FORM_CONFIG = {
    // 1. Paste your Google Form Action URL here
    actionUrl: "https://docs.google.com/forms/d/e/1FAIpQLSeHK3L7N_cb2rAlyK5GxDxdUkvTP0F_zrxGf_ExrENP5mDfCg/formResponse",

    // 2. Map the HTML input names to your Google Form "entry.XXXXXX" IDs
    fieldMapping: {
        // --- Contact Form Fields ---
        "contact_name": "entry.1704007659", // Name
        "email":        "entry.920374262",  // Email ID
        "school_name":  "", // MISSING IN GOOGLE FORM! Replace with Entry ID for School Name
        "mobile":       "entry.1161193115", // Mobile number
        "location":     "", // MISSING IN GOOGLE FORM! Replace with Entry ID for Location
        "message":      "", // MISSING IN GOOGLE FORM! Replace with Entry ID for Message

        // --- Brochure Form Fields ---
        "name":         "entry.1704007659", // Name
        "email":        "entry.920374262",  // Email ID
        "school":       "", // MISSING IN GOOGLE FORM! Replace with Entry ID for Brochure School
        "phone":        "entry.1161193115"  // Mobile number
    }
};

// ============================================================================
// FORM HANDLING LOGIC (Do not edit below unless you know what you are doing)
// ============================================================================

document.addEventListener('DOMContentLoaded', () => {

    async function submitToGoogleForm(form, submitBtn, btnText, successCallback) {
        if (GOOGLE_FORM_CONFIG.actionUrl === "YOUR_GOOGLE_FORM_ACTION_URL_HERE") {
            alert("Google Form is not configured yet! Please update google-form-handler.js");
            submitBtn.innerHTML = btnText;
            submitBtn.disabled = false;
            return;
        }

        const formData = new FormData(form);
        const googleFormData = new URLSearchParams();

        // Map local form fields to Google Form entry IDs
        for (const [key, value] of formData.entries()) {
            const entryId = GOOGLE_FORM_CONFIG.fieldMapping[key];
            if (entryId) {
                googleFormData.append(entryId, value);
            }
        }

        try {
            // We use mode: 'no-cors' to bypass CORS errors. 
            // This means we can't read the response, but it successfully submits to Google.
            await fetch(GOOGLE_FORM_CONFIG.actionUrl, {
                method: 'POST',
                mode: 'no-cors',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: googleFormData.toString()
            });

            // Assuming success since no-cors doesn't give us a status code
            form.reset();
            if (successCallback) successCallback();

        } catch (error) {
            console.error("Form submission error:", error);
            alert("Oops! Something went wrong. Please try again.");
        } finally {
            submitBtn.innerHTML = btnText;
            submitBtn.disabled = false;
        }
    }

    // --- Contact Forms ---
    const contactForms = document.querySelectorAll('#contact-form, #main-contact-form');
    contactForms.forEach(form => {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const submitBtn = form.querySelector('button[type="submit"]');
            const originalBtnText = submitBtn.innerHTML;
            submitBtn.innerHTML = 'Sending...';
            submitBtn.disabled = true;

            submitToGoogleForm(form, submitBtn, originalBtnText, () => {
                alert("Thank you! Your message has been sent successfully.");
            });
        });
    });

    // --- Brochure Forms ---
    const brochureForms = document.querySelectorAll('#brochure-form');
    brochureForms.forEach(form => {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const submitBtn = form.querySelector('button[type="submit"]');
            const originalBtnText = submitBtn.innerHTML;
            submitBtn.innerHTML = 'Downloading...';
            submitBtn.disabled = true;

            submitToGoogleForm(form, submitBtn, originalBtnText, () => {
                alert("Thank you! Your brochure will download shortly.");
                
                // Simulate brochure download
                const link = document.createElement('a');
                link.href = 'assets/brochure.pdf'; 
                link.download = 'Spark_EdX_Brochure.pdf';
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
                
                // Close modal if open
                if (typeof closeBrochureModal === 'function') {
                    closeBrochureModal();
                }
            });
        });
    });

});
