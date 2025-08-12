# Online-bookstore-management



This object-oriented Python project streamlines the management of an online bookstore, handling inventory, sales, and user interactions with admin/user modes, cart functionality, discounts, and reporting.

## Features
- **Inventory Management**: Efficiently manage books, magazines, and DVDs with separate classes for each item type.
- **User Modes**: Switch between admin and user modes using numeric input (1 for Admin, 2 for User), with password `admin123` for admin access.
  - **Admin Mode Menu**:
    - 0. Add Books
    - 1. Add Magazine
    - 2. Add DVD
    - 3. Items Management
  - **User Mode Menu**:
    - 0. Print items on display
    - 1. Add Book to Cart
    - 2. Add Magazine to Cart
    - 3. Add DVD to Cart
    - 4. View Cart
    - 5. Remove Book from Cart
    - 6. Remove Magazine from Cart
    - 7. Remove DVD from Cart
    - 8. Checkout
    - 9. Exit
- **Cart Functionality**: Add, delete, or clear items in the cart with a single action.
- **Discounts**: Implement special discounts (customize in code).
- **User-Friendly Interface**: Simple and intuitive navigation for admins and users.
- **Detailed Reporting**: Generate reports on sales, inventory levels, and user activity.

## Repository Structure
- `src/`: Python scripts for the management system (e.g., `bookstore_management.py`)
## Technologies
- Python

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/YoussefWael18/Online-bookstore-management.git
   cd Online-bookstore-management
