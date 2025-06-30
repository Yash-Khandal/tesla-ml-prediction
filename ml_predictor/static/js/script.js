// Tesla ML Prediction Dashboard - Interactive Features

document.addEventListener('DOMContentLoaded', function() {
    // Form Animation and Validation
    const form = document.getElementById('predictionForm');
    const submitBtn = form.querySelector('button[type="submit"]');
    
    // Add loading state to submit button
    form.addEventListener('submit', function() {
        submitBtn.innerHTML = `
            <span class="loading me-2"></span>
            Processing...
        `;
        submitBtn.disabled = true;
    });
    
    // Form field animations
    const formControls = document.querySelectorAll('.form-control, .form-select');
    formControls.forEach(control => {
        control.addEventListener('focus', function() {
            this.parentElement.style.transform = 'translateY(-2px)';
            this.parentElement.style.transition = 'transform 0.3s ease';
        });
        
        control.addEventListener('blur', function() {
            this.parentElement.style.transform = 'translateY(0)';
        });
    });
    
    // Price counter animation
    const priceAmount = document.querySelector('.price-amount');
    if (priceAmount) {
        const targetPrice = parseFloat(priceAmount.textContent.replace(/[$,]/g, ''));
        animatePrice(priceAmount, targetPrice);
    }
    
    // Tesla model selection effects
    const modelSelect = document.querySelector('select[name="tesla_model"]');
    if (modelSelect) {
        modelSelect.addEventListener('change', function() {
            const selectedModel = this.value;
            updateModelInfo(selectedModel);
        });
    }
});

// Animate price counting up
function animatePrice(element, targetPrice) {
    let currentPrice = 0;
    const increment = targetPrice / 100;
    
    const timer = setInterval(() => {
        currentPrice += increment;
        if (currentPrice >= targetPrice) {
            currentPrice = targetPrice;
            clearInterval(timer);
        }
        element.textContent = `$${currentPrice.toLocaleString('en-US', {
            minimumFractionDigits: 2,
            maximumFractionDigits: 2
        })}`;
    }, 20);
}

// Update model information based on selection
function updateModelInfo(model) {
    const modelInfo = {
        'Model 3': {
            icon: 'fas fa-car',
            description: 'Most popular Tesla model',
            avgPrice: '$45,000'
        },
        'Model Y': {
            icon: 'fas fa-car-side',
            description: 'Compact SUV',
            avgPrice: '$55,000'
        },
        'Model S': {
            icon: 'fas fa-car-alt',
            description: 'Luxury sedan',
            avgPrice: '$95,000'
        },
        'Model X': {
            icon: 'fas fa-truck',
            description: 'Luxury SUV',
            avgPrice: '$105,000'
        }
    };
    
    // Add visual feedback (you can expand this)
    console.log(`Selected: ${model} - ${modelInfo[model]?.description || 'Unknown model'}`);
}

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
