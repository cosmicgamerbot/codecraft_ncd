// Profile page logic
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
console.log('Profile JS Loaded');