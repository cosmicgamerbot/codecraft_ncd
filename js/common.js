// Common utilities shared across all pages

function showNotification(message, type = 'info') {
    const colors = {
        success: 'bg-green-500',
        error: 'bg-red-500',
        info: 'bg-blue-500',
        warning: 'bg-yellow-500'
    };
    const icons = {
        success: 'check_circle',
        error: 'error',
        info: 'info',
        warning: 'warning'
    };
    const notification = document.createElement('div');
    notification.className = `fixed top-20 right-4 ${colors[type]} text-white px-6 py-3 rounded-lg shadow-lg z-50 fade-in`;
    notification.innerHTML = `<span class="material-symbols-rounded align-middle mr-2">${icons[type]}</span>${message}`;
    document.body.appendChild(notification);
    setTimeout(() => notification.remove(), type === 'error' ? 4000 : 2500);
}

function showSuccess(message) { showNotification(message, 'success'); }
function showError(message) { showNotification(message, 'error'); }

function safeGetItem(key, defaultValue = null) {
    try {
        const item = localStorage.getItem(key);
        return item ? JSON.parse(item) : defaultValue;
    } catch (error) {
        console.error(`Error reading ${key}:`, error);
        return defaultValue;
    }
}

function safeSetItem(key, value) {
    try {
        localStorage.setItem(key, JSON.stringify(value));
        return true;
    } catch (error) {
        console.error(`Error writing ${key}:`, error);
        showError('Failed to save data');
        return false;
    }
}

function getCurrentUser() {
    return safeGetItem('campusconnect_current_user');
}

function isAuthenticated() {
    return getCurrentUser() !== null;
}

function requireAuth() {
    if (!isAuthenticated()) {
        window.location.href = '/index.html';
        return false;
    }
    return true;
}

function logout() {
    if (confirm('Are you sure you want to logout?')) {
        localStorage.removeItem('campusconnect_current_user');
        window.location.href = '/index.html';
    }
}

async function callNetlifyFunction(functionName, data) {
    try {
        const response = await fetch(`/.netlify/functions/${functionName}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        const result = await response.json();
        if (!response.ok) throw new Error(result.error || 'Request failed');
        return result;
    } catch (error) {
        console.error(`API Error (${functionName}):`, error);
        throw error;
    }
}

function formatCurrency(amount) {
    return `₹${amount.toLocaleString('en-IN')}`;
}

console.log('Common JS Loaded');