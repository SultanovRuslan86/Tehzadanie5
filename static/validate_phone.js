function validatePhoneNumber() {
    var phoneNumberInput = document.getElementById('phone_number');
    var phoneNumber = phoneNumberInput.value;

    var phoneRegex = /^\+7\(\d{3}\)\d{3}-\d{2}-\d{2}$/;

    if (!phoneRegex.test(phoneNumber)) {
        alert('Invalid phone number format!');
        return false;
    }

    return true;
}