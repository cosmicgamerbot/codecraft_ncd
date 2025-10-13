// Library page logic
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
console.log('Library JS Loaded');