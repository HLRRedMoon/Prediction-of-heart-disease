function updateBullets(currentStep) {
    const bullets = document.querySelectorAll('.bullet');
    bullets.forEach((bullet, index) => {
        if (index < currentStep - 1) {
            bullet.classList.add('completed');
        } else {
            bullet.classList.remove('completed');
        }
        if (index === currentStep - 1) {
            bullet.classList.add('current');
        } else {
            bullet.classList.remove('current');
        }
    });
}

function nextStep(step) {
    document.getElementById('step' + (step - 1)).className = "step hidden";
    document.getElementById('step' + step).className = "step ";
    updateBullets(step);
}

function previousStep(step) {
    document.getElementById('step' + (step + 1)).className = "step hidden";
    document.getElementById('step' + step).className = "step ";
    updateBullets(step);
}
