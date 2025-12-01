# TEMPLATES AND FRONTEND SETUP

## templates/base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Hospital ICU Management System{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css">
    <style>
        :root {
            --primary-color: #2c3e50;
            --secondary-color: #3498db;
            --danger-color: #e74c3c;
            --success-color: #27ae60;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #ecf0f1;
        }
        
        navbar {
            background-color: var(--primary-color) !important;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .sidebar {
            background-color: var(--primary-color);
            min-height: 100vh;
            padding: 20px;
            color: white;
        }
        
        .sidebar a {
            color: white;
            text-decoration: none;
            padding: 10px;
            display: block;
            border-radius: 4px;
            margin: 5px 0;
            transition: background-color 0.3s;
        }
        
        .sidebar a:hover {
            background-color: var(--secondary-color);
        }
        
        .card {
            border: none;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        
        .card-header {
            background-color: var(--secondary-color);
            color: white;
            border: none;
        }
        
        .btn-primary {
            background-color: var(--secondary-color);
            border-color: var(--secondary-color);
        }
        
        .btn-primary:hover {
            background-color: #2980b9;
        }
        
        .table thead {
            background-color: var(--primary-color);
            color: white;
        }
        
        .badge-urgent {
            background-color: var(--danger-color);
        }
        
        .badge-high {
            background-color: #e67e22;
        }
        
        .badge-medium {
            background-color: var(--secondary-color);
        }
        
        .badge-low {
            background-color: var(--success-color);
        }
    </style>
    {% block extra_css %}{% endblock %}
</head>
<body>
    <!-- Navigation Bar -->
    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="/">
                <i class="bi bi-hospital"></i> Hospital ICU Management
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="/admin">Admin Panel</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/api/docs">API Docs</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <div class="container-fluid">
        <div class="row">
            <!-- Sidebar -->
            <div class="col-md-3 sidebar d-none d-md-block">
                <h5 class="mb-4"><i class="bi bi-menu-button"></i> Navigation</h5>
                <a href="/" class="active"><i class="bi bi-house"></i> Dashboard</a>
                <hr style="border-color: rgba(255,255,255,0.2);">
                
                <h6 class="text-uppercase mt-3 mb-3">Core Management</h6>
                <a href="/patients"><i class="bi bi-person"></i> Patients</a>
                <a href="/staff"><i class="bi bi-people"></i> Staff</a>
                <hr style="border-color: rgba(255,255,255,0.2);">
                
                <h6 class="text-uppercase mt-3 mb-3">Doctor Services</h6>
                <a href="/prescriptions"><i class="bi bi-prescription"></i> Prescriptions</a>
                <a href="/treatments"><i class="bi bi-bandaid"></i> Treatment Plans</a>
                <hr style="border-color: rgba(255,255,255,0.2);">
                
                <h6 class="text-uppercase mt-3 mb-3">Nurse Services</h6>
                <a href="/admissions"><i class="bi bi-door-open"></i> Admissions</a>
                <a href="/observations"><i class="bi bi-clipboard-check"></i> Observations</a>
                <hr style="border-color: rgba(255,255,255,0.2);">
                
                <h6 class="text-uppercase mt-3 mb-3">Other</h6>
                <a href="/equipment"><i class="bi bi-tools"></i> Equipment</a>
                <a href="/reports"><i class="bi bi-file-earmark-text"></i> Reports</a>
            </div>

            <!-- Main Content -->
            <div class="col-md-9 ms-auto p-4">
                {% block content %}
                <div class="alert alert-info">
                    Welcome to Hospital ICU Management System. Select an option from the navigation.
                </div>
                {% endblock %}
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
```

## templates/patients/patient_list.html

```html
{% extends 'base.html' %}

{% block title %}Patients - Hospital ICU Management{% endblock %}

{% block content %}
<div class="card">
    <div class="card-header">
        <div class="row align-items-center">
            <div class="col">
                <h4 class="mb-0"><i class="bi bi-person"></i> Patient Management</h4>
            </div>
            <div class="col-auto">
                <a href="/patients/add/" class="btn btn-light">
                    <i class="bi bi-plus"></i> Add Patient
                </a>
            </div>
        </div>
    </div>
    <div class="card-body">
        <div class="row mb-3">
            <div class="col-md-6">
                <input type="text" id="searchInput" class="form-control" placeholder="Search by Patient ID, Name...">
            </div>
            <div class="col-md-6">
                <select id="statusFilter" class="form-select">
                    <option value="">All Status</option>
                    <option value="admitted">Admitted</option>
                    <option value="discharged">Discharged</option>
                </select>
            </div>
        </div>

        <div class="table-responsive">
            <table class="table table-hover">
                <thead>
                    <tr>
                        <th>Patient ID</th>
                        <th>Name</th>
                        <th>Age</th>
                        <th>Blood Group</th>
                        <th>Status</th>
                        <th>Contact</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody id="patientTableBody">
                    <!-- Data loaded via JavaScript/API -->
                </tbody>
            </table>
        </div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    loadPatients();
    
    document.getElementById('searchInput').addEventListener('input', loadPatients);
    document.getElementById('statusFilter').addEventListener('change', loadPatients);
});

function loadPatients() {
    const search = document.getElementById('searchInput').value;
    const status = document.getElementById('statusFilter').value;
    
    fetch(`/api/patients/?search=${search}`)
        .then(response => response.json())
        .then(data => {
            const tbody = document.getElementById('patientTableBody');
            tbody.innerHTML = '';
            
            data.results.forEach(patient => {
                const age = new Date().getFullYear() - new Date(patient.date_of_birth).getFullYear();
                const statusBadge = patient.is_admitted ? 
                    '<span class="badge bg-success">Admitted</span>' : 
                    '<span class="badge bg-secondary">Discharged</span>';
                
                tbody.innerHTML += `
                    <tr>
                        <td><strong>${patient.patient_id}</strong></td>
                        <td>${patient.first_name} ${patient.last_name}</td>
                        <td>${age}</td>
                        <td>${patient.blood_group}</td>
                        <td>${statusBadge}</td>
                        <td>${patient.phone}</td>
                        <td>
                            <a href="/patients/${patient.id}/edit/" class="btn btn-sm btn-info">Edit</a>
                            <button class="btn btn-sm btn-danger" onclick="deletePatient(${patient.id})">Delete</button>
                        </td>
                    </tr>
                `;
            });
        })
        .catch(error => console.error('Error:', error));
}

function deletePatient(id) {
    if (confirm('Are you sure?')) {
        fetch(`/api/patients/${id}/`, {method: 'DELETE'})
            .then(() => loadPatients())
            .catch(error => alert('Error: ' + error));
    }
}
</script>
{% endblock %}
```

## static/js/dashboard.js

```javascript
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
```

## static/css/style.css

```css
/* Hospital ICU Management - Custom Styles */

:root {
    --primary-color: #2c3e50;
    --secondary-color: #3498db;
    --danger-color: #e74c3c;
    --success-color: #27ae60;
    --warning-color: #f39c12;
    --info-color: #3498db;
    --light-color: #ecf0f1;
    --dark-color: #34495e;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: var(--light-color);
    color: var(--dark-color);
}

/* Typography */
h1, h2, h3, h4, h5, h6 {
    color: var(--primary-color);
    margin-bottom: 1rem;
}

/* Cards */
.card {
    border: none;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.card-header {
    background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
    color: white;
    border: none;
    border-radius: 8px 8px 0 0;
    font-weight: 600;
}

/* Buttons */
.btn-primary {
    background-color: var(--secondary-color);
    border-color: var(--secondary-color);
    transition: all 0.3s ease;
}

.btn-primary:hover {
    background-color: #2980b9;
    border-color: #2980b9;
}

.btn-sm {
    border-radius: 4px;
}

/* Tables */
.table {
    background-color: white;
}

.table thead {
    background-color: var(--primary-color);
    color: white;
}

.table tbody tr:hover {
    background-color: var(--light-color);
}

/* Forms */
.form-control, .form-select {
    border: 1px solid #ddd;
    border-radius: 4px;
    transition: border-color 0.3s ease;
}

.form-control:focus, .form-select:focus {
    border-color: var(--secondary-color);
    box-shadow: 0 0 0 0.2rem rgba(52, 152, 219, 0.25);
}

/* Badges */
.badge {
    padding: 0.5rem 0.75rem;
    border-radius: 4px;
    font-weight: 500;
}

.badge-urgent {
    background-color: var(--danger-color);
}

.badge-high {
    background-color: var(--warning-color);
}

.badge-medium {
    background-color: var(--secondary-color);
}

.badge-low {
    background-color: var(--success-color);
}

/* Responsive */
@media (max-width: 768px) {
    .sidebar {
        display: none;
    }
}
```

