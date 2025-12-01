// Hospital ICU Management - Dashboard Script

document.addEventListener('DOMContentLoaded', function() {
    initializeEventListeners();
    loadDashboardData();
});

function initializeEventListeners() {
    // Add event listeners for forms, buttons, etc.
    console.log('Event listeners initialized');
}

function loadDashboardData() {
    // Load summary statistics
    fetch('/api/patients/')
        .then(response => response.json())
        .then(data => {
            console.log('Dashboard data loaded:', data);
        })
        .catch(error => console.error('Error loading dashboard:', error));
}

// API Helper Functions
const API = {
    get: async (endpoint) => {
        const response = await fetch(`/api${endpoint}`);
        return response.json();
    },
    
    post: async (endpoint, data) => {
        const response = await fetch(`/api${endpoint}`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(data)
        });
        return response.json();
    },
    
    put: async (endpoint, data) => {
        const response = await fetch(`/api${endpoint}`, {
            method: 'PUT',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(data)
        });
        return response.json();
    },
    
    delete: async (endpoint) => {
        const response = await fetch(`/api${endpoint}`, {
            method: 'DELETE'
        });
        return response.status === 204;
    }
};

// Utility Functions
function showNotification(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    document.body.insertBefore(alertDiv, document.body.firstChild);
}

function formatDate(dateString) {
    return new Date(dateString).toLocaleDateString('en-IN');
}

function calculateAge(dateOfBirth) {
    return Math.floor((new Date() - new Date(dateOfBirth)) / (365.25 * 24 * 60 * 60 * 1000));
}