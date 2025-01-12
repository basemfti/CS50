 # BANK PROGRAM 
    #### Video Demo:(https://youtu.be/KQviDp4VB0c)
    #### Description:Bank Program
Overview
The Bank Program is a simple command-line application designed to help users manage their finances by providing basic banking functionalities. Users can deposit money, withdraw funds, and check their account balance. The program is built using Python and integrates the pyttsx3 library to provide text-to-speech capabilities, enhancing user interaction.

Features
Show Balance: Display the current balance.
Deposit: Add a specified amount to the balance.
Withdraw: Remove a specified amount from the balance, ensuring sufficient funds are available.
Voice Feedback: Uses pyttsx3 for voice notifications and confirmations.
Input Validation: Ensures valid amounts are entered for deposits and withdrawals.
Project Structure
project.py: Contains the main banking functionalities and the command-line interface.
test_project.py: Contains test cases to ensure the proper functioning of the banking features.
File Descriptions
project.py
This file contains the core functions of the bank program:

show_balance(balance): Displays the current balance and provides voice feedback.
deposit(): Prompts the user to enter an amount to deposit. Validates the input and returns the amount if valid, otherwise returns 0.
withdraw(balance): Prompts the user to enter an amount to withdraw. Ensures the amount does not exceed the balance and is greater than 0, returning the amount if valid, otherwise returns 0.
main(): The main function that drives the program. It includes a while loop to continuously prompt the user for actions until they choose to exit. It calls the appropriate functions based on user input.
test_project.py
This file contains the test cases for the bank program using pytest:

test_show_balance(capsys, engine): Tests if the balance display function works correctly and captures the output.
test_deposit_valid_amount(monkeypatch): Tests the deposit function with a valid amount.
test_deposit_invalid_amount(monkeypatch): Tests the deposit function with an invalid amount (negative).
test_withdraw_valid_amount(monkeypatch): Tests the withdraw function with a valid amount that is less than the balance.
test_withdraw_insufficient_funds(monkeypatch): Tests the withdraw function when the withdrawal amount exceeds the balance.
test_withdraw_invalid_amount(monkeypatch): Tests the withdraw function with an invalid amount (negative).
Design Choices
Voice Feedback
The integration of pyttsx3 for text-to-speech functionality was chosen to enhance user interaction, making the program more accessible and user-friendly. This allows users to receive audible feedback for their actions, improving the overall user experience.

Input Validation
Input validation is crucial for ensuring the program's reliability and preventing errors. The deposit and withdraw functions include checks to ensure that the amounts entered are valid, preventing negative deposits and withdrawals that exceed the current balance.

Testing
Automated testing using pytest ensures that the core functionalities of the program work as expected. The tests cover various scenarios, including valid and invalid inputs, to ensure robustness.
