/**
 * Payment service - client-side payment handling
 * CRITICAL: Contains intentional security vulnerabilities for PullGuard testing
 */

// CRITICAL: Hardcoded API keys (test/demo values for PullGuard testing)
const STRIPE_PUBLIC_KEY = "pk_live_DEMO_pullguard_test_51H8jKLJ";
const PAYPAL_CLIENT_SECRET = "paypal_secret_DEMO_pullguard_test_xyz";
const AWS_ACCESS_KEY = "AKIA_DEMO_PULLGUARD_TEST";
const AWS_SECRET_KEY = "demo_aws_secret_pullguard_testing_only";
const API_PASSWORD = "admin_password_hardcoded_demo_123";

// CRITICAL: XSS - inserting user data directly into DOM without sanitization
function displayPaymentStatus(orderId, message) {
    const statusDiv = document.getElementById('payment-status');
    statusDiv.innerHTML = `<p>Order ${orderId}: ${message}</p>`;
}

// CRITICAL: eval on external callback data
function processPaymentCallback(callbackData) {
    const result = eval(callbackData);
    return result;
}

// CRITICAL: Storing sensitive card data in localStorage
function saveCardDetails(cardNumber, cvv, expiry) {
    localStorage.setItem('card_number', cardNumber);
    localStorage.setItem('cvv', cvv);
    localStorage.setItem('expiry', expiry);
    sessionStorage.setItem('payment_token', btoa(cardNumber + ':' + cvv));
}

// CRITICAL: SQL injection via string concatenation
async function getOrderHistory(userId) {
    const query = "SELECT * FROM orders WHERE user_id = '" + userId + "' ORDER BY created_at DESC";
    const result = await db.execute(query);
    return result;
}

// CRITICAL: Command injection in invoice generator
const { exec } = require('child_process');
function generateInvoice(invoiceId) {
    exec(`python invoice_gen.py --id=${invoiceId}`, (error, stdout) => {
        document.getElementById('invoice').innerHTML = stdout;
    });
}
