// Authentication Logic

function showLogin() {
    document.getElementById('login-form').classList.remove('hidden');
    document.getElementById('signup-form').classList.add('hidden');
}

function showSignup() {
    document.getElementById('login-form').classList.add('hidden');
    document.getElementById('signup-form').classList.remove('hidden');
}

document.getElementById('loginForm')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    const email = document.getElementById('login-email').value.trim();
    const password = document.getElementById('login-password').value;
    if (!email || !password) {
        showError('Please enter both email and password');
        return;
    }
    const users = safeGetItem('campusconnect_users', []);
    const user = users.find(u => u.email === email && u.password === password);
    if (user) {
        safeSetItem('campusconnect_current_user', user);
        showSuccess('Welcome back!');
        setTimeout(() => window.location.href = '/home.html', 1000);
    } else {
        showError('Invalid credentials!');
    }
});

document.getElementById('signupForm')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    const name = document.getElementById('signup-name').value.trim();
    const roll = document.getElementById('signup-roll').value.trim();
    const email = document.getElementById('signup-email').value.trim();
    const password = document.getElementById('signup-password').value;
    if (!name || !roll || !email || !password) {
        showError('Please fill all fields');
        return;
    }
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        showError('Please enter a valid email address');
        return;
    }
    if (password.length < 6) {
        showError('Password must be at least 6 characters');
        return;
    }
    const users = safeGetItem('campusconnect_users', []);
    if (users.find(u => u.email === email)) {
        showError('User already exists!');
        return;
    }
    if (users.find(u => u.roll === roll)) {
        showError('Roll number already registered!');
        return;
    }
    const newUser = {
        id: Date.now(),
        name, roll, email, password,
        wallet: 1000,
        points: 0,
        campus: 'Main Campus',
        createdAt: new Date().toISOString()
    };
    users.push(newUser);
    if (!safeSetItem('campusconnect_users', users)) {
        showError('Failed to create account');
        return;
    }
    safeSetItem('campusconnect_current_user', newUser);
    showSuccess('Account created successfully!');
    setTimeout(() => window.location.href = '/home.html', 1000);
});

document.addEventListener('DOMContentLoaded', () => {
    if (window.location.pathname === '/' || window.location.pathname === '/index.html') {
        const currentUser = getCurrentUser();
        if (currentUser) window.location.href = '/home.html';
    }
});

console.log('Auth JS Loaded');