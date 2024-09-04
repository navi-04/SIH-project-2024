        // Simulated database
        let users = JSON.parse(localStorage.getItem('users')) || [];
        let products = JSON.parse(localStorage.getItem('products')) || [];
        let requests = JSON.parse(localStorage.getItem('requests')) || [];
        let prebookings = JSON.parse(localStorage.getItem('prebookings')) || [];

        function saveToLocalStorage() {
            localStorage.setItem('users', JSON.stringify(users));
            localStorage.setItem('products', JSON.stringify(products));
            localStorage.setItem('requests', JSON.stringify(requests));
            localStorage.setItem('prebookings', JSON.stringify(prebookings));
        }
        
        function showRegisterMenu() {
            hideAllSections();
            document.getElementById('registerMenu').classList.remove('hidden');
        }

        function showLoginForm() {
            hideAllSections();
            document.getElementById('loginForm').classList.remove('hidden');
        }

        function exit() {
            alert('Thank you for using our application');
        }

        function backToMainMenu() {
            hideAllSections();
            document.getElementById('mainMenu').classList.remove('hidden');
        }

        function showFarmerRegistration() {
            hideAllSections();
            document.getElementById('farmerRegistration').classList.remove('hidden');
        }

        function showConsumerRegistration() {
            hideAllSections();
            document.getElementById('consumerRegistration').classList.remove('hidden');
        }

        function logout() {
            hideAllSections();
            document.getElementById('mainMenu').classList.remove('hidden');
        }

        function hideAllSections() {
            const sections = ['mainMenu', 'registerMenu', 'farmerRegistration', 'consumerRegistration', 'loginForm', 'farmerDashboard', 'consumerDashboard', 'productManagement', 'buyProductForm', 'preBookingForm'];
            sections.forEach(section => document.getElementById(section).classList.add('hidden'));
        }

        function isValidEmail(email) {
            const re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
            return re.test(String(email).toLowerCase());
        }

        function isValidPhoneNumber(phone) {
            const re = /^\+?1?\d{9,15}$/;
            return re.test(String(phone));
        }

        function verifyViaOTP(phone) {
            // Simulating OTP verification
            return confirm('OTP sent. Click OK to simulate successful verification.');
        }

        document.getElementById('farmerForm').addEventListener('submit', function(e) {
            e.preventDefault();
            const email = document.getElementById('farmerEmail').value;
            const password = document.getElementById('farmerPassword').value;
            const phone = document.getElementById('farmerPhone').value;

            if (!isValidEmail(email)) {
                alert('Invalid email format');
                return;
            }

            if (!isValidPhoneNumber(phone)) {
                alert('Invalid phone number');
                return;
            }

            if (verifyViaOTP(phone)) {
                users.push({
                    type: 'farmer',
                    email: email,
                    password: password,
                    address: document.getElementById('farmerAddress').value,
                    phone: phone,
                    pincode: document.getElementById('farmerPincode').value,
                    products: document.getElementById('farmerProducts').value.split(',')
                });
                saveToLocalStorage();
                alert('Farmer user created successfully');
                backToMainMenu();
            } else {
                alert('Failed to create farmer user');
            }
        });

        document.getElementById('consumerForm').addEventListener('submit', function(e) {
            e.preventDefault();
            const email = document.getElementById('consumerEmail').value;
            const password = document.getElementById('consumerPassword').value;
            const phone = document.getElementById('consumerPhone').value;

            if (!isValidEmail(email)) {
                alert('Invalid email format');
                return;
            }

            if (!isValidPhoneNumber(phone)) {
                alert('Invalid phone number');
                return;
            }

            if (verifyViaOTP(phone)) {
                users.push({
                    type: 'consumer',
                    email: email,
                    password: password,
                    phone: phone
                });
                saveToLocalStorage();
                alert('Consumer user created successfully');
                backToMainMenu();
            } else {
                alert('Failed to create consumer user');
            }
        });

        document.getElementById('loginFormElement').addEventListener('submit', function(e) {
            e.preventDefault();
            const email = document.getElementById('loginEmail').value;
            const password = document.getElementById('loginPassword').value;
            const userType = document.getElementById('userType').value;

            const user = users.find(u => u.email === email && u.password === password && u.type === userType);

            if (user) {
                alert('Login successful');
                if (user.type === 'farmer') {
                    showFarmerDashboard();
                } else {
                    showConsumerDashboard();
                }
            } else {
                alert('Invalid username or password');
            }
        });

        function showFarmerDashboard() {
            hideAllSections();
            document.getElementById('farmerDashboard').classList.remove('hidden');
            viewAvailableProducts();
        }

        function showConsumerDashboard() {
            hideAllSections();
            document.getElementById('consumerDashboard').classList.remove('hidden');
            viewAvailableProducts();
        }

        function showAddProductForm() {
            document.getElementById('productFormTitle').textContent = 'Add Product';
            document.getElementById('productManagement').classList.remove('hidden');
            document.getElementById('productForm').onsubmit = addProduct;
        }

        function showUpdateProductForm() {
            document.getElementById('productFormTitle').textContent = 'Update Product';
            document.getElementById('productManagement').classList.remove('hidden');
            document.getElementById('productForm').onsubmit = updateProduct;
        }

        function showDeleteProductForm() {
            document.getElementById('productFormTitle').textContent = 'Delete Product';
            document.getElementById('productManagement').classList.remove('hidden');
            document.getElementById('productForm').onsubmit = deleteProduct;
        }

        function addProduct(e) {
            e.preventDefault();
            const product = {
                name: document.getElementById('productName').value,
                description: document.getElementById('productDescription').value,
                capacity: document.getElementById('productCapacity').value,
                price: document.getElementById('productPrice').value,
                available: document.getElementById('productAvailability').value,
                duration: document.getElementById('productDuration').value
            };
            products.push(product);
            saveToLocalStorage();
            alert('Product added successfully');
            viewAvailableProducts();
        }

        function updateProduct(e) {
            e.preventDefault();
            const productName = document.getElementById('productName').value;
            const productIndex = products.findIndex(p => p.name === productName);
            if (productIndex !== -1) {
                products[productIndex] = {
                    name: productName,
                    description: document.getElementById('productDescription').value,
                    capacity: document.getElementById('productCapacity').value,
                    price: document.getElementById('productPrice').value,
                    available: document.getElementById('productAvailability').value,
                    duration: document.getElementById('productDuration').value
                };
                saveToLocalStorage();
                alert('Product updated successfully');
                viewAvailableProducts();
            } else {
                alert('Product not found');
            }
        }

        function deleteProduct(e) {
            e.preventDefault();
            const productName = document.getElementById('productName').value;
            const productIndex = products.findIndex(p => p.name === productName);
            if (productIndex !== -1) {
                products.splice(productIndex, 1);
                alert('Product deleted successfully');
                viewAvailableProducts();
            } else {
                alert('Product not found');
            }
        }

        function viewAvailableProducts() {
            const productList = document.getElementById('productList');
            productList.classList.remove('hidden');
            productList.innerHTML = '<h3>Available Products</h3>';
            if (products.length === 0) {
                productList.innerHTML += '<p>No products available</p>';
            } else {
                products.forEach(product => {
                    productList.innerHTML += `
                        <p>Name: ${product.name}, Capacity: ${product.capacity}, Price: ${product.price}, 
                        Available: ${product.available}, Duration: ${product.duration}</p>
                    `;
                });
            }
        }

        function showBuyProductForm() {
            document.getElementById('buyProductForm').classList.remove('hidden');
        }

        function showPreBookingForm() {
            document.getElementById('preBookingForm').classList.remove('hidden');
        }

        document.getElementById('buyForm').addEventListener('submit', function(e) {
            e.preventDefault();
            const request = {
                product: document.getElementById('buyProductName').value,
                capacity: document.getElementById('buyProductCapacity').value,
                date: document.getElementById('buyProductDate').value
            };
            requests.push(request);
            alert(`Purchase confirmed for ${request.product} with a capacity of ${request.capacity}. Delivery is scheduled for ${request.date}.`);
        });

        document.getElementById('preBookForm').addEventListener('submit', function(e) {
            e.preventDefault();
            const prebooking = {
                product: document.getElementById('preBookProductName').value,
                capacity: document.getElementById('preBookProductCapacity').value,
                date: document.getElementById('preBookProductDate').value
            };
            prebookings.push(prebooking);
            alert(`Pre-booking confirmed for ${prebooking.product} with a capacity of ${prebooking.capacity}. Delivery is scheduled for ${prebooking.date}.`);
        });

        // Initialize the application
        backToMainMenu();