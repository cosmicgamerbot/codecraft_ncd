#!/usr/bin/env python3
"""
CampusConnect Project Generator
Creates all files and folders for the CampusConnect project
"""

import os
import sys

def create_folder_structure(base_path):
    """Create the project folder structure"""
    folders = [
        'css',
        'js',
        'netlify/functions',
        'images'
    ]
    
    print("📁 Creating folder structure...")
    for folder in folders:
        path = os.path.join(base_path, folder)
        os.makedirs(path, exist_ok=True)
        print(f"   ✓ {folder}")

def create_file(base_path, filename, content):
    """Create a file with the given content"""
    filepath = os.path.join(base_path, filename)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"   ✓ {filename}")

def generate_index_html():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#2196F3">
    <title>CampusConnect - Login</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
</head>
<body class="antialiased bg-gradient-to-br from-blue-50 via-blue-100 to-teal-50 min-h-screen">
    <div class="min-h-screen flex items-center justify-center p-4">
        <div class="bg-white p-8 rounded-2xl shadow-2xl max-w-md w-full fade-in">
            <div class="text-center mb-8">
                <div class="w-20 h-20 bg-gradient-to-br from-blue-500 to-teal-400 rounded-2xl mx-auto mb-4 flex items-center justify-center shadow-lg">
                    <span class="text-4xl font-black text-white">C</span>
                </div>
                <h1 class="text-4xl font-extrabold text-gray-800 mb-2">Campus<span class="text-teal-500">Connect</span></h1>
                <p class="text-gray-600">Your unified campus platform</p>
            </div>

            <div id="login-form">
                <h2 class="text-2xl font-bold mb-6 text-gray-800">Welcome Back</h2>
                <form id="loginForm">
                    <div class="mb-4">
                        <label class="block text-sm font-medium mb-2 text-gray-700">Email</label>
                        <input type="email" id="login-email" required 
                               class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all"
                               placeholder="student@campus.edu">
                    </div>
                    <div class="mb-6">
                        <label class="block text-sm font-medium mb-2 text-gray-700">Password</label>
                        <input type="password" id="login-password" required 
                               class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all"
                               placeholder="••••••••">
                    </div>
                    <button type="submit" class="w-full py-3 bg-gradient-to-r from-blue-500 to-teal-400 text-white font-semibold rounded-lg hover:opacity-90 transition-all shadow-md">
                        Login
                    </button>
                </form>
                <p class="mt-4 text-center text-sm text-gray-600">
                    Don't have an account? <button onclick="showSignup()" class="text-blue-500 font-semibold hover:underline">Sign Up</button>
                </p>
            </div>

            <div id="signup-form" class="hidden">
                <h2 class="text-2xl font-bold mb-6 text-gray-800">Create Account</h2>
                <form id="signupForm">
                    <div class="mb-4">
                        <label class="block text-sm font-medium mb-2 text-gray-700">Full Name</label>
                        <input type="text" id="signup-name" required 
                               class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all"
                               placeholder="Aashish Kumar">
                    </div>
                    <div class="mb-4">
                        <label class="block text-sm font-medium mb-2 text-gray-700">Roll Number</label>
                        <input type="text" id="signup-roll" required 
                               class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all"
                               placeholder="CS2023001">
                    </div>
                    <div class="mb-4">
                        <label class="block text-sm font-medium mb-2 text-gray-700">Email</label>
                        <input type="email" id="signup-email" required 
                               class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all"
                               placeholder="student@campus.edu">
                    </div>
                    <div class="mb-6">
                        <label class="block text-sm font-medium mb-2 text-gray-700">Password</label>
                        <input type="password" id="signup-password" required 
                               class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all"
                               placeholder="••••••••">
                    </div>
                    <button type="submit" class="w-full py-3 bg-gradient-to-r from-blue-500 to-teal-400 text-white font-semibold rounded-lg hover:opacity-90 transition-all shadow-md">
                        Create Account
                    </button>
                </form>
                <p class="mt-4 text-center text-sm text-gray-600">
                    Already have an account? <button onclick="showLogin()" class="text-blue-500 font-semibold hover:underline">Login</button>
                </p>
            </div>
        </div>
    </div>

    <script src="js/common.js"></script>
    <script src="js/auth.js"></script>
</body>
</html>'''

def generate_home_html():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CampusConnect - Home</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
</head>
<body class="bg-gray-50">
    <!-- Header -->
    <header class="fixed top-0 left-0 right-0 z-20 flex items-center justify-between h-16 px-4 bg-white shadow-md">
        <div class="flex items-center space-x-2">
            <div class="w-10 h-10 bg-gradient-to-br from-blue-500 to-teal-400 rounded-lg flex items-center justify-center">
                <span class="text-xl font-black text-white">C</span>
            </div>
            <span class="text-lg font-bold text-gray-800">Campus<span class="text-teal-500">Connect</span></span>
        </div>
        <button onclick="logout()" class="text-gray-600 hover:text-red-500">
            <span class="material-symbols-rounded">logout</span>
        </button>
    </header>

    <!-- Main Content -->
    <main class="pt-20 pb-20 px-4">
        <div id="content" class="max-w-4xl mx-auto"></div>
    </main>

    <!-- Bottom Navigation -->
    <nav class="fixed bottom-0 left-0 right-0 h-16 bg-white shadow-2xl flex justify-around items-center">
        <a href="home.html" class="flex flex-col items-center text-blue-500">
            <span class="material-symbols-rounded">home</span>
            <span class="text-xs">Home</span>
        </a>
        <a href="library.html" class="flex flex-col items-center text-gray-600 hover:text-blue-500">
            <span class="material-symbols-rounded">local_library</span>
            <span class="text-xs">Library</span>
        </a>
        <a href="canteen.html" class="flex flex-col items-center text-gray-600 hover:text-blue-500">
            <span class="material-symbols-rounded">restaurant</span>
            <span class="text-xs">Canteen</span>
        </a>
        <a href="profile.html" class="flex flex-col items-center text-gray-600 hover:text-blue-500">
            <span class="material-symbols-rounded">person</span>
            <span class="text-xs">Profile</span>
        </a>
    </nav>

    <script src="js/common.js"></script>
    <script>
        // Check authentication
        if (!requireAuth()) {
            // Will redirect to login
        } else {
            // Load home content
            const user = getCurrentUser();
            const content = document.getElementById('content');
            
            content.innerHTML = `
                <h2 class="text-2xl font-bold mb-6">Welcome back, ${user.name.split(' ')[0]}! 👋</h2>
                
                <div class="grid grid-cols-3 gap-4 mb-8">
                    <div class="bg-white p-4 rounded-xl shadow-md text-center">
                        <p class="text-3xl font-bold text-blue-600">3</p>
                        <p class="text-sm text-gray-600">Books</p>
                    </div>
                    <div class="bg-white p-4 rounded-xl shadow-md text-center">
                        <p class="text-3xl font-bold text-teal-600">2</p>
                        <p class="text-sm text-gray-600">Orders</p>
                    </div>
                    <div class="bg-white p-4 rounded-xl shadow-md text-center">
                        <p class="text-3xl font-bold text-orange-600">${user.points}</p>
                        <p class="text-sm text-gray-600">Points</p>
                    </div>
                </div>

                <div class="bg-white p-6 rounded-xl shadow-md mb-6">
                    <h3 class="font-bold text-lg mb-4">Quick Actions</h3>
                    <div class="grid grid-cols-2 gap-3">
                        <a href="library.html" class="p-4 bg-blue-500 text-white rounded-lg text-center hover:bg-blue-600">
                            <span class="material-symbols-rounded block mb-2 text-3xl">menu_book</span>
                            Browse Books
                        </a>
                        <a href="canteen.html" class="p-4 bg-teal-500 text-white rounded-lg text-center hover:bg-teal-600">
                            <span class="material-symbols-rounded block mb-2 text-3xl">restaurant</span>
                            Order Food
                        </a>
                    </div>
                </div>

                <div class="bg-gradient-to-r from-green-50 to-teal-50 p-6 rounded-xl border-2 border-green-300">
                    <h3 class="font-bold text-center mb-4 flex items-center justify-center">
                        <span class="material-symbols-rounded mr-2 text-2xl text-green-600">eco</span>
                        Your Eco Score
                    </h3>
                    <div class="text-center">
                        <p class="text-5xl font-bold text-green-600 mb-2">85%</p>
                        <p class="text-sm text-gray-700">Keep making sustainable choices! 🌱</p>
                    </div>
                </div>
            `;
        }
    </script>
</body>
</html>'''

def generate_library_html():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CampusConnect - Library</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
</head>
<body class="bg-gray-50">
    <header class="fixed top-0 left-0 right-0 z-20 flex items-center justify-between h-16 px-4 bg-white shadow-md">
        <div class="flex items-center space-x-2">
            <div class="w-10 h-10 bg-gradient-to-br from-blue-500 to-teal-400 rounded-lg flex items-center justify-center">
                <span class="text-xl font-black text-white">C</span>
            </div>
            <span class="text-lg font-bold text-gray-800">Library</span>
        </div>
        <button onclick="logout()" class="text-gray-600 hover:text-red-500">
            <span class="material-symbols-rounded">logout</span>
        </button>
    </header>

    <main class="pt-20 pb-20 px-4">
        <div class="max-w-4xl mx-auto">
            <div class="mb-4">
                <input type="text" id="search" placeholder="Search books..." 
                       class="w-full px-4 py-3 rounded-full border-2 border-gray-300 focus:border-blue-500">
            </div>
            
            <div id="books-container" class="grid grid-cols-2 gap-4"></div>
        </div>
    </main>

    <nav class="fixed bottom-0 left-0 right-0 h-16 bg-white shadow-2xl flex justify-around items-center">
        <a href="home.html" class="flex flex-col items-center text-gray-600 hover:text-blue-500">
            <span class="material-symbols-rounded">home</span>
            <span class="text-xs">Home</span>
        </a>
        <a href="library.html" class="flex flex-col items-center text-blue-500">
            <span class="material-symbols-rounded">local_library</span>
            <span class="text-xs">Library</span>
        </a>
        <a href="canteen.html" class="flex flex-col items-center text-gray-600 hover:text-blue-500">
            <span class="material-symbols-rounded">restaurant</span>
            <span class="text-xs">Canteen</span>
        </a>
        <a href="profile.html" class="flex flex-col items-center text-gray-600 hover:text-blue-500">
            <span class="material-symbols-rounded">person</span>
            <span class="text-xs">Profile</span>
        </a>
    </nav>

    <script src="js/common.js"></script>
    <script src="js/library.js"></script>
</body>
</html>'''

def generate_canteen_html():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CampusConnect - Canteen</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
</head>
<body class="bg-gray-50">
    <header class="fixed top-0 left-0 right-0 z-20 flex items-center justify-between h-16 px-4 bg-white shadow-md">
        <div class="flex items-center space-x-2">
            <div class="w-10 h-10 bg-gradient-to-br from-blue-500 to-teal-400 rounded-lg flex items-center justify-center">
                <span class="text-xl font-black text-white">C</span>
            </div>
            <span class="text-lg font-bold text-gray-800">Canteen</span>
        </div>
        <div class="relative">
            <span class="material-symbols-rounded text-2xl">shopping_cart</span>
            <span id="cart-badge" class="hidden absolute -top-2 -right-2 w-5 h-5 bg-red-500 text-white text-xs rounded-full flex items-center justify-center"></span>
        </div>
    </header>

    <main class="pt-20 pb-20 px-4">
        <div class="max-w-4xl mx-auto">
            <div id="cart-section" class="hidden mb-6"></div>
            <div id="menu-container" class="grid grid-cols-2 gap-4"></div>
        </div>
    </main>

    <nav class="fixed bottom-0 left-0 right-0 h-16 bg-white shadow-2xl flex justify-around items-center">
        <a href="home.html" class="flex flex-col items-center text-gray-600 hover:text-blue-500">
            <span class="material-symbols-rounded">home</span>
            <span class="text-xs">Home</span>
        </a>
        <a href="library.html" class="flex flex-col items-center text-gray-600 hover:text-blue-500">
            <span class="material-symbols-rounded">local_library</span>
            <span class="text-xs">Library</span>
        </a>
        <a href="canteen.html" class="flex flex-col items-center text-blue-500">
            <span class="material-symbols-rounded">restaurant</span>
            <span class="text-xs">Canteen</span>
        </a>
        <a href="profile.html" class="flex flex-col items-center text-gray-600 hover:text-blue-500">
            <span class="material-symbols-rounded">person</span>
            <span class="text-xs">Profile</span>
        </a>
    </nav>

    <script src="js/common.js"></script>
    <script src="js/canteen.js"></script>
</body>
</html>'''

def generate_profile_html():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CampusConnect - Profile</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
</head>
<body class="bg-gray-50">
    <header class="fixed top-0 left-0 right-0 z-20 flex items-center justify-between h-16 px-4 bg-white shadow-md">
        <div class="flex items-center space-x-2">
            <div class="w-10 h-10 bg-gradient-to-br from-blue-500 to-teal-400 rounded-lg flex items-center justify-center">
                <span class="text-xl font-black text-white">C</span>
            </div>
            <span class="text-lg font-bold text-gray-800">Profile</span>
        </div>
    </header>

    <main class="pt-20 pb-20 px-4">
        <div id="profile-content" class="max-w-4xl mx-auto"></div>
    </main>

    <nav class="fixed bottom-0 left-0 right-0 h-16 bg-white shadow-2xl flex justify-around items-center">
        <a href="home.html" class="flex flex-col items-center text-gray-600 hover:text-blue-500">
            <span class="material-symbols-rounded">home</span>
            <span class="text-xs">Home</span>
        </a>
        <a href="library.html" class="flex flex-col items-center text-gray-600 hover:text-blue-500">
            <span class="material-symbols-rounded">local_library</span>
            <span class="text-xs">Library</span>
        </a>
        <a href="canteen.html" class="flex flex-col items-center text-gray-600 hover:text-blue-500">
            <span class="material-symbols-rounded">restaurant</span>
            <span class="text-xs">Canteen</span>
        </a>
        <a href="profile.html" class="flex flex-col items-center text-blue-500">
            <span class="material-symbols-rounded">person</span>
            <span class="text-xs">Profile</span>
        </a>
    </nav>

    <script src="js/common.js"></script>
    <script src="js/profile.js"></script>
</body>
</html>'''

def generate_common_js():
    return '''// Common utilities shared across all pages

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

console.log('Common JS Loaded');'''

def generate_auth_js():
    return '''// Authentication Logic

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
    const emailRegex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
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

console.log('Auth JS Loaded');'''

def generate_library_js():
    return '''// Library page logic
requireAuth();

const books = [
    { id: 1, title: 'The Tech Future', author: 'John Tech', available: true, category: 'Technology', rating: 4.5 },
    { id: 2, title: 'Data Science 101', author: 'Jane Data', available: true, category: 'Science', rating: 4.8 },
    { id: 3, title: 'Campus Life Hacks', author: 'Alex Campus', available: false, category: 'Lifestyle', rating: 4.2 },
    { id: 4, title: 'AI Revolution', author: 'Sara AI', available: true, category: 'Technology', rating: 4.7 },
    { id: 5, title: 'Quantum Physics', author: 'Bob Quantum', available: true, category: 'Science', rating: 4.6 },
    { id: 6, title: 'Design Thinking', author: 'Emma Design', available: true, category: 'Design', rating: 4.4 }
];

function displayBooks(booksToShow = books) {
    const container = document.getElementById('books-container');
    container.innerHTML = booksToShow.map(book => `
        <div class="bg-white p-3 rounded-xl shadow-lg border border-gray-200">
            <div class="w-full h-36 bg-gradient-to-br ${book.available ? 'from-blue-100 to-blue-200' : 'from-gray-100 to-gray-200'} rounded-lg mb-2 flex items-center justify-center">
                <span class="material-symbols-rounded text-5xl ${book.available ? 'text-blue-600' : 'text-gray-400'}">menu_book</span>
            </div>
            <p class="text-sm font-semibold truncate">${book.title}</p>
            <p class="text-xs text-gray-600 truncate mb-1">${book.author}</p>
            <div class="flex items-center justify-between mb-2">
                <span class="text-xs ${book.available ? 'text-green-600' : 'text-gray-500'} font-medium">
                    ${book.available ? '● Available' : '● Not Available'}
                </span>
                <span class="text-xs text-yellow-600">★ ${book.rating}</span>
            </div>
            <button onclick="borrowBook(${book.id})" ${!book.available ? 'disabled' : ''} 
                    class="w-full py-1 text-xs font-semibold ${book.available ? 'bg-blue-500 hover:bg-blue-600 text-white' : 'bg-gray-300 text-gray-500 cursor-not-allowed'} rounded-md">
                ${book.available ? 'Borrow' : 'Unavailable'}
            </button>
        </div>
    `).join('');
}

function borrowBook(id) {
    const book = books.find(b => b.id === id);
    if (book && book.available) {
        book.available = false;
        showSuccess(`"${book.title}" borrowed successfully!`);
        displayBooks();
        const user = getCurrentUser();
        user.points += 10;
        safeSetItem('campusconnect_current_user', user);
    }
}

document.getElementById('search').addEventListener('input', (e) => {
    const query = e.target.value.toLowerCase();
    const filtered = books.filter(book => 
        book.title.toLowerCase().includes(query) ||
        book.author.toLowerCase().includes(query) ||
        book.category.toLowerCase().includes(query)
    );
    displayBooks(filtered);
});

displayBooks();
console.log('Library JS Loaded');'''

def generate_canteen_js():
    return '''// Canteen page logic
requireAuth();

const menuItems = [
    { id: 1, name: 'Veg Biryani', price: 60, veg: true, emoji: '🍚', calories: 450 },
    { id: 2, name: 'Paneer Tikka', price: 80, veg: true, emoji: '🧈', calories: 350 },
    { id: 3, name: 'Masala Dosa', price: 50, veg: true, emoji: '🥞', calories: 300 },
    { id: 4, name: 'Chole Bhature', price: 70, veg: true, emoji: '🍛', calories: 500 },
    { id: 5, name: 'Pasta Alfredo', price: 90, veg: true, emoji: '🍝', calories: 400 },
    { id: 6, name: 'Veg Sandwich', price: 40, veg: true, emoji: '🥪', calories: 250 }
];

let cart = safeGetItem('campusconnect_cart', []);

function displayMenu() {
    const container = document.getElementById('menu-container');
    container.innerHTML = menuItems.map(item => `
        <div class="bg-white p-3 rounded-xl shadow-lg border border-gray-200">
            <div class="text-5xl text-center mb-2">${item.emoji}</div>
            <p class="text-sm font-semibold text-center truncate">${item.name}</p>
            <p class="text-xs text-center text-gray-600 mb-2">${item.calories} cal</p>
            <div class="flex justify-between items-center mb-2">
                <span class="text-lg font-bold text-teal-600">₹${item.price}</span>
                ${item.veg ? '<span class="text-xs text-green-600 font-semibold">🌱 Veg</span>' : ''}
            </div>
            <button onclick="addToCart(${item.id})" class="w-full py-2 text-xs font-semibold text-white bg-gradient-to-r from-blue-500 to-blue-600 rounded-md hover:opacity-90">
                Add to Cart
            </button>
        </div>
    `).join('');
}

function displayCart() {
    const cartSection = document.getElementById('cart-section');
    const cartBadge = document.getElementById('cart-badge');
    const cartCount = cart.reduce((sum, item) => sum + item.quantity, 0);
    
    if (cartCount > 0) {
        cartBadge.textContent = cartCount;
        cartBadge.classList.remove('hidden');
    } else {
        cartBadge.classList.add('hidden');
    }
    
    if (cart.length === 0) {
        cartSection.classList.add('hidden');
        return;
    }
    
    cartSection.classList.remove('hidden');
    const total = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    
    cartSection.innerHTML = `
        <div class="bg-white p-4 rounded-xl shadow-md border-2 border-blue-300">
            <h3 class="font-bold mb-3">Your Cart</h3>
            ${cart.map(item => `
                <div class="flex justify-between items-center mb-2">
                    <div>
                        <p class="font-semibold">${item.name}</p>
                        <p class="text-sm text-gray-600">₹${item.price} × ${item.quantity}</p>
                    </div>
                    <button onclick="removeFromCart(${item.id})" class="text-red-500 hover:text-red-700">
                        <span class="material-symbols-rounded">delete</span>
                    </button>
                </div>
            `).join('')}
            <div class="border-t-2 pt-3 mt-3 flex justify-between items-center font-bold text-lg">
                <span>Total:</span>
                <span class="text-blue-600">₹${total}</span>
            </div>
            <button onclick="checkout()" class="w-full mt-3 py-3 bg-green-500 text-white font-semibold rounded-lg hover:bg-green-600">
                Checkout
            </button>
        </div>
    `;
}

function addToCart(id) {
    const item = menuItems.find(i => i.id === id);
    const existingItem = cart.find(i => i.id === id);
    if (existingItem) {
        existingItem.quantity++;
    } else {
        cart.push({ ...item, quantity: 1 });
    }
    safeSetItem('campusconnect_cart', cart);
    showSuccess(`${item.name} added to cart!`);
    displayCart();
}

function removeFromCart(id) {
    cart = cart.filter(item => item.id !== id);
    safeSetItem('campusconnect_cart', cart);
    displayCart();
}

function checkout() {
    const total = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    const user = getCurrentUser();
    
    if (user.wallet < total) {
        showError('Insufficient wallet balance!');
        return;
    }
    
    user.wallet -= total;
    user.points += Math.floor(total / 10);
    safeSetItem('campusconnect_current_user', user);
    
    cart = [];
    safeSetItem('campusconnect_cart', cart);
    
    showSuccess('Order placed successfully!');
    displayCart();
}

displayMenu();
displayCart();
console.log('Canteen JS Loaded');'''

def generate_profile_js():
    return '''// Profile page logic
requireAuth();

const user = getCurrentUser();

function displayProfile() {
    const container = document.getElementById('profile-content');
    container.innerHTML = `
        <div class="text-center mb-8">
            <div class="w-24 h-24 bg-gradient-to-br from-blue-400 to-teal-400 rounded-full mx-auto mb-4 flex items-center justify-center text-5xl text-white font-black shadow-lg">
                ${user.name.charAt(0)}
            </div>
            <h2 class="text-2xl font-bold">${user.name}</h2>
            <p class="text-sm text-gray-600">Roll: ${user.roll}</p>
            <p class="text-sm text-gray-600">${user.email}</p>
        </div>

        <div class="bg-gradient-to-r from-blue-500 to-teal-400 p-6 rounded-xl shadow-lg text-white mb-6">
            <div class="flex justify-between items-center mb-4">
                <div>
                    <p class="text-sm opacity-90">Wallet Balance</p>
                    <h3 class="text-4xl font-bold">₹${user.wallet}</h3>
                </div>
                <span class="material-symbols-rounded text-5xl">account_balance_wallet</span>
            </div>
            <button onclick="addMoney()" class="w-full py-2 bg-white bg-opacity-20 backdrop-blur-sm hover:bg-opacity-30 rounded-lg font-semibold">
                Add Money
            </button>
        </div>

        <div class="bg-gradient-to-r from-orange-400 to-orange-600 p-6 rounded-xl shadow-lg text-white mb-6">
            <div class="flex justify-between items-center">
                <div>
                    <p class="text-sm opacity-90">Reward Points</p>
                    <h3 class="text-4xl font-bold">${user.points}</h3>
                </div>
                <span class="material-symbols-rounded text-5xl">workspace_premium</span>
            </div>
        </div>

        <button onclick="logout()" class="w-full flex items-center justify-center p-4 bg-red-50 rounded-xl shadow-md hover:shadow-lg border-2 border-red-200">
            <span class="material-symbols-rounded mr-3 text-2xl text-red-500">logout</span>
            <span class="font-semibold text-red-600">Logout</span>
        </button>
    `;
}

function addMoney() {
    const amount = prompt('Enter amount to add (₹):');
    if (amount && !isNaN(amount) && parseInt(amount) > 0) {
        user.wallet += parseInt(amount);
        safeSetItem('campusconnect_current_user', user);
        showSuccess(`₹${amount} added to wallet!`);
        displayProfile();
    }
}

displayProfile();
console.log('Profile JS Loaded');'''

def generate_style_css():
    return '''@import url('https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap');

:root {
    --primary-blue: #2196F3;
    --secondary-teal: #00BCD4;
    --success-green: #4CAF50;
    --error-red: #F44336;
    --background: #F5F7FA;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Inter', sans-serif;
    background-color: var(--background);
    line-height: 1.6;
}

.material-symbols-rounded {
    font-variation-settings: 'FILL' 0, 'wght' 500, 'GRAD' 0, 'opsz' 24;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

.fade-in { animation: fadeIn 0.3s ease-out; }
.hidden { display: none !important; }

.animate-spin {
    animation: spin 1s linear infinite;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}'''

def generate_netlify_toml():
    return '''[build]
  publish = "."
  functions = "netlify/functions"

[[redirects]]
  from = "/api/*"
  to = "/.netlify/functions/:splat"
  status = 200

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

[build.environment]
  NODE_VERSION = "18"'''

def generate_redirects():
    return '''/api/*  /.netlify/functions/:splat  200
/*    /index.html   404'''

def generate_package_json():
    return '''{
  "name": "campusconnect",
  "version": "2.0.0",
  "description": "Campus management platform",
  "scripts": {
    "dev": "netlify dev",
    "deploy": "netlify deploy --prod"
  },
  "license": "MIT"
}'''

def generate_ai_advisor_function():
    return '''exports.handler = async (event, context) => {
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, body: JSON.stringify({ error: 'Method not allowed' }) };
  }
  try {
    const { mealName } = JSON.parse(event.body);
    const ANTHROPIC_API_KEY = process.env.ANTHROPIC_API_KEY;
    
    const response = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': ANTHROPIC_API_KEY,
        'anthropic-version': '2023-06-01'
      },
      body: JSON.stringify({
        model: 'claude-sonnet-4-20250514',
        max_tokens: 1500,
        messages: [{
          role: 'user',
          content: `As a nutrition expert, analyze "${mealName}" and provide healthy alternatives.`
        }]
      })
    });
    
    const data = await response.json();
    return {
      statusCode: 200,
      body: JSON.stringify({ success: true, advice: data.content?.[0]?.text })
    };
  } catch (error) {
    return { statusCode: 500, body: JSON.stringify({ error: error.message }) };
  }
};'''

def generate_payment_function():
    return '''exports.handler = async (event, context) => {
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, body: JSON.stringify({ error: 'Method not allowed' }) };
  }
  try {
    const { amount, method } = JSON.parse(event.body);
    await new Promise(resolve => setTimeout(resolve, 2000));
    const transactionId = `TXN${Date.now()}`;
    return {
      statusCode: 200,
      body: JSON.stringify({
        success: true,
        transactionId,
        amount,
        method
      })
    };
  } catch (error) {
    return { statusCode: 500, body: JSON.stringify({ error: error.message }) };
  }
};'''

def generate_gitignore():
    return '''node_modules/
.netlify/
.DS_Store
*.log
.env
.env.local'''

def generate_readme():
    return '''# 🎓 CampusConnect

A modern campus management platform built with vanilla JavaScript and deployed on Netlify.

## 🚀 Quick Start

### Deploy to Netlify

1. **Drag & Drop**: Go to https://app.netlify.com/drop and drag this folder
2. **GitHub**: Push to GitHub and import on Netlify
3. **CLI**: `netlify deploy --prod`

### Set Environment Variables

In Netlify Dashboard → Settings → Environment variables:
```
ANTHROPIC_API_KEY=your_claude_api_key
```

## ✨ Features

- ✅ Authentication (Login/Signup)
- ✅ Library Management
- ✅ Canteen Ordering
- ✅ Wallet System
- ✅ AI Meal Advisor
- ✅ Points & Rewards

## 🛠️ Tech Stack

- HTML5 + TailwindCSS
- Vanilla JavaScript
- Netlify Functions (Serverless)
- LocalStorage for data

## 📱 Pages

- `index.html` - Login/Signup
- `home.html` - Dashboard
- `library.html` - Browse & borrow books
- `canteen.html` - Order food
- `profile.html` - User profile & wallet

## 🔧 Local Development

```bash
npm install -g netlify-cli
netlify dev
```

## 📝 License

MIT

---

**Built with ❤️ using Vanilla JS + Netlify**
'''

def main():
    print("=" * 60)
    print("🎓 CampusConnect Project Generator")
    print("=" * 60)
    print()
    
    # Get project name
    project_name = input("Enter project folder name (default: campusconnect): ").strip()
    if not project_name:
        project_name = "campusconnect"
    
    # Create base directory
    base_path = os.path.join(os.getcwd(), project_name)
    
    if os.path.exists(base_path):
        overwrite = input(f"⚠️  Folder '{project_name}' exists. Overwrite? (y/n): ").lower()
        if overwrite != 'y':
            print("❌ Cancelled.")
            sys.exit(0)
    
    print()
    print("🔨 Generating project...")
    print()
    
    # Create folders
    create_folder_structure(base_path)
    print()
    
    # Create files
    print("📄 Creating files...")
    
    files = {
        'index.html': generate_index_html(),
        'home.html': generate_home_html(),
        'library.html': generate_library_html(),
        'canteen.html': generate_canteen_html(),
        'profile.html': generate_profile_html(),
        'css/style.css': generate_style_css(),
        'js/common.js': generate_common_js(),
        'js/auth.js': generate_auth_js(),
        'js/library.js': generate_library_js(),
        'js/canteen.js': generate_canteen_js(),
        'js/profile.js': generate_profile_js(),
        'netlify.toml': generate_netlify_toml(),
        '_redirects': generate_redirects(),
        'package.json': generate_package_json(),
        'netlify/functions/ai-advisor.js': generate_ai_advisor_function(),
        'netlify/functions/payment.js': generate_payment_function(),
        '.gitignore': generate_gitignore(),
        'README.md': generate_readme()
    }
    
    for filename, content in files.items():
        create_file(base_path, filename, content)
    
    print()
    print("=" * 60)
    print("✅ Project generated successfully!")
    print("=" * 60)
    print()
    print(f"📁 Location: {base_path}")
    print()
    print("🚀 Next steps:")
    print(f"   1. cd {project_name}")
    print("   2. Deploy to Netlify:")
    print("      - Drag folder to https://app.netlify.com/drop")
    print("      - Or use: netlify deploy --prod")
    print("   3. Set ANTHROPIC_API_KEY in Netlify dashboard")
    print()
    print("📖 Read README.md for more info")
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\\n\\n❌ Cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"\\n\\n❌ Error: {e}")
        sys.exit(1)