import pytest

test_files = [
    "test_001_RegistrationByEmail.py",
    "test_001_LoginByEmail.py",
    "test_001_ChangePassword.py",
    "test_001_purchaseFromBOX.py"
]

if __name__ == "__main__":
    for test_file in test_files:
        print(f"Running {test_file}...")
        pytest.main([test_file])