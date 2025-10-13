// Canteen page logic
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
console.log('Canteen JS Loaded');